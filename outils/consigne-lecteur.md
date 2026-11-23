# Consigne donnée au lecteur d'un lot de résumés, pour la cartographie

Ce texte est remis tel quel au lecteur, avec le chemin de son lot à la place de `{lot}`.
Le lecteur est une personne ou un programme d'intelligence artificielle, d'un modèle moins coûteux que celui qui décide.
La formulation d'une consigne oriente la lecture : elle fait donc partie du dossier.

---

Tu lis un lot de résumés d'articles sur le COVID long. Chaque résumé a été retenu parce qu'il contient un terme
d'une piste de recherche. Ton travail : dire si l'article porte vraiment sur cette piste, et en tirer les relations
qu'il rapporte. Tu ne juges pas la piste. Rien de ce que tu écris n'est un avis médical.

## Ce que tu lis

Le fichier `{lot}`. Il donne la piste (`piste`, `sujet`), les termes qui ont fait retenir les résumés (`termes`),
et une liste de références : `numero`, `titre`, `annee`, `doi`, `resume`.

## Règles

1. Tu lis le titre et le résumé, et eux seuls. Pas de recherche en ligne. N'utilise pas ta mémoire de l'article :
   ce qui n'est pas dans le résumé n'existe pas.
2. Tu traites toutes les références du lot, dans l'ordre, sans en sauter.
3. Une citation se copie telle quelle depuis le résumé : d'un seul tenant, 200 caractères au plus, sans rien corriger.
   Elle sera recherchée mot pour mot par un programme.
4. Tu n'écris que le fichier demandé. Si tu écris un script, il porte le nom de ton lot et reste dans le même dossier.

## Ce que tu produis, pour chaque référence

**La pertinence**, un mot parmi trois :

| Pertinence | Sens |
| --- | --- |
| centrale | Le sujet de la piste est l'objet principal de l'article |
| secondaire | L'article le mesure ou le teste parmi d'autres choses |
| en passant | Le terme apparaît, mais l'article ne mesure ni ne teste rien sur ce sujet |

**Le type**, un parmi six : « mesure chez des patients », « essai », « modèle animal ou cellulaire », « revue »,
« hypothèse », « autre ».

**Les relations**, de zéro à trois, seulement si la pertinence est « centrale » ou « secondaire », et seulement
celles qui touchent le sujet de la piste. Une relation dit : telle entité, telle relation, telle entité.
Les entités sont des noms courts en anglais, tels que le résumé les écrit (une molécule, une cellule, un symptôme,
un groupe de patients). La relation est un verbe parmi : `increased_in`, `decreased_in`, `unchanged_in`,
`associated_with`, `not_associated_with`, `causes`, `improves`, `does_not_improve`, `predicts`, `binds`.
Chaque relation porte une citation, et son **sens** pour la piste : « soutient », « contredit » ou « neutre ».
Une revue ou un texte d'hypothèse n'a pas de relation : elle ne rapporte pas de mesure.

## Le fichier à écrire

Écris, à côté du lot, le fichier du même nom terminé par `-lu.json` (par exemple `P08-lot-01-lu.json`) :

```json
{
  "lot": "nom du fichier du lot",
  "lectures": [
    {"numero": 123, "pertinence": "centrale | secondaire | en passant",
     "type": "mesure chez des patients | essai | modèle animal ou cellulaire | revue | hypothèse | autre",
     "relations": [
       {"entite_1": "fibrin", "relation": "increased_in", "entite_2": "long COVID patients",
        "sens": "soutient | contredit | neutre", "citation": "passage copié tel quel"}
     ]}
  ]
}
```

Termine par un résumé de cinq lignes au plus : nombre de références lues, répartition des pertinences,
nombre de relations, et ce qui t'a posé un doute.
