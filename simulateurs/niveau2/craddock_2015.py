"""
Reproduction du réseau de Craddock et al. : l'ordre des traitements compte-t-il ?

Le modèle relie trois systèmes chez l'homme : l'axe du stress (CRH, ACTH, cortisol
et son récepteur), l'axe sexuel (GnRH, LH/FSH, testostérone) et une immunité simplifiée.
Il a été construit pour la maladie de la guerre du Golfe, pas pour le COVID long.

D'où viennent les données
-------------------------
- Le réseau : relevé à la main sur la figure 2 de Craddock et al. 2015 (PLOS ONE,
  doi:10.1371/journal.pone.0132774, licence CC BY).
- La règle de calcul et les cinq états stables publiés : Craddock et al. 2014
  (PLOS ONE, doi:10.1371/journal.pone.0084839).
- Les taux publiés : figures 5 et 6 de l'article de 2015.

Deux lectures d'un traitement
-----------------------------
L'équation 4 de l'article décale le nœud traité d'un cran. Mais les taux de sa figure 5
ne se retrouvent que si un nœud freiné descend de deux crans. Faute du code des auteurs,
ce fichier calcule les deux lectures et les donne côte à côte.

Usage : python3 craddock_2015.py   (environ une minute)
"""

from reseau_logique import etats_stables, issues

# nœud : (activateurs, inhibiteurs).
# Le stress, entrée externe de CRH, est tenu à sa valeur normale et n'est pas représenté :
# comme CRH a aussi des inhibiteurs, un activateur normal ne change jamais sa valeur visée.
RESEAU = {
    "CRH":    (["T1Cyt", "IIR"], ["CORT", "TEST"]),
    "ACTH":   (["CRH", "T1Cyt", "IIR"], ["GRD", "TEST"]),
    "CORT":   (["ACTH", "T1Cyt", "IIR"], ["TEST"]),
    "GRD":    (["CORT", "GR"], []),
    "GR":     (["GRD"], []),
    "ICell":  (["IIR", "T1Cyt"], ["CORT", "T2Cyt"]),
    "IIR":    (["ICell"], []),
    "T1Cell": (["T1Cyt", "IIR", "TEST"], ["T2Cyt"]),
    "T1Cyt":  (["T1Cell", "ICell"], []),
    "T2Cell": (["T2Cyt"], ["T1Cyt"]),
    "T2Cyt":  (["T2Cell"], []),
    "GnRH":   ([], ["T1Cyt", "TEST", "CORT"]),
    "LH/FSH": (["GnRH"], ["T1Cyt", "TEST", "CORT"]),
    "TEST":   (["LH/FSH"], ["CORT"]),
}

# Les cinq états stables publiés (figure 2 de l'article de 2014) : seuls les nœuds
# qui ne sont pas à leur valeur normale sont écrits.
IMMUNITE_TH2 = {"ICell": -1, "IIR": -1, "T1Cell": -1, "T1Cyt": -1, "T2Cell": 1, "T2Cyt": 1}
RECEPTEUR_HAUT = {"ACTH": -1, "GRD": 1, "GR": 1}
ECARTS_PUBLIES = {
    "SS0": {},                                    # l'état sain
    "SS1": RECEPTEUR_HAUT,
    "SS2": IMMUNITE_TH2,
    "SS3": RECEPTEUR_HAUT | IMMUNITE_TH2,
    "SS4": {"CORT": 1, "GRD": 1, "GR": 1, "T1Cell": 1, "T1Cyt": 1,     # l'état malade :
            "T2Cell": -1, "T2Cyt": -1,                                 # cortisol haut,
            "GnRH": -1, "LH/FSH": -1, "TEST": -1},                     # testostérone basse
}

# Figure 5 de l'article de 2015 : un seul temps, plusieurs cibles à la fois.
# (taux de retour à l'état sain publié en %, {cible: sens du traitement})
FIGURE_5 = [
    (37.06, {"GR": -1, "T1Cyt": -1}),
    (7.99,  {"GR": -1, "T2Cyt": +1}),
    (56.50, {"CORT": -1, "GR": -1, "T1Cyt": -1}),
    (38.08, {"ACTH": -1, "GR": -1, "T1Cyt": -1}),
    (38.06, {"GR": -1, "T1Cyt": -1, "TEST": +1}),
    (37.56, {"GR": -1, "IIR": -1, "T1Cyt": -1}),
    (37.48, {"GR": -1, "T1Cyt": -1, "T2Cyt": +1}),
    (57.32, {"ACTH": -1, "CORT": -1, "GR": -1, "T1Cyt": -1}),
    (56.97, {"CORT": -1, "GR": -1, "IIR": -1, "T1Cyt": -1}),
    (56.31, {"CORT": -1, "GR": -1, "T1Cyt": -1, "TEST": +1}),
    (56.16, {"CORT": -1, "GR": -1, "T1Cyt": -1, "T2Cyt": +1}),
    (46.63, {"ACTH": +1, "CORT": -1, "GR": -1, "T1Cyt": -1}),
]

