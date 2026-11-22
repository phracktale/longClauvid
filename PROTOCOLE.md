# Protocole de recherche

Version du 2026-11-22.

Le protocole applique l'inférence forte (Platt, 1964) : pour chaque paire d'hypothèses,
chercher l'observation qui en élimine une, plutôt qu'accumuler des indices favorables.

Les phases 0 à 5 se font sans laboratoire. La phase 6 exige une équipe clinique
et un comité d'éthique.

## Les sept phases

| Phase | Travail | Livrable | Critère de passage |
| --- | --- | --- | --- |
| 0. Cadrage | Registre des hypothèses, plan d'analyse, dépôt horodaté avant toute analyse | Registre versionné | Chaque hypothèse porte une prédiction réfutable |
| 1. Cartographie | Requêtes sur PubMed, Europe PMC, OpenAlex et les registres d'essais ; extraction de triplets entité–relation–entité | Graphe de connaissances, diagramme de sélection des articles | Précision de l'extraction d'au moins 90 % sur un échantillon relu à la main |
| 2. Détection | Recherche de ponts : A lié à B, B lié à C, A et C jamais cités ensemble (modèle ABC de Swanson, 1986) | Liste classée de pistes et de croisements | Chaque piste remplit les trois critères ci-dessous |
| 3. Confrontation | Matrice hypothèses × prédictions ; un relecteur défend, un autre attaque | Pour chaque paire d'hypothèses, le test décisif | Au moins une prédiction opposée par paire |
| 4. Simulation | Trois niveaux, voir `simulateurs/` | Puissance des plans d'essai, comportements attendus | Contrôles négatifs conformes ; un modèle publié reproduit |
| 5. Validation | Tests des prédictions sur données et échantillons existants | Analyses pré-enregistrées | Résultat retrouvé sur un second jeu de données |
| 6. Passage clinique | Essais N-de-1, essais enrichis par biomarqueur, plateforme adaptative | Protocole d'essai | Avis d'un comité d'éthique ; patients associés à la conception |

Le critère de la phase 0 est automatisé : `python3 outils/valider_registre.py`.

## Une piste est « sous-exploitée » si elle remplit trois critères

1. Le résultat est publié et biologiquement précis : une molécule, une cellule, un mécanisme.
2. Aucun essai contrôlé terminé ne l'a testé sur des patients sélectionnés pour ce mécanisme.
3. Elle est rarement citée avec les autres pistes qu'elle pourrait éclairer.

## Niveaux de preuve

| Niveau | Définition |
| --- | --- |
| A | Répliqué par des équipes indépendantes |
| B | Une étude solide, ou deux cohortes |
| C | Une seule équipe, ou étude non contrôlée |
| D | Hypothèse théorique |

Une piste ne monte de niveau qu'après réplication par une équipe indépendante.

## Statuts d'une hypothèse

`ouverte` → `soutenue`, `affaiblie` ou `réfutée` selon les tests ; `abandonnée` si elle
n'est plus instruite. Tout changement de statut s'écrit dans l'historique de la fiche,
avec la source ou le résultat qui le motive.

## Règles de traçabilité

- Une affirmation = une source (adresse, DOI ou PMID), et la date de lecture.
- Registre, requêtes, code et résultats vivent dans ce dépôt ; chaque décision est
  consignée dans `JOURNAL.md` avec son motif.
- Chaque simulation est identifiée par sa graine et sa version de code (le commit).
- Les résultats négatifs sont consignés et publiés comme les positifs.

## Règles de fiabilité

- Double extraction indépendante en phase 1, avec mesure de l'accord entre lecteurs.
- Toute analyse de sous-groupes corrige les comparaisons multiples.
- Chaque analyse et chaque simulateur embarque un contrôle négatif.
- Une sortie de modèle de langage est un candidat à vérifier, jamais une preuve.
- Le profil de risque d'un candidat est examiné avant son efficacité attendue.

## Les trois niveaux de simulation

| Niveau | Ce qu'il simule | Question tranchée | État |
| --- | --- | --- | --- |
| 1. Cohorte virtuelle | Des essais entiers sur des patients à endotype caché | Quel plan d'essai peut voir un effet limité à un sous-groupe ? | Construit |
| 2. Modèles mécanistes | Des systèmes de régulation à plusieurs états stables | Quelle intervention, de quelle durée, fait sortir de l'état malade ? | Premier modèle construit (Kashi 2019) ; modèle à plusieurs variables à faire (Craddock 2015) |
| 3. Criblage de repositionnement | Graphe de connaissances, génétique, modèles métaboliques | Quels médicaments existants touchent les cibles d'un endotype ? | À faire |
