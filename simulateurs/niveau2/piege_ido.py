"""
Simulateur de niveau 2 : le piège métabolique IDO (Kashi, Davis et Phair, 2019).

Source : https://pmc.ncbi.nlm.nih.gov/articles/PMC6787624
(équations 1 à 3 et légende de la figure 3).

Le modèle
---------
Une seule variable : le tryptophane du cytosol, en molécules par cellule.
- Entrée : le transporteur LAT1, réversible, freiné par les autres acides aminés.
- Sortie : l'enzyme IDO1, inhibée par son propre substrat quand il est abondant.

Comme IDO1 ralentit quand le tryptophane monte, deux états stables coexistent :
un état normal (peu de tryptophane, IDO1 active) et un état « piégé »
(beaucoup de tryptophane, IDO1 presque à l'arrêt). Entre les deux, un seuil.

Ce que ce fichier ajoute à l'article
------------------------------------
À lire comme des explorations du modèle, pas comme des résultats publiés :
- la valeur de chaque levier à laquelle un des deux états disparaît ;
- les durées d'entrée dans le piège et de sortie (l'article ne publie que des états stationnaires) ;
- une IDO2 fonctionnelle, que l'article suppose inactive et ne chiffre pas.

Unités : molécules par cellule pour les quantités, jours pour les durées.
Usage  : python3 piege_ido.py
"""

from dataclasses import dataclass, replace

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

MINUTES_PAR_JOUR = 1440

# États stationnaires publiés (un seul chiffre significatif dans l'article).
TRP_NORMAL_PUBLIE = 2e7
TRP_PIEGE_PUBLIE = 5e9


@dataclass(frozen=True)
class Parametres:
    """Valeurs de la légende de la figure 3, sauf les deux dernières (extension IDO2)."""

    kcat_ido1: float = 84.0        # tryptophanes dégradés par minute et par enzyme
    ido1: float = 208.0            # enzymes IDO1 par cellule
    km_ido1: float = 3.4e7
    ki_ido1: float = 2.5e8         # inhibition d'IDO1 par le tryptophane lui-même
    vmax_lat1: float = 1.2e8       # « Vmf » : vitesse maximale d'entrée, par minute
    trp_externe: float = 1.5e9     # « TECF » : tryptophane du liquide extracellulaire
    keq: float = 3.43
    ks_externe: float = 2.2e10
    ks_cytosol: float = 2.0e9
    concurrents: float = 5.0e6     # « A » : autres grands acides aminés neutres
    ki_concurrents: float = 4.3e3
    # Extension hors article : IDO2, une enzyme sans inhibition par le substrat.
    vmax_ido2: float = 0.0         # 0 = IDO2 inactive, comme le suppose l'article
    km_ido2: float = 6.8e8         # 20 x km_ido1 : rapport des valeurs in vitro citées (100 µM / 5 µM)


def flux_lat1(trp, p):
    """Entrée nette de tryptophane par LAT1 (équation 1), en molécules par minute."""
    force_motrice = 1 - trp / (p.trp_externe * p.keq)
    occupation = (1 + p.trp_externe / p.ks_externe + trp / p.ks_cytosol
                  + p.concurrents / p.ki_concurrents)
    return p.vmax_lat1 * force_motrice * (p.trp_externe / p.ks_externe) / occupation


def flux_ido1(trp, p):
    """Dégradation par IDO1 (équation 2) : elle ralentit quand le tryptophane abonde."""
    return p.kcat_ido1 * p.ido1 * trp / (p.km_ido1 + trp * (1 + trp / p.ki_ido1))


def flux_ido2(trp, p):
    """Dégradation par IDO2 (extension) : cinétique simple, sans inhibition."""
    return p.vmax_ido2 * trp / (p.km_ido2 + trp)


def variation_par_jour(trp, p):
    """Équation 3 : ce qui entre moins ce qui est dégradé, en molécules par jour."""
    return MINUTES_PAR_JOUR * (flux_lat1(trp, p) - flux_ido1(trp, p) - flux_ido2(trp, p))


