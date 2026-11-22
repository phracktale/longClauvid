"""
Teste l'affirmation « inexplorée » de chaque piste de la banque, à trois endroits :
1. la copie locale de la bibliothèque de l'association #ApresJ20 (outils/bibliotheque_apresj20.py) ;
2. le registre d'essais ClinicalTrials.gov, limité au COVID long et à l'EM/SFC ;
3. Europe PMC, limité aux articles dont le titre ou le résumé nomme ces maladies.

Les termes cherchés sont écrits ci-dessous, piste par piste : une requête fait partie du résultat.
Une absence ne prouve rien ; une présence oblige à lire ce qui a été trouvé.

Usage :
    python3 analyses/banque/inexploree.py            # toutes les pistes
    python3 analyses/banque/inexploree.py B012 B016  # certaines pistes

Chaque rapport est écrit dans cache/inexploree/, hors du dépôt. Deux requêtes en ligne par piste.
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
BIBLIOTHEQUE = RACINE / "cache" / "apresj20.json"
RAPPORTS = RACINE / "cache" / "inexploree"
EN_TETES = {"User-Agent": "copie-locale-lecture-seule/1.0"}
LIGNES = 40               # nombre de titres affichés par recherche, les plus récents d'abord

MALADIES = ('"long covid" OR "post-covid" OR "post-acute sequelae" OR "post-acute COVID" OR PASC'
            ' OR "myalgic encephalomyelitis" OR "chronic fatigue syndrome"')

# Par piste : les motifs cherchés dans la bibliothèque (expressions régulières, sans tenir compte
# de la casse), puis les termes envoyés tels quels à ClinicalTrials.gov et à Europe PMC.
RECHERCHES = {
    "B001": ([r"pyruvate dehydrogenase", r"dichloroacetate", r"\bPDK[124]?\b", r"\bPDH\b"],
             '"pyruvate dehydrogenase" OR dichloroacetate OR PDK1 OR PDK4'),
    "B002": ([r"plasmalogen", r"peroxisom", r"ether (phospho)?lipid", r"\bVLCFA"],
             "plasmalogen OR plasmalogens OR peroxisome OR peroxisomal OR fenofibrate OR phenylbutyrate"),
    "B003": ([r"orexin", r"hypocretin", r"narcolep"],
             "orexin OR hypocretin OR narcolepsy OR daridorexant OR suvorexant OR oveporexton"),
    "B004": ([r"ryanodine", r"\bRyR[12]?\b", r"calstabin", r"dantrolene", r"rycal"],
             "ryanodine OR RyR1 OR calstabin OR Rycal OR ARM210 OR dantrolene"),
    "B005": ([r"catechol", r"\bDOPAC\b", r"\bDHPG\b", r"droxidopa", r"synuclein"],
             'catechol OR catechols OR catecholamine OR DOPAC OR DHPG OR droxidopa OR "alpha-synuclein"'),
    "B006": ([r"selenoprotein", r"SELENOP", r"selenium", r"triiodothyronine", r"\bT3\b"],
             '"selenoprotein P" OR SELENOP OR selenium OR triiodothyronine OR "low T3"'),
    "B007": ([r"cibinetide", r"ARA[ -]?290", r"innate repair", r"erythropoietin", r"corneal confocal"],
             'cibinetide OR "ARA 290" OR "innate repair receptor" OR erythropoietin OR "corneal confocal"'),
    "B008": ([r"D-lact", r"lactic acidosis"],
             '"D-lactate" OR "D-lactic"'),
    "B009": ([r"vasopressin", r"copeptin", r"desmopressin", r"diabetes insipidus", r"antidiuretic"],
             'vasopressin OR copeptin OR desmopressin OR "diabetes insipidus"'),
    "B010": ([r"endothelin", r"macitentan", r"bosentan", r"ambrisentan", r"aprocitentan", r"sparsentan"],
             "endothelin OR bosentan OR macitentan OR ambrisentan OR aprocitentan OR sparsentan"),
    "B011": ([r"humanin", r"MOTS-c", r"mitochondrial[- ]derived peptide"],
             'humanin OR "MOTS-c" OR "mitochondrial-derived peptide"'),
    "B012": ([r"\biron\b", r"hepcidin", r"ferritin", r"transferrin"],
             'iron OR hepcidin OR ferritin OR "ferric carboxymaltose"'),
    "B013": ([r"\bHLA\b", r"human leukocyte antigen", r"DRB1", r"DQA1"],
             'HLA OR "human leukocyte antigen" OR DRB1 OR DQA1'),
    "B014": ([r"FOXP4", r"rs9367106", r"genome-wide association"],
             "FOXP4 OR rs9367106"),
    "B015": ([r"pregnan"],
             "pregnancy OR pregnant"),
    "B016": ([r"sleep apn", r"\bOSA\b", r"\bCPAP\b", r"positive airway pressure"],
             '"sleep apnea" OR "sleep apnoea" OR CPAP OR "positive airway pressure"'),
    "B017": ([r"insulin resistance", r"metformin", r"\bTyG\b", r"triglyceride", r"pioglitazone", r"liver enzyme"],
             '"insulin resistance" OR metformin OR pioglitazone OR "liver enzymes" OR "triglyceride-glucose"'),
    "B018": ([r"hypermobil", r"ehlers", r"connective tissue", r"beighton"],
             'hypermobility OR "Ehlers-Danlos" OR "connective tissue" OR Beighton'),
    "B019": ([r"IL-13", r"IL-5\b", r"interleukin[- ]13", r"interleukin[- ]5\b", r"mononucleosis", r"pre-?pandemic"],
             '"IL-13" OR "IL-5" OR "interleukin-13" OR "interleukin-5" OR "infectious mononucleosis"'),
    "B020": ([r"mitochondrial DNA", r"mtDNA", r"copy number", r"mendelian randomi"],
             '"mitochondrial DNA copy number" OR "mtDNA copy number" OR "Mendelian randomization"'),
    "B021": ([r"antibiotic", r"doxycycline", r"azithromycin", r"minocycline", r"moxifloxacin", r"levofloxacin"],
             "antibiotic OR antibiotics OR doxycycline OR azithromycin OR minocycline"),
}


def demander(adresse, parametres):
    requete = urllib.request.Request(adresse + "?" + urllib.parse.urlencode(parametres), headers=EN_TETES)
    with urllib.request.urlopen(requete, timeout=90) as reponse:
        contenu = json.load(reponse)
    time.sleep(1)
    return contenu


def annee(reference):
    trouvee = re.search(r"(19|20)\d\d", reference["date"])
    return trouvee.group(0) if trouvee else "----"


def dans_la_bibliotheque(motifs, references):
    """Les références dont le titre, le résumé ou les mots-clés contiennent au moins un des motifs."""
    motif = re.compile("|".join(motifs), re.IGNORECASE)
    trouvees = [reference for reference in references
                if motif.search(" ".join([reference["title"], reference["abstractNote"], *reference["mots_cles"]]))]
    trouvees.sort(key=annee, reverse=True)
    return [f"{annee(reference)}  {reference['title']}  {reference['DOI'] or reference['url']}" for reference in trouvees]


def dans_le_registre(termes):
    """Les essais de ClinicalTrials.gov qui portent sur nos maladies et contiennent un des termes."""
    reponse = demander("https://clinicaltrials.gov/api/v2/studies",
                       {"query.cond": MALADIES, "query.term": termes, "pageSize": LIGNES, "countTotal": "true"})
    lignes = []
    for etude in reponse["studies"]:
        protocole = etude["protocolSection"]
        interventions = [i["name"] for i in protocole.get("armsInterventionsModule", {}).get("interventions", [])]
        lignes.append(f"{protocole['identificationModule']['nctId']}  {protocole['statusModule']['overallStatus']}  "
                      f"{protocole['identificationModule']['briefTitle']}  [{' ; '.join(interventions)[:90]}]")
    return reponse["totalCount"], lignes


def dans_europe_pmc(termes):
    """Les articles dont le titre ou le résumé contient un des termes et nomme une de nos maladies."""
    reponse = demander("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                       {"query": f"TITLE_ABS:({termes}) AND TITLE_ABS:({MALADIES})", "format": "json",
                        "resultType": "lite", "pageSize": LIGNES, "sort": "P_PDATE_D desc"})
    lignes = [f"{article.get('pubYear')}  {article.get('title')}  {article.get('journalTitle') or 'prépublication'}  "
              f"{article.get('source')}:{article.get('id')}" for article in reponse["resultList"]["result"]]
    return reponse["hitCount"], lignes


def main():
    pistes = sys.argv[1:] or sorted(RECHERCHES)
    references = json.loads(BIBLIOTHEQUE.read_text(encoding="utf-8"))["references"]
    RAPPORTS.mkdir(parents=True, exist_ok=True)
    for piste in pistes:
        motifs, termes = RECHERCHES[piste]
        bibliotheque = dans_la_bibliotheque(motifs, references)
        essais, lignes_essais = dans_le_registre(termes)
        articles, lignes_articles = dans_europe_pmc(termes)
        rapport = [
            f"# {piste}",
            f"\n## Bibliothèque #ApresJ20 : {len(bibliotheque)} référence(s) pour {' | '.join(motifs)}",
            *bibliotheque[:LIGNES],
            f"\n## ClinicalTrials.gov : {essais} essai(s) pour {termes}",
            *lignes_essais,
            f"\n## Europe PMC : {articles} article(s) pour {termes}",
            *lignes_articles,
        ]
        (RAPPORTS / f"{piste}.md").write_text("\n".join(rapport) + "\n", encoding="utf-8")
        print(f"{piste}  bibliothèque {len(bibliotheque):4d} ; essais {essais:4d} ; Europe PMC {articles:5d}", flush=True)


if __name__ == "__main__":
    main()
