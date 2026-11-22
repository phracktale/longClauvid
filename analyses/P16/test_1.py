"""
Test 1 du plan de la piste P16 : analyses/P16/PLAN.md.

Le variant rs9273363 est associé au COVID long dans l'étude de 23andMe : rapport de cotes de 1,06
pour l'allèle C. Le test cherche le même variant dans l'analyse principale de DecodeME, sur l'EM/SFC,
et lit le résultat par la règle du plan. Rien ne s'ajuste après avoir vu le chiffre.

Les deux fichiers publics se téléchargent dans cache/P16/, hors du dépôt (350 Mo).

Usage :
    python3 analyses/P16/test_1.py telecharger
    python3 analyses/P16/test_1.py
"""

import gzip
import math
import shutil
import sys
import urllib.request
from pathlib import Path

from puissance import ALPHA, puissance

CACHE = Path(__file__).resolve().parents[2] / "cache" / "P16"
RESULTATS = "gwas_1.regenie.gz"          # l'analyse principale
CONTROLES = "gwas_qced.var.gz"           # la liste des variants contrôlés par les auteurs
ADRESSES = {RESULTATS: "https://osf.io/download/v4w8g/", CONTROLES: "https://osf.io/download/6uj5x/"}

# Le variant du plan : sa position sur le génome GRCh38, ses deux allèles, et l'effet publié pour l'allèle C.
CHROMOSOME, POSITION, ALLELES = "6", "32658495", {"A", "C"}
ALLELE_DU_TEST = "C"
RAPPORT_PUBLIE = 1.06
PUISSANCE_REQUISE = 0.80


def telecharger():
    CACHE.mkdir(parents=True, exist_ok=True)
    for nom, adresse in ADRESSES.items():
        destination = CACHE / nom
        if not destination.is_file():
            requete = urllib.request.Request(adresse, headers={"User-Agent": "copie-locale-lecture-seule/1.0"})
            with urllib.request.urlopen(requete, timeout=3000) as reponse, open(destination, "wb") as fichier:
                shutil.copyfileobj(reponse, fichier)
        print(f"{nom} : {destination.stat().st_size} octets")


def lignes_du_variant():
    """Renvoie les lignes du fichier de résultats à la position du variant, chacune en dictionnaire."""
    trouvees = []
    with gzip.open(CACHE / RESULTATS, "rt") as fichier:
        colonnes = fichier.readline().split()
        for ligne in fichier:
            if POSITION not in ligne:        # tri rapide : la plupart des lignes s'écartent ici
                continue
            valeurs = dict(zip(colonnes, ligne.split()))
            if valeurs["CHROM"].removeprefix("chr") == CHROMOSOME and valeurs["GENPOS"] == POSITION:
                trouvees.append(valeurs)
    return trouvees


def est_controle(identifiant):
    """Le variant figure-t-il dans la liste des variants contrôlés ?"""
    with gzip.open(CACHE / CONTROLES, "rt") as fichier:
        return any(ligne.strip() == identifiant for ligne in fichier if POSITION in ligne)


def lecture(rapport_de_cotes, p, puissance_du_test):
    """La règle de la section 5 du plan, pour un test : la première ligne remplie donne la lecture."""
    if rapport_de_cotes > 1 and p < ALPHA:
        return "le test passe"
    if rapport_de_cotes < 1 and p < ALPHA:
        return "résultat contraire"
    if puissance_du_test >= PUISSANCE_REQUISE:
        return "le test échoue"
    return "non informatif"


def main():
    if sys.argv[1:] == ["telecharger"]:
        return telecharger()

    lignes = lignes_du_variant()
    print(f"{len(lignes)} ligne(s) à la position {CHROMOSOME}:{POSITION}")
    for valeurs in lignes:
        print("  " + " ".join(f"{cle}={valeur}" for cle, valeur in valeurs.items()))

    retenues = [v for v in lignes if {v["ALLELE0"], v["ALLELE1"]} == ALLELES]
    if len(retenues) != 1:
        print(f"Test 1 : non lu ({len(retenues)} ligne avec les allèles A et C).")
        return
    variant = retenues[0]
    if not est_controle(variant["ID"]):
        print(f"Test 1 : non lu. Le variant {variant['ID']} n'est pas dans la liste des variants contrôlés.")
        return

    # L'effet du fichier est celui de ALLELE1 : on le ramène à l'allèle C.
    signe = 1 if variant["ALLELE1"] == ALLELE_DU_TEST else -1
    effet, erreur_type = signe * float(variant["BETA"]), float(variant["SE"])
    rapport_de_cotes = math.exp(effet)
    bas, haut = math.exp(effet - 1.96 * erreur_type), math.exp(effet + 1.96 * erreur_type)
    p = 10 ** -float(variant["LOG10P"])
    frequence = float(variant["A1FREQ"])
    cas, temoins = int(variant["N_CASES"]), int(variant["N_CONTROLS"])
    puissance_du_test = puissance(RAPPORT_PUBLIE, frequence, cas, temoins)

    print(f"\nVariant {variant['ID']}, contrôlé par les auteurs ; allèle d'effet du fichier : {variant['ALLELE1']}")
    print(f"Effectifs : {cas} cas, {temoins} témoins ; fréquence de l'allèle {variant['ALLELE1']} : {frequence:.3f}")
    print(f"Puissance pour l'effet publié ({RAPPORT_PUBLIE}), au seuil p < {ALPHA} : {puissance_du_test:.0%}")
    print(f"Allèle {ALLELE_DU_TEST} : rapport de cotes {rapport_de_cotes:.3f} "
          f"(intervalle à 95 % : {bas:.3f} à {haut:.3f}), p = {p:.2g}")
    print(f"Test 1 : {lecture(rapport_de_cotes, p, puissance_du_test)}")


if __name__ == "__main__":
    main()
