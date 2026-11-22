# Piste P15 : résultat du test sur les données de 2019

Analyse du 2026-11-22, faite après le dépôt du [plan](PLAN.md). Les seuils et la règle sont ceux du plan ;
rien n'a été ajusté. Pour refaire : `python3 analyses/P15/arn_ribosomique.py telecharger`, puis la même commande
sans argument.

**Lecture fixée d'avance : indécidable. L'écart publié n'existe que dans une des deux séries de bibliothèques.**

**Ce que les données montrent, hors règle : l'écart vient de cinq bibliothèques de témoins sains,
qui contiennent de 30 à 400 fois plus de lectures d'ARN ribosomique que la bibliothèque médiane.
Dans l'autre série, les patients ne diffèrent pas des témoins sains sur ces mesures.**

> Ce résultat ne produit aucun avis médical. Il porte sur un jeu de données, pas sur l'humanine ni sur MOTS-c.

## 1. Ce que rend la règle du plan

| Comparaison | Contrôle négatif | Écart de A | Série 1 | Série 2 | Étape qui décide | Lecture |
| --- | --- | --- | --- | --- | --- | --- |
| EM/SFC contre témoins sains | Passé (−0,05 log2) | −3,08 log2 (de −5,80 à −0,36) | −6,80 | +0,64 | 3 : le signe change d'une série à l'autre | Indécidable |
| Fatigue après fièvre Q contre témoins sains | Passé (−0,09 log2) | −2,59 log2 (de −5,34 à +0,16) | −5,47 | +0,29 | 3 : le signe change d'une série à l'autre | Indécidable |

A est le signal publié : les deux ARN ribosomiques de la mitochondrie, MT-RNR1 et MT-RNR2.
Entre parenthèses, l'intervalle de confiance à 95 %. Lecture d'ensemble : **indécidable**.

L'écart est bien là sur les 40 bibliothèques : l'étape 2 est passée. Mais il vient tout entier de la première série.
C'est le cas que l'étape 3 devait arrêter.

Les conditions de l'étape 4, celle de l'artefact, sont remplies elles aussi. L'étape 3 passe avant :
la lecture reste « indécidable ».

## 2. Les mesures

Écart entre le groupe et les témoins sains, en log2. Un écart négatif veut dire : plus bas que chez les témoins sains.

| Mesure | EM/SFC | Fatigue après fièvre Q | Témoins infectés, hors règle |
| --- | --- | --- | --- |
| A, ARN ribosomiques de la mitochondrie | −3,08 | −2,59 | −2,03 |
| B, ARN 18S et 28S du cytoplasme | −5,04 | −3,48 | −4,15 |
| D, gènes codants de la mitochondrie | −0,31 | −0,23 | +0,32 |
| E, ARN 5S et 5,8S | −3,41 | −1,75 | −3,20 |
| A corrigé de B | −0,17 | −0,57 | |

À groupe égal, A suit B d'une bibliothèque à l'autre : corrélation de rang de 0,89, pente de 0,58.

Moyenne de A et de B dans chaque série, en log2 du rapport aux gènes codants du noyau :

| Série | Mesure | Témoins sains | EM/SFC | Fatigue après fièvre Q | Témoins infectés |
| --- | --- | --- | --- | --- | --- |
| 1 | A | −5,78 | −12,58 | −11,25 | −11,04 |
| 1 | B | −3,50 | −13,44 | −10,54 | −12,05 |
| 2 | A | −12,43 | −11,79 | −12,14 | −11,23 |
| 2 | B | −12,65 | −12,79 | −12,58 | −12,40 |

Sept cases sur huit se tiennent entre −10,5 et −13,4. La huitième, les témoins sains de la série 1,
est à part pour A comme pour B.

Les mesures de chaque bibliothèque sont dans [mesures.csv](mesures.csv).

## 3. Description faite après coup

Cette partie n'était pas dans le plan. Elle ne change pas la lecture. `python3 analyses/P15/description.py`.

Part des lectures alignées qui tombent sur les quatre gènes d'ARN ribosomique, mitochondrie et cytoplasme réunis :

| Série | Témoins sains | EM/SFC | Fatigue après fièvre Q | Témoins infectés |
| --- | --- | --- | --- | --- |
| 1 | De 0,55 à 7,62 % | De 0,00 à 0,02 % | De 0,01 à 0,28 % | De 0,01 à 1,16 % |
| 2 | De 0,01 à 0,02 % | De 0,01 à 0,03 % | De 0,01 à 0,03 % | De 0,02 à 0,05 % |

La médiane des 40 bibliothèques est de 0,02 %. Les cinq témoins sains de la série 1 sont tous au-dessus de 0,5 %.
Trois autres bibliothèques de cette série dépassent 0,1 % : deux patients de la fièvre Q et un témoin infecté.
Toutes les bibliothèques de la série 2 restent sous 0,1 %.

## 4. Ce que j'en tire, hors règle

Trois faits, lus après coup :

- L'écart publié oppose cinq bibliothèques de témoins sains à toutes les autres, pas des patients à des témoins.
  Les témoins infectés sans fatigue sont du côté des patients.
- Dans ces cinq bibliothèques, l'ARN ribosomique du cytoplasme monte autant que celui de la mitochondrie.
  Une baisse propre aux mitochondries des patients ne ferait pas cela.
- Dans la série 2, sur cinq personnes par groupe, l'écart de A est de +0,6 et de +0,3 log2 : aucun écart.

Tout se passe comme si le retrait de l'ARN ribosomique avait échoué, ou n'avait pas été fait,
dans cinq bibliothèques de témoins sains. C'est une interprétation : les fiches ne disent rien de tel,
et seuls les auteurs peuvent le confirmer. Une lettre leur est destinée : voir [DEMANDES.md](DEMANDES.md).

## 5. Conséquence pour le registre

Celle que le plan prévoit pour « indécidable » : une ligne dans la fiche P15, et rien d'autre ne change.
La piste reste au niveau C.

Une décision reste à prendre, et elle revient au porteur du projet : continuer ou non à citer
le résultat d'expression de 2019 comme un appui de la piste. La règle ne permet pas de le retirer.
La description de la section 3 va contre lui.

## 6. Écarts au plan

Aucun dans les mesures ni dans la règle. Les fichiers avaient le format attendu.

## 7. Limites

- La lecture « hors règle » a été faite après avoir vu les données. Elle vaut moins qu'un test écrit d'avance.
- La cause du contraste entre les deux séries n'est pas connue : les fiches ne décrivent qu'un protocole.
- L'article de 2019 n'a pas été réanalysé : son calcul d'expression différentielle n'est pas refait ici.
- Ce jeu de données ne dit rien des peptides eux-mêmes, ni des vésicules extracellulaires du COVID long,
  l'autre appui de la piste.
- La réplication sur d'autres personnes, prévue en section 6 du plan, n'est pas faite.
