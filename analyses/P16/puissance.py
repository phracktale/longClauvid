"""
Puissance des quatre tests du plan d'analyse de la piste P16 (région HLA).

Chaque test cherche, dans l'étude d'une maladie, l'allèle ou le variant désigné par l'étude de l'autre.
Le seuil est celui du plan : p inférieur à 0,05 / 4, et même sens que dans l'étude d'origine.

Formule : test allélique, approximation normale du logarithme du rapport de cotes,
celle des calculs du statisticien (analyses/banque/calculs-statistique.py) :
    erreur type = racine( 1 / (2 x cas x p x (1 - p)) + 1 / (2 x témoins x p x (1 - p)) )
    p : fréquence de l'allèle chez les témoins

Hypothèses, toutes écrites ici :
- L'effet à retrouver est celui de l'étude d'origine, pris tel quel. Un premier résultat surestime
  souvent l'effet : la puissance réelle est plus basse.
- Quand un article ne donne pas la fréquence de l'allèle, plusieurs valeurs sont essayées.
- Effectifs : DecodeME, 15 579 cas et 259 909 témoins ; 23andMe, 54 390 cas et 124 777 témoins.

Usage : python3 analyses/P16/puissance.py
"""

import math

from scipy.stats import norm

ALPHA = 0.05 / 4
DECODEME = (15_579, 259_909)
VINGT_TROIS_AND_ME = (54_390, 124_777)

# Test : (étude où l'on cherche, rapport de cotes de l'étude d'origine, fréquences essayées)
TESTS = {
    "1. rs9273363 dans DecodeME": (DECODEME, 1.06, (0.2, 0.3, 0.4)),
    "2. DRB1*11:04 dans DecodeME": (DECODEME, 1.18, (0.01, 0.02, 0.05)),
    "3. DQA1*03:01 dans DecodeME": (DECODEME, 0.95, (0.10, 0.15, 0.20)),
    "4. DQA1*05:01 dans 23andMe": (VINGT_TROIS_AND_ME, 0.917, (0.232,)),
}


def puissance(rapport_de_cotes, frequence, cas, temoins, alpha=ALPHA):
    """Probabilité de voir l'effet, s'il existe, au risque alpha bilatéral."""
    variance = 1 / (2 * cas * frequence * (1 - frequence)) + 1 / (2 * temoins * frequence * (1 - frequence))
    signal = abs(math.log(rapport_de_cotes)) / math.sqrt(variance)
    seuil = norm.isf(alpha / 2)
    return norm.cdf(signal - seuil) + norm.cdf(-signal - seuil)


def main():
    print(f"Seuil : p < {ALPHA}, soit 0,05 / 4\n")
    for nom, ((cas, temoins), rapport, frequences) in TESTS.items():
        valeurs = ", ".join(f"{puissance(rapport, f, cas, temoins):.0%} à la fréquence {f}" for f in frequences)
        print(f"  {nom}, rapport de cotes {rapport} : {valeurs}")


if __name__ == "__main__":
    main()
