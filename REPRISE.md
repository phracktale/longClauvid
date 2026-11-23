# Reprendre le projet dans une nouvelle session

État au 2026-11-23. Ce fichier sert à repartir sans rien perdre : il dit où en est le projet,
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
| Banque d'hypothèses | 26 pistes relues : 15 vérifiées, 3 promues, 3 écartées, 5 à vérifier ; cinq datent du 2026-11-23 (B022 à B026) ; chaque piste a eu un contradicteur, qui défend une mise à l'écart ou attaque une piste gardée | `registre/banque.yaml`, `analyses/banque/RELECTURE.md` |
| Registre | 17 pistes : P15, P16 et P17 viennent de la banque | `registre/pistes.yaml` |
| P15, humanine et MOTS-c | Plan déposé, tests faits. Jeu de 2019 : lecture « indécidable » ; l'écart vient de cinq bibliothèques de témoins sains chargées d'ARN ribosomique. Trois autres jeux de données : signal non retrouvé. Ce résultat est retiré des appuis de la piste, qui ne repose plus que sur les vésicules du COVID long. Une lettre aux auteurs de 2019 est partie le 2026-11-22 | `analyses/P15/RESULTATS.md` |
| P16, région HLA | Plan déposé. Test 1 fait : il échoue. Tests 2 à 4 non lus ; deux lettres parties le 2026-11-22. DecodeME a répondu par un message automatique : sa boîte ne répond pas aux messages reçus | `analyses/P16/RESULTATS.md` |
| P17, ADN mitochondrial | Plan déposé. Le test n'est pas faisable aujourd'hui : 18 % de puissance au mieux. La piste reste au registre. Une lettre partie le 2026-11-22 | `analyses/P17/PLAN.md` |
| Lot 2, suivi après l'arrêt des traitements | Six demandes envoyées ; une réponse automatique, rien sur le fond | `analyses/lot-2/` |
| Lot 1, échantillons déjà collectés | Deux demandes envoyées, aucune réponse | `analyses/lot-1/` |
| Fiche T03, metformine | Corrigée : deux essais sur un COVID long installé, sans bénéfice montré | `registre/transpositions.yaml` |
| Simulateurs | Niveaux 1 et 2 construits, deux modèles publiés reproduits | `simulateurs/` |
| Bibliothèque de l'association #ApresJ20 | 10 466 références, copie locale à refaire dans chaque session | `outils/bibliotheque_apresj20.py` |

Douze demandes sont parties le 2026-11-22 : huit pour les lots 1 et 2, quatre pour les pistes P15 à P17.
Une absence de réponse se constate à partir du 2027-01-22.

## 4. À faire, dans l'ordre

1. **Lire en entier six articles** que les programmes ne peuvent pas ouvrir : cinq pistes en dépendent.
   Le porteur du projet a donné son accord le 2026-11-22 pour les quatre premiers ; c'est le travail d'une personne.
   Pour B008 : l'étude de 2009 de la revue In Vivo (PMID 19567398). Pour B009 : PMID 41475665 et PMID 27401397.
   Pour B016 : l'article de la revue Sleep (PMID 37166330). Pour B004, depuis sa contradiction : l'article de 2008
   de la revue PNAS (PMID 18268335). Pour B023, déposée le 2026-11-23 : PMID 38310391.
   Une personne avec un accès de bibliothèque suffit.
   Deux lectures de plus préciseraient deux pistes gardées : PMID 42205163 pour B005, PMID 33367564 pour B019.
2. **Faire relire la banque par une personne du métier**, et réécrire le test d'une piste avant de la promouvoir.
   Les quinze pistes gardées ont été attaquées par un programme le 2026-11-22 : B004 repasse « à vérifier »,
   le niveau de B018 revient à C, neuf décisions sont reformulées. Aucun des quinze tests proposés n'est prêt :
   il manque un seuil, un sens attendu ou un jeu de données dont l'existence soit montrée.
   Le détail est dans le champ `relecture.attaque` de chaque piste. Relecteur, contradicteur et décideur
   restent des programmes du même type.
