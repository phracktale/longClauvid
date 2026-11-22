# Consigne donnée au relecteur d'un plan d'analyse

Ce texte est remis tel quel au relecteur, avec le dossier du plan à la place de `{dossier}`.
Le relecteur est une personne ou un programme d'intelligence artificielle ; ce n'est pas l'auteur du plan.
Il lit le plan avant l'ouverture des données : après, la règle ne se corrige plus sans laisser de trace.
La formulation d'une consigne oriente la lecture : elle fait donc partie du dossier.

---

Le plan `{dossier}/PLAN.md` va être déposé. Ton travail est de chercher ce qui, dans ce plan, laisserait
un choix à faire après l'ouverture des données. Tu ne juges pas si la question est la bonne.

## Ce que tu lis

- Le plan : `{dossier}/PLAN.md`, et les programmes du même dossier
- La fiche de la piste : `registre/pistes.yaml`
- La grille de relecture : `outils/grille-statistique.md`

Tous les chemins partent de la racine du dépôt.

## Règles

1. Pas de recherche en ligne. N'ouvre et ne télécharge aucune donnée.
2. Ne modifie aucun fichier du dépôt. Tu peux lancer les programmes du dossier.
3. Chaque remarque cite la phrase du plan qu'elle vise, copiée telle quelle.
4. Une remarque sans exemple ne compte pas. Pas de remarque de style.

## Ce que tu cherches

| Type | Ce que c'est |
| --- | --- |
| non classé | Un résultat possible que la règle de décision ne classe pas. Donne des valeurs chiffrées |
| ambigu | Un résultat que la règle classe de deux façons, ou une mesure qui peut se calculer de deux façons |
| chiffre | Un chiffre du plan qui ne correspond pas à la sortie du programme du dossier |
| source | Un constat « lu avant ce plan » sans source, ou une source qui ne peut pas le porter |
| conclusion | Une lecture que la règle tire et que le résultat ne permettrait pas |

## Le fichier à écrire

Écris `cache/relecture/plans/{piste}.json`, et rien d'autre :

```json
{
  "plan": "{dossier}/PLAN.md",
  "remarques": [
    {"type": "non classé | ambigu | chiffre | source | conclusion",
     "citation": "la phrase du plan, copiée telle quelle",
     "probleme": "ce qui ne va pas, en deux phrases au plus",
     "exemple": "le cas chiffré qui le montre",
     "correction": "la plus petite modification qui règle le problème"}
  ],
  "avis": "prêt | à corriger",
  "raison": "trois phrases au plus"
}
```

Termine par un résumé de huit lignes au plus. La décision ne t'appartient pas.
