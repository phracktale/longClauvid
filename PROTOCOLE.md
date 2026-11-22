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
| 2. Détection | Recherche de ponts : A lié à B, B lié à C, A et C jamais cités ensemble (modèle ABC de Swanson, 1986) ; transpositions depuis des maladies mieux maîtrisées | Liste classée de pistes, de croisements et de transpositions | Chaque piste et chaque transposition remplit ses trois critères ci-dessous |
| 3. Confrontation | Matrice hypothèses × prédictions ; un relecteur défend, un autre attaque | Pour chaque paire d'hypothèses, le test décisif | Au moins une prédiction opposée par paire |
| 4. Simulation | Trois niveaux, voir `simulateurs/` | Puissance des plans d'essai, comportements attendus | Contrôles négatifs conformes ; un modèle publié reproduit |
| 5. Validation | Tests des prédictions sur données et échantillons existants | Analyses pré-enregistrées | Résultat retrouvé sur un second jeu de données |
| 6. Passage clinique | Essais N-de-1, essais enrichis par biomarqueur, plateforme adaptative | Protocole d'essai | Avis d'un comité d'éthique ; patients associés à la conception |

Les critères des phases 0 et 3 sont automatisés : `python3 outils/valider_registre.py`.
Celui de la phase 3 vérifie que chaque paire d'hypothèses a deux prédictions différentes ;
il ne remplace pas la relecture contradictoire.

## Confronter deux hypothèses

Les hypothèses ne s'excluent pas : plusieurs peuvent être vraies chez des patients différents.
Une confrontation demande, pour un patient ou une réponse donnés, laquelle est à l'œuvre.
Chaque fiche de `registre/confrontations.yaml` dit quelle mesure le montre, et où cette mesure
est possible :

| Accès | Définition |
| --- | --- |
| échantillons existants | Du sang déjà conservé par un essai ou une cohorte |
| suivi d'essais | Des données de suivi après l'arrêt d'un traitement |
| nouvelle collecte | Une biopsie, des cellules fraîches ou des prélèvements répétés |

Les confrontations se traitent par lots : celles qui partagent les mêmes échantillons
et les mêmes dosages s'instruisent ensemble.

## Une piste est « sous-exploitée » si elle remplit trois critères

1. Le résultat est publié et biologiquement précis : une molécule, une cellule, un mécanisme.
2. Aucun essai contrôlé terminé ne l'a testé sur des patients sélectionnés pour ce mécanisme.
3. Elle est rarement citée avec les autres pistes qu'elle pourrait éclairer.

## Transposer depuis une maladie mieux maîtrisée

Seconde source de pistes en phase 2 : partir des maladies qu'on sait guérir, contrôler
ou prévenir, et qui partagent un processus biologique avec nos pistes.
Les fiches sont dans `registre/transpositions.yaml`.

Une transposition entre au registre si elle remplit trois critères :

1. Le processus est documenté dans la maladie de référence, et au moins soupçonné
   dans le COVID long ou l'EM/SFC.
2. Un levier a été testé en clinique sur ce processus dans la maladie de référence.
3. Ce qui a déjà été tenté dans nos maladies est consigné, échecs compris.

Le degré de maîtrise se dit en cinq mots, parce qu'ils ne se transposent pas de la même façon :

| Maîtrise | Définition |
| --- | --- |
| guérison | La maladie disparaît et le traitement s'arrête |
| rémission | Plus de signes sans traitement, rechute possible |
| contrôle | Maladie tenue en respect tant que le traitement dure |
| prévention | On empêche la maladie d'apparaître |
| échec | Le levier a échoué dans la maladie de référence : contre-exemple à connaître |

Trois garde-fous :

- Une analogie n'est pas une preuve. Le niveau d'une transposition est celui de la preuve
  du processus dans nos maladies, pas celui du médicament ailleurs.
- Le sens de l'anomalie se vérifie d'abord : une même cible peut être trop active
  dans une maladie et pas assez dans l'autre (TRPM3, IDO1).
- Un essai négatif en tout-venant ne réfute pas une transposition s'il n'a ni sélectionné
  ses patients sur le processus, ni vérifié que la cible était atteinte. Il se consigne quand même.

Trois leçons de méthode viennent du VIH (fiches T01 à T03) : un marqueur quantitatif
a accéléré les essais, les combinaisons ont réussi là où chaque médicament seul échouait,
et l'arrêt programmé du traitement distingue une rémission d'un simple contrôle.

## Banque d'hypothèses à vérifier

La banque (`registre/banque.yaml`) est une boîte de dépôt. Des agents de recherche,
qui sont des programmes d'intelligence artificielle, ou des personnes y déposent des pistes
trouvées dans la littérature. Elle sert à ne rien perdre, pas à conclure.

- Une entrée « à vérifier » n'a été relue par personne. Elle ne compte pour rien :
  aucune fiche du registre ne peut s'appuyer sur elle.
- Chaque source dit si la page a été ouverte ou si seul son extrait a été lu.
  Une référence écrite de mémoire est interdite.
- Un agent ne modifie jamais le registre. Il dépose, un autre relit.
- Pour passer à « vérifiée », chaque source est rouverte par quelqu'un d'autre que le déposant,
  et la piste passe la grille de relecture statistique, déposée dans `outils/grille-statistique.md`
  avec les premières entrées.
- « Vérifiée » ne veut pas dire « vraie » : les erreurs sont relevées, la source qui porte le signal
  est lue en entier, et la piste reste une question à tester. Si cette source n'est lue que par son résumé,
  la piste reste « à vérifier ».
- Le relecteur suit `outils/consigne-relecteur.md` et lit des copies locales des sources
  (`outils/sources_banque.py`). Chaque affirmation de la piste reçoit un verdict et une citation ;
  un programme recherche chaque citation mot pour mot (`outils/relecture_banque.py`).
- Le texte déposé n'est pas réécrit. Les corrections vont dans le champ `relecture` de la piste,
  les doutes de la grille à la fin de son champ `risques`.
- Une mise à l'écart passe devant un contradicteur, qui défend la piste contre son motif
  en suivant `outils/consigne-contradicteur.md`. Son avis et le motif d'origine restent dans la piste.
- Une piste gardée passe devant un contradicteur chargé de l'attaquer, qui suit
  `outils/consigne-contradicteur-piste-gardee.md`. Son avis et la décision d'origine restent dans la piste.
- L'affirmation « inexplorée » se teste aussi contre la bibliothèque de l'association #ApresJ20,
  qui recense la littérature du COVID long. Une absence dans cette bibliothèque ne prouve rien.
  La recherche se fait sur une copie locale (`outils/bibliotheque_apresj20.py`), pas en ligne.
  Les termes cherchés, dans la bibliothèque comme dans les registres, sont écrits dans
  `analyses/banque/inexploree.py`.
- Une entrée vérifiée peut être promue en piste ; elle suit alors les règles du registre.
- Une entrée écartée reste dans la banque, avec son motif. Un échec se consigne aussi.

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
| 2. Modèles mécanistes | Des systèmes de régulation à plusieurs états stables | Quelle intervention, de quelle durée, fait sortir de l'état malade ? | Deux modèles publiés reproduits : Kashi 2019, et le réseau de Craddock 2015 pour ses états stables |
| 3. Criblage de repositionnement | Graphe de connaissances, génétique, modèles métaboliques | Quels médicaments existants touchent les cibles d'un endotype ? | À faire |
