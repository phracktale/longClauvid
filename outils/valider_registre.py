"""
Valide le registre des hypothèses.

Il automatise deux critères de passage du protocole :
- phase 0 : « chaque hypothèse porte une prédiction réfutable », et rien n'est affirmé sans source ;
- phase 3 : « au moins une prédiction opposée par paire d'hypothèses ».

Ce que le script contrôle
-------------------------
- les identifiants sont uniques ;
- chaque source a une adresse, un type connu et une date de lecture ;
- chaque piste a un niveau de preuve (A à D) et ne cite que des sources existantes ;
- chaque hypothèse a un énoncé, une prédiction, une réfutation, un test et un historique,
  et ne cite que des pistes, des sources et un endotype existants ;
- chaque endotype renvoie à une hypothèse existante ;
- chaque transposition dit ce qui a déjà été tenté, porte un degré de maîtrise connu
  et ne renvoie qu'à des sources, pistes, hypothèses et endotypes existants ;
- chaque paire d'hypothèses a sa confrontation, avec deux prédictions différentes ;
- chaque entrée de la banque d'hypothèses à vérifier a ses sources, dit comment elles ont été lues,
  et porte un statut connu ; une entrée écartée donne son motif ; une entrée vérifiée ou écartée
  porte sa relecture, datée, avec sa décision.

Usage : python3 outils/valider_registre.py
"""

import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

import yaml

REGISTRE = Path(__file__).resolve().parent.parent / "registre"

TYPES_DE_SOURCE = {"article", "prepublication", "registre", "institution",
                   "communique", "presse", "forum"}
NIVEAUX_DE_PREUVE = {"A", "B", "C", "D"}
STATUTS = {"ouverte", "soutenue", "affaiblie", "réfutée", "abandonnée"}
MAITRISES = {"guérison", "rémission", "contrôle", "prévention", "échec"}
ACCES = {"échantillons existants", "suivi d'essais", "nouvelle collecte"}
STATUTS_DE_BANQUE = {"à vérifier", "vérifiée", "promue", "écartée"}
LECTURES = {"page", "extrait"}    # la page a été ouverte, ou seul son extrait a été lu
LONGUEUR_MINIMALE = 40    # caractères : une prédiction tient au moins en une phrase

CHAMPS_SOURCE = ["id", "titre", "url", "type", "lu_le"]
CHAMPS_PISTE = ["id", "nom", "resultat", "inexploite", "niveau", "sources"]
CHAMPS_ENDOTYPE = ["id", "nom", "marqueurs", "candidats"]
CHAMPS_HYPOTHESE = ["id", "titre", "statut", "creee_le", "pistes", "enonce",
                    "prediction", "refutation", "test", "historique"]
CHAMPS_TRANSPOSITION = ["id", "nom", "processus", "maladie", "maitrise", "levier", "preuve",
                        "deja_tente", "lecon", "prochain_test", "niveau", "liens", "sources"]
CHAMPS_CONFRONTATION = ["paire", "question", "mesure", "si_premiere", "si_seconde",
                        "acces", "donnees"]
CHAMPS_BANQUE = ["id", "titre", "domaine_source", "processus_commun", "enonce",
                 "pourquoi_inexploree", "test_propose", "donnees_existantes", "risques",
                 "niveau", "sources", "origine", "date", "statut"]


def charger(dossier=REGISTRE):
    """Lit tout le registre et le renvoie sous forme de dictionnaire."""
    def lire(chemin):
        return yaml.safe_load(chemin.read_text(encoding="utf-8"))

    hypotheses = []
    for fichier in sorted((dossier / "hypotheses").glob("*.yaml")):
        hypotheses.append(lire(fichier) | {"fichier": fichier.name})

    return {
        "sources": lire(dossier / "sources.yaml"),
        "pistes": lire(dossier / "pistes.yaml"),
        "endotypes": lire(dossier / "endotypes.yaml"),
        "transpositions": lire(dossier / "transpositions.yaml"),
        "confrontations": lire(dossier / "confrontations.yaml"),
        "banque": lire(dossier / "banque.yaml") or [],
        "hypotheses": hypotheses,
    }


def identifiants(elements, famille, erreurs):
    """Renvoie l'ensemble des identifiants et signale les doublons."""
    tous = [element.get("id") for element in elements]
    for doublon in sorted({i for i in tous if tous.count(i) > 1}):
        erreurs.append(f"{famille} : identifiant en double « {doublon} »")
    return set(tous)


