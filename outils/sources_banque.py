"""
Copie locale des sources de la banque, pour les relire sans solliciter les sites à chaque lecture.

Pour chaque adresse citée dans registre/banque.yaml, le script prend le texte le plus complet
qu'une interface officielle fournit :
- article de PubMed : le résumé, puis le texte intégral de PubMed Central quand l'éditeur l'autorise ;
- prépublication de medRxiv : le texte intégral de la version citée, par l'interface de bioRxiv ;
- essai de ClinicalTrials.gov : la fiche complète, par l'interface du registre ;
- autre page ou PDF : la page elle-même.

Une source peut porter un champ « texte » : l'adresse où son texte intégral se lit, quand l'adresse
citée ne donne qu'un résumé ou qu'elle est bloquée. Le script copie alors les deux adresses.

Une page qui répond par un contrôle anti-robot est notée « bloquée » : le script ne le contourne pas.

La copie n'est pas versée au dépôt (dossier cache/, ignoré par git) : les articles restent
la propriété de leurs auteurs, on les lit, on ne les republie pas.

Usage :
    python3 outils/sources_banque.py telecharger    # une requête par source, espacées d'une seconde
    python3 outils/sources_banque.py bilan          # pour chaque piste, ce qui est lisible et à quel niveau

Le PDF se convertit avec l'outil « pdftotext » ; sans lui, le PDF est gardé tel quel.
"""

import json
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
BANQUE = RACINE / "registre" / "banque.yaml"
COPIE = RACINE / "cache" / "sources-banque"
INDEX = COPIE / "index.json"
PAUSE = 1                 # seconde entre deux requêtes
ATTENTE_APRES_REFUS = 30  # secondes d'attente quand un site répond « trop de requêtes »
EN_TETES = {"User-Agent": "copie-locale-lecture-seule/1.0"}   # rien du projet n'est envoyé aux sites
NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CONTROLES_ANTI_ROBOT = ("Just a moment", "Client Challenge", "Checking your browser", "Access Denied")

# Niveaux de lecture, du plus complet au moins complet.
TEXTE, RESUME, FICHE, PAGE, BLOQUEE = "texte intégral", "résumé", "fiche de registre", "page", "bloquée"


def demander(adresse, nouvel_essai=True):
    """Renvoie (code, contenu, type de contenu). Un refus du site donne son code et un contenu vide."""
    requete = urllib.request.Request(adresse, headers=EN_TETES)
    try:
        with urllib.request.urlopen(requete, timeout=90) as reponse:
            resultat = reponse.status, reponse.read(), reponse.headers.get("Content-Type", "")
    except urllib.error.HTTPError as erreur:
        resultat = erreur.code, b"", ""
    except OSError:                     # connexion impossible ou coupée
        resultat = 0, b"", ""
    time.sleep(PAUSE)
    if resultat[0] == 429 and nouvel_essai:     # « trop de requêtes » : on attend, puis un seul nouvel essai
        time.sleep(ATTENTE_APRES_REFUS)
        return demander(adresse, nouvel_essai=False)
    return resultat


def texte_xml(noeud, sans_tableaux=False):
    """Le texte d'un élément XML, blancs réduits. Les tableaux qu'il contient peuvent être laissés de côté."""
    morceaux = [noeud.text or ""]
    for enfant in noeud:
        if not (sans_tableaux and enfant.tag == "table-wrap"):
            morceaux.append(texte_xml(enfant, sans_tableaux))
        morceaux.append(enfant.tail or "")
    return " ".join("".join(morceaux).split())


def lignes_xml(element):
    """Rend un article en XML ligne par ligne : un titre, un paragraphe ou une ligne de tableau par ligne."""
    if element.tag == "tr":
        return [" | ".join(texte_xml(cellule) for cellule in element)]
    if element.tag in ("p", "title", "article-title"):
        # Certains éditeurs glissent le tableau dans le paragraphe : on le rend à part, ligne par ligne.
        tableaux = [ligne for tableau in element.iter("table-wrap") for ligne in lignes_xml(tableau)]
        return [texte_xml(element, sans_tableaux=True)] + tableaux
    return [ligne for enfant in element for ligne in lignes_xml(enfant)]


def texte_d_article(xml):
    """Renvoie (texte, complet) pour un article au format JATS, celui de PubMed Central et de medRxiv."""
    article = ET.fromstring(xml)
    if article.tag != "article":
        article = article.find(".//article")
    if article is None:
        return "", False
    corps = article.find("body")
    lignes = []
    for partie in (article.find("front"), corps, article.find("back/sec"), article.find("floats-group")):
        if partie is not None:
            lignes += lignes_xml(partie)
    return "\n".join(ligne for ligne in lignes if ligne), corps is not None


