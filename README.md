# longClauvid

Recherche ouverte et traçable sur le COVID long, l'encéphalomyélite myalgique (EM/SFC)
et les syndromes post-infectieux. Le dépôt repère des pistes sous-exploitées,
les confronte entre elles et les simule avant qu'une équipe clinique ne les teste.

> **Ce dépôt produit des hypothèses classées, pas des traitements.**
> Rien ici n'est un avis médical. Plusieurs candidats cités sont des médicaments
> à risque sérieux, à n'utiliser que dans un essai clinique.

## Contenu

| Dossier | Rôle |
| --- | --- |
| `docs/cadrage.md` | L'état des lieux des essais, les pistes sous-exploitées, les typologies de patients |
| `PROTOCOLE.md` | Les sept phases, leurs critères de passage, les règles de traçabilité et de fiabilité |
| `JOURNAL.md` | Chaque décision, avec son motif et les options écartées |
| `registre/` | Sources, pistes, endotypes, transpositions, confrontations et hypothèses, un fichier par hypothèse |
| `registre/banque.yaml` | La banque d'hypothèses à vérifier, alimentée par des agents de recherche ; chaque piste relue porte ses corrections et sa décision |
| `analyses/` | Les plans d'analyse, déposés avant toute donnée, et les demandes aux équipes |
| `outils/valider_registre.py` | Refuse une hypothèse sans prédiction réfutable ou une affirmation sans source |
| `outils/bibliotheque_apresj20.py` | Copie locale de la bibliothèque de l'association #ApresJ20, pour y chercher sans la solliciter |
| `outils/grille-statistique.md` | Dix questions pour relire une piste de la banque |
| `outils/sources_banque.py` | Copie locale des sources de la banque, en texte intégral quand une interface officielle le donne |
| `outils/consigne-chercheur.md` | La consigne remise à l'agent de recherche qui dépose des pistes en banque |
| `outils/consigne-relecteur.md` | La consigne remise au relecteur d'une piste, telle quelle |
| `outils/consigne-contradicteur.md` | La consigne remise à celui qui défend une piste écartée |
| `outils/consigne-contradicteur-piste-gardee.md` | La consigne remise à celui qui attaque une piste gardée |
| `outils/consigne-relecteur-de-plan.md` | La consigne remise à celui qui relit un plan d'analyse avant l'ouverture des données |
| `outils/relecture_banque.py` | Prépare la relecture et recherche mot pour mot chaque citation du relecteur et des contradicteurs |
| `analyses/banque/` | Le compte rendu de la relecture, les termes du test « inexplorée » et les calculs d'effectifs |
| `analyses/P15/`, `P16/`, `P17/` | Pour chaque piste promue : son plan d'analyse, ses calculs et ses lettres |
| `REPRISE.md` | Où en est le projet et quoi faire ensuite, pour reprendre dans une nouvelle session |
| `simulateurs/niveau1/` | Cohorte virtuelle : quel plan d'essai peut voir un effet limité à un sous-groupe |
| `simulateurs/niveau2/` | Modèles mécanistes : le piège métabolique IDO de Kashi 2019, et le réseau logique de Craddock 2015 |
| `verifier.py` | Lance tous les contrôles du dépôt |
| `LICENSE`, `LICENSES/` | Les licences : MIT pour le code, CC BY 4.0 pour le reste |

## Démarrer

```bash
pip install -r requirements.txt
python3 verifier.py                              # tous les contrôles
python3 outils/valider_registre.py               # le registre seul
python3 simulateurs/niveau1/simulateur_endotypes.py
python3 simulateurs/niveau2/piege_ido.py
python3 simulateurs/niveau2/craddock_2015.py     # environ une minute
python3 outils/sources_banque.py bilan           # après « telecharger » : ce qui est lisible de chaque source
```

## Où en est le protocole

| Phase | État |
| --- | --- |
| 0. Cadrage | Registre ouvert le 2026-11-22 : 7 hypothèses, 17 pistes, 5 endotypes, 11 transpositions, 21 confrontations, 152 sources ; 21 pistes en banque, relues : 14 vérifiées, dont 3 promues au registre, 3 écartées, 4 à vérifier |
| 1. Cartographie | À faire : la revue actuelle est ciblée, pas systématique |
| 2. Détection | Première série de 11 transpositions ; détection systématique à faire |
| 3. Confrontation | Première matrice : 21 paires, sans relecture contradictoire |
| 4. Simulation | Niveaux 1 et 2 construits, deux modèles publiés reproduits ; niveau 3 à faire |
| 5. Validation | Cinq plans d'analyse déposés (lots 1 et 2, pistes P15 à P17) ; douze demandes envoyées le 2026-11-22, aucune réponse sur le fond ; premiers tests faits sur des données publiques pour P15 et P16 |
| 6. Passage clinique | Exige une équipe habilitée et un comité d'éthique |

## Résultats à ce jour

