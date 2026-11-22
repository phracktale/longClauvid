"""
Figure du niveau 2 : les deux flux du modèle et leurs trois croisements.

Refait la figure 3 de Kashi et al. 2019 à partir de piege_ido.py,
pour contrôler la reproduction d'un coup d'œil.

Usage : python3 figure_piege_ido.py   (écrit piege_ido.png à côté de ce fichier)
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from piege_ido import Parametres, etats_stationnaires, flux_ido1, flux_lat1

# Couleurs : palette catégorielle validée (bleu, orange) et encres neutres.
FOND = "#fcfcfb"
ENCRE = "#0b0b0b"
ENCRE_SECONDAIRE = "#52514e"
ENCRE_DISCRETE = "#898781"
GRILLE = "#e1e0d9"
AXE = "#c3c2b7"
BLEU = "#2a78d6"
ORANGE = "#eb6834"


def main():
    p = Parametres()
    (normal, _), (seuil, _), (piege, _) = etats_stationnaires(p)
    trp = np.logspace(6, np.log10(p.trp_externe * p.keq), 600)

    plt.rcParams.update({"font.family": "sans-serif", "font.size": 11})
    figure, axe = plt.subplots(figsize=(8, 5.4), facecolor=FOND)
    axe.set_facecolor(FOND)

    axe.plot(trp, flux_lat1(trp, p), color=BLEU, linewidth=2, solid_capstyle="round",
             label="Entrée par LAT1")
    axe.plot(trp, flux_ido1(trp, p), color=ORANGE, linewidth=2, solid_capstyle="round",
             label="Dégradation par IDO1")

    # Les trois états stationnaires : un point à l'encre, cerclé de la couleur du fond.
    points = [
        (normal, "A  état normal\n(stable)", (12, -8), "top"),
        (seuil, "B  seuil\n(instable)", (12, 12), "bottom"),
        (piege, "C  état piégé\n(stable)", (12, 6), "bottom"),
    ]
    for valeur, texte, decalage, ancrage in points:
        axe.plot(valeur, flux_ido1(valeur, p), "o", color=ENCRE, markersize=9,
                 markeredgecolor=FOND, markeredgewidth=2, zorder=5)
        axe.annotate(texte, (valeur, flux_ido1(valeur, p)), xytext=decalage,
                     textcoords="offset points", ha="left", va=ancrage,
                     color=ENCRE, fontsize=10.5, linespacing=1.25,
                     bbox={"facecolor": FOND, "edgecolor": "none", "pad": 1.5})

    # Étiquettes directes, à l'encre : l'identité vient du trait coloré voisin.
    axe.text(1.25e6, 7350, "Entrée par LAT1", color=ENCRE_SECONDAIRE, fontsize=10.5)
    axe.text(9e7, 10350, "Dégradation par IDO1", color=ENCRE_SECONDAIRE, fontsize=10.5,
             ha="center")

    axe.set_xscale("log")
    axe.set_xlim(1e6, 3e10)
    axe.set_ylim(0, 11200)
    axe.set_xlabel("Tryptophane du cytosol (molécules par cellule, échelle logarithmique)",
                   color=ENCRE_SECONDAIRE)
    axe.set_ylabel("Flux (molécules par minute et par cellule)", color=ENCRE_SECONDAIRE)
    axe.yaxis.set_major_formatter(lambda valeur, _: f"{valeur:,.0f}".replace(",", " "))

    axe.grid(axis="y", color=GRILLE, linewidth=1)
    axe.set_axisbelow(True)
    axe.tick_params(colors=ENCRE_DISCRETE, length=0, which="both")
    for cote in ("top", "right", "left"):
        axe.spines[cote].set_visible(False)
    axe.spines["bottom"].set_color(AXE)

    legende = axe.legend(loc="upper right", handlelength=1.6, facecolor=FOND,
                         edgecolor="none", framealpha=1)
    for texte in legende.get_texts():
        texte.set_color(ENCRE_SECONDAIRE)

    figure.text(0.02, 0.95, "Deux états stables là où l'entrée du tryptophane croise sa dégradation",
                color=ENCRE, fontsize=13, fontweight="bold")
    figure.text(0.02, 0.90, "Modèle de Kashi, Davis et Phair (2019), paramètres de leur figure 3",
                color=ENCRE_SECONDAIRE, fontsize=10.5)

    figure.tight_layout(rect=(0, 0, 1, 0.90))
    sortie = Path(__file__).with_name("piege_ido.png")
    figure.savefig(sortie, dpi=200, facecolor=FOND)
    print(f"Figure écrite : {sortie.name}")


if __name__ == "__main__":
    main()
