# Lot 2 : que deviennent les répondeurs quand le traitement s'arrête ?

Plan d'analyse déposé le 2026-11-22, avant toute demande et toute réception de données.
La date du commit fait foi. Toute modification ultérieure s'écrit en bas de ce fichier,
avec sa date et son motif.

**Vérification faite essai par essai, un seul des cinq traitements a déjà publié un suivi
après l'arrêt : le daratumumab. Ce suivi ne départage pas encore les hypothèses,
faute d'une mesure sur les sérums conservés.**

> Ce plan ne produit aucun avis médical. Il dit quelles données demander,
> et comment les lire une fois reçues.

## 1. La question

L'hypothèse H6 dit que la maladie est un second état stable : on n'en sort qu'en franchissant
un seuil, et une fois sorti on y reste. Elle prédit que l'amélioration des répondeurs persiste
après l'élimination du médicament. Elle est réfutée si l'effet disparaît toujours à l'arrêt.

Chaque hypothèse rivale dit autre chose : la maladie est entretenue par une cause toujours
présente, et la rechute suit le retour de cette cause.

| Paire | Traitement | Cause entretenue selon l'hypothèse rivale |
| --- | --- | --- |
| H1 et H6 | Daratumumab | Des IgG qui se fixent aux neurones |
| H2 et H6 | Baricitinib | Une boucle interféron alimentée en continu |
| H3 et H6 | Rapamycine | Un défaut du contrôle des protéines dans le muscle |
| H4 et H6 | Anticorps anti-spike | Un antigène viral persistant |
| H6 et H7 | Naltrexone | Un canal TRPM3 défaillant |

## 2. Ce que la vérification a montré

