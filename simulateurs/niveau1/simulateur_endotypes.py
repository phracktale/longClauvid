"""
Simulateur de niveau 1 : confrontation de plans d'essai sur une cohorte virtuelle.

Question posée
--------------
Un traitement agit fortement chez une fraction des patients (un « endotype »)
et pas du tout chez les autres. Quel plan d'essai a une chance réelle de le voir ?

Trois plans comparés
--------------------
1. Essai parallèle « tout-venant » : on randomise tout le monde, traitement contre placebo.
2. Essai parallèle « enrichi » : on n'inclut que les patients positifs à un biomarqueur imparfait.
3. Série d'essais N-de-1 : chaque patient alterne plusieurs fois traitement et placebo.

Conventions
-----------
- Le critère de jugement est un score continu, exprimé en écarts-types entre patients (ET = 1).
- « effet » = amélioration moyenne chez les répondeurs, dans cette même unité (d de Cohen).
- Tous les tests sont bilatéraux au seuil de 5 % ; on ne compte que les résultats favorables.

Hypothèses fortes du plan N-de-1 (à vérifier avant tout usage réel)
-------------------------------------------------------------------
- L'effet apparaît et disparaît vite (pas d'effet rémanent d'une période sur la suivante).
- L'état du patient est stable sur la durée de l'essai.

Usage : python3 simulateur_endotypes.py
"""

import numpy as np
from scipy import stats

SEUIL = 0.05
NB_SIMULATIONS = 20000
GRAINE = 20261122


def puissance_parallele(nb_patients, part_repondeurs, effet, generateur):
    """Part des essais simulés où le traitement bat le placebo (test t de Student)."""
    nb_par_bras = nb_patients // 2
    forme = (NB_SIMULATIONS, nb_par_bras)

    placebo = generateur.normal(0, 1, forme)
    est_repondeur = generateur.random(forme) < part_repondeurs
    traite = generateur.normal(0, 1, forme) + effet * est_repondeur

    t, p = stats.ttest_ind(traite, placebo, axis=1)
    return np.mean((p < SEUIL) & (t > 0))


def puissance_parallele_formule(nb_patients, part_repondeurs, effet):
    """Même grandeur par la formule de l'approximation normale (contrôle du simulateur)."""
    nb_par_bras = nb_patients // 2
    effet_moyen = part_repondeurs * effet
    variance_traite = 1 + part_repondeurs * (1 - part_repondeurs) * effet**2
    erreur_type = np.sqrt((1 + variance_traite) / nb_par_bras)
    return stats.norm.cdf(effet_moyen / erreur_type - stats.norm.ppf(1 - SEUIL / 2))


def patients_requis_tout_venant(part_repondeurs, effet, puissance=0.80):
    """Effectif total d'un essai tout-venant pour atteindre la puissance voulue."""
    effet_moyen = part_repondeurs * effet
    variance_traite = 1 + part_repondeurs * (1 - part_repondeurs) * effet**2
    z = stats.norm.ppf(1 - SEUIL / 2) + stats.norm.ppf(puissance)
    nb_par_bras = z**2 * (1 + variance_traite) / effet_moyen**2
    return 2 * int(np.ceil(nb_par_bras))


def enrichissement(part_repondeurs, sensibilite, specificite):
    """Effet d'un biomarqueur imparfait : part de vrais répondeurs parmi les positifs,
    et part de patients positifs (donc inclus) parmi les patients dépistés."""
    vrais_positifs = part_repondeurs * sensibilite
    faux_positifs = (1 - part_repondeurs) * (1 - specificite)
    part_positifs = vrais_positifs + faux_positifs
    return vrais_positifs / part_positifs, part_positifs


