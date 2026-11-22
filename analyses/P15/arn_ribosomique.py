"""
Analyse de la piste P15, telle que le plan la fixe : analyses/P15/PLAN.md.

Question : la baisse d'expression de MT-RNR1 et MT-RNR2 publiée en 2019 suit-elle le retrait
de l'ARN ribosomique, d'une bibliothèque à l'autre ?

Le programme lit les 40 fichiers d'expression déposés (jeu GSE130353), calcule par bibliothèque
les mesures du plan, puis applique sa règle de décision. Les seuils sont ceux du plan, écrits ici
en constantes : rien ne s'ajuste après avoir vu les données.

Les données et l'annotation se téléchargent dans cache/P15/, hors du dépôt.

Usage :
    python3 analyses/P15/arn_ribosomique.py essai         # la règle, éprouvée sur des données inventées
    python3 analyses/P15/arn_ribosomique.py telecharger   # les 40 fichiers et l'annotation Ensembl 68
    python3 analyses/P15/arn_ribosomique.py               # l'analyse
"""

import csv
import gzip
import math
import re
import shutil
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path
from statistics import mean, median

import numpy as np
from scipy import stats

RACINE = Path(__file__).resolve().parents[2]
CACHE = RACINE / "cache" / "P15"
FICHIERS = CACHE / "GSE130353"
ARCHIVE = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/suppl/GSE130353_RAW.tar"
ANNOTATION = "https://ftp.ensembl.org/pub/release-68/gtf/homo_sapiens/Homo_sapiens.GRCh37.68.gtf.gz"
MESURES = Path(__file__).with_name("mesures.csv")

# Les seuils du plan. Les écarts sont en log2 ; un écart négatif veut dire : plus bas chez les patients.
ECART_NET = -2.0            # A, B ou l'écart corrigé « de −2 log2 ou plus bas »
ECART_FAIBLE = -1.0         # B « au-dessus de −1 log2 » ; D « de −1 log2 ou plus bas »
SEUIL_CORRELATION = 0.5     # A suit B d'une bibliothèque à l'autre, à groupe égal
SEUIL_MENAGE = 0.5          # écart médian des gènes de ménage, en valeur absolue

# Les gènes du plan, dans l'annotation Ensembl 68.
ARN_MITO = ("ENSG00000211459", "ENSG00000210082")       # MT-RNR1 et MT-RNR2
ARN_CYTO = ("ENSG00000225840", "ENSG00000226958")       # RN18S1 et RN28S1
MENAGE = ("ACTB", "GAPDH", "B2M", "PPIA", "RPLP0", "TBP", "HPRT1", "PGK1", "GUSB", "YWHAZ")
EFFECTIFS_ATTENDUS = {"noyau": 22_045, "codants_mito": 13, "petits_arn": 558}

# Le groupe se lit au début du nom de fichier. « CSF » est une coquille du dépôt, sur deux fichiers.
GROUPES = {"HC": "témoins sains", "CFS": "EM/SFC", "CSF": "EM/SFC",
           "QFS": "fatigue après fièvre Q", "PQ": "témoins infectés"}
TEMOINS = "témoins sains"
COMPARAISONS = ("EM/SFC", "fatigue après fièvre Q")
SERIE_2_A_PARTIR_DE = 13_000    # numéros de bibliothèque : 12461 à 12480, puis 13120 à 13139

NOMS_DES_MESURES = {"A": "ARN ribosomiques de la mitochondrie", "B": "ARN 18S et 28S du cytoplasme",
                    "D": "gènes codants de la mitochondrie", "E": "ARN 5S et 5,8S"}
SOMME_DE_LA_MESURE = {"A": "arn_mito", "B": "arn_cyto", "D": "codants_mito", "E": "petits_arn"}

ILLISIBLE = "illisible : le contrôle négatif échoue"
NON_REPRODUIT = "signal non reproduit sur les données déposées"
ARTEFACT = "signal probablement artefactuel, tant qu'une contre-analyse n'est pas faite"
NON_EXPLIQUE = "signal non expliqué par le retrait de l'ARN ribosomique"
INDECIDABLE = "indécidable"
APPUI_PERDU, APPUI_GARDE = "appui perdu", "appui gardé"


# --- Lire les fichiers ---

