"""
Prépare la lecture des résumés retenus par la carte, puis contrôle et compte ce que les lecteurs rendent.

Phase 1 du protocole, pour une piste à la fois : un lecteur lit chaque résumé retenu par les termes de la piste
(analyses/cartographie/cartographie.py) en suivant outils/consigne-lecteur.md. Il dit si l'étude porte vraiment
sur la piste, de quel type elle est, et en tire des relations entité–relation–entité, chacune avec une citation.

Les lots et les fichiers rendus restent dans cache/cartographie/, hors du dépôt : ils contiennent les résumés.
Seuls des décomptes et des identifiants d'articles (DOI) entrent au dépôt.

Usage :
    python3 analyses/cartographie/lots.py preparer P08 P14 P01    # des lots de 35 résumés dans cache/cartographie/
    python3 analyses/cartographie/lots.py controler               # citations retrouvées mot pour mot, décomptes
    python3 analyses/cartographie/lots.py echantillon 30          # tire au sort des relations à relire (graine fixe)
"""

import json
import random
import sys
from collections import Counter
from pathlib import Path

from cartographie import BIBLIOTHEQUE, PISTES, RACINE, annee, compter, sans_doublons

DOSSIER = RACINE / "cache" / "cartographie"
TAILLE_DU_LOT = 35
GRAINE = 20261123
RESUME_MINIMAL = 300        # caractères ; en dessous, le résumé est tronqué et la lecture ne reposerait que sur le titre
PERTINENCES = {"centrale", "secondaire", "en passant"}
TYPES = {"mesure chez des patients", "essai", "méta-analyse", "modèle animal ou cellulaire", "revue", "hypothèse",
         "autre"}
VERBES = {"increased_in", "decreased_in", "unchanged_in", "detected_in", "not_detected_in", "associated_with",
          "not_associated_with", "causes", "improves", "does_not_improve", "predicts", "binds"}
POPULATIONS = {"COVID long", "EM/SFC", "COVID-19 aigu", "autre"}
SENS = {"soutient", "contredit", "neutre"}


def dans_la_grille(valeur, grille):
    return valeur if valeur in grille else "hors grille"


def sans_espaces(texte):
    return " ".join((texte or "").split())


def preparer(pistes):
    references = sans_doublons(json.loads(BIBLIOTHEQUE.read_text(encoding="utf-8"))["references"])
    for piste in pistes:
        nom, motifs = PISTES[piste]
        numeros = compter(references, motifs)
        avec_resume = [n for n in numeros if len(references[n].get("abstractNote") or "") >= RESUME_MINIMAL]
        dossier = DOSSIER / piste
        dossier.mkdir(parents=True, exist_ok=True)
        for debut in range(0, len(avec_resume), TAILLE_DU_LOT):
            lot = [{"numero": n, "titre": references[n].get("title"), "annee": annee(references[n]),
                    "doi": references[n].get("DOI"), "resume": references[n].get("abstractNote")}
                   for n in avec_resume[debut:debut + TAILLE_DU_LOT]]
            fichier = dossier / f"{piste}-lot-{debut // TAILLE_DU_LOT + 1:02d}.json"
            fichier.write_text(json.dumps({"piste": piste, "sujet": nom, "termes": motifs, "references": lot},
                                          ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{piste} {nom} : {len(numeros)} références retenues, {len(avec_resume)} avec un résumé "
              f"d'au moins {RESUME_MINIMAL} caractères, "
              f"{-(-len(avec_resume) // TAILLE_DU_LOT)} lot(s)")


def lectures():
    """Renvoie (piste, lecture, résumé d'origine) pour chaque référence lue."""
    for rendu in sorted(DOSSIER.glob("P*/P*-lot-*-lu.json")):
        lot = json.loads(Path(str(rendu).replace("-lu.json", ".json")).read_text(encoding="utf-8"))
        resumes = {reference["numero"]: reference for reference in lot["references"]}
        for lecture in json.loads(rendu.read_text(encoding="utf-8"))["lectures"]:
            yield lot["piste"], lecture, resumes.get(lecture["numero"])


def controler():
    par_piste = {}
    for piste, lecture, origine in lectures():
        bilan = par_piste.setdefault(piste, {"lues": 0, "pertinence": Counter(), "type": Counter(), "sens": Counter(),
                                             "verbe": Counter(), "population": Counter(),
                                             "relations": 0, "introuvables": 0, "hors_grille": 0})
        bilan["lues"] += 1
        if (origine is None or lecture.get("pertinence") not in PERTINENCES or lecture.get("type") not in TYPES):
            bilan["hors_grille"] += 1
            continue
        bilan["pertinence"][lecture["pertinence"]] += 1
        bilan["type"][lecture["type"]] += 1
        for relation in lecture.get("relations") or []:
            bilan["relations"] += 1
            bilan["sens"][dans_la_grille(relation.get("sens"), SENS)] += 1
            bilan["verbe"][dans_la_grille(relation.get("relation"), VERBES)] += 1
            bilan["population"][dans_la_grille(relation.get("population"), POPULATIONS)] += 1
            citation = sans_espaces(relation.get("citation"))
            if not citation or citation not in sans_espaces(origine["resume"]):
                bilan["introuvables"] += 1
    for piste, bilan in sorted(par_piste.items()):
        print(f"{piste} : {bilan['lues']} résumés lus ; pertinence {dict(bilan['pertinence'])} ; type {dict(bilan['type'])} ; "
              f"{bilan['relations']} relations, sens {dict(bilan['sens'])}, verbe {dict(bilan['verbe'])}, "
              f"population {dict(bilan['population'])} ; "
              f"{bilan['introuvables']} citation(s) introuvable(s) ; {bilan['hors_grille']} lecture(s) hors grille")
    return par_piste


def echantillon(taille):
    relations = [(piste, lecture, relation, origine) for piste, lecture, origine in lectures() if origine
                 for relation in lecture.get("relations") or []]
    random.Random(GRAINE).shuffle(relations)
    tirage = [{"piste": piste, "numero": lecture["numero"], "titre": origine["titre"], "resume": origine["resume"],
               "pertinence": lecture.get("pertinence"), "type": lecture.get("type"), "relation": relation}
              for piste, lecture, relation, origine in relations[:taille]]
    fichier = DOSSIER / "echantillon.json"
    fichier.write_text(json.dumps(tirage, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(tirage)} relations tirées au sort parmi {len(relations)} (graine {GRAINE}) : {fichier}")


def main():
    if sys.argv[1:2] == ["preparer"] and sys.argv[2:]:
        preparer(sys.argv[2:])
    elif sys.argv[1:] == ["controler"]:
        controler()
    elif sys.argv[1:2] == ["echantillon"] and sys.argv[2:]:
        echantillon(int(sys.argv[2]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
