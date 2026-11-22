# Reprendre le projet dans une nouvelle session

État au 2026-11-22, 21 h 30. Ce fichier sert à repartir sans rien perdre : il dit où en est le projet,
quelles règles s'appliquent et quoi faire ensuite. Il se met à jour à la fin de chaque session de travail.

**Pour reprendre : ouvrir le dépôt, lire ce fichier, puis `JOURNAL.md` pour le détail des décisions.**

## 1. Ce qui fait foi

| Question | Fichier |
| --- | --- |
| Que contient le projet ? | `README.md` |
| Quelles règles de preuve ? | `PROTOCOLE.md` |
| Pourquoi telle décision ? | `JOURNAL.md`, la plus récente en haut |
| Vue d'ensemble rédigée | `docs/cadrage.md` |
| Où en est la banque ? | `analyses/banque/RELECTURE.md` |
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
| Banque d'hypothèses | 21 pistes relues : 15 vérifiées, 3 écartées, 3 à vérifier ; les mises à l'écart ont eu un contradicteur | `registre/banque.yaml`, `analyses/banque/RELECTURE.md` |
| Lot 2, suivi après l'arrêt des traitements | Six demandes envoyées ; une réponse automatique, rien sur le fond | `analyses/lot-2/` |
| Lot 1, échantillons déjà collectés | Deux demandes envoyées, aucune réponse | `analyses/lot-1/` |
| Fiche T03, metformine | Corrigée : deux essais sur un COVID long installé, sans bénéfice montré | `registre/transpositions.yaml` |
| Simulateurs | Niveaux 1 et 2 construits, deux modèles publiés reproduits | `simulateurs/` |
| Bibliothèque de l'association #ApresJ20 | 10 466 références, copie locale à refaire dans chaque session | `outils/bibliotheque_apresj20.py` |

Une absence de réponse aux huit demandes se constate à partir du 2027-01-22.

## 4. À faire, dans l'ordre

1. **Lire en entier quatre articles** que les programmes ne peuvent pas ouvrir : trois pistes en dépendent.
   Pour B008 : l'étude de 2009 de la revue In Vivo (PMID 19567398). Pour B009 : PMID 41475665 et PMID 27401397.
   Pour B016 : l'article de la revue Sleep (PMID 37166330). Une personne avec un accès de bibliothèque suffit.
2. **Faire attaquer les quinze pistes gardées** : seules les mises à l'écart ont eu un contradicteur.
   La relecture contradictoire a levé deux mises à l'écart sur cinq ; l'inverse est possible.
   Une relecture par une personne du métier vaudrait mieux qu'un programme de plus.
3. **Choisir les pistes vérifiées à promouvoir** au registre : décision du porteur du projet.
   Trois tests ne demandent aucun laboratoire. B011 : relire deux gènes dans un jeu de données public (GSE130353).
   B013 et B020 : des statistiques résumées, à demander pour DecodeME. B002 : demander les plasmalogènes
   aux auteurs des lipidomiques déjà faites.
4. **Étude PHOTOCOV** : introuvable sous ce nom dans quatre sources. Il faut son nom complet,
   son promoteur ou sa ville.
5. **Relever les réponses** aux huit demandes et les inscrire aux journaux des envois.
   La lettre à Bergen n'est pas dans la boîte du projet : le porteur du projet la suit de son côté.
6. **Sous-lot 1b** : trouver une équipe habilitée pour les dosages sur échantillons conservés.
7. **Zones non couvertes** par le chercheur en biologie : ferroptose, acides biliaires, hypoxie et HIF.
   Le tissu conjonctif est désormais couvert par B018.
8. **Cartographie** : la revue actuelle est ciblée. La bibliothèque #ApresJ20 permet de la rendre systématique.
9. **Taux publiés du modèle de Craddock** : en attente du code demandé à son auteur.
10. **Version partagée du document de cadrage**, hors dépôt : elle n'a ni la section sur la banque
    ni la correction de la fiche T03.

## 5. Façon de travailler

- Une branche par changement, une demande de fusion, fusion par rebasage, puis retour sur `main`.
- Avant chaque commit : `python3 verifier.py`.
- Une correction se date et se motive ; on ne réécrit pas l'histoire. Les plans d'analyse
  se modifient en bas de fichier, jamais dans la règle de décision. Le texte déposé en banque
  ne se réécrit pas : la relecture s'ajoute.
- Une case « non trouvé » ne s'écrit qu'après une seconde source.
- Les agents de recherche déposent hors du dépôt ; l'intégration dans la banque est faite à part.
- Relire une piste : `outils/sources_banque.py`, puis `outils/relecture_banque.py`, avec
  `outils/consigne-relecteur.md`. Une piste écartée passe ensuite devant un contradicteur,
  avec `outils/consigne-contradicteur.md`. La marche à suivre est à la fin de `analyses/banque/RELECTURE.md`.
- Un site qui répond par un contrôle anti-robot n'est pas contourné : la source est notée bloquée.

## 6. Ce qui ne survit pas à un changement de session

- Les copies locales, dans le dossier `cache/`, hors dépôt : la bibliothèque, les sources de la banque,
  les fichiers rendus par les relecteurs. Les deux premières se refont en sept minutes ; les fichiers
  des relecteurs ne se refont qu'en relisant. Leur contenu utile est dans le champ `relecture` des pistes.
- Le fil de la conversation. Tout ce qui compte doit donc être dans ce fichier, dans `JOURNAL.md`
  ou dans les journaux des envois.
- Le travail de la session du 2026-11-22 au soir est sur la branche `ccr-8543cc2e-yawna7`,
  sans demande de fusion ouverte : elle reste à ouvrir.