def lire_annotation(chemin):
    """Renvoie {identifiant du gène: (chromosome, nom, type)} pour chaque gène de l'annotation."""
    genes = {}
    with gzip.open(chemin, "rt") as fichier:
        for ligne in fichier:
            champs = ligne.rstrip("\n").split("\t")
            if len(champs) < 9:
                continue
            attributs = dict(re.findall(r'(\S+) "([^"]*)"', champs[8]))
            genes.setdefault(attributs["gene_id"],
                             (champs[0], attributs.get("gene_name"), attributs.get("gene_biotype")))
    return genes


def ensembles_de_genes(annotation):
    """Les listes de gènes de la section 4 du plan, plus une liste par gène de ménage."""
    ensembles = {"noyau": set(), "codants_mito": set(), "petits_arn": set(),
                 "arn_mito": set(ARN_MITO), "arn_cyto": set(ARN_CYTO)} | {nom: set() for nom in MENAGE}
    for gene, (chromosome, nom, type_du_gene) in annotation.items():
        if type_du_gene == "protein_coding":
            ensembles["codants_mito" if chromosome == "MT" else "noyau"].add(gene)
        if type_du_gene == "rRNA":
            ensembles["petits_arn"].add(gene)
        if nom in MENAGE:
            ensembles[nom].add(gene)
    return ensembles


def lire_bibliotheque(chemin):
    """Renvoie {identifiant du gène: expression} pour un fichier du programme MMSEQ.

    L'expression est la colonne log_mu, un logarithme népérien, ramenée à l'échelle linéaire.
    Un gène marqué comme non observé compte pour zéro.
    """
    expression = {}
    with gzip.open(chemin, "rt") as fichier:
        lignes = (ligne for ligne in fichier if ligne.strip() and not ligne.startswith("#"))
        colonnes = next(lignes).split()
        gene, log_mu, observe = (colonnes.index(nom) for nom in ("feature_id", "log_mu", "observed"))
        for ligne in lignes:
            champs = ligne.split()
            vu = champs[observe] == "1" and champs[log_mu] not in ("NA", "NaN", "nan")
            expression[champs[gene]] = math.exp(float(champs[log_mu])) if vu else 0.0
    return expression


def sommes_d_une_bibliotheque(expression, ensembles):
    """La somme des expressions de chaque ensemble de gènes, à l'échelle linéaire."""
    return {nom: sum(expression.get(gene, 0.0) for gene in genes) for nom, genes in ensembles.items()}


# --- Mesurer ---

def en_log2(sommes, numerateur):
    """log2 de (somme / N) pour chaque bibliothèque.

    Une somme nulle prend la moitié de la plus petite valeur non nulle des 40 bibliothèques.
    """
    non_nulles = [s[numerateur] for s in sommes if s[numerateur] > 0]
    if not non_nulles:
        if numerateur == "arn_cyto":        # B ne se calcule pas : le plan prévoit la lecture « indécidable »
            return [math.nan] * len(sommes)
        raise SystemExit(f"Mesure incalculable : « {numerateur} » vaut zéro dans toutes les bibliothèques.")
    plancher = min(non_nulles) / 2
    return [math.log2((s[numerateur] or plancher) / s["noyau"]) for s in sommes]


def mesurer(bibliotheques, sommes):
    """Ajoute à chaque bibliothèque les mesures A, B, D et E du plan, et les dix gènes de ménage."""
    for mesure, numerateur in (SOMME_DE_LA_MESURE | {gene: gene for gene in MENAGE}).items():
        for bibliotheque, valeur in zip(bibliotheques, en_log2(sommes, numerateur)):
            bibliotheque[mesure] = valeur


def valeurs(bibliotheques, mesure, groupe, serie=None):
    return [b[mesure] for b in bibliotheques if b["groupe"] == groupe and serie in (None, b["serie"])]


def ecart(bibliotheques, mesure, patients, serie=None):
    """Moyenne des patients moins moyenne des témoins sains, en log2."""
    return mean(valeurs(bibliotheques, mesure, patients, serie)) - mean(valeurs(bibliotheques, mesure, TEMOINS, serie))