def signaler_champs_vides(element, champs, nom, erreurs):
    for champ in champs:
        if not element.get(champ):
            erreurs.append(f"{nom} : champ « {champ} » absent ou vide")


def signaler_inconnus(cites, connus, nom, famille, erreurs):
    for inconnu in sorted(set(cites or []) - connus):
        erreurs.append(f"{nom} : {famille} inconnue « {inconnu} »")


def erreurs_du_registre(registre):
    """Renvoie la liste des erreurs ; une liste vide signifie que le registre est valide."""
    erreurs = []
    sources = identifiants(registre["sources"], "sources", erreurs)
    pistes = identifiants(registre["pistes"], "pistes", erreurs)
    endotypes = identifiants(registre["endotypes"], "endotypes", erreurs)
    hypotheses = identifiants(registre["hypotheses"], "hypothèses", erreurs)
    identifiants(registre["transpositions"], "transpositions", erreurs)

    for source in registre["sources"]:
        nom = f"source {source.get('id')}"
        signaler_champs_vides(source, CHAMPS_SOURCE, nom, erreurs)
        if not str(source.get("url", "")).startswith("http"):
            erreurs.append(f"{nom} : adresse invalide")
        if source.get("type") not in TYPES_DE_SOURCE:
            erreurs.append(f"{nom} : type inconnu « {source.get('type')} »")

    for piste in registre["pistes"]:
        nom = f"piste {piste.get('id')}"
        signaler_champs_vides(piste, CHAMPS_PISTE, nom, erreurs)
        if piste.get("niveau") not in NIVEAUX_DE_PREUVE:
            erreurs.append(f"{nom} : niveau de preuve inconnu « {piste.get('niveau')} »")
        signaler_inconnus(piste.get("sources"), sources, nom, "source", erreurs)

    for endotype in registre["endotypes"]:
        nom = f"endotype {endotype.get('id')}"
        signaler_champs_vides(endotype, CHAMPS_ENDOTYPE, nom, erreurs)
        if endotype.get("hypothese") and endotype["hypothese"] not in hypotheses:
            erreurs.append(f"{nom} : hypothèse inconnue « {endotype['hypothese']} »")
        for candidat in endotype.get("candidats") or []:
            signaler_inconnus(candidat.get("sources"), sources,
                              f"{nom}, candidat {candidat.get('nom')}", "source", erreurs)

    for hypothese in registre["hypotheses"]:
        nom = f"hypothèse {hypothese.get('id')}"
        signaler_champs_vides(hypothese, CHAMPS_HYPOTHESE, nom, erreurs)
        if not hypothese["fichier"].startswith(f"{hypothese.get('id')}-"):
            erreurs.append(f"{nom} : le fichier {hypothese['fichier']} ne porte pas son identifiant")
        if hypothese.get("statut") not in STATUTS:
            erreurs.append(f"{nom} : statut inconnu « {hypothese.get('statut')} »")
        if hypothese.get("endotype") and hypothese["endotype"] not in endotypes:
            erreurs.append(f"{nom} : endotype inconnu « {hypothese['endotype']} »")
        signaler_inconnus(hypothese.get("pistes"), pistes, nom, "piste", erreurs)
        signaler_inconnus(hypothese.get("sources"), sources, nom, "source", erreurs)
        for champ in ("prediction", "refutation"):
            texte = hypothese.get(champ)
            if texte and len(texte) < LONGUEUR_MINIMALE:    # vide : déjà signalé plus haut
                erreurs.append(f"{nom} : « {champ} » trop courte pour être testable")

    for transposition in registre["transpositions"]:
        nom = f"transposition {transposition.get('id')}"
        signaler_champs_vides(transposition, CHAMPS_TRANSPOSITION, nom, erreurs)
        if transposition.get("maitrise") not in MAITRISES:
            erreurs.append(f"{nom} : maîtrise inconnue « {transposition.get('maitrise')} »")
        if transposition.get("niveau") not in NIVEAUX_DE_PREUVE:
            erreurs.append(f"{nom} : niveau de preuve inconnu « {transposition.get('niveau')} »")
        signaler_inconnus(transposition.get("sources"), sources, nom, "source", erreurs)
        signaler_inconnus(transposition.get("liens"), pistes | hypotheses | endotypes,
                          nom, "fiche liée", erreurs)

    paires_vues = []
    for confrontation in registre["confrontations"]:
        paire = tuple(confrontation.get("paire") or [])
        nom = f"confrontation {'-'.join(paire)}"
        paires_vues.append(tuple(sorted(paire)))
        signaler_champs_vides(confrontation, CHAMPS_CONFRONTATION, nom, erreurs)
        signaler_inconnus(paire, hypotheses, nom, "hypothèse", erreurs)
        signaler_inconnus(confrontation.get("sources"), sources, nom, "source", erreurs)
        if confrontation.get("acces") not in ACCES:
            erreurs.append(f"{nom} : accès inconnu « {confrontation.get('acces')} »")
        if confrontation.get("si_premiere") == confrontation.get("si_seconde"):
            erreurs.append(f"{nom} : les deux prédictions sont identiques")
        for champ in ("si_premiere", "si_seconde"):
            texte = confrontation.get(champ)
            if texte and len(texte) < LONGUEUR_MINIMALE:
                erreurs.append(f"{nom} : « {champ} » trop courte pour être testable")

    paires_attendues = set(combinations(sorted(hypotheses), 2))
    for paire in sorted(paires_attendues - set(paires_vues)):
        erreurs.append(f"confrontations : paire manquante {paire[0]}-{paire[1]}")
    for paire, nombre in sorted(Counter(paires_vues).items()):
        if nombre > 1:
            erreurs.append(f"confrontations : paire en double {'-'.join(paire)}")

    identifiants(registre["banque"], "banque", erreurs)
    for entree in registre["banque"]:
        nom = f"banque {entree.get('id')}"
        signaler_champs_vides(entree, CHAMPS_BANQUE, nom, erreurs)
        if entree.get("niveau") not in NIVEAUX_DE_PREUVE:
            erreurs.append(f"{nom} : niveau de preuve inconnu « {entree.get('niveau')} »")
        if entree.get("statut") not in STATUTS_DE_BANQUE:
            erreurs.append(f"{nom} : statut inconnu « {entree.get('statut')} »")
        for source in entree.get("sources") or []:
            if not source.get("titre") or not str(source.get("url")).startswith("http"):
                erreurs.append(f"{nom} : source sans titre ou sans adresse")
            if source.get("lu") not in LECTURES:
                erreurs.append(f"{nom} : source sans mention « page » ou « extrait »")
        if entree.get("statut") == "écartée" and not entree.get("motif"):
            erreurs.append(f"{nom} : écartée sans motif")
        relecture = entree.get("relecture") or {}
        if entree.get("statut") in ("vérifiée", "écartée") and not (relecture.get("date") and relecture.get("decision")):
            erreurs.append(f"{nom} : {entree['statut']} sans relecture datée")
        if entree.get("statut") == "promue":
            signaler_inconnus([entree.get("promue_en")], pistes | hypotheses,
                              nom, "fiche de promotion", erreurs)

    return erreurs


