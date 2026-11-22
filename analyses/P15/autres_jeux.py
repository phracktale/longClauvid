"""
Suite de la piste P15 : le signal de 2019 se retrouve-t-il chez d'autres personnes ?

Applique la section 6 du plan (analyses/P15/PLAN.md) aux jeux de données publics qui remplissent
ses quatre critères et ont des estimations déposées. Les mesures et la règle sont celles du plan :
elles viennent du programme arn_ribosomique.py, sans changement de seuil.

Trois jeux se lisent. Deux autres ont été ouverts et ne remplissent pas le critère 4,
faute de MT-RNR1 et de MT-RNR2 dans leurs fichiers : GSE270045 et GSE128078.

Les données se téléchargent dans cache/P15/autres/, hors du dépôt.

Usage :
    python3 analyses/P15/autres_jeux.py telecharger
    python3 analyses/P15/autres_jeux.py genes     # les listes de gènes, fixées avant de lire les écarts
    python3 analyses/P15/autres_jeux.py           # l'analyse
"""

import csv
import gzip
import math
import re
import shutil
import sys
import tarfile
import urllib.request

from arn_ribosomique import (ARN_MITO, ARTEFACT, CACHE, ECART_FAIBLE, ECART_NET, ILLISIBLE, INDECIDABLE, MENAGE,
                             NON_EXPLIQUE, NON_REPRODUIT, SEUIL_CORRELATION, SEUIL_MENAGE, ecart, ecart_corrige,
                             ecart_des_genes_de_menage, en_log2, intervalle, lien_a_groupe_egal, lire_annotation)

AUTRES = CACHE / "autres"
GEO = "https://ftp.ncbi.nlm.nih.gov/geo/series/"
FICHES = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={serie}&targ=gsm&form=text&view=brief"
ANNOTATION = "https://ftp.ensembl.org/pub/release-113/gtf/homo_sapiens/Homo_sapiens.GRCh38.113.gtf.gz"
DONNEES = {
    "GSE251872": GEO + "GSE251nnn/GSE251872/suppl/GSE251872_RAW.tar",
    "GSE251849": GEO + "GSE251nnn/GSE251849/suppl/GSE251849_Counts.txt.gz",
    "GSE226260": GEO + "GSE226nnn/GSE226260/suppl/GSE226260_AdditionalSamples.rawCounts.csv.gz",
}

PATIENTS, TEMOINS = "patients", "témoins"
PRESENT = "signal présent"
# Section 6 du plan : B se calcule sur les gènes dont le nom commence ainsi.
MOTIF_DE_B = re.compile(r"^(RN18S|RN28S|RN45S|RNA18S|RNA28S|RNA45S)")
MESURES = {"A": "arn_mito", "B": "arn_cyto", "D": "codants_mito"}
# GSE226260 : du plus ancien au plus récent, d'après le champ « time of_blood_draw » des fiches.
RANG_DU_TEMPS = {"Acute": 0, "3_6M": 1, "6_12M": 2, ">12M": 3}


# --- Télécharger ---

def telecharger():
    AUTRES.mkdir(parents=True, exist_ok=True)
    adresses = {CACHE / ANNOTATION.rsplit("/", 1)[1]: ANNOTATION}
    for serie, adresse in DONNEES.items():
        adresses[AUTRES / adresse.rsplit("/", 1)[1]] = adresse
        adresses[AUTRES / f"{serie}_gsm.txt"] = FICHES.format(serie=serie)
    for destination, adresse in adresses.items():
        if not destination.is_file():
            requete = urllib.request.Request(adresse, headers={"User-Agent": "copie-locale-lecture-seule/1.0"})
            with urllib.request.urlopen(requete, timeout=900) as reponse, open(destination, "wb") as fichier:
                shutil.copyfileobj(reponse, fichier)
        print(f"{destination.name} : {destination.stat().st_size} octets")
    with tarfile.open(AUTRES / "GSE251872_RAW.tar") as archive:
        archive.extractall(AUTRES / "GSE251872", filter="data")


# --- Lire les fiches et les fichiers ---

def fiches(serie):
    """Les fiches d'échantillons d'une série : numéro, titre, description, source et caractères."""
    texte = (AUTRES / f"{serie}_gsm.txt").read_text(encoding="utf-8")
    resultat = []
    for bloc in texte.split("^SAMPLE = ")[1:]:
        def champ(nom):
            return [valeur.strip() for valeur in re.findall(rf"!Sample_{nom} = (.*)", bloc)]
        resultat.append({
            "numero": bloc.split("\n", 1)[0].strip(), "titre": champ("title")[0],
            "description": champ("description")[0] if champ("description") else "",
            "source": champ("source_name_ch1")[0],
            "caracteres": dict(valeur.split(": ", 1) for valeur in champ("characteristics_ch1") if ": " in valeur),
        })
    return resultat


