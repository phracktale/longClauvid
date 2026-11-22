"""
Prépare la relecture des pistes de la banque, puis contrôle les citations des relecteurs.

Le relecteur lit une piste et les copies locales de ses sources (outils/sources_banque.py),
en suivant outils/consigne-relecteur.md. Il rend un fichier de relecture où chaque affirmation
de la piste porte un verdict et une citation de la source.

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


def citations_introuvables(relecture, copies=COPIE):
    """Renvoie les affirmations dont la citation n'est pas mot pour mot dans la copie locale nommée."""
    introuvables = []
    for affirmation in relecture["affirmations"]:
        citation = sans_espaces(affirmation.get("citation") or "")
        fichier = copies / Path(affirmation.get("fichier") or "absent").name
        if not citation:
            if affirmation["verdict"] == "confirmée":      # une confirmation sans citation ne vaut rien
                introuvables.append(affirmation)
        elif not fichier.is_file() or citation not in sans_espaces(fichier.read_text(encoding="utf-8")):
            introuvables.append(affirmation)
    return introuvables


def controler():
    for fichier in sorted(DOSSIERS.glob("B*.json")):
        relecture = json.loads(fichier.read_text(encoding="utf-8"))
        verdicts = Counter(affirmation["verdict"] for affirmation in relecture["affirmations"])
        doutes = [str(q["question"]) for q in relecture["grille"] if q["doute"] == "oui"]
        introuvables = citations_introuvables(relecture)
        print(f"{relecture['id']}  {len(relecture['affirmations'])} affirmations : "
              + ", ".join(f"{nombre} {verdict}" for verdict, nombre in verdicts.most_common())
              + f" ; doutes aux questions {', '.join(doutes) or 'aucune'}"
              + f" ; {len(introuvables)} citation(s) introuvable(s)")
        for affirmation in introuvables:
            print(f"      introuvable [{affirmation['verdict']}] {affirmation['affirmation'][:110]}")


def main():
    if sys.argv[1:] == ["preparer"]:
        preparer()
    elif sys.argv[1:] == ["controler"]:
        controler()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
