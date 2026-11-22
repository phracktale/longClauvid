# Consigne donnée au contradicteur d'une mise à l'écart

Ce texte est remis tel quel au contradicteur, avec l'identifiant de la piste à la place de `{id}`.
Le contradicteur est une personne ou un programme d'intelligence artificielle ; ce n'est ni le déposant,
ni le relecteur, ni celui qui a décidé. La formulation d'une consigne oriente la lecture :
elle fait donc partie du dossier.

---

La piste `{id}` de la banque d'hypothèses vient d'être écartée. Tu es son avocat : ton travail est de chercher
ce qui s'oppose à cette mise à l'écart. Tu ne plaides pas contre l'évidence : si le motif est exact, tu le dis.

## Ce que tu lis

- La piste, avec sa relecture et son motif de mise à l'écart : `cache/relecture/{id}/fiche.yaml`
- La liste de ses sources, avec le chemin de leur copie locale : `cache/relecture/{id}/sources.md`
- La grille de relecture : `outils/grille-statistique.md`

Tous les chemins partent de la racine du dépôt.

## Règles

1. Lis les copies locales, et elles seules. Pas de recherche en ligne.
2. N'utilise pas ta mémoire pour combler un manque. Ce qui n'est pas dans une copie locale est « non vérifiable ».
3. Une citation se copie telle quelle depuis la copie locale : d'un seul tenant, 200 caractères au plus,
   sans rien corriger. Elle sera recherchée mot pour mot par un programme.
4. Dans le champ « fichier », mets le nom du fichier de la copie locale, sans le chemin.

## Ce que tu produis

### 1. Le contrôle du motif

Découpe en faits vérifiables le champ `motif` de la piste, puis les champs `corrections` et `inexploree`
de sa relecture. Pour chaque fait : est-il confirmé par la copie locale, inexact, contredit, ou non trouvé ?
Donne la citation. Le verdict s'écrit « confirmée », « inexacte », « contredite » ou « non trouvée ».

### 2. La défense de la piste

Cherche dans les copies ce qui plaide pour garder la piste, et que la mise à l'écart ne dit pas :
un résultat qui va dans son sens, une analyse de sensibilité qui tient, une limite de l'étude contraire,
un écart entre ce que le motif affirme et ce que la source montre. Un argument sans citation ne compte pas.

### 3. Ton avis

Un seul mot parmi trois, puis ta raison en trois phrases au plus :

| Avis | Sens |
| --- | --- |
| tient | Le motif est exact et suffit à écarter la piste |
| tient en partie | Le motif est exact, mais il ne suffit pas, ou il doit être reformulé |
| ne tient pas | Un fait du motif est faux, ou un argument sérieux a été ignoré |

Dis aussi ce qu'il faudrait changer dans le motif, s'il y a lieu.

## Le fichier à écrire

Écris `cache/relecture/contre/{id}.json`, et rien d'autre dans le dépôt :

```json
{
  "id": "{id}",
  "affirmations": [
    {"champ": "motif", "affirmation": "le fait, en une phrase",
     "verdict": "confirmée | inexacte | contredite | non trouvée",
     "fichier": "nom de la copie locale", "citation": "passage copié tel quel",
     "commentaire": "ce que dit la source, si le verdict n'est pas « confirmée »"}
  ],
  "defense": [
    {"argument": "l'argument, en une phrase", "fichier": "nom de la copie locale", "citation": "passage copié tel quel"}
  ],
  "avis": "tient | tient en partie | ne tient pas",
  "raison": "trois phrases au plus",
  "a_changer": "ce qu'il faudrait changer dans le motif, ou une chaîne vide"
}
```

Termine par un résumé de huit lignes au plus. La décision ne t'appartient pas.