def charger_gse251872():
    """EM/SFC après une infection, cellules mononucléées : un fichier par personne."""
    groupe = {f["numero"]: PATIENTS if ", PI-ME/CFS," in f["titre"] else TEMOINS for f in fiches("GSE251872")}
    chemins = sorted((AUTRES / "GSE251872").glob("GSM*.txt.gz"))
    bibliotheques = [{"nom": c.name.split(".")[0], "groupe": groupe[c.name.split("_")[0]]} for c in chemins]
    expression = {}
    for rang, chemin in enumerate(chemins):
        with gzip.open(chemin, "rt") as fichier:
            next(fichier)
            for ligne in fichier:
                gene, _, valeur = ligne.rstrip("\n").split("\t")
                expression.setdefault(gene, [0.0] * len(chemins))[rang] = float(valeur)
    return bibliotheques, expression


def charger_gse251849():
    """COVID long, cellules mononucléées : un tableau, une colonne par personne."""
    groupes = {"Healthy": TEMOINS, "COVID convalescent": TEMOINS, "Long COVID": PATIENTS, "Long COVID brain fog": PATIENTS}
    groupe = {f["description"]: groupes[f["caracteres"]["group"]] for f in fiches("GSE251849")}
    with gzip.open(AUTRES / "GSE251849_Counts.txt.gz", "rt") as fichier:
        colonnes = fichier.readline().split()[1:]
        expression = {champs[0]: [float(v) for v in champs[1:]] for champs in (ligne.split() for ligne in fichier)}
    return [{"nom": colonne, "groupe": groupe[colonne]} for colonne in colonnes], expression


def charger_gse226260():
    """COVID long, sang total, ARN polyadénylés : plusieurs prélèvements par personne, on garde le plus ancien."""
    premiers = {}
    for f in fiches("GSE226260"):
        if f["source"] != "Whole blood":
            continue
        personne, jour = f["titre"].split(".")[:2]
        rang = (RANG_DU_TEMPS[f["caracteres"]["time of_blood_draw"]], int(jour) if jour.isdigit() else math.inf, f["numero"])
        if personne not in premiers or rang < premiers[personne][0]:
            statut = PATIENTS if f["caracteres"]["current long_covid_status"] == "PASC" else TEMOINS
            premiers[personne] = (rang, f["titre"], statut)
    groupe = {titre: statut for _, titre, statut in premiers.values()}
    with gzip.open(AUTRES / "GSE226260_AdditionalSamples.rawCounts.csv.gz", "rt", newline="") as fichier:
        lignes = csv.reader(fichier)
        colonnes = next(lignes)[1:]
        gardees = [rang for rang, colonne in enumerate(colonnes) if colonne in groupe]
        expression = {ligne[0].split(".")[0]: [float(ligne[1 + rang]) for rang in gardees] for ligne in lignes}
    return [{"nom": colonnes[rang], "groupe": groupe[colonnes[rang]]} for rang in gardees], expression


JEUX = {
    "GSE251872": ("EM/SFC après une infection, cellules mononucléées", charger_gse251872, False),
    "GSE251849": ("COVID long, cellules mononucléées", charger_gse251849, False),
    "GSE226260": ("COVID long, sang total, ARN polyadénylés", charger_gse226260, True),
}


# --- Mesurer ---

def ensembles_d_un_jeu(annotation, genes_du_jeu):
    """Les listes de gènes de la section 6 du plan, parmi les gènes que le jeu contient."""
    ensembles = {"noyau": set(), "codants_mito": set(), "arn_cyto": set(),
                 "arn_mito": set(ARN_MITO) & set(genes_du_jeu)} | {nom: set() for nom in MENAGE}
    for gene in genes_du_jeu:
        chromosome, nom, type_du_gene = annotation.get(gene, (None, None, None))
        if type_du_gene == "protein_coding":
            ensembles["codants_mito" if chromosome == "MT" else "noyau"].add(gene)
        if nom and MOTIF_DE_B.match(nom):
            ensembles["arn_cyto"].add(gene)
        if nom in MENAGE:
            ensembles[nom].add(gene)
    return ensembles


def mesurer(bibliotheques, expression, ensembles):
    """Ajoute à chaque bibliothèque A, B et D, et les gènes de ménage, en log2 du rapport aux gènes du noyau."""
    sommes = [{nom: sum(expression[gene][rang] for gene in genes) for nom, genes in ensembles.items()}
              for rang in range(len(bibliotheques))]
    for mesure, numerateur in (MESURES | {gene: gene for gene in MENAGE}).items():
        for bibliotheque, valeur in zip(bibliotheques, en_log2(sommes, numerateur)):
            bibliotheque[mesure] = valeur