class TexteDePage(HTMLParser):
    """Garde le texte visible d'une page HTML, sans les scripts ni les styles."""

    def __init__(self):
        super().__init__()
        self.morceaux = []
        self.ignore = 0

    def handle_starttag(self, balise, attributs):
        if balise in ("script", "style", "noscript"):
            self.ignore += 1

    def handle_endtag(self, balise):
        if balise in ("script", "style", "noscript") and self.ignore:
            self.ignore -= 1

    def handle_data(self, donnees):
        if not self.ignore and donnees.strip():
            self.morceaux.append(" ".join(donnees.split()))


def texte_de_page(html):
    lecteur = TexteDePage()
    lecteur.feed(html)
    return "\n".join(lecteur.morceaux)


def texte_de_pdf(contenu, fichier):
    """Convertit un PDF en texte avec pdftotext. Sans cet outil, garde le PDF et renvoie un texte vide."""
    pdf = fichier.with_suffix(".pdf")
    pdf.write_bytes(contenu)
    if not shutil.which("pdftotext"):
        return ""
    subprocess.run(["pdftotext", "-layout", str(pdf), str(fichier)], check=True)
    return fichier.read_text(encoding="utf-8", errors="replace")


def resumes_pubmed(pmids):
    """Une seule requête pour tous les résumés. Renvoie {pmid: (texte, identifiant PubMed Central ou None)}."""
    code, contenu, _ = demander(f"{NCBI}?db=pubmed&retmode=xml&id={','.join(sorted(pmids))}")
    if code != 200:
        return {}
    resumes = {}
    for article in ET.fromstring(contenu).findall("PubmedArticle"):
        citation = article.find("MedlineCitation")
        revue = citation.find("Article/Journal")
        lignes = [
            "".join(citation.find("Article/ArticleTitle").itertext()),
            f"{revue.findtext('Title')}, {revue.findtext('JournalIssue/PubDate/Year') or revue.findtext('JournalIssue/PubDate/MedlineDate')}",
            "",
        ]
        for partie in citation.findall("Article/Abstract/AbstractText"):
            titre = partie.get("Label")
            lignes.append((f"{titre}: " if titre else "") + "".join(partie.itertext()))
        identifiants = {i.get("IdType"): i.text for i in article.findall("PubmedData/ArticleIdList/ArticleId")}
        resumes[citation.findtext("PMID")] = "\n".join(lignes), identifiants.get("pmc")
    return resumes


def texte_pmc(pmc):
    """Texte intégral d'un article de PubMed Central, ou texte vide si l'éditeur ne l'autorise pas."""
    code, contenu, _ = demander(f"{NCBI}?db=pmc&id={pmc.removeprefix('PMC')}")
    if code != 200:
        return ""
    texte, complet = texte_d_article(contenu)
    return texte if complet else ""


def lire_medrxiv(doi, numero):
    """Texte intégral d'une prépublication, dans la version citée, par l'interface de bioRxiv."""
    code, contenu, _ = demander(f"https://api.biorxiv.org/details/medrxiv/{doi}/na/json")
    versions = json.loads(contenu).get("collection", []) if code == 200 else []
    citee = next((version for version in versions if version["version"] == numero), None)
    if citee is None:
        return "", BLOQUEE
    en_tete = (f"Version {numero} du {citee['date']} ; dernière version en ligne : "
               f"{versions[-1]['version']}, du {versions[-1]['date']}")
    code, xml, _ = demander(citee["jatsxml"])
    texte, complet = texte_d_article(xml) if code == 200 else ("", False)
    if complet:
        return f"{en_tete}\n{texte}", TEXTE
    return f"{citee['title']}\n{en_tete}\n\n{citee['abstract']}", RESUME


def lire_page(adresse, fichier):
    """Lit une page ou un PDF tels quels. Renvoie (texte, niveau)."""
    code, contenu, type_de_contenu = demander(adresse)
    if code != 200:
        return "", BLOQUEE
    if "pdf" in type_de_contenu or contenu.startswith(b"%PDF"):
        return texte_de_pdf(contenu, fichier), PAGE
    html = contenu.decode("utf-8", errors="replace")
    titre = re.search(r"<title[^>]*>(.*?)</title>", html, re.S)
    if titre and any(controle in titre.group(1) for controle in CONTROLES_ANTI_ROBOT):
        return "", BLOQUEE
    return texte_de_page(html), PAGE


