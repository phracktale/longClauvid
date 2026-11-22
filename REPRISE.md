# Reprendre le projet dans une nouvelle session

État au 2026-11-22, 20 h 15. Ce fichier sert à repartir sans rien perdre : il dit où en est le projet,
quelles règles s'appliquent et quoi faire ensuite. Il se met à jour à la fin de chaque session de travail.

**Pour reprendre : ouvrir le dépôt, lire ce fichier, puis `JOURNAL.md` pour le détail des décisions.**

## 1. Ce qui fait foi

| Question | Fichier |
| --- | --- |
| Que contient le projet ? | `README.md` |
| Quelles règles de preuve ? | `PROTOCOLE.md` |
| Pourquoi telle décision ? | `JOURNAL.md`, la plus récente en haut |
| Vue d'ensemble rédigée | `docs/cadrage.md` |
| Tout est-il cohérent ? | `python3 verifier.py`, qui doit finir par « Tous les contrôles passent » |

## 2. Règles fixées par le porteur du projet

- Le dépôt est public, sous licences MIT et CC BY 4.0. Les résultats doivent pouvoir être réutilisés.
- Aucun nom, aucune adresse électronique du porteur du projet ni des destinataires dans le dépôt.
  Les lettres y sont signées « [name] ».
- Rien n'est un avis médical. Les candidats sont des hypothèses pour des essais.
- Un résultat confié sous embargo n'entre pas dans le dépôt.
- Les demandes de fusion sont fusionnées automatiquement depuis le 2026-11-22, une fois les contrôles passés.
- Les lettres partent de la boîte du projet, après relecture du porteur du projet.
  Tout envoi se consigne dans le fichier `DEMANDES.md` du lot.
- Économie de moyens : un script pour récupérer des données en masse, un modèle moins coûteux
  pour lire et trier, le modèle principal pour décider et rédiger.
- Réponses en français, courtes, sourcées, sans adoucir.

## 3. Où en est le travail

| Chantier | État | Détail |
| --- | --- | --- |
| Lot 2, suivi après l'arrêt des traitements | Six demandes envoyées, aucune réponse | `analyses/lot-2/` |
| Lot 1, échantillons déjà collectés | Deux demandes envoyées, aucune réponse | `analyses/lot-1/` |
| Banque d'hypothèses à vérifier | 21 pistes déposées par deux agents, aucune relue | `registre/banque.yaml` |
| Simulateurs | Niveaux 1 et 2 construits, deux modèles publiés reproduits | `simulateurs/` |
| Bibliothèque de l'association #ApresJ20 | 10 466 références, copie locale à refaire dans chaque session | `outils/bibliotheque_apresj20.py` |

Une absence de réponse aux huit demandes se constate à partir du 2027-01-22.

## 4. À faire, dans l'ordre

1. **Relire la banque.** Pour chaque piste : rouvrir les sources, appliquer `outils/grille-statistique.md`,
   tester « inexplorée » sur la copie locale de la bibliothèque. Puis passer la piste à « vérifiée »
   ou « écartée », avec le motif. Les douze pistes de biologie (B001 à B012) n'ont pas encore été
   relues par le statisticien.
   Les sources ont surtout été lues par leur résumé : la relecture doit ouvrir les textes.
   Zones que le chercheur en biologie n'a pas couvertes : ferroptose, acides biliaires,
   hypoxie et HIF, tissu conjonctif. Ce qu'il a écarté est dans `JOURNAL.md`.
2. **Vérifier une remarque du statisticien** : selon lui, l'essai REVIVE teste la metformine
   sur un COVID long installé, ce que la fiche T03 ne dit pas. À confirmer sur le protocole de l'essai.
3. **Relever les réponses** aux huit demandes et les inscrire aux journaux des envois.
4. **Sous-lot 1b** : trouver une équipe habilitée pour les dosages sur échantillons conservés.
5. **Cartographie** : la revue actuelle est ciblée. La bibliothèque #ApresJ20 permet de la rendre systématique.
6. **Taux publiés du modèle de Craddock** : en attente du code demandé à son auteur.
7. **Étude PHOTOCOV** : signalée par le porteur du projet comme non terminée. Rien n'a été cherché.
8. **Document de cadrage** : `docs/cadrage.md` et sa version partagée hors dépôt n'ont pas encore
   de section sur la banque.

## 5. Façon de travailler

- Une branche par changement, une demande de fusion, fusion par rebasage, puis retour sur `main`.
- Avant chaque commit : `python3 verifier.py`.
- Une correction se date et se motive ; on ne réécrit pas l'histoire. Les plans d'analyse
  se modifient en bas de fichier, jamais dans la règle de décision.
- Une case « non trouvé » ne s'écrit qu'après une seconde source.
- Les agents de recherche déposent hors du dépôt ; l'intégration dans la banque est faite à part.

## 6. Ce qui ne survit pas à un changement de session

- La copie locale de la bibliothèque (dossier `cache/`, hors dépôt) : la refaire avec
  `python3 outils/bibliotheque_apresj20.py telecharger`, quatre minutes, une centaine de requêtes espacées.
- Le fil de la conversation. Tout ce qui compte doit donc être dans ce fichier, dans `JOURNAL.md`
  ou dans les journaux des envois.
