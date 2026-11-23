# Consigne donnée à l'agent de recherche qui dépose des pistes en banque

Ce texte est remis tel quel à l'agent, avec le nom de la zone à la place de `{zone}` et son identifiant de fichier
à la place de `{fichier}`. L'agent est une personne ou un programme d'intelligence artificielle. Il dépose ; un autre relit.
La formulation d'une consigne oriente la recherche : elle fait donc partie du dossier.

La consigne des deux premiers agents, lancés le 2026-11-22, n'a pas été conservée. Celle-ci est écrite le 2026-11-23,
d'après les règles du protocole et la forme des 21 premières pistes.

---

Tu cherches, dans la littérature, des pistes sur le COVID long et l'EM/SFC dans une zone que le projet n'a pas couverte :
**{zone}**. Tu ne conclus rien : tu déposes des questions à tester, qu'un autre relira contre leurs sources.
Rien de ce que tu écris n'est un avis médical.

## Ce que tu lis d'abord

- Les règles de la banque : `PROTOCOLE.md`, sections « Une piste est sous-exploitée », « Banque d'hypothèses à vérifier »
  et « Niveaux de preuve ».
- Ce qui existe déjà, pour ne pas le redéposer : les noms des pistes de `registre/pistes.yaml`, des fiches de
  `registre/transpositions.yaml`, et les titres de `registre/banque.yaml`.
- Deux pistes déjà déposées, pour la forme : B003 et B012 dans `registre/banque.yaml`. Ne lis pas leur champ `relecture`
  comme un modèle à remplir : il n'est pas de ton ressort.
- La grille de relecture, pour savoir ce qui sera demandé à ta piste : `outils/grille-statistique.md`.

## Ce qu'est une piste

Un processus biologique précis de la zone (une molécule, une cellule, un mécanisme), mesuré au moins une fois
dans le COVID long ou l'EM/SFC, ou bien documenté et maîtrisé dans une autre maladie et seulement soupçonné dans les nôtres.
Elle porte une prédiction qui peut être réfutée, et un test faisable sur des données ou des échantillons qui existent déjà.

## Règles

1. Tu cherches par les interfaces officielles, et par elles seules : Europe PMC (recherche et texte intégral en accès ouvert),
   PubMed (résumés), ClinicalTrials.gov (interface du registre). Une requête à la fois, une seconde de pause entre deux.
   Rien du projet n'est envoyé aux sites.
2. Un site qui répond par un contrôle anti-robot n'est pas contourné : la source est notée bloquée.
3. Une référence écrite de mémoire est interdite. Chaque source citée a été ouverte par toi pendant cette recherche.
   Son champ `lu` vaut « page » si tu as ouvert sa page, son résumé ou son texte, « extrait » si tu n'as lu que l'extrait
   d'une liste de résultats. Son titre dit entre parenthèses ce que tu as lu : « (résumé) » ou « (texte intégral) ».
4. Un chiffre se recopie depuis la source, avec son effectif. Un calcul de ta main se dit comme tel.
5. L'affirmation « inexplorée » se prouve par ses requêtes : écris les termes exacts, l'interface et le nombre de résultats,
   puis ce que tu as trouvé. Termine par « Non trouvé ne veut pas dire inexistant. »
6. Cherche aussi ce qui va contre la piste : résultat nul, essai négatif, effet de sens contraire. Ce que tu trouves
   va dans le champ `risques`, avec les dangers du médicament ou du levier évoqué, examinés avant son efficacité attendue.
7. Trois pistes au plus. Mieux vaut une piste bien sourcée que trois fragiles. Si la zone ne donne rien de solide,
   dépose moins, ou rien, et dis-le.
8. Tu écris hors du dépôt, dans `cache/depots/`, et nulle part ailleurs. Tes fichiers de travail portent `{fichier}`
   dans leur nom. Tu ne modifies ni le registre ni la banque, et tu ne fais aucun commit.

## Les fichiers à écrire

### `cache/depots/{fichier}.yaml`

Une liste YAML, une entrée par piste, avec ces champs et eux seuls :

```yaml
- titre: l'affirmation de la piste, en une phrase
  domaine_source: la maladie ou le domaine d'où vient le résultat
  processus_commun: ce qui se mesure, précisément
  enonce: l'hypothèse, puis « Si c'est vrai, ... » avec ce qu'on doit observer
  pourquoi_inexploree: les requêtes, leurs résultats, ce qui a été trouvé
  test_propose: le test sur l'existant, puis « La piste est réfutée si ... »
  donnees_existantes: les cohortes, biobanques ou jeux de données nommés, avec ce qui reste à confirmer
  risques: ce qui va contre la piste, les limites des sources, les dangers du levier
  niveau: A, B, C ou D, selon le protocole
  sources:
  - titre: titre de la source, revue et année (résumé)
    url: https://...
    lu: page
  origine: agent biologie
  date: 'AAAA-MM-JJ'
```

Écris en français, en phrases courtes, sans jargon inutile.

### `cache/depots/{fichier}-compte-rendu.md`

Quinze lignes au plus : les requêtes faites, les pistes déposées, les pistes écartées avec leur motif en une ligne,
ce que tu n'as pas pu lire, et les limites de ta recherche.

Termine par un résumé de huit lignes au plus. La décision de garder une piste ne t'appartient pas.