def etats_stationnaires(p):
    """États où entrée et sortie s'équilibrent, du plus bas au plus haut.

    Renvoie une liste de couples (tryptophane, est_stable).
    Un seul couple : un seul état possible. Trois couples : normal, seuil, piégé.
    """
    plafond = p.trp_externe * p.keq    # au-delà, LAT1 ferait sortir le tryptophane
    grille = np.logspace(3, np.log10(plafond), 4000)
    variation = variation_par_jour(grille, p)

    etats = []
    for i in np.flatnonzero(np.sign(variation[:-1]) != np.sign(variation[1:])):
        racine = brentq(variation_par_jour, grille[i], grille[i + 1], args=(p,))
        est_stable = variation[i] > 0    # on passe d'un gain à une perte : on y revient
        etats.append((racine, est_stable))
    return etats


def est_bistable(p):
    return len(etats_stationnaires(p)) == 3


def valeur_critique(p, champ, valeur_monostable):
    """Valeur du paramètre `champ` à laquelle l'un des deux états stables disparaît.

    Dichotomie entre la valeur actuelle (deux états stables) et `valeur_monostable`.
    Renvoie None si `valeur_monostable` laisse encore deux états stables.
    """
    bistable, monostable = getattr(p, champ), valeur_monostable
    if est_bistable(replace(p, **{champ: monostable})):
        return None
    for _ in range(50):
        milieu = (bistable + monostable) / 2
        if est_bistable(replace(p, **{champ: milieu})):
            bistable = milieu
        else:
            monostable = milieu
    return monostable


def jours_de_trajet(depart, arrivee, p):
    """Durée pour que le tryptophane passe de `depart` à `arrivee` avec les paramètres p.

    Renvoie None si le trajet est impossible : la variation s'annule en route
    ou va dans l'autre sens.
    """
    sens = np.sign(arrivee - depart)
    etapes = np.geomspace(depart, arrivee, 400)
    if np.any(sens * variation_par_jour(etapes, p) <= 0):
        return None
    duree, _ = quad(lambda trp: 1 / variation_par_jour(trp, p), depart, arrivee, limit=200)
    return duree


def simuler(trp_initial, etapes):
    """Enchaîne des étapes (durée en jours, paramètres) et renvoie le tryptophane final.

    Sert à vérifier les durées calculées par `jours_de_trajet` avec une méthode indépendante.
    """
    trp = trp_initial
    for duree, p in etapes:
        solution = solve_ivp(lambda t, y: variation_par_jour(y, p), (0, duree), [trp],
                             method="LSODA", rtol=1e-9, atol=1e2)
        trp = solution.y[0, -1]
    return trp


def modifier(p, **facteurs):
    """Copie de p dont chaque paramètre cité est multiplié par son facteur."""
    return replace(p, **{champ: getattr(p, champ) * f for champ, f in facteurs.items()})


def virgule(texte):
    """Notation française des décimales pour l'affichage."""
    return texte.replace(".", ",")


def en_duree(jours):
    if jours < 60:
        return f"{jours:.0f} jours"
    if jours < 730:
        return f"{jours / 30.44:.0f} mois"
    return virgule(f"{jours / 365.25:.1f} ans")


