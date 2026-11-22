# Piste P15 : résultats, sur les données de 2019 puis sur d'autres personnes

Analyse du 2026-11-22, faite après le dépôt du [plan](PLAN.md). Les seuils et la règle sont ceux du plan ;
rien n'a été ajusté. Pour refaire : `python3 analyses/P15/arn_ribosomique.py telecharger`, puis la même commande
sans argument. Les autres jeux de données sont en section 5.

**Lecture fixée d'avance : indécidable. L'écart publié n'existe que dans une des deux séries de bibliothèques.**

**Ce que les données montrent, hors règle : l'écart vient de cinq bibliothèques de témoins sains,
qui contiennent de 30 à 400 fois plus de lectures d'ARN ribosomique que la bibliothèque médiane.
Dans l'autre série, les patients ne diffèrent pas des témoins sains sur ces mesures.**

**Chez d'autres personnes : signal non retrouvé. Dans trois autres jeux de données publics,
41 patients et 47 témoins, l'écart est de +0,01, de −0,19 et de +0,35 log2.**

> Ce résultat ne produit aucun avis médical. Il porte sur des données d'expression de deux gènes,
> pas sur l'humanine ni sur MOTS-c eux-mêmes.

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

## 5. Chez d'autres personnes

C'est la section 6 du plan : le même signal, cherché dans d'autres jeux de données publics.
`python3 analyses/P15/autres_jeux.py telecharger`, puis la même commande sans argument.

Sur les sept jeux retenus par le plan, trois se lisent :

| Jeu | Maladie, cellules | Patients / témoins | Écart de A | Écart de D | Contrôle négatif | Lecture |
| --- | --- | --- | --- | --- | --- | --- |
| [GSE251872](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251872) | EM/SFC après une infection, cellules mononucléées | 12 / 15 | +0,01 log2 (de −0,29 à +0,30) | 0,00 | Passé (+0,01) | Non reproduit |
| [GSE251849](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251849) | COVID long, cellules mononucléées | 11 / 12 | −0,19 log2 (de −0,84 à +0,46) | −0,04 | Passé (0,00) | Non reproduit |
| [GSE226260](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE226260) | COVID long, sang total, ARN polyadénylés | 18 / 20 | +0,35 log2 (de −0,05 à +0,74) | +0,03 | Passé (−0,09) | Non reproduit |

Lecture d'ensemble, fixée par le plan : **signal non retrouvé chez d'autres personnes.**
Sur 41 patients et 47 témoins, aucun écart n'approche les −2 log2 du seuil, ni les −4 à −5 log2 publiés.
La borne basse des trois intervalles reste au-dessus de −1 log2.

Les quatre autres jeux ne se lisent pas :

| Jeu | Raison |
| --- | --- |
| GSE270045 | Critère 4 : MT-RNR1 et MT-RNR2 ne sont pas dans le fichier déposé |
| GSE128078 | Critère 4 : le fichier déposé ne contient aucun gène de la mitochondrie |
| GSE227375, GSE224615 | Pas d'estimation déposée : il faudrait réaligner les lectures brutes |

L'indicateur technique B ne se calcule dans aucun des trois jeux lus : aucun gène n'y porte le nom
des ARN 18S, 28S ou 45S. Le plan l'avait prévu. La lecture « non reproduit » ne dépend pas de B.

## 6. Conséquence pour le registre

Celles que le plan prévoit : une ligne dans la fiche P15 pour la lecture « indécidable » du jeu de 2019,
une autre pour le signal non retrouvé chez d'autres personnes. La piste reste au niveau C.

Une décision reste à prendre, et elle revient au porteur du projet : continuer ou non à citer
le résultat d'expression de 2019 comme un appui de la piste. La règle ne permet pas de le retirer.
La description de la section 3 et les trois autres jeux de données vont contre lui.

## 7. Écarts au plan

- Aucun dans les mesures ni dans la règle. Les fichiers de 2019 avaient le format attendu.
- La description de la section 3 a été ajoutée après coup. Elle est donnée comme telle.
- Pour servir aux autres jeux, trois fonctions du programme déposé ont reçu un paramètre de plus,
  et une lecture de la série a été corrigée. Les sorties sur les données de 2019 sont identiques avant et après.
- GSE226260 : le prélèvement le plus ancien d'une personne est choisi par le temps de prélèvement de la fiche,
  puis par le nombre de jours écrit dans le titre de l'échantillon, puis par le numéro d'échantillon.
- GSE251849 : la fiche ne dit pas comment les ARN ont été sélectionnés. Le jeu est lu par la règle complète.

## 8. Limites

- La lecture « hors règle » de la section 4 a été faite après avoir vu les données. Elle vaut moins qu'un test écrit d'avance.
- La cause du contraste entre les deux séries n'est pas connue : les fiches ne décrivent qu'un protocole.
- L'article de 2019 n'a pas été réanalysé : son calcul d'expression différentielle n'est pas refait ici.
- Les trois autres jeux ne portent pas sur des monocytes isolés, ni sur la fatigue après fièvre Q.
  Une baisse propre aux monocytes pourrait y être diluée.
- Dans ces trois jeux, un écart plus petit que 1 log2 n'est pas exclu.
- Ce travail ne dit rien des peptides eux-mêmes, ni des vésicules extracellulaires du COVID long,
  l'autre appui de la piste.