# Figure 6 : suites d'interventions sur une seule cible, toutes des freinages.
# (taux publié en %, suite des cibles)
FIGURE_6 = [
    (40, ["T1Cyt", "GR"]),
    (52, ["T1Cyt", "GR", "GR"]),
    (63, ["T1Cyt", "GR", "T1Cyt", "GR"]),
    (73, ["T1Cyt", "GR", "T1Cyt", "GR", "GR"]),
]

CIBLES_TRAITABLES = ["ACTH", "CORT", "GR", "IIR", "T1Cyt", "T2Cyt", "TEST"]


def etat_complet(ecarts):
    """Écrit un état sur tous les nœuds à partir de ses seuls écarts à la normale."""
    return {noeud: ecarts.get(noeud, 0) for noeud in RESEAU}


ETATS_PUBLIES = {nom: etat_complet(ecarts) for nom, ecarts in ECARTS_PUBLIES.items()}
SAIN = ETATS_PUBLIES["SS0"]
MALADE = ETATS_PUBLIES["SS4"]


def nom_de(etat):
    """Nom publié d'un état stable donné sous forme de tuple, ou « autre »."""
    for nom, publie in ETATS_PUBLIES.items():
        if etat == tuple(publie.values()):
            return nom
    return "autre"


def issues_nommees(interventions, nb_simulations=10000):
    """Part des essais finissant dans chaque état publié, en partant de l'état malade."""
    brutes = issues(MALADE, RESEAU, interventions, nb_simulations)
    return {nom_de(etat): part for etat, part in brutes.items()}


def retour_au_sain(interventions, nb_simulations=10000):
    return issues_nommees(interventions, nb_simulations).get("SS0", 0.0)


def a_la_suite(cibles, crans):
    """Une suite de freinages, une cible à la fois."""
    return [{cible: -crans} for cible in cibles]


def en_un_temps(traitement, crans):
    """Toutes les cibles en même temps, chacune décalée du nombre de crans demandé."""
    return [{cible: sens * crans for cible, sens in traitement.items()}]


def main():
    print("1. ÉTATS STABLES (4 782 969 états essayés)")
    trouves = etats_stables(RESEAU)
    publies = list(ETATS_PUBLIES.values())
    identiques = len(trouves) == len(publies) and all(etat in publies for etat in trouves)
    print(f"   {len(trouves)} états stables trouvés, {len(publies)} publiés :"
          f" {'identiques' if identiques else 'DIFFÉRENTS'}")

    for crans in (1, 2):
        print(f"\n2. TRAITEMENTS, lecture « {crans} cran{'s' if crans > 1 else ''} »,"
              f" départ : état malade (SS4)")
        seules = max(retour_au_sain([{cible: sens * crans}], 2000)
                     for cible in CIBLES_TRAITABLES for sens in (-1, 1))
        print(f"   meilleure cible seule, un seul temps : {seules:.0%} de retour à l'état sain")
        print(f"   {'T1Cyt puis GR':30s} {retour_au_sain(a_la_suite(['T1Cyt', 'GR'], crans)):6.1%}")
        print(f"   {'GR puis T1Cyt (ordre inverse)':30s}"
              f" {retour_au_sain(a_la_suite(['GR', 'T1Cyt'], crans)):6.1%}")
        print(f"   {'les deux en même temps':30s}"
              f" {retour_au_sain(en_un_temps({'T1Cyt': -1, 'GR': -1}, crans)):6.1%}")
        apres_t1cyt = issues_nommees(a_la_suite(["T1Cyt"], crans))
        print("   après T1Cyt seul :",
              ", ".join(f"{nom} {part:.0%}" for nom, part in sorted(apres_t1cyt.items())))

    print("\n3. FIGURE 6 : suites d'interventions (publié | 1 cran | 2 crans)")
    for publie, cibles in FIGURE_6:
        print(f"   {publie:3d} % | {retour_au_sain(a_la_suite(cibles, 1)):6.1%} |"
              f" {retour_au_sain(a_la_suite(cibles, 2)):6.1%}   {', '.join(cibles)}")

    print("\n4. FIGURE 5 : un seul temps, plusieurs cibles (publié | 1 cran | 2 crans)")
    for publie, traitement in FIGURE_5:
        cibles = ", ".join(f"{cible}{'+' if sens > 0 else '-'}" for cible, sens in traitement.items())
        print(f"   {publie:5.2f} % | {retour_au_sain(en_un_temps(traitement, 1)):6.1%} |"
              f" {retour_au_sain(en_un_temps(traitement, 2)):6.1%}   {cibles}")


if __name__ == "__main__":
    main()