def main():
    base = Parametres()
    (normal, _), (seuil, _), (piege, _) = etats_stationnaires(base)

    print("1. REPRODUCTION DE L'ARTICLE")
    print(f"   état normal  : {normal:.2e} molécules/cellule (publié : ~{TRP_NORMAL_PUBLIE:.0e},"
          f" écart {100 * (normal / TRP_NORMAL_PUBLIE - 1):+.0f} %)")
    print(f"   seuil        : {seuil:.2e} (non publié)")
    print(f"   état piégé   : {piege:.2e} (publié : ~{TRP_PIEGE_PUBLIE:.0e},"
          f" écart {100 * (piege / TRP_PIEGE_PUBLIE - 1):+.0f} %)")
    print(f"   état piégé / état normal : x{piege / normal:.0f}"
          " (publié : plus de deux ordres de grandeur)")
    print(f"   dégradation par IDO1 dans l'état piégé : {flux_ido1(piege, base):.0f} molécules/min,"
          f" contre {flux_ido1(normal, base):.0f} dans l'état normal"
          f" ({100 * (flux_ido1(piege, base) / flux_ido1(normal, base) - 1):+.0f} %)")

    print("\n2. LEVIERS : À QUEL NIVEAU UN DES DEUX ÉTATS DISPARAÎT")
    leviers = [
        ("LAT1, vitesse d'entrée", "vmax_lat1"),
        ("tryptophane externe", "trp_externe"),
        ("quantité d'IDO1", "ido1"),
        ("acides aminés concurrents", "concurrents"),
    ]
    for nom, champ in leviers:
        valeur = getattr(base, champ)
        for cible in (valeur * 1000, valeur / 1000):
            critique = valeur_critique(base, champ, cible)
            (restant, _), = etats_stationnaires(replace(base, **{champ: cible}))
            etat_restant = "normal" if restant < seuil else "piégé"
            facteur = virgule(f"{critique / valeur:.3g}")
            print(f"   {nom:27s} x{facteur:<6s} -> seul l'état {etat_restant} subsiste")
    capacite_ido1 = base.kcat_ido1 * base.ido1
    ido2_critique = valeur_critique(base, "vmax_ido2", 10 * capacite_ido1)
    print(f"   {'IDO2 fonctionnelle':27s} >= {100 * ido2_critique / capacite_ido1:.0f} %"
          " de la capacité d'IDO1 -> seul l'état normal subsiste")

    print("\n3. ENTRÉE DANS LE PIÈGE : DURÉE POUR ALLER DE L'ÉTAT NORMAL AU SEUIL")
    declencheurs = [
        ("LAT1 x2", modifier(base, vmax_lat1=2)),
        ("LAT1 x5", modifier(base, vmax_lat1=5)),
        ("tryptophane externe x2", modifier(base, trp_externe=2)),
        ("IDO1 /2", modifier(base, ido1=0.5)),
        ("IDO1 /10", modifier(base, ido1=0.1)),
    ]
    for nom, p in declencheurs:
        print(f"   {nom:25s} {en_duree(jours_de_trajet(normal, seuil, p))}")

    print("\n4. SORTIE DU PIÈGE : DURÉE POUR REDESCENDRE DE L'ÉTAT PIÉGÉ SOUS LE SEUIL")
    ido2_10 = replace(base, vmax_ido2=0.10 * capacite_ido1)
    ido2_50 = replace(base, vmax_ido2=0.50 * capacite_ido1)
    interventions = [
        ("tryptophane externe /2", modifier(base, trp_externe=0.5)),
        ("tryptophane externe /10", modifier(base, trp_externe=0.1)),
        ("concurrents x10", modifier(base, concurrents=10)),
        ("IDO1 x3", modifier(base, ido1=3)),
        ("IDO1 x10", modifier(base, ido1=10)),
        ("IDO1 x3 + tryptophane /2", modifier(base, ido1=3, trp_externe=0.5)),
        ("IDO2 à 10 % d'IDO1", ido2_10),
        ("IDO2 à 50 % d'IDO1", ido2_50),
    ]
    for nom, p in interventions:
        jusqu_au_seuil = jours_de_trajet(piege, seuil, p)
        if jusqu_au_seuil is None:
            print(f"   {nom:26s} pas de sortie : le piège subsiste")
            continue
        avec_marge = jours_de_trajet(piege, seuil / 2, p)
        print(f"   {nom:26s} seuil franchi en {en_duree(jusqu_au_seuil):9s}"
              f" | avec marge (seuil / 2) : {en_duree(avec_marge)}")

    print("\n5. CONTRÔLE PAR SIMULATION : ARRÊTER TROP TÔT FAIT RECHUTER")
    traitement = modifier(base, ido1=10)
    duree = jours_de_trajet(piege, seuil, traitement)
    for part in (0.9, 1.1):
        final = simuler(piege, [(part * duree, traitement), (20000, base)])
        issue = "retour à l'état normal" if final < seuil else "rechute dans le piège"
        print(f"   IDO1 x10 pendant {part:.0%} de la durée calculée, puis arrêt : {issue}"
              f" ({final:.2e})")


if __name__ == "__main__":
    main()
