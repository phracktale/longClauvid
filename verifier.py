"""
Vérifie tout le dépôt en une commande : python3 verifier.py

Cinq blocs, chacun avec un contrôle négatif (on vérifie aussi que l'outil
sait dire non) :
1. le registre est valide, et un registre abîmé est bien refusé ;
2. le simulateur de niveau 1 ne voit pas d'effet là où il n'y en a pas ;
3. le simulateur de niveau 2 retrouve les valeurs publiées de Kashi 2019,
   et une sortie du piège interrompue trop tôt mène bien à la rechute ;
4. le moteur de réseaux logiques retrouve des résultats calculables à la main,
   et un traitement donné dans le mauvais ordre échoue bien ;
5. le réseau de Craddock redonne les cinq états stables publiés, et la figure
   de 2014, qui diffère sur deux flèches, ne les redonne pas.

Durée : environ une demi-minute, dont la moitié pour essayer les 4,8 millions d'états
du réseau de Craddock.

Le script s'arrête avec un code d'erreur si un contrôle échoue.
"""

import copy
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

RACINE = Path(__file__).resolve().parent
for dossier in ("outils", "simulateurs/niveau1", "simulateurs/niveau2"):
    sys.path.append(str(RACINE / dossier))

import craddock_2015             # noqa: E402  (import après l'ajout des dossiers)
import piege_ido                 # noqa: E402
import reseau_logique            # noqa: E402
import simulateur_endotypes     # noqa: E402
import valider_registre         # noqa: E402

echecs = []


def controle(libelle, reussi, detail=""):
    print(f"  {'OK   ' if reussi else 'ÉCHEC'} {libelle}{' : ' + detail if detail else ''}")
    if not reussi:
        echecs.append(libelle)


def proche(valeur, attendu, tolerance):
    return abs(valeur - attendu) <= tolerance


# Une entrée de banque complète : les contrôles la dégradent pour vérifier qu'elle est alors refusée.
ENTREE_DE_BANQUE = {
    "id": "B000", "titre": "Exemple", "domaine_source": "Exemple", "processus_commun": "Exemple",
    "enonce": "Exemple", "pourquoi_inexploree": "Exemple", "test_propose": "Exemple",
    "donnees_existantes": "aucune trouvée", "risques": "Exemple", "niveau": "D",
    "sources": [{"titre": "Article", "url": "https://exemple.org", "lu": "page"}],
    "origine": "exemple", "date": "2026-11-22", "statut": "à vérifier",
}


def verifier_registre():
    print("1. Registre")
    registre = valider_registre.charger()
    erreurs = valider_registre.erreurs_du_registre(registre)
    controle("le registre est valide", not erreurs, f"{len(erreurs)} erreur(s)")

    abime = copy.deepcopy(registre)
    abime["hypotheses"][0]["refutation"] = ""
    abime["pistes"][0]["sources"] = ["source-inventee"]
    abime["transpositions"][0]["deja_tente"] = ""
    abime["transpositions"][0]["liens"] = ["H99"]
    paire_retiree = abime["confrontations"].pop()["paire"]
    abime["confrontations"][0]["si_seconde"] = abime["confrontations"][0]["si_premiere"]
    abime["banque"] = [
        ENTREE_DE_BANQUE | {"id": "B-sans-source", "sources": []},
        ENTREE_DE_BANQUE | {"id": "B-de-memoire", "sources": [{"titre": "Article", "url": "https://exemple.org"}]},
        ENTREE_DE_BANQUE | {"id": "B-ecartee", "statut": "écartée"},
        ENTREE_DE_BANQUE | {"id": "B-non-relue", "statut": "vérifiée"},
    ]
    refus = valider_registre.erreurs_du_registre(abime)
    controle("une hypothèse sans réfutation est refusée",
             any("refutation" in erreur for erreur in refus))
    controle("une source inventée est refusée",
             any("source-inventee" in erreur for erreur in refus))
    controle("une transposition qui tait ce qui a déjà été tenté est refusée",
             any("deja_tente" in erreur for erreur in refus))
    controle("une transposition liée à une hypothèse inexistante est refusée",
             any("H99" in erreur for erreur in refus))
    controle("une paire d'hypothèses sans confrontation est signalée",
             any(f"paire manquante {'-'.join(paire_retiree)}" in erreur for erreur in refus))
    controle("deux prédictions identiques dans une confrontation sont refusées",
             any("prédictions sont identiques" in erreur for erreur in refus))
    controle("une entrée de banque sans source est refusée",
             any("B-sans-source : champ « sources »" in erreur for erreur in refus))
    controle("une source de banque qui ne dit pas comment elle a été lue est refusée",
             any("B-de-memoire : source sans mention" in erreur for erreur in refus))
    controle("une entrée de banque écartée sans motif est refusée",
             any("B-ecartee : écartée sans motif" in erreur for erreur in refus))
    controle("une entrée de banque vérifiée sans relecture est refusée",
             any("B-non-relue : vérifiée sans relecture datée" in erreur for erreur in refus))
    controle("une entrée de banque complète est acceptée",
             not valider_registre.erreurs_du_registre(registre | {"banque": [ENTREE_DE_BANQUE]}))