- **Niveau 1.** Un essai tout-venant de 200 patients ne détecte qu'une fois sur cinq
  un traitement très efficace chez 20 % des patients ; un biomarqueur imparfait porte
  cette chance à 77 %. Détail : `simulateurs/niveau1/RESULTATS.md`.
- **Niveau 2.** Le modèle de Kashi 2019 est reproduit aux arrondis publiés près.
  Avec ses paramètres, on entre dans le piège en quelques semaines et on en sort
  en mois ou en années. Détail : `simulateurs/niveau2/RESULTATS.md`.
- **Niveau 2 bis.** Le réseau de Craddock est reproduit : ses cinq états stables publiés
  sont retrouvés, et eux seuls. Dans ce modèle, l'ordre des traitements décide : 25 % de
  retours à l'état sain dans un sens, 0 % dans l'autre. Les taux publiés ne sont retrouvés
  qu'en partie. Détail : `simulateurs/niveau2/RESULTATS_RESEAU_LOGIQUE.md`.
- **Confrontations.** Huit paires d'hypothèses sur vingt et une se tranchent sans nouveau
  prélèvement : quatre sur du sang déjà conservé, quatre sur le suivi d'essais après l'arrêt
  du traitement. Détail : `registre/confrontations.yaml`.
- **Lot 2.** Un seul traitement a publié un suivi après l'arrêt : dans le pilote du daratumumab,
  5 répondeuses sur 6 restent améliorées à 12–24 mois. Ce résultat ne départage pas encore
  les hypothèses 1 et 6. Détail : `analyses/lot-2/PLAN.md`.
- **Lot 1.** Aucune des quatre paires n'a de mesure conjointe publiée. Un constat existe déjà :
  dans la cohorte LIINC, l'antigène n'est pas plus fréquent chez les femmes. Deux paires peuvent
  avancer sans nouveau dosage. Détail : `analyses/lot-1/PLAN.md`.
- **Transpositions.** Onze processus partagés avec des maladies mieux maîtrisées, dont trois
  fiches sur le VIH. Les transpositions déjà essayées dans le COVID long ont échoué chez
  des patients non sélectionnés. Détail : `registre/transpositions.yaml`.
- **Banque.** Les 21 pistes déposées ont été relues contre leurs sources : 14 sont vérifiées,
  3 écartées, 4 restent à vérifier. « Vérifiée » ne veut pas dire « vraie ». Les chiffres recopiés
  étaient presque toujours exacts ; l'affirmation « inexplorée » était fausse ou incomplète
  pour 16 pistes. Cinq mises à l'écart ont eu un contradicteur : deux ont été levées.
  Les quinze pistes gardées en ont eu un à leur tour, chargé de les attaquer : une repasse
  « à vérifier », un niveau de preuve baisse, et aucun des quinze tests proposés n'est prêt.
  Trois pistes vérifiées sont promues au registre (P15 à P17) : leur premier test ne demande
  aucun laboratoire. Détail : `analyses/banque/RELECTURE.md`.
- **Pistes promues.** Un plan d'analyse est déposé pour chacune, avant toute donnée, et relu
  avant son dépôt. P15 : lecture fixée d'avance « indécidable » ; la baisse d'expression publiée
  en 2019 n'existe que dans une des deux séries de bibliothèques, et elle vient de cinq bibliothèques
  de témoins sains chargées d'ARN ribosomique. Elle n'est pas retrouvée dans trois autres jeux
  de données, sur 41 patients et 47 témoins. Le porteur du projet a retiré ce résultat des appuis
  de la piste. P16 : le variant le plus associé au COVID long
  n'est pas associé à l'EM/SFC dans DecodeME ; les trois autres comparaisons attendent un chiffre
  des équipes. P17 : le test prévu n'est pas faisable aujourd'hui, faute d'un jeu de cas assez grand ;
  la piste reste au registre.
  Détail : `analyses/P15/RESULTATS.md`, `analyses/P16/RESULTATS.md`, `analyses/P17/PLAN.md`.
- **Metformine.** Elle a été testée sur un COVID long installé dans deux essais randomisés,
  sans bénéfice montré ; la fiche T03, qui disait le contraire, est corrigée.

## Règles du dépôt

1. Une affirmation = une source dans `registre/sources.yaml`, avec sa date de lecture.
2. Une décision = une entrée dans `JOURNAL.md`, avec son motif.
3. Une hypothèse ne se supprime pas : son statut change, son historique s'allonge.
4. Un résultat négatif se consigne comme un résultat positif.
5. `python3 verifier.py` doit passer avant chaque commit.

## Réutiliser

Tout le dépôt est réutilisable, y compris à des fins commerciales, à condition de citer la source.

| Contenu | Licence |
| --- | --- |
| Code (`*.py`) | MIT, voir `LICENSE` |
| Registre, documents, résultats, figure | CC BY 4.0, voir `LICENSES/CC-BY-4.0.txt` |

Citation suggérée : « longClauvid, <https://github.com/phracktale/longClauvid>, consulté le [date] ».

Les articles cités dans `registre/sources.yaml` restent la propriété de leurs auteurs :
le registre n'en reprend que les références et un résumé.
