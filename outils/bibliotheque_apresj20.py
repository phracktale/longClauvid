"""
Copie locale de la bibliothèque Zotero de l'association #ApresJ20, pour y chercher sans la solliciter.

La bibliothèque recense la littérature du COVID long. Ce script la télécharge une fois,
lentement, puis toutes les recherches se font sur la copie locale : zéro requête de plus.

La copie n'est pas versée au dépôt (dossier cache/, ignoré par git) : c'est le travail
de l'association, on le consulte, on ne le republie pas.

Usage :
    python3 outils/bibliotheque_apresj20.py telecharger      # une centaine de requêtes, 4 minutes
    python3 outils/bibliotheque_apresj20.py chercher ferroptosis
    python3 outils/bibliotheque_apresj20.py chercher bile acid   # tous les mots doivent être présents
"""

import json
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

ADRESSE = "https://api.zotero.org/groups/5562177"
COPIE = Path(__file__).resolve().parent.parent / "cache" / "apresj20.json"
PAR_PAGE = 100           # le maximum accepté par Zotero
PAUSE = 2                # secondes entre deux requêtes
ESSAIS = 3               # tentatives par requête, quand la connexion est coupée
EN_TETES = {
    "Zotero-API-Version": "3",
    "User-Agent": "longClauvid (https://github.com/phracktale/longClauvid) ; copie locale, lecture seule",
}
CHAMPS_GARDES = ["title", "date", "DOI", "url", "publicationTitle", "abstractNote", "itemType", "dateAdded"]


def demander(chemin):
    """Fait une requête et renvoie (contenu, en-têtes). Attend si Zotero le demande."""
    requete = urllib.request.Request(ADRESSE + chemin, headers=EN_TETES)
    for essai in range(1, ESSAIS + 1):
        try:
            with urllib.request.urlopen(requete, timeout=60) as reponse:
                contenu = json.load(reponse)
                en_tetes = reponse.headers
            break
        except urllib.error.HTTPError:
            raise                      # un refus du serveur ne se retente pas
        except (OSError, ValueError) as erreur:   # connexion coupée ou réponse tronquée
            if essai == ESSAIS:
                raise
            print(f"Connexion coupée ({erreur}) ; nouvel essai dans 15 secondes", flush=True)
            time.sleep(15)
    attente = en_tetes.get("Backoff") or en_tetes.get("Retry-After")
    time.sleep(int(attente) if attente else PAUSE)
    return contenu, en_tetes


def telecharger():
    collections, _ = demander("/collections?limit=100")
    noms = {c["key"]: c["data"]["name"] for c in collections if not c["data"].get("deleted")}

    # Une copie incomplète est reprise là où elle s'est arrêtée : rien n'est redemandé.
    references = []
    if COPIE.exists():
        ancienne = json.loads(COPIE.read_text(encoding="utf-8"))
        if not ancienne["complete"]:
            references = ancienne["references"]
    debut = len(references)
    total = None
    while total is None or debut < total:
        page, en_tetes = demander(f"/items/top?limit={PAR_PAGE}&start={debut}")
        total = int(en_tetes["Total-Results"])
        for element in page:
            donnees = element["data"]
            reference = {champ: donnees.get(champ, "") for champ in CHAMPS_GARDES}
            reference["cle"] = element["key"]
            reference["mots_cles"] = [mot["tag"] for mot in donnees.get("tags", [])]
            reference["collections"] = [noms.get(cle, cle) for cle in donnees.get("collections", [])]
            references.append(reference)
        debut += PAR_PAGE
        ecrire(references, complete=debut >= total)
        print(f"{len(references)} références sur {total}", flush=True)
    print(f"Copie écrite : {COPIE}")


def ecrire(references, complete):
    COPIE.parent.mkdir(exist_ok=True)
    copie = {"telecharge_le": time.strftime("%Y-%m-%d"), "complete": complete, "references": references}
    COPIE.write_text(json.dumps(copie, ensure_ascii=False), encoding="utf-8")


def simplifier(texte):
    """Minuscules, sans accents : « Fatigué » et « fatigue » se valent."""
    sans_accents = unicodedata.normalize("NFD", texte).encode("ascii", "ignore").decode()
    return sans_accents.lower()


def chercher(mots, references=None):
    """Renvoie les références dont le titre, le résumé ou les mots-clés contiennent tous les mots."""
    if references is None:
        references = json.loads(COPIE.read_text(encoding="utf-8"))["references"]
    mots = [simplifier(mot) for mot in mots]
    trouvees = []
    for reference in references:
        texte = simplifier(" ".join([reference["title"], reference["abstractNote"], *reference["mots_cles"]]))
        if all(mot in texte for mot in mots):
            trouvees.append(reference)
    return trouvees


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "telecharger":
        telecharger()
    elif len(sys.argv) >= 3 and sys.argv[1] == "chercher":
        trouvees = chercher(sys.argv[2:])
        print(f"{len(trouvees)} référence(s) pour « {' '.join(sys.argv[2:])} »")
        for reference in trouvees[:20]:
            print(f"- {reference['date'][:4] or '----'}  {reference['title']}  {reference['DOI'] or reference['url']}")
        if len(trouvees) > 20:
            print(f"… et {len(trouvees) - 20} autres")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