def verifier_niveau_1():
    print("2. Simulateur de niveau 1 (plans d'essai)")
    generateur = np.random.default_rng(simulateur_endotypes.GRAINE)

    faux_parallele = simulateur_endotypes.puissance_parallele(200, 0.3, 0.0, generateur)
    faux_moyen, faux_hetero = simulateur_endotypes.puissances_n_de_1(60, 3, 0.3, 0.0, 0.5, generateur)
    controle("effet nul, essai parallèle : 2,5 % de faux positifs attendus",
             proche(faux_parallele, 0.025, 0.005), f"{faux_parallele:.1%}")
    controle("effet nul, N-de-1, effet moyen : 2,5 % attendus",
             proche(faux_moyen, 0.025, 0.005), f"{faux_moyen:.1%}")
    controle("effet nul, N-de-1, hétérogénéité : 5 % attendus",
             proche(faux_hetero, 0.05, 0.007), f"{faux_hetero:.1%}")

    simulation = simulateur_endotypes.puissance_parallele(200, 0.2, 0.8, generateur)
    formule = simulateur_endotypes.puissance_parallele_formule(200, 0.2, 0.8)
    controle("la simulation recoupe la formule analytique à 1,5 point près",
             proche(simulation, formule, 0.015), f"{simulation:.1%} contre {formule:.1%}")


def verifier_niveau_2():
    print("3. Simulateur de niveau 2 (piège métabolique IDO)")
    base = piege_ido.Parametres()
    etats = piege_ido.etats_stationnaires(base)
    controle("trois états stationnaires : stable, instable, stable",
             [stable for _, stable in etats] == [True, False, True])
    (normal, _), (seuil, _), (piege, _) = etats

    controle("état normal à 25 % près de la valeur publiée (~2e7)",
             proche(normal / piege_ido.TRP_NORMAL_PUBLIE, 1, 0.25), f"{normal:.2e}")
    controle("état piégé à 25 % près de la valeur publiée (~5e9)",
             proche(piege / piege_ido.TRP_PIEGE_PUBLIE, 1, 0.25), f"{piege:.2e}")
    controle("état piégé plus de 100 fois au-dessus de l'état normal",
             piege / normal > 100, f"x{piege / normal:.0f}")

    plus_de_lat1 = piege_ido.etats_stationnaires(piege_ido.modifier(base, vmax_lat1=3))
    moins_de_lat1 = piege_ido.etats_stationnaires(piege_ido.modifier(base, vmax_lat1=1 / 3))
    controle("LAT1 augmenté : seul l'état piégé subsiste (affirmation de l'article)",
             len(plus_de_lat1) == 1 and plus_de_lat1[0][0] > seuil)
    controle("LAT1 diminué : seul l'état normal subsiste (affirmation de l'article)",
             len(moins_de_lat1) == 1 and moins_de_lat1[0][0] < seuil)

    # Contrôle négatif : deux méthodes indépendantes doivent s'accorder sur le seuil.
    traitement = piege_ido.modifier(base, ido1=10)
    duree = piege_ido.jours_de_trajet(piege, seuil, traitement)
    trop_court = piege_ido.simuler(piege, [(0.9 * duree, traitement), (20000, base)])
    assez_long = piege_ido.simuler(piege, [(1.1 * duree, traitement), (20000, base)])
    controle("traitement arrêté à 90 % de la durée calculée : rechute",
             proche(trop_court / piege, 1, 0.01))
    controle("traitement poursuivi à 110 % : retour à l'état normal",
             proche(assez_long / normal, 1, 0.01))

    sans_ido2 = piege_ido.jours_de_trajet(piege, seuil, replace(base, vmax_ido2=0.0))
    controle("sans intervention, on ne sort pas du piège", sans_ido2 is None)


