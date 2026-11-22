"""
Description des 40 bibliothèques du jeu GSE130353, faite APRÈS l'ouverture des données.

Elle ne fait pas partie du plan (analyses/P15/PLAN.md) et ne change pas sa lecture.
Elle répond à une question simple, posée en voyant le résultat : dans chaque bibliothèque,
quelle part des lectures tombe sur les ARN ribosomiques ?

Pour chaque bibliothèque : le nombre de lectures alignées sur un seul gène (colonne unique_hits)
pour les deux ARN ribosomiques de la mitochondrie et pour les deux pseudogènes des ARN 18S et 28S,
divisé par le nombre de fragments alignés, donné à la première ligne du fichier.

Usage : python3 analyses/P15/description.py     (après « arn_ribosomique.py telecharger »)
"""

import gzip
import re
from statistics import median

from arn_ribosomique import ARN_CYTO, ARN_MITO, FICHIERS, GROUPES, SERIE_2_A_PARTIR_DE


def parts_d_une_bibliotheque(chemin):
    """Renvoie la part des fragments alignés sur l'ARN ribosomique de la mitochondrie, puis du cytoplasme."""
    lectures = {}
    with gzip.open(chemin, "rt") as fichier:
        fragments = int(re.search(r"Mapped fragments: (\d+)", fichier.readline()).group(1))
        colonnes = fichier.readline().split()
        gene, unique = colonnes.index("feature_id"), colonnes.index("unique_hits")
        for ligne in fichier:
            champs = ligne.split()
            if champs[gene] in ARN_MITO + ARN_CYTO:
                lectures[champs[gene]] = int(champs[unique])
    return (sum(lectures[g] for g in ARN_MITO) / fragments, sum(lectures[g] for g in ARN_CYTO) / fragments)


def main():
    parts = {}
    for chemin in sorted(FICHIERS.glob("*.gene.mmseq.txt.gz")):
        _, nom, _, numero = chemin.name.split(".")[0].split("_")
        serie = 2 if int(numero) >= SERIE_2_A_PARTIR_DE else 1
        groupe = GROUPES[re.match(r"[A-Z]+", nom).group()]
        parts.setdefault((serie, groupe), []).append((nom, *parts_d_une_bibliotheque(chemin)))

    print("Part des fragments alignés sur l'ARN ribosomique, en % : mitochondrie, puis cytoplasme")
    for (serie, groupe), bibliotheques in sorted(parts.items()):
        detail = " ; ".join(f"{nom} {100 * mito:.2f} et {100 * cyto:.2f}" for nom, mito, cyto in bibliotheques)
        print(f"  série {serie}, {groupe} : {detail}")

    print("\nMêmes parts, les deux compartiments réunis : de la plus petite à la plus grande, et médiane")
    for (serie, groupe), bibliotheques in sorted(parts.items()):
        totaux = sorted(100 * (mito + cyto) for _, mito, cyto in bibliotheques)
        print(f"  série {serie}, {groupe} : de {totaux[0]:.2f} à {totaux[-1]:.2f} %, médiane {median(totaux):.2f} %")
    tous = [100 * (mito + cyto) for bibliotheques in parts.values() for _, mito, cyto in bibliotheques]
    print(f"  les 40 bibliothèques : médiane {median(tous):.3f} %")


if __name__ == "__main__":
    main()
