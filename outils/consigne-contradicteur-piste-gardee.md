# Consigne donnée au contradicteur d'une piste gardée

Ce texte est remis tel quel au contradicteur, avec l'identifiant de la piste à la place de `{id}`.
Le contradicteur est une personne ou un programme d'intelligence artificielle ; ce n'est ni le déposant,
ni le relecteur, ni celui qui a décidé. La formulation d'une consigne oriente la lecture :
elle fait donc partie du dossier.

Cette consigne est le pendant de `outils/consigne-contradicteur.md`, qui fait défendre une piste écartée.
Ici, le contradicteur attaque une piste gardée.

---

La piste `{id}` de la banque d'hypothèses a été gardée après sa relecture. Tu es chargé de l'attaquer :
ton travail est de chercher ce qui s'oppose à cette décision. Tu n'attaques pas contre l'évidence :
si la décision est exacte, tu le dis.

## Ce que tu lis

- La piste, avec sa relecture et sa décision : `cache/relecture/{id}/fiche.yaml`
- La liste de ses sources, avec le niveau de lecture et le chemin de leur copie locale : `cache/relecture/{id}/sources.md`
- La grille de relecture : `outils/grille-statistique.md`
- Les règles de décision et leur interprétation : la section « Règles de décision » de `analyses/banque/RELECTURE.md`
- Si la fiche porte un champ `promue_en` : la piste de ce nom dans `registre/pistes.yaml`, puis le plan
  et les résultats de son dossier, `analyses/<ce nom>/PLAN.md` et `analyses/<ce nom>/RESULTATS.md`, s'ils existent.
  Ces fichiers disent ce qui a déjà été testé ou retiré : n'attaque pas un appui que le projet a déjà retiré.

Tous les chemins partent de la racine du dépôt.

## Règles

1. Lis les copies locales, et elles seules. Pas de recherche en ligne.
2. N'utilise pas ta mémoire pour combler un manque. Ce qui n'est pas dans une copie locale est « non vérifiable ».
3. Une citation se copie telle quelle depuis la copie locale d'une source : d'un seul tenant, 200 caractères au plus,
   sans rien corriger. Elle sera recherchée mot pour mot par un programme. Un fichier du dépôt ne se cite pas.
4. Dans le champ « fichier », mets le nom du fichier de la copie locale, sans le chemin.
5. Lis chaque copie en entier. Pour une copie de plus de 80 000 caractères, cherche d'abord
   les passages utiles par mots-clés, puis lis autour.

## Ce que tu produis

### 1. Le contrôle de la décision

Découpe en faits vérifiables le champ `decision` de la relecture, puis ses champs `corrections` et `inexploree`,
et les constats de son champ `contradiction` s'il existe. Pour chaque fait : est-il confirmé par la copie locale,
inexact, contredit, ou non trouvé ? Donne la citation.
Le verdict s'écrit « confirmée », « inexacte », « contredite » ou « non trouvée ».

### 2. L'attaque de la piste

Cherche dans les copies ce qui s'oppose au maintien de la piste, à son statut ou à son niveau,
et que la relecture ne dit pas. Pose au moins ces six questions :

1. La source qui porte le signal est-elle lue en entier ? Regarde le niveau de sa copie dans `sources.md`.
   Si elle n'est lue que par son résumé, la règle met la piste « à vérifier ».
2. Cette source va-t-elle contre la piste : résultat nul sur son critère principal, effet de sens contraire,
   témoins qui montrent le même écart, sous-groupe choisi après coup ?
3. La grille classe-t-elle le signal « probablement artefactuel » (questions 5, 8 ou 9),
   sans contre-analyse qui le confirme ?
4. Une autre source de la piste rapporte-t-elle un échec de réplication ou un résultat de sens contraire ?
5. Le niveau de preuve est-il trop haut au regard de sa définition dans la grille ?
6. Le test proposé peut-il réfuter la piste : un seuil, un jeu de données ou des échantillons dont l'existence est montrée ?

Un argument sans citation ne compte pas.

### 3. Ton avis

Un seul mot parmi trois, puis ta raison en trois phrases au plus :

| Avis | Sens |
| --- | --- |
| tient | La décision est exacte : la piste peut rester à ce statut et à ce niveau |
| tient en partie | La piste peut rester, mais son niveau, son test ou le texte de sa décision doit changer |
| ne tient pas | Une règle met la piste « à vérifier » ou « écartée », ou un fait qui porte la décision est faux |

Dis aussi ce qu'il faudrait changer, s'il y a lieu : le statut, le niveau, le texte de la décision.

## Le fichier à écrire

Écris `cache/relecture/attaque/{id}.json`, et rien d'autre dans le dépôt :

```json
{
  "id": "{id}",
  "affirmations": [
    {"champ": "decision", "affirmation": "le fait, en une phrase",
     "verdict": "confirmée | inexacte | contredite | non trouvée",
     "fichier": "nom de la copie locale", "citation": "passage copié tel quel",
     "commentaire": "ce que dit la source, si le verdict n'est pas « confirmée »"}
  ],
  "attaque": [
    {"argument": "l'argument, en une phrase", "fichier": "nom de la copie locale", "citation": "passage copié tel quel"}
  ],
  "avis": "tient | tient en partie | ne tient pas",
  "raison": "trois phrases au plus",
  "a_changer": "ce qu'il faudrait changer, ou une chaîne vide"
}
```

Termine par un résumé de huit lignes au plus. La décision ne t'appartient pas.
