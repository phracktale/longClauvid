"""
Prépare la relecture des pistes de la banque, puis contrôle les citations des relecteurs.

Le relecteur lit une piste et les copies locales de ses sources (outils/sources_banque.py),
en suivant outils/consigne-relecteur.md. Il rend un fichier de relecture où chaque affirmation
de la piste porte un verdict et une citation de la source.

Une piste écartée passe ensuite devant un contradicteur, qui la défend contre son motif
en suivant outils/consigne-contradicteur.md. Une piste gardée passe devant un contradicteur qui l'attaque,
en suivant outils/consigne-contradicteur-piste-gardee.md. Leurs citations sont contrôlées de la même façon.

Une citation qu'on ne retrouve pas mot pour mot dans la copie locale est signalée :
c'est le contrôle négatif de la relecture, qu'elle soit faite par une personne ou par un programme.

Les dossiers et les fichiers de relecture restent dans cache/, hors du dépôt : ils citent les articles.

Usage :
    python3 outils/relecture_banque.py preparer     # un dossier par piste dans cache/relecture/
    python3 outils/relecture_banque.py controler    # verdicts et citations de chaque relecture rendue
"""

import json
import sys
from collections import Counter
from pathlib import Path

import yaml

from sources_banque import BANQUE, COPIE, INDEX, RACINE

DOSSIERS = RACINE / "cache" / "relecture"

# Les deux contradicteurs : sous-dossier de leurs fichiers, champ de leurs arguments, sens de ces arguments.
CONTRADICTEURS = (
    ("contre", "defense", "pour la piste"),       # défend une piste écartée
    ("attaque", "attaque", "contre la piste"),    # attaque une piste gardée
)


def copies_d_une_source(source, index):
    """Les copies locales d'une source : celle de l'adresse citée, et celle du champ « texte »."""
    copies = []
    for adresse in (source["url"], source.get("texte")):
        copie = index.get(adresse) if adresse else None
        if copie and copie["fichier"]:
            copies.append(copie)
    return copies


def preparer():
    banque = yaml.safe_load(BANQUE.read_text(encoding="utf-8"))
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    for entree in banque:
        dossier = DOSSIERS / entree["id"]
        dossier.mkdir(parents=True, exist_ok=True)
        (dossier / "fiche.yaml").write_text(
            yaml.dump(entree, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")
        lignes = [f"# Sources de la piste {entree['id']}", ""]
        for numero, source in enumerate(entree["sources"], start=1):
            lignes.append(f"{numero}. {source['titre']}")
            copies = copies_d_une_source(source, index)
            for copie in copies:
                chemin = (COPIE / copie["fichier"]).relative_to(RACINE)
                lignes.append(f"   - {copie['niveau']}, {copie['caracteres']} caractères : `{chemin}`")
            if not copies:
                lignes.append("   - aucune copie locale : la page est bloquée")
        (dossier / "sources.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(banque)} dossiers écrits dans {DOSSIERS}")


def sans_espaces(texte):
    """Ramène tous les blancs à une espace : une citation coupée par un saut de ligne reste retrouvée."""
    return " ".join(texte.split())


def citations_introuvables(elements, copies=COPIE):
    """Renvoie les éléments dont la citation n'est pas mot pour mot dans la copie locale nommée.

    Un élément est une affirmation, avec son verdict, ou un argument du contradicteur, sans verdict.
    """
    introuvables = []
    for element in elements:
        citation = sans_espaces(element.get("citation") or "")
        fichier = copies / Path(element.get("fichier") or "absent").name
        if not citation:
            if element.get("verdict", "confirmée") == "confirmée":   # sans citation, ni confirmation ni argument
                introuvables.append(element)
        elif not fichier.is_file() or citation not in sans_espaces(fichier.read_text(encoding="utf-8")):
            introuvables.append(element)
    return introuvables


def controler():
    for fichier in sorted(DOSSIERS.glob("B*.json")):
        relecture = json.loads(fichier.read_text(encoding="utf-8"))
        verdicts = Counter(affirmation["verdict"] for affirmation in relecture["affirmations"])
        doutes = [str(q["question"]) for q in relecture["grille"] if q["doute"] == "oui"]
        introuvables = citations_introuvables(relecture["affirmations"])
        print(f"{relecture['id']}  {len(relecture['affirmations'])} affirmations : "
              + ", ".join(f"{nombre} {verdict}" for verdict, nombre in verdicts.most_common())
              + f" ; doutes aux questions {', '.join(doutes) or 'aucune'}"
              + f" ; {len(introuvables)} citation(s) introuvable(s)")
        for affirmation in introuvables:
            print(f"      introuvable [{affirmation['verdict']}] {affirmation['affirmation'][:110]}")

    for sous_dossier, champ, sens in CONTRADICTEURS:
        for fichier in sorted((DOSSIERS / sous_dossier).glob("B*.json")):
            contre = json.loads(fichier.read_text(encoding="utf-8"))
            verdicts = Counter(affirmation["verdict"] for affirmation in contre["affirmations"])
            introuvables = citations_introuvables(contre["affirmations"] + contre[champ])
            print(f"{contre['id']}  contradicteur : « {contre['avis']} » ; faits contrôlés : "
                  + ", ".join(f"{nombre} {verdict}" for verdict, nombre in verdicts.most_common())
                  + f" ; {len(contre[champ])} argument(s) {sens}"
                  + f" ; {len(introuvables)} citation(s) introuvable(s)")
            for element in introuvables:
                print(f"      introuvable {(element.get('affirmation') or element.get('argument'))[:110]}")


def main():
    if sys.argv[1:] == ["preparer"]:
        preparer()
    elif sys.argv[1:] == ["controler"]:
        controler()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
