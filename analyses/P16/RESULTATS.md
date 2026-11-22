# Piste P16 : résultat du test 1

Analyse du 2026-11-22, faite après le dépôt du [plan](PLAN.md). Le seuil et la règle sont ceux du plan ;
rien n'a été ajusté. Pour refaire : `python3 analyses/P16/test_1.py telecharger`, puis la même commande sans argument.

**Le test 1 échoue : le variant le plus associé au COVID long n'est pas associé à l'EM/SFC dans DecodeME.
Les trois autres tests ne sont pas lus : ils attendent un chiffre des équipes.**

> Ce résultat ne produit aucun avis médical. Un variant associé à une maladie ne trie pas des patients.

## 1. Le test 1

| | |
| --- | --- |
| Variant | rs9273363 : chromosome 6, position 32 658 495 du génome GRCh38, allèles C et A |
| Fichier | `gwas_1.regenie.gz`, l'analyse principale de DecodeME ; le variant est dans la liste contrôlée par les auteurs |
| Effet publié pour le COVID long, à retrouver | Rapport de cotes de 1,06 (de 1,04 à 1,08) pour l'allèle C |
| Effet lu pour l'EM/SFC | Rapport de cotes de 0,996 (de 0,970 à 1,023) pour l'allèle C ; p = 0,79 |
| Effectifs | 15 579 cas et 259 909 témoins ; fréquence de l'allèle A : 30 % |
| Puissance pour l'effet publié, au seuil p < 0,0125 | 98 % |
| Lecture | **Le test échoue** |

Le fichier donne l'effet de l'allèle A ; il est ramené ici à l'allèle C, comme le plan le prévoit.
L'intervalle de DecodeME exclut l'effet publié : sa borne haute, 1,023, est sous la borne basse de 23andMe, 1,04.

## 2. Les trois autres tests

| Test | État |
| --- | --- |
| 2, DRB1*11:04 dans DecodeME | Non lu : lettre prête, non envoyée |
| 3, DQA1*03:01 dans DecodeME | Non lu : lettre prête, non envoyée |
| 4, DQA1*05:01 dans 23andMe | Non lu : lettre prête, non envoyée |

## 3. Lecture pour la piste

Celle que le plan prévoit quand aucun test ne passe et qu'au moins un échoue :
**aucun allèle commun détecté parmi ceux qui ont été lus, pour des effets de la taille publiée.**
Un seul test sur quatre est lu.

Conséquence pour le registre : une ligne dans la fiche P16. Le niveau reste C.

## 4. Écarts au plan

Aucun. Le programme a été écrit après le dépôt du plan et avant de lire le chiffre ; il applique la lecture
que le plan décrit.

## 5. Limites

- Ce variant n'est pas un allèle HLA : il est situé entre HLA-DQA1 et HLA-DQB1. Les tests 2 à 4 portent sur des allèles.
- Les cas sont déclarés par les participants dans les deux études, et les témoins ne sont pas de même nature.
- L'étude de 23andMe réunit trois ascendances, DecodeME une seule.
- Un échec dit qu'un effet de 1,06 est exclu pour ce variant. Il ne dit rien d'un autre variant de la région.