| Traitement | Essai | Durée du traitement | Suivi hors traitement | Source |
| --- | --- | --- | --- | --- |
| Daratumumab | Pilote ouvert, 10 patientes | 4 injections en 6 semaines ; 3 de plus pour 4 patientes | 12 à 24 mois depuis l'inclusion | [Fluge 2025](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1607353/full) |
| Daratumumab | ResetME, randomisé, 66 participants, en cours | 5 injections, la dernière à 26 semaines | 72 semaines par participant, soit 46 après la dernière injection | [Fiche du projet](https://mrr.mecfs-research.org/en/mrr/projects/Kc46hyZDSCyX9ump8KepRA) |
| Baricitinib | REVERSE-LC, randomisé, 550 patients visés, en cours | 6 mois | Une visite à 12 mois, soit 6 mois après l'arrêt | [Registre](https://clinicaltrials.gov/study/NCT06631287), [projet](https://www.icudelirium.org/projects/reverse-lc) |
| Rapamycine | Étude ouverte sans groupe témoin, 86 patients | Prescription continue, évaluations à 30, 60 et 90 jours | Aucun dans l'étude publiée. L'essai suivant prévoit un retrait randomisé : poursuite ou placebo pendant 60 jours | [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12538759/) |
| Anticorps anti-spike | outSMART-LC (AER002), randomisé, 36 participants | Une seule perfusion | Jusqu'à un an ; critères principaux à 3 mois | [Registre](https://classic.clinicaltrials.gov/show/NCT05877508), [fiche](https://reaganudall.org/clinical-trial/anti-sars-cov-2-monoclonal-antibodies-long-covid-covid-19) |
| Naltrexone | Essai canadien, randomisé, terminé | 16 semaines | Aucune évaluation après la 16e semaine | [Protocole](https://pubmed.ncbi.nlm.nih.gov/38740499/) |
| Naltrexone | Brave-LC, randomisé, 6 à 25 ans | 16 semaines | Non trouvé | [Registre](https://clinicaltrials.gov/study/NCT07916259) |

Ce que le pilote du daratumumab a déjà publié :

- Six patientes sur dix se sont nettement améliorées. Cinq le sont restées jusqu'à la fin
  du suivi ; la sixième a rechuté en partie.
- Les IgG totales, au plus bas vers 5 mois, sont ensuite remontées.
- Une des cinq a rechuté en partie 26 mois après le début du traitement.

Ces faits vont dans le sens de la prédiction de H6, mais H1 les prédit aussi : si les plasmocytes
en cause ont disparu, les IgG totales peuvent revenir sans les IgG nocives. Seule la fixation
des IgG aux neurones, mesurée sur les sérums du suivi, départage les deux.

Conséquence pour le registre : la paire H6 et H7 est reclassée en « nouvelle collecte ».
Aucun des deux essais de la naltrexone n'inscrit d'évaluation après l'arrêt.

## 3. Le repère d'arrêt

« Après l'arrêt » ne veut pas dire la même chose pour chaque traitement.

| Traitement | Repère |
| --- | --- |
| Daratumumab | Le retour des IgG totales à leur niveau de départ : l'effet dure plus longtemps que le médicament |
| Baricitinib, rapamycine, naltrexone | La dernière prise, plus cinq demi-vies du médicament |
| Anticorps anti-spike | La disparition de l'antigène plasmatique, chez les patients qui en portaient |

Les demi-vies sont à relever dans la notice de chaque produit avant l'analyse. Elles ne l'ont pas été ici.

## 4. Les données demandées

Des chiffres agrégés suffisent. Aucune donnée individuelle n'est demandée.

1. Le nombre de répondeurs dans chaque bras à la fin du traitement, selon le critère de l'essai.
2. Parmi eux, le nombre de ceux qui répondent encore 3, 6 et 12 mois après le repère.
3. La durée médiane de traitement chez ceux qui tiennent et chez ceux qui rechutent.
4. Le marqueur de l'hypothèse rivale aux mêmes dates, s'il a été mesuré.

## 5. La règle de décision, fixée avant les données

Pour chaque traitement :

| Situation | Lecture |
| --- | --- |
| Essai contrôlé, et l'écart entre traitement et placebo persiste au moins 3 mois après le repère (intervalle de confiance à 95 % excluant zéro) | H6 soutenue pour ce traitement |
| Essai contrôlé, et l'écart a disparu 3 mois après le repère, quelle que soit la durée du traitement | H6 affaiblie pour ce traitement |
| La rechute suit le retour du marqueur de l'hypothèse rivale | L'hypothèse rivale est soutenue |
| La rémission tient alors que ce marqueur est revenu | H6 soutenue contre l'hypothèse rivale |
| Essai ouvert ou sans groupe témoin | Résultat descriptif, niveau C : aucun statut ne change |
| Essai négatif : pas plus de répondeurs que sous placebo | Non informatif pour ce lot |

Pour le statut de H6 dans le registre :

- « soutenue » : l'écart persiste dans au moins un essai contrôlé ;
- « affaiblie » : l'écart a disparu dans tous les essais contrôlés disponibles, au moins deux ;
- inchangé dans tous les autres cas.

## 6. Limites connues d'avance

- Les effectifs sont petits. Un essai de 66 participants compte au plus quelques dizaines de répondeurs.
- Sans groupe témoin, une amélioration durable peut venir de l'évolution naturelle de la maladie.
- Deux essais sur sept sont négatifs ou sans effet global : ils ne renseigneront pas ce lot.
- Les équipes peuvent ne pas répondre. Une absence de réponse se consigne dans `DEMANDES.md`.
- Le modèle de Craddock, reproduit dans ce dépôt, suggère qu'un repère biologique vaut mieux
  qu'un délai fixe. Ce plan en tient compte pour le daratumumab et l'anticorps, pas pour les autres.

## Modifications

### 2026-11-22, quelques heures après le dépôt : trois corrections du tableau de la section 2

La règle de décision de la section 5 n'est pas modifiée. Aucune donnée n'a été reçue entre-temps.

| Essai | Première version | Correction | Motif |
| --- | --- | --- | --- |
| REVERSE-LC | Suivi hors traitement « non trouvé » | Une visite à 12 mois, six mois après l'arrêt | La page du projet le dit ; la fiche du registre n'avait pas pu être lue |
| AER002 | Suivi de 3 mois | Évaluations jusqu'à un an | Trois mois est l'échéance des critères principaux, pas la fin du suivi |
| Rapamycine | « Aucun arrêt programmé » | Un retrait randomisé est prévu dans l'essai suivant | L'article le décrit ; seul son résumé avait été lu |

Conséquence : trois essais en cours ou prévus comportent un suivi après l'arrêt, et non un seul.