def puissances_n_de_1(nb_patients, nb_paires, part_repondeurs, effet, et_intra, generateur):
    """Série d'essais N-de-1. Renvoie deux puissances :
    - détecter un effet moyen (le traitement fait mieux que le placebo en moyenne) ;
    - détecter une hétérogénéité (les patients ne répondent pas tous pareil).

    Chaque paire fournit une différence traitement - placebo pour un même patient.
    et_intra = écart-type des fluctuations d'un patient d'une période à l'autre.
    """
    est_repondeur = generateur.random((NB_SIMULATIONS, nb_patients)) < part_repondeurs
    effet_individuel = effet * est_repondeur

    differences = generateur.normal(
        effet_individuel[:, :, None],
        np.sqrt(2) * et_intra,
        (NB_SIMULATIONS, nb_patients, nb_paires),
    )
    moyenne_par_patient = differences.mean(axis=2)

    # Effet moyen : test t sur les moyennes individuelles.
    t, p = stats.ttest_1samp(moyenne_par_patient, 0, axis=1)
    puissance_effet_moyen = np.mean((p < SEUIL) & (t > 0))

    # Hétérogénéité : la dispersion entre patients dépasse-t-elle celle attendue
    # du seul bruit intra-patient ? (test F d'analyse de variance)
    carre_moyen_entre = nb_paires * moyenne_par_patient.var(axis=1, ddof=1)
    carre_moyen_intra = differences.var(axis=2, ddof=1).mean(axis=1)
    f = carre_moyen_entre / carre_moyen_intra
    p_f = stats.f.sf(f, nb_patients - 1, nb_patients * (nb_paires - 1))
    puissance_heterogeneite = np.mean(p_f < SEUIL)

    return puissance_effet_moyen, puissance_heterogeneite


def pourcent(valeur):
    return f"{100 * valeur:5.1f} %"


def main():
    generateur = np.random.default_rng(GRAINE)

    effet = 0.8            # effet fort chez les répondeurs
    nb_patients = 200      # taille d'un essai de phase 2 typique
    sensibilite = specificite = 0.80
    nb_patients_n1, nb_paires = 60, 3
    parts = [0.10, 0.20, 0.30, 0.50]

    print("CONTRÔLES NÉGATIFS (effet nul : on attend 2,5 % / 2,5 % / 5 %)")
    faux_positifs_parallele = puissance_parallele(nb_patients, 0.3, 0.0, generateur)
    faux_moyen, faux_hetero = puissances_n_de_1(nb_patients_n1, nb_paires, 0.3, 0.0, 0.5, generateur)
    print(f"  parallèle : {pourcent(faux_positifs_parallele)}"
          f" | N-de-1 effet moyen : {pourcent(faux_moyen)}"
          f" | N-de-1 hétérogénéité : {pourcent(faux_hetero)}")

    print(f"\nPUISSANCE PAR PLAN (effet chez les répondeurs = {effet} ET)")
    print(f"  Parallèle : {nb_patients} patients. Enrichi : biomarqueur sensibilité = spécificité = "
          f"{sensibilite:.0%}.")
    print(f"  N-de-1 : {nb_patients_n1} patients x {nb_paires} paires de périodes.\n")
    entete = ("répondeurs | tout-venant (formule) | patients requis | enrichi (dépistés) "
              "| N-de-1 effet moyen / hétérogénéité, ET intra 0,5 | idem, ET intra 0,8")
    print(entete)

    for part in parts:
        tout_venant = puissance_parallele(nb_patients, part, effet, generateur)
        formule = puissance_parallele_formule(nb_patients, part, effet)
        requis = patients_requis_tout_venant(part, effet)

        part_vrais, part_positifs = enrichissement(part, sensibilite, specificite)
        enrichi = puissance_parallele(nb_patients, part_vrais, effet, generateur)
        depistes = int(np.ceil(nb_patients / part_positifs))

        moyen_05, hetero_05 = puissances_n_de_1(nb_patients_n1, nb_paires, part, effet, 0.5, generateur)
        moyen_08, hetero_08 = puissances_n_de_1(nb_patients_n1, nb_paires, part, effet, 0.8, generateur)

        print(f"   {part:4.0%}    |  {pourcent(tout_venant)} ({pourcent(formule)})  |"
              f"     {requis:5d}       | {pourcent(enrichi)} ({depistes:4d})   |"
              f"          {pourcent(moyen_05)} / {pourcent(hetero_05)}              |"
              f"  {pourcent(moyen_08)} / {pourcent(hetero_08)}")


if __name__ == "__main__":
    main()
