"""
Simulateur de niveau 2 bis : moteur de réseaux logiques à plusieurs variables.

Pourquoi ce fichier
-------------------
Le piège IDO (piege_ido.py) n'a qu'une variable : il ne peut pas dire si l'ordre
de deux traitements compte. Il faut pour cela un réseau, où chaque nœud en active
ou en freine d'autres. Ce moteur applique les règles de Craddock et al. :
la logique vient de l'article de 2014, la simulation de celui de 2015.
Le réseau de ces articles est dans craddock_2015.py.

Les règles
----------
- Chaque nœud vaut -1 (bas), 0 (normal) ou 1 (haut).
- Un réseau est un dictionnaire : nœud -> (activateurs, inhibiteurs).
- Chaque nœud est attiré vers une « valeur visée », calculée à partir de ses entrées
  (équation 2 et tables 1 à 3 de l'article de 2014) :
    - on retient l'activateur le plus haut et l'inhibiteur le plus haut ;
    - un nœud qui n'a que des activateurs prend la valeur du plus haut ;
    - un nœud qui n'a que des inhibiteurs prend l'opposé du plus haut ;
    - un nœud qui a les deux ne réagit qu'aux entrées hautes : il vise 1 si un
      activateur est haut, perd un cran si un inhibiteur est haut, et vise 0 sinon.
- Le réseau évolue un nœud à la fois : parmi les nœuds qui ne sont pas à leur
  valeur visée, on en tire un au sort, et il bouge d'un seul cran.
- Un état est stable quand tous les nœuds sont à leur valeur visée.
- Une intervention décale les nœuds traités (équation 4 de l'article de 2015).
- Comme le tirage au sort compte, on répète la simulation et on mesure
  la part des essais qui finissent dans chaque état.

Simplification assumée
----------------------
Après chaque intervention, le réseau évolue ici jusqu'à un état stable avant
l'intervention suivante. Dans l'article, les interventions sont séparées par
un nombre de pas fixé, de 10 à 50.

Usage : python3 reseau_logique.py   (deux réseaux de démonstration)
"""

import random
from collections import Counter
from itertools import permutations, product

VALEURS = (-1, 0, 1)
PAS_MAXIMUM = 1000        # au-delà, on considère que le réseau oscille
NB_SIMULATIONS = 10000
GRAINE = 20261122

# Démonstration 1, sans valeur biologique : une cause qui s'entretient seule,
# et une conséquence entretenue par la cause et par elle-même.
RESEAU_CAUSE_CONSEQUENCE = {
    "cause": (["cause"], []),
    "consequence": (["cause", "consequence"], []),
}

# Démonstration 2 : deux nœuds qui se freinent l'un l'autre (une bascule).
# Son issue dépend du tirage au sort, avec des probabilités calculables à la main.
RESEAU_BASCULE = {
    "a": ([], ["b"]),
    "b": ([], ["a"]),
}


def borner(valeur):
    return max(-1, min(1, valeur))


def valeur_visee(noeud, etat, reseau):
    """Valeur vers laquelle un nœud est attiré. Chaque nœud a au moins une entrée."""
    activateurs, inhibiteurs = reseau[noeud]
    activation = max((etat[source] for source in activateurs), default=None)
    inhibition = max((etat[source] for source in inhibiteurs), default=None)

    if inhibition is None:
        return activation
    if activation is None:
        return -inhibition
    if inhibition == 1:
        return 0 if activation == 1 else -1
    return 1 if activation == 1 else 0


def etat_vise(etat, reseau):
    return {noeud: valeur_visee(noeud, etat, reseau) for noeud in reseau}


def etats_stables(reseau):
    """Tous les états où chaque nœud est déjà à sa valeur visée.

    Tous les états sont essayés : 3 puissance le nombre de nœuds.
    """
    noeuds = list(reseau)
    stables = []
    for valeurs in product(VALEURS, repeat=len(noeuds)):
        etat = dict(zip(noeuds, valeurs))
        if all(valeur_visee(noeud, etat, reseau) == etat[noeud] for noeud in noeuds):
            stables.append(etat)
    return stables