def identifiant_pubmed(adresse):
    """Le numéro PubMed d'une adresse de PubMed ou d'une recherche Europe PMC, sinon None."""
    trouve = (re.match(r"https://pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", adresse)
              or re.search(r"europepmc/webservices/rest/search\?query=EXT_ID:(\d+)", adresse))
    return trouve.group(1) if trouve else None


def nom_de_fichier(adresse):
    """Un nom lisible et stable : l'adresse sans son protocole, réduite aux lettres et aux chiffres."""
    return re.sub(r"[^a-z0-9]+", "-", adresse.split("://", 1)[1].lower()).strip("-")[:90] + ".txt"


def adresses_d_une_source(source):
    """Les adresses où la source se lit : celle que la piste cite, et son champ « texte » s'il existe."""
    return [adresse for adresse in (source["url"], source.get("texte")) if adresse]


def meilleure_copie(source, index):
    """La copie la plus longue parmi les adresses de la source ; sans copie, le dernier état connu."""
    copies = [index.get(adresse, {"fichier": None, "niveau": "non téléchargée", "caracteres": 0})
              for adresse in adresses_d_une_source(source)]
    return max(reversed(copies), key=lambda copie: copie["caracteres"])


def telecharger():
    banque = yaml.safe_load(BANQUE.read_text(encoding="utf-8"))
    adresses = sorted({adresse for entree in banque for source in entree["sources"]
                       for adresse in adresses_d_une_source(source)})
    COPIE.mkdir(parents=True, exist_ok=True)
    index = json.loads(INDEX.read_text(encoding="utf-8")) if INDEX.exists() else {}
    resumes = resumes_pubmed({pmid for pmid in map(identifiant_pubmed, adresses) if pmid})

    for numero, adresse in enumerate(adresses, start=1):
        if index.get(adresse, {}).get("niveau") in (TEXTE, FICHE, PAGE):
            continue                                  # déjà lue au mieux : rien n'est redemandé
        fichier = COPIE / nom_de_fichier(adresse)
        pmid = identifiant_pubmed(adresse)
        pmc = re.search(r"/articles/(PMC\d+)", adresse)
        medrxiv = re.match(r"https://www\.medrxiv\.org/content/(10\.\d+/[\d.]+)v(\d+)", adresse)
        essai = re.match(r"https://clinicaltrials\.gov/study/(NCT\d+)", adresse)

        if pmid:
            texte, pmc_de_l_article = resumes.get(pmid, ("", None))
            niveau = RESUME if texte else BLOQUEE
            integral = texte_pmc(pmc_de_l_article) if pmc_de_l_article else ""
            if integral:
                texte, niveau = integral, TEXTE
        elif pmc:
            texte = texte_pmc(pmc.group(1))
            niveau = TEXTE if texte else BLOQUEE
        elif medrxiv:
            texte, niveau = lire_medrxiv(medrxiv.group(1), medrxiv.group(2))
        elif essai:
            code, contenu, _ = demander(f"https://clinicaltrials.gov/api/v2/studies/{essai.group(1)}")
            texte = json.dumps(json.loads(contenu), ensure_ascii=False, indent=1) if code == 200 else ""
            niveau = FICHE if texte else BLOQUEE
        else:
            texte, niveau = lire_page(adresse, fichier)

        if texte:
            fichier.write_text(texte, encoding="utf-8")
        index[adresse] = {"fichier": fichier.name if texte else None, "niveau": niveau, "caracteres": len(texte)}
        INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{numero:3d}/{len(adresses)}  {niveau:17s} {len(texte):7d} caractères  {adresse}", flush=True)
    print(f"Copie écrite : {COPIE}")


def bilan():
    banque = yaml.safe_load(BANQUE.read_text(encoding="utf-8"))
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    for entree in banque:
        print(f"\n{entree['id']}  {entree['titre'][:90]}")
        for source in entree["sources"]:
            copie = meilleure_copie(source, index)
            print(f"  {copie['niveau']:17s} {copie['caracteres']:7d}  {source['titre'][:80]}")
    par_niveau = {}        # une source citée par plusieurs pistes ne compte qu'une fois
    for source in {source["url"]: source for entree in banque for source in entree["sources"]}.values():
        niveau = meilleure_copie(source, index)["niveau"]
        par_niveau[niveau] = par_niveau.get(niveau, 0) + 1
    print("\n" + " ; ".join(f"{niveau}, {nombre}" for niveau, nombre in sorted(par_niveau.items())))


def main():
    if sys.argv[1:] == ["telecharger"]:
        telecharger()
    elif sys.argv[1:] == ["bilan"]:
        bilan()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
