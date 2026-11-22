"""
Simulateur de niveau 2 bis : réseaux logiques à plusieurs variables.

Pourquoi ce fichier
-------------------
Le piège IDO (piege_ido.py) n'a qu'une variable : il ne peut pas dire si l'ordre
de deux traitements compte. Il faut pour cela un réseau, où chaque nœud en active
ou en freine d'autres. C'est le formalisme de Craddock et al. (2015).

État du travail (2026-11-22)
----------------------------
Le moteur est construit et vérifié sur deux réseaux de démonstration.
Le réseau de Craddock 2015 n'est PAS chargé : dans l'article, la liste des
interactions n'existe que dans une figure, et la règle de mise à jour que dans
des équations en image. Voir RESULTATS_RESEAU_LOGIQUE.md pour ce qui manque.

Ce qui vient de l'article (texte lu sur la page PLOS ONE)
---------------------------------------------------------
- Chaque nœud vaut -1 (bas), 0 (normal) ou 1 (haut).
- Le réseau évolue un nœud à la fois : parmi les nœuds qui ne sont pas à leur
  valeur visée, on en tire un au sort, et il bouge d'un seul cran.
- Un état est stable quand tous les nœuds sont à leur valeur visée.
- Une intervention décale d'un cran les nœuds traités.
- Comme le tirage au sort compte, on répète la simulation et on mesure
  la part des essais qui reviennent à l'état sain.

Ce qui est provisoire
---------------------
- La valeur visée d'un nœud est ici un simple vote : la somme de ses entrées
  (activatrices moins inhibitrices), ramenée entre -1 et 1. C'est la fonction
  `etat_vise`, à remplacer par la règle de l'article.
- Entre deux interventions, le réseau retrouve ici un état stable. Dans l'article,
  les interventions sont espacées de 10 à 50 pas, stabilisé ou non.

Usage : python3 reseau_logique.py
"""

import random
from collections import Counter
from itertools import permutations, product

VALEURS = (-1, 0, 1)
PAS_MAXIMUM = 1000        # au-delà, on considère que le réseau oscille
NB_SIMULATIONS = 10000
GRAINE = 20261122

# Un réseau est un dictionnaire : nœud -> liste de (source, signe).
# Signe +1 : la source active le nœud. Signe -1 : elle le freine.

# Démonstration 1, sans valeur biologique : une cause qui s'entretient seule,
# et une conséquence entretenue par la cause et par elle-même.
RESEAU_CAUSE_CONSEQUENCE = {
    "cause": [("cause", +1)],
    "consequence": [("cause", +1), ("consequence", +1)],
}

# Démonstration 2 : deux nœuds qui se freinent l'un l'autre (une bascule).
# Son issue dépend du tirage au sort, avec des probabilités calculables à la main.
RESEAU_BASCULE = {
    "a": [("b", -1)],
    "b": [("a", -1)],
}


def borner(valeur):
    return max(-1, min(1, valeur))


def etat_vise(etat, reseau):
    """Valeur vers laquelle chaque nœud est attiré. Règle provisoire : le vote."""
    return {noeud: borner(sum(signe * etat[source] for source, signe in entrees))
            for noeud, entrees in reseau.items()}


def etats_stables(reseau):
    """Tous les états où chaque nœud est déjà à sa valeur visée."""
    noeuds = list(reseau)
    stables = []
    for valeurs in product(VALEURS, repeat=len(noeuds)):
        etat = dict(zip(noeuds, valeurs))
        if etat_vise(etat, reseau) == etat:
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
    """Une intervention : décale d'un cran les nœuds traités (+1 ou -1)."""
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
    """Répète la simulation ; renvoie la part des essais finissant dans chaque état."""
    hasard = random.Random(graine)
    decompte = Counter()
    for _ in range(nb_simulations):
        final = traiter(depart, reseau, interventions, hasard)
        decompte[tuple(final.values()) if final else "oscillation"] += 1
    return {etat: nombre / nb_simulations for etat, nombre in decompte.items()}


def taux_de_retour(depart, cible, reseau, interventions):
    """Part des essais qui finissent dans l'état cible."""
    return issues(depart, reseau, interventions).get(tuple(cible.values()), 0.0)


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
