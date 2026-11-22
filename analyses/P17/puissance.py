"""
Puissance d'une randomisation mendélienne, pour le plan d'analyse de la piste P17.

Question : avec quels jeux de cas peut-on refaire le résultat de la prépublication,
un rapport de cotes d'environ 0,83 par écart type de nombre de copies d'ADN mitochondrial ?

Formule (Burgess, International Journal of Epidemiology 2014, PMID 24608958), issue binaire :
    puissance = Phi( |ln(rapport de cotes)| x racine(R2 x N x K x (1 - K)) - z )
    N  : taille de l'échantillon de l'issue ; K : part de cas ; N x K x (1 - K) = cas x témoins / N
    R2 : part de la variance de l'exposition expliquée par les instruments
    z  : quantile de la loi normale pour le risque alpha, test bilatéral

Hypothèses, toutes écrites ici :
- R2 est déduit des 84 instruments et de leur statistique F moyenne de 85,5 (tableau de la prépublication),
  avec les 465 809 personnes de l'étude du nombre de copies (PMID 34859289) : R2 = kF / (N - k - 1 + kF).
- L'effet à retrouver est celui de la prépublication, pris tel quel. Un premier résultat surestime
  souvent l'effet : la puissance réelle est donc plus basse que celle calculée ici.
- Les effectifs sont ceux des manifestes publics, relevés le 2026-11-22.

Usage : python3 analyses/P17/puissance.py
"""

import math

from scipy.stats import norm

INSTRUMENTS, F_MOYEN, N_EXPOSITION = 84, 85.5, 465_809
RAPPORT_DE_COTES = 0.83
ALPHA = 0.05

# Jeu de cas : (cas, témoins, remarque)
JEUX = {
    "DecodeME, le jeu d'origine": (15_579, 259_909, "référence, pas une réplication"),
    "FinnGen R10, fatigue post-virale": (195, 382_198, "indépendant"),
    "Pan-UK Biobank, fatigue chronique déclarée": (1_882, 418_591, "partage UK Biobank avec les instruments"),
    "FinnGen et Pan-UK Biobank réunis": (195 + 1_882, 382_198 + 418_591, "méta-analyse"),
    "COVID long, définition large (HGI)": (6_450, 1_093_995, "autre maladie : extension, pas réplication"),
}


def variance_expliquee(instruments=INSTRUMENTS, f_moyen=F_MOYEN, n=N_EXPOSITION):
    """R2 des instruments, d'après leur nombre et leur statistique F moyenne."""
    return instruments * f_moyen / (n - instruments - 1 + instruments * f_moyen)


def puissance(cas, temoins, r2, rapport_de_cotes=RAPPORT_DE_COTES, alpha=ALPHA):
    """Probabilité de voir l'effet, s'il existe, au risque alpha bilatéral."""
    n_efficace = cas * temoins / (cas + temoins)          # N x K x (1 - K)
    signal = abs(math.log(rapport_de_cotes)) * math.sqrt(r2 * n_efficace)
    return norm.cdf(signal - norm.isf(alpha / 2))


def cas_necessaires(r2, cible=0.80, temoins_par_cas=10):
    """Nombre de cas pour atteindre la puissance cible, à dix témoins par cas."""
    cas = 100
    while puissance(cas, cas * temoins_par_cas, r2) < cible:
        cas += 100
    return cas


def main():
    r2 = variance_expliquee()
    print(f"Variance expliquée par les instruments : {r2:.2%}")
    print(f"Effet à retrouver : rapport de cotes {RAPPORT_DE_COTES} par écart type ; alpha {ALPHA}\n")
    for nom, (cas, temoins, remarque) in JEUX.items():
        print(f"  {puissance(cas, temoins, r2):5.0%}  {nom} : {cas} cas ({remarque})")
    print(f"\nCas nécessaires pour 80 % de puissance, à dix témoins par cas : {cas_necessaires(r2)}")
    print("Sensibilité à la variance expliquée, pour FinnGen et Pan-UK Biobank réunis :")
    cas, temoins, _ = JEUX["FinnGen et Pan-UK Biobank réunis"]
    for essai in (0.010, 0.015, 0.020, 0.030):
        print(f"  R2 = {essai:.1%} : puissance {puissance(cas, temoins, essai):.0%}")


if __name__ == "__main__":
    main()