def verifier_reseau_logique():
    print("4. Simulateur de niveau 2 bis (réseaux logiques)")
    reseau = reseau_logique.RESEAU_CAUSE_CONSEQUENCE
    sain = {"cause": 0, "consequence": 0}
    malade = {"cause": 1, "consequence": 1}
    stables = reseau_logique.etats_stables(reseau)
    controle("cause et conséquence : 6 états stables, dont le sain et le malade",
             len(stables) == 6 and sain in stables and malade in stables)

    cause_dabord = reseau_logique.taux_de_retour(
        malade, sain, reseau, [{"cause": -1}, {"consequence": -1}])
    consequence_dabord = reseau_logique.taux_de_retour(
        malade, sain, reseau, [{"consequence": -1}, {"cause": -1}])
    controle("freiner la cause puis la conséquence ramène toujours à l'état sain",
             cause_dabord == 1.0, f"{cause_dabord:.0%}")
    # Contrôle négatif : dans l'ordre inverse, la cause rallume la conséquence.
    controle("dans l'ordre inverse, le traitement échoue toujours",
             consequence_dabord == 0.0, f"{consequence_dabord:.0%}")

    bascule = reseau_logique.issues({"a": 1, "b": 1}, reseau_logique.RESEAU_BASCULE)
    controle("bascule : état (0, 0) dans 50 % des tirages, à 2 points près (calcul à la main)",
             proche(bascule.get((0, 0), 0), 0.50, 0.02), f"{bascule.get((0, 0), 0):.1%}")
    controle("bascule : état (-1, 1) dans 25 % des tirages, à 2 points près",
             proche(bascule.get((-1, 1), 0), 0.25, 0.02), f"{bascule.get((-1, 1), 0):.1%}")


def verifier_craddock():
    print("5. Réseau de Craddock (états stables publiés, ordre des traitements)")
    reseau = craddock_2015.RESEAU
    trouves = reseau_logique.etats_stables(reseau)
    publies = list(craddock_2015.ETATS_PUBLIES.values())
    controle("les 5 états stables publiés sont retrouvés, et eux seuls",
             len(trouves) == 5 and all(etat in publies for etat in trouves),
             f"{len(trouves)} trouvés parmi {3 ** len(reseau):,} états".replace(",", " "))

    # Contrôle négatif : la figure de 2014 fait freiner T1Cell par le cortisol
    # et n'a pas la flèche T1Cyt -> T1Cell. L'état malade publié n'y est pas stable.
    figure_2014 = reseau | {"T1Cell": (["IIR", "TEST"], ["CORT", "T2Cyt"])}
    malade = craddock_2015.MALADE
    controle("contrôle négatif : avec la figure de 2014, l'état malade n'est plus stable",
             reseau_logique.etat_vise(malade, figure_2014) != malade)

    une_cible = max(craddock_2015.retour_au_sain([{cible: sens}], 2000)
                    for cible in craddock_2015.CIBLES_TRAITABLES for sens in (-1, 1))
    controle("aucune cible seule ne ramène à l'état sain (comme dans l'article)",
             une_cible == 0.0, f"{une_cible:.0%}")

    bon_ordre = craddock_2015.retour_au_sain(craddock_2015.a_la_suite(["T1Cyt", "GR"], 1))
    mauvais_ordre = craddock_2015.retour_au_sain(craddock_2015.a_la_suite(["GR", "T1Cyt"], 1))
    controle("T1Cyt puis GR : un quart de retours, à 2 points près (calcul : 1/2 x 1/2)",
             proche(bon_ordre, 0.25, 0.02), f"{bon_ordre:.1%}")
    controle("GR puis T1Cyt, l'ordre inverse : aucun retour à l'état sain",
             mauvais_ordre == 0.0, f"{mauvais_ordre:.1%}")

    # Figure 5 de l'article : les lignes sans hausse de TEST ni de T2Cyt, sauf la deuxième.
    lignes_retrouvees = [0, 1, 2, 3, 5, 7, 8, 11]
    ecarts = []
    for numero in lignes_retrouvees:
        publie, traitement = craddock_2015.FIGURE_5[numero]
        simule = craddock_2015.retour_au_sain(craddock_2015.en_un_temps(traitement, 2))
        ecarts.append(abs(100 * simule - publie))
    controle("figure 5, lecture « 2 crans » : 8 taux publiés sur 12 retrouvés à 2 points près",
             max(ecarts) <= 2.0, f"écart maximal {max(ecarts):.1f} point")


def main():
    verifier_registre()
    verifier_niveau_1()
    verifier_niveau_2()
    verifier_reseau_logique()
    verifier_craddock()
    if echecs:
        print(f"\n{len(echecs)} contrôle(s) en échec.")
        sys.exit(1)
    print("\nTous les contrôles passent.")


if __name__ == "__main__":
    main()
