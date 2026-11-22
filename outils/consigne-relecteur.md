# Consigne donnée au relecteur d'une piste de la banque

Ce texte est remis tel quel au relecteur, avec l'identifiant de la piste à la place de `{id}`.
Le relecteur est une personne ou un programme d'intelligence artificielle ; ce n'est jamais le déposant.
La formulation d'une consigne oriente la relecture : elle fait donc partie du dossier.

---

Tu relis la piste `{id}` de la banque d'hypothèses d'un projet de recherche ouverte sur le COVID long
et l'EM/SFC. Tu ne l'as pas déposée : ne lui fais pas confiance. Ton travail est de la confronter
à ses sources, pas de la défendre.

## Ce que tu lis

- La piste : `cache/relecture/{id}/fiche.yaml`
- La liste de ses sources, avec le chemin de leur copie locale : `cache/relecture/{id}/sources.md`
- La grille de relecture : `outils/grille-statistique.md`

Tous les chemins partent de la racine du dépôt.

## Règles

1. Lis les copies locales, et elles seules. Pas de recherche en ligne.
2. N'utilise pas ta mémoire pour combler un manque. Si une information n'est pas dans une copie locale,
   écris « non trouvée ». Une source dont la copie n'est qu'un résumé se juge sur ce résumé.
3. Lis chaque copie en entier. Pour une copie de plus de 80 000 caractères, cherche d'abord
   les passages utiles par mots-clés, puis lis autour.
4. Une citation se copie telle quelle depuis la copie locale : d'un seul tenant, 200 caractères au plus,
   sans rien corriger. Elle sera recherchée mot pour mot par un programme.

## Ce que tu produis

### 1. La vérification des affirmations

Découpe la piste en affirmations vérifiables : chaque chiffre, effectif, résultat, plan d'étude,
événement indésirable ou état d'un essai, dans tous les champs de la piste. Laisse de côté le décompte
des recherches du champ `pourquoi_inexploree` (nombre de résultats d'une requête) : il est contrôlé à part.

Pour chaque affirmation, donne un verdict :

| Verdict | Sens |
| --- | --- |
| confirmée | La copie locale dit la même chose |
| inexacte | La copie locale dit autre chose : donne ce qu'elle dit |
| non trouvée | La copie locale n'en parle pas, ou la copie n'est qu'un résumé qui ne le dit pas |
| contredite | La copie locale dit le contraire |

### 2. La grille

Applique les dix questions de la grille à la source, ou aux sources, qui portent le signal de la piste ;
pas aux sources de contexte. Pour chaque question : y a-t-il un doute (« oui », « non », « sans objet »),
et pourquoi, en une phrase appuyée sur la source.

### 3. Ce que la piste tait

Relève ce que les sources disent d'important et que la piste ne dit pas : résultat contraire,
limite reconnue par les auteurs, financement par un fabricant, lien d'intérêts, analyse non prévue
au protocole, correction ou rétractation.

### 4. Le niveau de preuve

Propose un niveau de A à D, selon la définition de la grille, et dis si celui de la piste est justifié.

## Le fichier à écrire

Écris `cache/relecture/{id}.json`, et rien d'autre dans le dépôt :

```json
{
  "id": "{id}",
  "sources": [
    {"titre": "titre cité par la piste", "fichier": "nom de la copie locale ou null",
     "lu": "texte intégral | résumé | page partielle | non lisible", "remarque": ""}
  ],
  "affirmations": [
    {"champ": "risques", "affirmation": "l'affirmation, en une phrase",
     "verdict": "confirmée | inexacte | non trouvée | contredite",
     "fichier": "nom de la copie locale", "citation": "passage copié tel quel",
     "commentaire": "ce que dit la source, si le verdict n'est pas « confirmée »"}
  ],
  "grille": [
    {"question": 1, "doute": "oui | non | sans objet", "justification": "une phrase"}
  ],
  "omissions": ["ce que la piste tait, une phrase par point"],
  "niveau_propose": "C",
  "niveau_justifie": true,
  "commentaire_niveau": "une phrase",
  "synthese": "cinq phrases au plus : ce qui tient, ce qui ne tient pas"
}
```

Termine par un résumé de dix lignes au plus : nombre d'affirmations par verdict, doutes de la grille,
et ce qui devrait faire écarter ou garder la piste. La décision ne t'appartient pas.