3. **Instruire les trois pistes promues.** Les plans sont déposés, et les tests sur fichiers publics sont faits.
   Le porteur du projet a décidé le 2026-11-22 : l'appui de 2019 est retiré de P15, P17 reste au registre,
   les quatre lettres partent après fusion. Elles sont parties le même jour (`DEMANDES.md` de P15, P16 et P17).
   Reste à lire les tests 2 à 4 de P16 quand les équipes auront répondu, et la réponse des auteurs de 2019 pour P15.
   Pour DecodeME, la voie qui répond est peut-être le formulaire de demande d'accès de sa page pour les chercheurs.
   La réplication de P15 sur d'autres personnes est faite, sur les trois jeux qui se lisent.
   Deux autres jeux demanderaient de réaligner 223 bibliothèques : non engagé.
   Autre premier pas peu coûteux, pour B002 : demander aux auteurs des lipidomiques déjà faites si les plasmalogènes
   ont été mesurés et si un groupe de personnes rétablies existe. Celle de 2025 décrit un sens contraire à la piste.
   Les deux lettres sont rédigées, non envoyées : `analyses/banque/DEMANDES.md`. Elles attendent la relecture
   du porteur du projet.
4. **Relever les réponses** aux douze demandes et les inscrire aux journaux des envois.
   La lettre à Bergen n'est pas dans la boîte du projet : le porteur du projet la suit de son côté.
5. **Sous-lot 1b** : trouver une équipe habilitée pour les dosages sur échantillons conservés.
6. **Zones non couvertes** : fait le 2026-11-23 pour la ferroptose, les acides biliaires, l'hypoxie et HIF.
   Cinq pistes déposées, relues et contredites (B022 à B026) ; aucune n'est solide. Le tissu conjonctif est couvert par B018.
   Les agents de recherche suivent désormais `outils/consigne-chercheur.md`.
7. **Cartographie** : premier pas fait le 2026-11-23, `analyses/cartographie/CARTE.md`. Sur 10 466 références,
   1 258 contiennent un terme d'une piste. Reste la phase 1 proprement dite : lire les références retenues,
   en extraire les relations, mesurer la précision sur un échantillon relu à la main. C'est un travail de lecture
   en nombre, pour un modèle moins coûteux, à lancer piste par piste en commençant par les plus denses (P08, P14, P01).
8. **Taux publiés du modèle de Craddock** : en attente du code demandé à son auteur.
9. **Version partagée du document de cadrage**, hors dépôt : elle n'a ni la section sur la banque,
   ni les trois nouvelles pistes, ni la correction de la fiche T03, ni la contradiction des pistes gardées.

Abandonné par le porteur du projet le 2026-11-22 : la recherche de l'étude PHOTOCOV, introuvable sous ce nom.

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
  avec `outils/consigne-contradicteur.md`. Une piste gardée passe devant un contradicteur qui l'attaque,
  avec `outils/consigne-contradicteur-piste-gardee.md`. La marche à suivre est à la fin de `analyses/banque/RELECTURE.md`.
- Des agents lancés ensemble nomment leurs fichiers de travail d'après leur piste :
  deux scripts du même nom se sont écrasés le 2026-11-22, et un fichier annoncé n'était pas sur le disque.
- Un plan d'analyse passe devant un relecteur avant son dépôt, avec `outils/consigne-relecteur-de-plan.md`.
  Une fois les données ouvertes, sa règle ne se corrige plus : toute modification s'écrit en bas du plan.
- Un site qui répond par un contrôle anti-robot n'est pas contourné : la source est notée bloquée.

## 6. Ce qui ne survit pas à un changement de session

- Les copies locales, dans le dossier `cache/`, hors dépôt : la bibliothèque, les sources de la banque,
  les fichiers rendus par les relecteurs et les contradicteurs, les données de P15 (300 Mo) et de P16 (340 Mo), qui se retéléchargent. Les deux premières se refont en sept minutes ; les fichiers
  des relecteurs ne se refont qu'en relisant. Leur contenu utile est dans le champ `relecture` des pistes.
- Les dépendances Python : `pip install -r requirements.txt` avant `python3 verifier.py`.
- Les avis des contradicteurs et les dépôts des agents de recherche, dans `cache/relecture/` et `cache/depots/` :
  leur contenu utile est dans les champs `relecture` des pistes.
- Le fil de la conversation. Tout ce qui compte doit donc être dans ce fichier, dans `JOURNAL.md`
  ou dans les journaux des envois.
- Le travail de la session du 2026-11-22 au soir est dans la demande de fusion n° 14, fusionnée.
  Les plans d'analyse des pistes promues, leurs premiers résultats et les décisions du porteur du projet
  sont dans la demande de fusion n° 15, fusionnée. Le dépôt des plans y est le commit `534e29d`
  (`0de5a88` avant la fusion par rebasage : c'est ce second numéro que cite un message de commit).
- La contradiction des quinze pistes gardées, les lettres de B002 et le dépôt du 2026-11-23 sont sur la branche
  `ccr-48b05551-3su41y`, dans une demande de fusion ouverte le 2026-11-23 avec l'accord du porteur du projet.