def intervalle(bibliotheques, mesure, patients):
    """Intervalle de confiance à 95 % de l'écart, sans supposer des variances égales (test de Welch)."""
    test = stats.ttest_ind(valeurs(bibliotheques, mesure, patients), valeurs(bibliotheques, mesure, TEMOINS),
                           equal_var=False)
    bornes = test.confidence_interval(0.95)
    return bornes.low, bornes.high


def lien_a_groupe_egal(bibliotheques):
    """Le lien entre A et B, après avoir retiré à chaque valeur la moyenne de son groupe.

    Renvoie la corrélation de rang, et la pente de A sur B par les moindres carrés.
    """
    def centrees(mesure):
        moyennes = {groupe: mean(valeurs(bibliotheques, mesure, groupe)) for groupe in set(GROUPES.values())}
        return [b[mesure] - moyennes[b["groupe"]] for b in bibliotheques]
    a, b = centrees("A"), centrees("B")
    if not sum(valeur ** 2 for valeur in b) > 0:      # B constant ou incalculable
        return math.nan, math.nan
    correlation = stats.spearmanr(a, b).statistic
    pente = sum(x * y for x, y in zip(a, b)) / sum(y ** 2 for y in b)
    return correlation, pente


def ecart_corrige(bibliotheques, patients, pente):
    """Ce qui reste de l'écart de A une fois retiré ce que B permet de prévoir."""
    return ecart(bibliotheques, "A", patients) - pente * ecart(bibliotheques, "B", patients)


def ecart_des_genes_de_menage(bibliotheques, patients):
    """Médiane des dix écarts des gènes de ménage : le contrôle négatif du plan."""
    return median(ecart(bibliotheques, gene, patients) for gene in MENAGE)


# --- Décider ---

def lecture(bibliotheques, patients, correlation, pente):
    """La règle de la section 5 du plan, pour une comparaison : la première étape remplie donne la lecture."""
    if not abs(ecart_des_genes_de_menage(bibliotheques, patients)) < SEUIL_MENAGE:
        return ILLISIBLE
    if ecart(bibliotheques, "A", patients) > ECART_NET:
        return NON_REPRODUIT
    if not ecart(bibliotheques, "A", patients, serie=1) * ecart(bibliotheques, "A", patients, serie=2) > 0:
        return INDECIDABLE
    ecart_de_b = ecart(bibliotheques, "B", patients)
    if ecart_de_b <= ECART_NET and correlation >= SEUIL_CORRELATION:
        return ARTEFACT
    if ecart_de_b > ECART_FAIBLE and ecart_corrige(bibliotheques, patients, pente) <= ECART_NET:
        return NON_EXPLIQUE
    return INDECIDABLE


def lecture_d_ensemble(lectures):
    """Ce que les deux comparaisons disent ensemble de l'appui de 2019."""
    if all(lue in (NON_REPRODUIT, ARTEFACT) for lue in lectures):
        return APPUI_PERDU
    if all(lue == NON_EXPLIQUE for lue in lectures):
        return APPUI_GARDE
    return INDECIDABLE


def decider(bibliotheques):
    correlation, pente = lien_a_groupe_egal(bibliotheques)
    lectures = [lecture(bibliotheques, patients, correlation, pente) for patients in COMPARAISONS]
    return correlation, pente, lectures, lecture_d_ensemble(lectures)


# --- Éprouver la règle sur des données inventées ---

def bibliotheques_inventees(graine, ecart_de_a, ecart_de_b, couplage, ecart_de_a_serie_2=None):
    """40 bibliothèques inventées : un écart imposé chez les patients, et un couplage entre A et B.

    Le couplage imite le retrait de l'ARN ribosomique : une même efficacité, propre à chaque bibliothèque,
    agit sur B, et sur A en proportion du couplage.
    """
    generateur = np.random.default_rng(graine)
    bibliotheques = []
    for groupe in ("témoins sains", "EM/SFC", "fatigue après fièvre Q", "témoins infectés"):
        patient = groupe in COMPARAISONS
        for rang in range(10):
            serie = 1 + rang % 2
            retrait = generateur.normal(0, 0.5)
            ecart_impose = ecart_de_a_serie_2 if (serie == 2 and ecart_de_a_serie_2 is not None) else ecart_de_a
            bibliotheque = {
                "nom": f"{groupe} {rang + 1}", "groupe": groupe, "serie": serie,
                "A": patient * ecart_impose + couplage * retrait + generateur.normal(0, 0.3),
                "B": patient * ecart_de_b + retrait + generateur.normal(0, 0.3),
                "D": generateur.normal(0, 0.3), "E": generateur.normal(0, 0.3),
            }
            bibliotheques.append(bibliotheque | {gene: generateur.normal(0, 0.2) for gene in MENAGE})
    return bibliotheques