def evoluer(etat, reseau, hasard):
    """Laisse le réseau évoluer seul jusqu'à un état stable.

    À chaque pas, un seul nœud bouge d'un cran, tiré au sort parmi ceux
    qui ne sont pas à leur valeur visée. Renvoie None si le réseau oscille.
    """
    for _ in range(PAS_MAXIMUM):
        vise = etat_vise(etat, reseau)
        en_mouvement = [noeud for noeud in reseau if etat[noeud] != vise[noeud]]
        if not en_mouvement:
            return etat
        noeud = hasard.choice(en_mouvement)
        cran = 1 if vise[noeud] > etat[noeud] else -1
        etat = etat | {noeud: etat[noeud] + cran}
    return None


def intervenir(etat, poussee):
    """Une intervention : décale les nœuds traités. Exemple : {"GR": -1} baisse GR d'un cran."""
    return {noeud: borner(valeur + poussee.get(noeud, 0)) for noeud, valeur in etat.items()}


def traiter(etat, reseau, interventions, hasard):
    """Laisse le réseau s'équilibrer, puis applique les interventions dans l'ordre.

    Après chaque intervention, le réseau évolue seul jusqu'à un état stable.
    Renvoie l'état final, ou None si le réseau oscille.
    """
    etat = evoluer(etat, reseau, hasard)
    for poussee in interventions:
        if etat is None:
            return None
        etat = evoluer(intervenir(etat, poussee), reseau, hasard)
    return etat


def issues(depart, reseau, interventions=(), nb_simulations=NB_SIMULATIONS, graine=GRAINE):
    """Répète la simulation ; renvoie la part des essais finissant dans chaque état.

    Les états finaux sont donnés sous forme de tuples, dans l'ordre des nœuds du réseau.
    """
    hasard = random.Random(graine)
    decompte = Counter()
    for _ in range(nb_simulations):
        final = traiter(depart, reseau, interventions, hasard)
        decompte[tuple(final.values()) if final else "oscillation"] += 1
    return {etat: nombre / nb_simulations for etat, nombre in decompte.items()}


def taux_de_retour(depart, cible, reseau, interventions, nb_simulations=NB_SIMULATIONS):
    """Part des essais qui finissent dans l'état cible."""
    return issues(depart, reseau, interventions, nb_simulations).get(tuple(cible.values()), 0.0)


def main():
    reseau = RESEAU_CAUSE_CONSEQUENCE
    sain = {"cause": 0, "consequence": 0}
    malade = {"cause": 1, "consequence": 1}
    freiner = {"la cause": {"cause": -1}, "la conséquence": {"consequence": -1}}

    print("DÉMONSTRATION 1 : cause et conséquence (sans valeur biologique)")
    print(f"  états stables (cause, conséquence) : "
          f"{[tuple(etat.values()) for etat in etats_stables(reseau)]}")
    print("  départ : cause et conséquence hautes ; retour à l'état sain :")
    for ordre in permutations(freiner):
        taux = taux_de_retour(malade, sain, reseau, [freiner[nom] for nom in ordre])
        print(f"    freiner {' puis '.join(ordre):36s} {taux:6.0%}")
    ensemble = {"cause": -1, "consequence": -1}
    print(f"    freiner {'les deux en même temps':36s} "
          f"{taux_de_retour(malade, sain, reseau, [ensemble]):6.0%}")

    print("\nDÉMONSTRATION 2 : la bascule (issue tirée au sort)")
    print("  départ : a et b hauts, aucune intervention ; état final (a, b) :")
    for etat, part in sorted(issues({"a": 1, "b": 1}, RESEAU_BASCULE).items()):
        print(f"    {str(etat):10s} {part:6.1%}")
    print("  attendu par le calcul : (0, 0) 50 %, (-1, 1) 25 %, (1, -1) 25 %")


if __name__ == "__main__":
    main()
