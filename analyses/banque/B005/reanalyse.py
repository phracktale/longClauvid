"""Piste B005 : refait la comparaison de l'étude de 2026 en ajustant sur l'âge et le sexe.

Suit analyses/banque/B005/PLAN.md, écrit avant tout calcul.
Usage : python3 analyses/banque/B005/reanalyse.py "chemin/vers/Supplementary File 1 Indiv. Data.xlsx"
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

INDICE = "CSF_NE_DHPG_MHPG"
DOSAGES = ["CSF_MHPG", "CSF_DHPG", "CSF_NE", "CSF_DOPAC", "CSF_DOPA", "CSF_HVA", "CSF_DA"]
TEMOINS = "HV"
PUBLIES = {"PI-ME/CFS": -15.9, "PASC": -9.62, "PD": -19.4}
EFFECTIFS_PUBLIES = {"HV": 36, "PI-ME/CFS": 15, "PASC": 30, "PD": 32}


def charger(chemin):
    """Lit le classeur des auteurs ; « . » et « ^ » y marquent une valeur manquante."""
    d = pd.read_excel(chemin, sheet_name="Data")
    for colonne in [INDICE] + DOSAGES:
        d[colonne] = pd.to_numeric(d[colonne], errors="coerce")
    d["medicament"] = d["QueryDrugs"].notna()
    return d


def regression(d, mesure, groupes, confiance):
    """Moindres carrés : mesure ~ groupe + âge + sexe. Rend l'écart de chaque groupe aux témoins."""
    d = d[d["Cohort"].isin([TEMOINS] + groupes)].dropna(subset=[mesure, "Age", "Sex"])
    colonnes = [np.ones(len(d))] + [(d["Cohort"] == g).astype(float) for g in groupes]
    colonnes += [d["Age"].astype(float), d["Sex"].astype(float)]
    X = np.column_stack(colonnes)
    y = d[mesure].to_numpy(dtype=float)
    coefficients, *_ = np.linalg.lstsq(X, y, rcond=None)
    libertes = len(y) - X.shape[1]
    variance = ((y - X @ coefficients) ** 2).sum() / libertes
    erreurs = np.sqrt(np.diag(variance * np.linalg.inv(X.T @ X)))
    t_critique = stats.t.ppf(1 - (1 - confiance) / 2, libertes)
    lignes = []
    for i, groupe in enumerate(groupes, start=1):
        p = 2 * stats.t.sf(abs(coefficients[i] / erreurs[i]), libertes)
        lignes.append((groupe, int((d["Cohort"] == groupe).sum()), coefficients[i],
                       coefficients[i] - t_critique * erreurs[i], coefficients[i] + t_critique * erreurs[i], p))
    pente_age = coefficients[len(groupes) + 1]
    return lignes, int((d["Cohort"] == TEMOINS).sum()), pente_age


def afficher(titre, resultat, confiance):
    lignes, n_temoins, pente_age = resultat
    print(f"\n{titre} (témoins : {n_temoins} ; pente de l'âge : {pente_age:+.2f} par an)")
    for groupe, n, ecart, bas, haut, p in lignes:
        print(f"  {groupe:<22} n = {n:>2}  écart {ecart:+7.2f}  IC {confiance:.1%} [{bas:+7.2f} ; {haut:+7.2f}]  p = {p:.4f}")


def etape_0(d):
    """Retrouve les écarts publiés : analyse de variance puis test de Tukey, sans ajustement."""
    print("Étape 0 : chiffres publiés")
    ordre = ["HV", "PI-ME/CFS", "PASC", "PD"]
    series = [d.loc[d["Cohort"] == g, INDICE].dropna() for g in ordre]
    tukey = stats.tukey_hsd(*series)
    intervalles = tukey.confidence_interval(0.95)
    retrouve = True
    for i, groupe in enumerate(ordre):
        n = len(series[i])
        if n != EFFECTIFS_PUBLIES[groupe]:
            retrouve = False
        if i == 0:
            print(f"  {groupe:<10} n = {n} (publié : {EFFECTIFS_PUBLIES[groupe]})")
            continue
        ecart = series[i].mean() - series[0].mean()
        if abs(ecart - PUBLIES[groupe]) > 0.1:
            retrouve = False
        print(f"  {groupe:<10} n = {n} (publié : {EFFECTIFS_PUBLIES[groupe]})  écart {ecart:+.2f} "
              f"[{intervalles.low[i, 0]:+.2f} ; {intervalles.high[i, 0]:+.2f}]  p = {tukey.pvalue[i, 0]:.5f}  "
              f"(publié : {PUBLIES[groupe]:+.2f})")
    return retrouve


def main(chemin):
    d = charger(chemin)
    if not etape_0(d):
        print("\nLes chiffres publiés ne sont pas retrouvés : l'analyse s'arrête ici, comme le plan le prévoit.")
        return 1

    print("\nÂge moyen et part du sexe codé 1, parmi les personnes dosées :")
    doses = d.dropna(subset=[INDICE])
    print(doses.groupby("Cohort").agg(n=("Age", "size"), age=("Age", "mean"), sexe_1=("Sex", "mean")).round(2).to_string())

    deux = ["PI-ME/CFS", "PASC"]
    afficher("Étape 1, test principal : indice ~ groupe + âge + sexe, sans le groupe Parkinson",
             regression(d, INDICE, deux, 0.975), 0.975)

    print("\n--- Étape 2 : sensibilité, descriptif, sans correction ---")
    afficher("2.1 Les quatre groupes", regression(d, INDICE, deux + ["PD"], 0.95), 0.95)

    print("\n2.2 Patients sous médicament agissant sur la noradrénaline, par groupe :")
    print(d[d["medicament"]].groupby("Cohort").size().to_string())
    afficher("2.2 Sans ces patients", regression(d[~d["medicament"]], INDICE, deux, 0.95), 0.95)

    for dosage in DOSAGES:
        afficher(f"2.3 {dosage} seul", regression(d, dosage, deux, 0.95), 0.95)

    covid = d.copy()
    malaise = pd.to_numeric(covid["PEM"], errors="coerce")
    est_covid = covid["Cohort"] == "PASC"
    covid.loc[est_covid & (malaise == 1), "Cohort"] = "PASC avec malaise"
    covid.loc[est_covid & (malaise == 0), "Cohort"] = "PASC sans malaise"
    afficher("2.4 COVID long, avec et sans malaise post-effort",
             regression(covid, INDICE, ["PASC avec malaise", "PASC sans malaise"], 0.95), 0.95)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
