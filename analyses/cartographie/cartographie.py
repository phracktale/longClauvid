"""
Première carte de la littérature du COVID long, sur la copie locale de la bibliothèque #ApresJ20.

Pour chaque piste du registre et de la banque, le script compte les références de la bibliothèque
dont le titre ou le résumé contient ses termes. Il compte aussi ce que le registre ne couvre pas :
les mots les plus fréquents des titres qu'aucune piste ne retient.

Les termes cherchés sont écrits ci-dessous : une requête fait partie du résultat.
Un décompte n'est pas une preuve. Un terme présent dans un résumé ne dit pas que l'étude porte sur la piste.

Ce n'est pas encore la phase 1 du protocole : aucune relation n'est extraite, aucun graphe n'est construit.
C'est son premier pas, la sélection des articles.

Usage :
    python3 outils/bibliotheque_apresj20.py telecharger     # la copie locale, 4 minutes
    python3 analyses/cartographie/cartographie.py           # écrit analyses/cartographie/CARTE.md

Seuls des décomptes sortent du script : les titres et les résumés restent dans cache/, hors du dépôt.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RACINE / "analyses" / "banque"))
from inexploree import RECHERCHES          # noqa: E402  les termes des pistes de la banque, déjà déposés

BIBLIOTHEQUE = RACINE / "cache" / "apresj20.json"
CARTE = Path(__file__).resolve().parent / "CARTE.md"
ANNEES = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
MOTS_AFFICHES = 40

# Pistes du registre : leur nom, puis les motifs cherchés (expressions régulières, sans tenir compte de la casse).
# P15, P16 et P17 reprennent les termes de leur piste de banque.
PISTES = {
    "P01": ("IgG pathogènes, transfert passif", [r"passive transfer", r"autoantibod", r"auto-antibod", r"\bGPCR"]),
    "P02": ("Déplétion des plasmocytes", [r"daratumumab", r"plasma cell", r"immunoadsorption", r"rituximab",
                                          r"efgartigimod", r"B[- ]cell depletion"]),
    "P03": ("Boucle interféron–itaconate", [r"itaconate", r"interferon"]),
    "P04": ("WASF3 et stress du réticulum", [r"WASF3", r"endoplasmic reticulum stress", r"\bER stress",
                                             r"unfolded protein"]),
    "P05": ("Canal calcique TRPM3", [r"TRPM3", r"naltrexone"]),
    "P06": ("SMPDL3B", [r"SMPDL3B", r"sphingomyelin", r"PI-PLC"]),
    "P07": ("Surcharge sodium–calcium du muscle", [r"intracellular sodium", r"sodium MRI", r"23Na",
                                                   r"muscle biops", r"skeletal muscle"]),
    "P08": ("Fibrine, spike et complément", [r"fibrin", r"microclot", r"\bcomplement\b"]),
    "P09": ("Sérotonine et tryptophane", [r"serotonin", r"tryptophan", r"kynurenin"]),
    "P10": ("Hormones sexuelles", [r"testosterone", r"estradiol", r"estrogen", r"oestrogen", r"sex hormone"]),
    "P11": ("Modèles à états stables multiples", [r"bistab", r"multistab", r"stable state", r"attractor",
                                                 r"mathematical model", r"computational model"]),
    "P12": ("Réponse au danger cellulaire", [r"cell danger response", r"hypometabol"]),
    "P13": ("Génétique", [r"genome[- ]wide", r"\bGWAS\b", r"DecodeME", r"mendelian randomi"]),
    "P14": ("Antigène viral persistant", [r"viral persistence", r"persistent (viral )?antigen", r"antigen persistence",
                                          r"viral reservoir", r"persisten.{0,20}spike", r"spike.{0,20}persist",
                                          r"persistent infection"]),
    "P15": ("Humanine et MOTS-c", RECHERCHES["B011"][0]),
    "P16": ("Région HLA", RECHERCHES["B013"][0]),
    "P17": ("Nombre de copies d'ADN mitochondrial", RECHERCHES["B020"][0]),
}
PROMUES = {"B011", "B013", "B020"}       # déjà comptées sous P15, P16 et P17

# Mots trop généraux pour désigner un sujet : ils sont retirés avant de compter les mots des titres.
MOTS_VIDES = set("""
a an and are as at be by for from in into is it its of on or that the their this to was were with within without
after among between during following over under via versus vs
covid covid-19 long post sars-cov-2 sars cov coronavirus pandemic infection acute sequelae syndrome condition
conditions pasc post-covid post-covid-19 post-acute disease symptoms symptom patients patient study studies
analysis review systematic meta-analysis cohort case cases report clinical trial randomized controlled results
effects effect impact associated association risk factors outcomes persistent prospective retrospective
cross-sectional evidence new novel role using based among adults people health care months year years
follow-up one two three non de la le et des du en les un une
long-term long-covid individuals potential quality life function functional system severe chronic
""".split())


def texte(reference):
    return f"{reference.get('title') or ''} {reference.get('abstractNote') or ''}"


def annee(reference):
    trouve = re.search(r"(19|20)\d\d", reference.get("date") or "")
    return trouve.group(0) if trouve else ""


def compter(references, motifs):
    """Renvoie les références dont le titre ou le résumé contient au moins un des motifs."""
    expression = re.compile("|".join(motifs), re.IGNORECASE)
    return [numero for numero, reference in enumerate(references) if expression.search(texte(reference))]


def ligne(identifiant, nom, numeros, references):
    par_annee = Counter(annee(references[numero]) for numero in numeros)
    return (f"| {identifiant} | {nom} | {len(numeros)} | "
            + " | ".join(str(par_annee.get(a, 0)) for a in ANNEES) + " |")


def main():
    if not BIBLIOTHEQUE.is_file():
        sys.exit("Copie locale absente : lancer d'abord outils/bibliotheque_apresj20.py telecharger")
    bibliotheque = json.loads(BIBLIOTHEQUE.read_text(encoding="utf-8"))
    references = bibliotheque["references"]

    # Deux contrôles : un terme inventé ne trouve rien, le nom de la maladie trouve beaucoup.
    assert not compter(references, [r"zzqxjv"]), "contrôle négatif : un terme inventé a trouvé des références"
    temoin = len(compter(references, [r"long[- ]covid", r"post[- ]covid", r"post[- ]acute"]))
    assert temoin > len(references) / 2, "contrôle positif : le nom de la maladie est trop peu trouvé"

    en_tete = ["| Piste | Sujet | Références | " + " | ".join(ANNEES) + " |",
               "| --- | --- | --- | " + " | ".join("---" for _ in ANNEES) + " |"]
    retenues = set()
    lignes_registre, lignes_banque = [], []
    for identifiant, (nom, motifs) in PISTES.items():
        numeros = compter(references, motifs)
        retenues.update(numeros)
        lignes_registre.append((len(numeros), ligne(identifiant, nom, numeros, references)))
    for identifiant, (motifs, _) in RECHERCHES.items():
        if identifiant in PROMUES:
            continue
        numeros = compter(references, motifs)
        retenues.update(numeros)
        lignes_banque.append((len(numeros), ligne(identifiant, " ; ".join(motifs[:3]).replace("\\b", "").replace("|", "/"),
                                                  numeros, references)))

    avec_resume = sum(1 for reference in references if reference.get("abstractNote"))
    hors_carte = [reference for numero, reference in enumerate(references) if numero not in retenues]
    mots = Counter()
    for reference in hors_carte:
        vus = set(re.findall(r"[a-zà-ÿ][a-zà-ÿ0-9-]{2,}", (reference.get("title") or "").lower())) - MOTS_VIDES
        mots.update(vus)                     # un mot compte une fois par titre

    collections = Counter()
    for reference in hors_carte:
        collections.update(reference.get("collections") or [])
    toutes = Counter()
    for reference in references:
        toutes.update(reference.get("collections") or [])

    sortie = [
        "# Carte de la bibliothèque #ApresJ20, au regard du registre et de la banque",
        "",
        f"Écrite par `analyses/cartographie/cartographie.py` sur la copie du {bibliotheque['telecharge_le']}.",
        "Ne pas modifier à la main : relancer le script.",
        "",
        "Un décompte n'est pas une preuve. Une référence est comptée dès que son titre ou son résumé contient",
        "un des termes de la piste : elle peut n'en parler qu'en passant. Les termes sont dans le script.",
        "",
        "## Sélection",
        "",
        "| Étape | Références |",
        "| --- | --- |",
        f"| Dans la bibliothèque | {len(references)} |",
        f"| Avec un résumé | {avec_resume} |",
        f"| Retenues par au moins une piste du registre ou de la banque | {len(retenues)} |",
        f"| Retenues par aucune | {len(hors_carte)} |",
        "",
        "## Pistes du registre",
        "",
        *en_tete,
        *[texte_ligne for _, texte_ligne in sorted(lignes_registre, key=lambda x: -x[0])],
        "",
        "## Pistes de la banque",
        "",
        "Le sujet est donné par les trois premiers termes cherchés. Les pistes promues sont comptées plus haut.",
        "",
        *en_tete,
        *[texte_ligne for _, texte_ligne in sorted(lignes_banque, key=lambda x: -x[0])],
        "",
        "## Ce que ni le registre ni la banque ne retiennent",
        "",
        "Répartition, par rubrique de la bibliothèque, des références qu'aucune piste ne retient.",
        "Une référence peut appartenir à plusieurs rubriques.",
        "",
        "| Rubrique | Dans la bibliothèque | Retenues par aucune piste | Part |",
        "| --- | --- | --- | --- |",
        *[f"| {nom} | {toutes[nom]} | {collections[nom]} | {round(100 * collections[nom] / toutes[nom])} % |"
          for nom, _ in toutes.most_common()],
        "",
        f"Les {MOTS_AFFICHES} mots les plus fréquents de leurs titres, une fois retirés les mots généraux",
        "(liste dans le script). Un mot compte une fois par titre.",
        "",
        "| Mot | Titres |",
        "| --- | --- |",
        *[f"| {mot} | {nombre} |" for mot, nombre in mots.most_common(MOTS_AFFICHES)],
        "",
    ]
    CARTE.write_text("\n".join(sortie), encoding="utf-8")
    print(f"{len(references)} références, {len(retenues)} retenues par au moins une piste ; carte écrite : {CARTE}")


if __name__ == "__main__":
    main()