def sources_jamais_citees(registre):
    """Sources présentes mais citées nulle part : à rattacher ou à retirer."""
    citees = set()
    for piste in registre["pistes"]:
        citees.update(piste.get("sources") or [])
    for hypothese in registre["hypotheses"]:
        citees.update(hypothese.get("sources") or [])
    for endotype in registre["endotypes"]:
        for candidat in endotype.get("candidats") or []:
            citees.update(candidat.get("sources") or [])
    for fiche in registre["transpositions"] + registre["confrontations"]:
        citees.update(fiche.get("sources") or [])
    return sorted({source["id"] for source in registre["sources"]} - citees)


def main():
    registre = charger()
    erreurs = erreurs_du_registre(registre)

    print(f"Registre : {len(registre['hypotheses'])} hypothèses, {len(registre['pistes'])} pistes,"
          f" {len(registre['endotypes'])} endotypes, {len(registre['transpositions'])} transpositions,"
          f" {len(registre['confrontations'])} confrontations, {len(registre['sources'])} sources.")
    par_acces = Counter(confrontation.get("acces") for confrontation in registre["confrontations"])
    print("Confrontations selon l'accès aux données : "
          + " ; ".join(f"{acces}, {nombre}" for acces, nombre in par_acces.most_common()))
    par_statut = Counter(entree.get("statut") for entree in registre["banque"])
    print(f"Banque d'hypothèses à vérifier : {len(registre['banque'])} entrées"
          + "".join(f" ; {statut}, {nombre}" for statut, nombre in par_statut.most_common()))
    orphelines = sources_jamais_citees(registre)
    if orphelines:
        print(f"À noter : {len(orphelines)} sources de contexte, citées par aucune fiche :"
              f" {', '.join(orphelines)}")
    for erreur in erreurs:
        print(f"ERREUR  {erreur}")
    print("Registre valide." if not erreurs else f"{len(erreurs)} erreur(s).")
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
