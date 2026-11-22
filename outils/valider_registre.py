"""
Valide le registre des hypothèses.

C'est le critère de passage de la phase 0 du protocole :
« chaque hypothèse porte une prédiction réfutable », et rien n'est affirmé sans source.

Ce que le script contrôle
-------------------------
- les identifiants sont uniques ;
- chaque source a une adresse, un type connu et une date de lecture ;
- chaque piste a un niveau de preuve (A à D) et ne cite que des sources existantes ;
- chaque hypothèse a un énoncé, une prédiction, une réfutation, un test et un historique,
  et ne cite que des pistes, des sources et un endotype existants ;
- chaque endotype renvoie à une hypothèse existante ;
- chaque transposition dit ce qui a déjà été tenté, porte un degré de maîtrise connu
  et ne renvoie qu'à des sources, pistes, hypothèses et endotypes existants.

Usage : python3 outils/valider_registre.py
"""

import sys
from pathlib import Path

import yaml

REGISTRE = Path(__file__).resolve().parent.parent / "registre"

TYPES_DE_SOURCE = {"article", "prepublication", "registre", "institution",
                   "communique", "presse", "forum"}
NIVEAUX_DE_PREUVE = {"A", "B", "C", "D"}
STATUTS = {"ouverte", "soutenue", "affaiblie", "réfutée", "abandonnée"}
MAITRISES = {"guérison", "rémission", "contrôle", "prévention", "échec"}
LONGUEUR_MINIMALE = 40    # caractères : une prédiction tient au moins en une phrase

CHAMPS_SOURCE = ["id", "titre", "url", "type", "lu_le"]
CHAMPS_PISTE = ["id", "nom", "resultat", "inexploite", "niveau", "sources"]
CHAMPS_ENDOTYPE = ["id", "nom", "marqueurs", "candidats"]
CHAMPS_HYPOTHESE = ["id", "titre", "statut", "creee_le", "pistes", "enonce",
                    "prediction", "refutation", "test", "historique"]
CHAMPS_TRANSPOSITION = ["id", "nom", "processus", "maladie", "maitrise", "levier", "preuve",
                        "deja_tente", "lecon", "prochain_test", "niveau", "liens", "sources"]


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
    for transposition in registre["transpositions"]:
        citees.update(transposition.get("sources") or [])
    return sorted({source["id"] for source in registre["sources"]} - citees)


def main():
    registre = charger()
    erreurs = erreurs_du_registre(registre)

    print(f"Registre : {len(registre['hypotheses'])} hypothèses, {len(registre['pistes'])} pistes,"
          f" {len(registre['endotypes'])} endotypes, {len(registre['transpositions'])} transpositions,"
          f" {len(registre['sources'])} sources.")
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