# --- Décider ---

def lecture(bibliotheques, polyadenyle):
    """La règle de la section 5 du plan, telle que la section 6 l'applique à un autre jeu."""
    if not abs(ecart_des_genes_de_menage(bibliotheques, PATIENTS, TEMOINS)) < SEUIL_MENAGE:
        return ILLISIBLE
    if ecart(bibliotheques, "A", PATIENTS, temoins=TEMOINS) > ECART_NET:
        return NON_REPRODUIT
    if polyadenyle:
        return PRESENT
    correlation, pente = lien_a_groupe_egal(bibliotheques)
    ecart_de_b = ecart(bibliotheques, "B", PATIENTS, temoins=TEMOINS)
    if ecart_de_b <= ECART_NET and correlation >= SEUIL_CORRELATION:
        return ARTEFACT
    if ecart_de_b > ECART_FAIBLE and ecart_corrige(bibliotheques, PATIENTS, pente, TEMOINS) <= ECART_NET:
        return NON_EXPLIQUE
    return INDECIDABLE


def lecture_d_ensemble(lectures):
    """Le tableau de la fin de la section 6 : la première ligne remplie donne la lecture."""
    lus = [lue for lue in lectures if lue != ILLISIBLE]
    if any(lue in (NON_EXPLIQUE, PRESENT) for lue in lus):
        return "signal retrouvé chez d'autres personnes"
    if len(lus) >= 2 and all(lue in (NON_REPRODUIT, ARTEFACT) for lue in lus):
        return "signal non retrouvé chez d'autres personnes"
    return "non conclu"


# --- Lancer ---

def main():
    if sys.argv[1:] == ["telecharger"]:
        return telecharger()
    annotation = lire_annotation(CACHE / ANNOTATION.rsplit("/", 1)[1])
    lectures = []
    for serie, (titre, charger, polyadenyle) in JEUX.items():
        bibliotheques, expression = charger()
        ensembles = ensembles_d_un_jeu(annotation, expression.keys())
        effectifs = {groupe: sum(b["groupe"] == groupe for b in bibliotheques) for groupe in (PATIENTS, TEMOINS)}
        print(f"\n== {serie} : {titre} ; {effectifs[PATIENTS]} patients, {effectifs[TEMOINS]} témoins")
        print(f"  gènes : {len(ensembles['noyau'])} codants du noyau, {len(ensembles['codants_mito'])} codants de la mitochondrie, "
              f"{len(ensembles['arn_mito'])} ARN ribosomiques de la mitochondrie, "
              f"{sum(len(ensembles[nom]) == 1 for nom in MENAGE)} gènes de ménage sur {len(MENAGE)}")
        print(f"  gènes de B : {sorted(annotation[gene][1] for gene in ensembles['arn_cyto']) or 'aucun'}")
        if len(ensembles["arn_mito"]) != 2 or len(ensembles["codants_mito"]) != 13:
            print("  critère 4 non rempli : le jeu n'est pas lu")
            continue
        if sys.argv[1:] == ["genes"]:
            continue

        mesurer(bibliotheques, expression, ensembles)
        for mesure in MESURES:
            if math.isnan(bibliotheques[0][mesure]):
                print(f"  {mesure} ne se calcule pas")
                continue
            bas, haut = intervalle(bibliotheques, mesure, PATIENTS, TEMOINS)
            print(f"  écart de {mesure} : {ecart(bibliotheques, mesure, PATIENTS, temoins=TEMOINS):+.2f} log2 "
                  f"(intervalle à 95 % : {bas:+.2f} à {haut:+.2f})")
        correlation, pente = lien_a_groupe_egal(bibliotheques)
        if not math.isnan(correlation):
            print(f"  lien entre A et B, à groupe égal : corrélation de rang {correlation:.2f}, pente {pente:.2f} ; "
                  f"écart de A corrigé de B : {ecart_corrige(bibliotheques, PATIENTS, pente, TEMOINS):+.2f} log2")
        print(f"  gènes de ménage, écart médian : {ecart_des_genes_de_menage(bibliotheques, PATIENTS, TEMOINS):+.2f} log2")
        lectures.append(lecture(bibliotheques, polyadenyle))
        print(f"  lecture : {lectures[-1]}")

    if sys.argv[1:] != ["genes"]:
        print(f"\nLecture d'ensemble : {lecture_d_ensemble(lectures)}")


if __name__ == "__main__":
    main()