def essai(graine=20261122):
    """Renvoie une liste (cas, lecture attendue, lecture obtenue) : la règle doit savoir dire oui et non."""
    cas = [
        ("le retrait explique tout : A et B baissent ensemble", APPUI_PERDU, dict(ecart_de_a=-4.5, ecart_de_b=-4, couplage=1)),
        ("A baisse seul, sans lien avec B", APPUI_GARDE, dict(ecart_de_a=-4.5, ecart_de_b=0, couplage=0)),
        ("A baisse seul, bien qu'il suive B à groupe égal", APPUI_GARDE, dict(ecart_de_a=-4.5, ecart_de_b=0, couplage=1)),
        ("aucun écart", APPUI_PERDU, dict(ecart_de_a=0, ecart_de_b=0, couplage=1)),
        ("B baisse à moitié", INDECIDABLE, dict(ecart_de_a=-4.5, ecart_de_b=-1.5, couplage=1)),
        ("B baisse, mais A ne le suit pas", INDECIDABLE, dict(ecart_de_a=-4.5, ecart_de_b=-4, couplage=0)),
        ("B baisse peu, mais A le suit avec une forte pente", INDECIDABLE, dict(ecart_de_a=-4, ecart_de_b=-0.9, couplage=4)),
        ("écart de A de sens contraire dans les deux séries", INDECIDABLE,
         dict(ecart_de_a=-9, ecart_de_a_serie_2=2, ecart_de_b=0, couplage=0)),
    ]
    resultats = [(nom, attendu, decider(bibliotheques_inventees(graine, **reglages))[3])
                 for nom, attendu, reglages in cas]

    # Les gènes de ménage décalés chez les patients : le contrôle négatif doit arrêter la lecture.
    decalees = bibliotheques_inventees(graine, ecart_de_a=-4.5, ecart_de_b=-4, couplage=1)
    for bibliotheque in decalees:
        if bibliotheque["groupe"] in COMPARAISONS:
            for gene in MENAGE:
                bibliotheque[gene] += 1
    resultats.append(("gènes de ménage décalés de 1 log2 chez les patients", [ILLISIBLE, ILLISIBLE], decider(decalees)[2]))

    # Le lecteur de fichiers, sur un fichier inventé de trois gènes.
    with tempfile.TemporaryDirectory() as dossier:
        chemin = Path(dossier) / "essai.gene.mmseq.txt.gz"
        with gzip.open(chemin, "wt") as fichier:
            fichier.write("# commentaire\nfeature_id\tlog_mu\tsd\tobserved\n"
                          "G1\t0\t0.1\t1\nG2\t2.302585\t0.1\t1\nG3\t5\t0.1\t0\n")
        lu = lire_bibliotheque(chemin)
    arrondi = {gene: round(valeur, 3) for gene, valeur in lu.items()}
    resultats.append(("lecture d'un fichier inventé", {"G1": 1.0, "G2": 10.0, "G3": 0.0}, arrondi))
    return resultats


# --- Lancer ---

def telecharger():
    CACHE.mkdir(parents=True, exist_ok=True)
    for adresse in (ARCHIVE, ANNOTATION):
        destination = CACHE / adresse.rsplit("/", 1)[1]
        if not destination.is_file():
            requete = urllib.request.Request(adresse, headers={"User-Agent": "copie-locale-lecture-seule/1.0"})
            with urllib.request.urlopen(requete, timeout=600) as reponse, open(destination, "wb") as fichier:
                shutil.copyfileobj(reponse, fichier)
        print(f"{destination.name} : {destination.stat().st_size} octets")
    with tarfile.open(CACHE / "GSE130353_RAW.tar") as archive:
        archive.extractall(FICHIERS, filter="data")
    print(f"{len(list(FICHIERS.glob('*.gene.mmseq.txt.gz')))} fichiers dans {FICHIERS}")


def charger():
    """Lit l'annotation et les 40 fichiers ; renvoie les bibliothèques, avec leurs mesures."""
    ensembles = ensembles_de_genes(lire_annotation(CACHE / ANNOTATION.rsplit("/", 1)[1]))
    for nom, attendu in EFFECTIFS_ATTENDUS.items():
        if len(ensembles[nom]) != attendu:
            raise SystemExit(f"Annotation inattendue : {len(ensembles[nom])} gènes pour « {nom} », {attendu} attendus.")
    bibliotheques, sommes = [], []
    for chemin in sorted(FICHIERS.glob("*.gene.mmseq.txt.gz")):
        _, nom, _, numero = chemin.name.split(".")[0].split("_")
        expression = lire_bibliotheque(chemin)
        if len(ensembles["noyau"] & expression.keys()) < 15_000:
            raise SystemExit(f"{chemin.name} : les identifiants de gènes ne sont pas ceux de l'annotation Ensembl 68.")
        bibliotheques.append({"nom": nom, "groupe": GROUPES[re.match(r"[A-Z]+", nom).group()],
                              "serie": 2 if int(numero) >= SERIE_2_A_PARTIR_DE else 1})
        sommes.append(sommes_d_une_bibliotheque(expression, ensembles))
    if len(bibliotheques) != 40:
        raise SystemExit(f"{len(bibliotheques)} fichiers lus, 40 attendus. Lancer d'abord « telecharger ».")
    mesurer(bibliotheques, sommes)
    return bibliotheques


def analyser():
    bibliotheques = charger()
    with open(MESURES, "w", newline="", encoding="utf-8") as fichier:
        tableau = csv.writer(fichier)
        tableau.writerow(["bibliotheque", "groupe", "serie", "A", "B", "D", "E"])
        for b in bibliotheques:
            tableau.writerow([b["nom"], b["groupe"], b["serie"]] + [f"{b[m]:.3f}" for m in "ABDE"])

    print("Moyennes par groupe, en log2 du rapport aux gènes codants du noyau")
    for mesure, nom in NOMS_DES_MESURES.items():
        moyennes = ", ".join(f"{groupe} {mean(valeurs(bibliotheques, mesure, groupe)):.2f}"
                             for groupe in dict.fromkeys(GROUPES.values()))
        print(f"  {mesure}, {nom} : {moyennes}")

    correlation, pente, lectures, ensemble = decider(bibliotheques)
    for patients, lue in zip(COMPARAISONS, lectures):
        print(f"\n{patients} contre {TEMOINS}")
        for mesure in NOMS_DES_MESURES:
            bas, haut = intervalle(bibliotheques, mesure, patients)
            series = " ; ".join(f"série {serie} : {ecart(bibliotheques, mesure, patients, serie):+.2f}" for serie in (1, 2))
            print(f"  écart de {mesure} : {ecart(bibliotheques, mesure, patients):+.2f} log2 "
                  f"(intervalle à 95 % : {bas:+.2f} à {haut:+.2f}) ; {series}")
        print(f"  écart de A corrigé de B : {ecart_corrige(bibliotheques, patients, pente):+.2f} log2")
        print(f"  gènes de ménage, écart médian : {ecart_des_genes_de_menage(bibliotheques, patients):+.2f} log2")
        print(f"  lecture : {lue}")

    print(f"\nTémoins infectés contre {TEMOINS}, décrits sans entrer dans la règle")
    for mesure in NOMS_DES_MESURES:
        bas, haut = intervalle(bibliotheques, mesure, "témoins infectés")
        print(f"  écart de {mesure} : {ecart(bibliotheques, mesure, 'témoins infectés'):+.2f} log2 "
              f"(intervalle à 95 % : {bas:+.2f} à {haut:+.2f})")

    print(f"\nLien entre A et B, à groupe égal : corrélation de rang {correlation:.2f}, pente {pente:.2f}")
    print(f"Lecture d'ensemble : {ensemble}")
    print(f"Mesures par bibliothèque : {MESURES.relative_to(RACINE)}")


def main():
    if sys.argv[1:] == ["essai"]:
        for nom, attendu, obtenu in essai():
            print(f"  {'OK   ' if attendu == obtenu else 'ÉCHEC'} {nom} : {obtenu}")
    elif sys.argv[1:] == ["telecharger"]:
        telecharger()
    elif not sys.argv[1:]:
        analyser()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
