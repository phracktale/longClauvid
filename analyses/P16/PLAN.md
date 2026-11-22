# Piste P16 : le COVID long et l'EM/SFC partagent-ils un allèle HLA ?

Plan d'analyse déposé le 2026-11-22. La date du commit fait foi. Toute modification ultérieure
s'écrit en bas de ce fichier, avec sa date et son motif. Avant ce dépôt, le plan a été relu par un relecteur
qui n'en est pas l'auteur, puis corrigé : la consigne est dans `outils/consigne-relecteur-de-plan.md`,
le compte rendu dans `JOURNAL.md`.

**Quatre comparaisons, fixées avant toute donnée. Une seule se fait sur un fichier public.
Les trois autres demandent un chiffre aux équipes : les lettres sont prêtes, non envoyées.**

> Ce plan ne produit aucun avis médical. Un allèle HLA associé à une maladie ne trie pas des patients
> et ne désigne pas un médicament.

> Des résultats publiés ont été lus avant l'écriture de ce plan. Ils sont rapportés en section 2
> comme des constats, pas comme des tests. La règle de la section 5 ne vaut que pour les quatre chiffres
> qui n'ont pas encore été vus.

## 1. La question

Deux études pangénomiques trouvent la région HLA : celle de 23andMe pour le COVID long, DecodeME pour l'EM/SFC.
Elles ne désignent pas les mêmes allèles, et personne ne les a croisées. Un terrain commun prédit
qu'un allèle désigné par l'une se retrouve dans l'autre, dans le même sens.

## 2. Ce qui a été lu avant ce plan

| Étude | Constat |
| --- | --- |
| 23andMe, COVID long, 54 390 cas déclarés et 124 777 témoins, trois ascendances réunies | Variant rs9273363, entre HLA-DQA1 et HLA-DQB1 : rapport de cotes 1,06 (1,04–1,08) pour l'allèle C. DRB1*11:04 : 1,18. DQA1*03:01 : 0,95. C*07:01 : 0,94. B*08:01 : 0,93. 855 allèles HLA disponibles pour l'analyse |
| DecodeME, EM/SFC, 15 579 cas et 259 909 témoins de la UK Biobank, ascendance européenne | DQA1*05:01 moins fréquent chez les malades, 21,7 % contre 23,2 %. DRB1*03:01 (p = 0,27) et DQB1*02:01 (p = 0,042) ne sont pas associés, alors qu'ils lui sont liés. Seuls les allèles de fréquence supérieure à 1 % sont testés |
| Deux études norvégiennes, 426 patients EM/SFC | HLA-C*07:04 et HLA-DQB1*03:03 plus fréquents chez les malades ; signal de classe II dans la région HLA-DQB1 |
| Revue de 2002 sur l'haplotype ancestral 8.1, lue en résumé | Il porte HLA-A1, Cw7, B8, DRB1*0301, DQA1*0501 et DQB1*0201. C'est le plus commun en Europe du Nord |

Un rapprochement, fait à la lecture : B8, Cw7, DRB1*03:01, DQA1*05:01 et DQB1*02:01 appartiennent
au même haplotype, dit 8.1. B*08:01 et C*07:01 sont moins fréquents dans le COVID long, DQA1*05:01 dans l'EM/SFC.
C'est le sens que prédit un terrain commun. Deux réserves : la revue nomme B8 et Cw7 sans donner l'allèle précis ;
et deux autres allèles du même haplotype ne suivent pas dans DecodeME, dont les auteurs prévoient de refaire
l'analyse, parce que le typage y a été imputé séparément chez les cas et chez les témoins.

Ce rapprochement est un constat, pas un test. Il rend le quatrième test moins neuf qu'il n'y paraît.

Sources : [23andMe](https://www.medrxiv.org/content/10.1101/2024.10.07.24315052v1.full),
[DecodeME](https://www.medrxiv.org/content/10.1101/2025.08.06.25333109v1.full-text),
[Norvège, 2020](https://pubmed.ncbi.nlm.nih.gov/32210306/),
[Norvège, 2021](https://pubmed.ncbi.nlm.nih.gov/34403736/),
[haplotype 8.1](https://pubmed.ncbi.nlm.nih.gov/12849055/),
[notice des fichiers publics de DecodeME](https://osf.io/rgqs3/files/osfstorage).

## 3. Les quatre tests

Ce sont ceux de la fiche B013 de la banque, écrits avant toute donnée.

| Test | On cherche | Dans | Sens attendu | Où est le chiffre |
| --- | --- | --- | --- | --- |
| 1 | rs9273363, allèle C | DecodeME | Rapport de cotes au-dessus de 1 | Fichier public de statistiques résumées |
| 2 | DRB1*11:04 | DecodeME | Au-dessus de 1 | À demander à l'équipe |
| 3 | DQA1*03:01 | DecodeME | Au-dessous de 1 | À demander à l'équipe |
| 4 | DQA1*05:01 | 23andMe | Au-dessous de 1 | À demander aux auteurs |

Partout : un rapport de cotes par copie de l'allèle, et une valeur de p bilatérale, telle que le fichier
ou l'équipe la donne.

Le test 1 se lit ainsi, d'après la notice du fichier :

- Fichier : `gwas_1.regenie.gz`, l'analyse principale de DecodeME, sous licence CC BY 4.0.
- Le variant se repère par sa position : chromosome 6, position 32 658 495 du génome GRCh38, allèles A et C.
- Il doit figurer dans la liste des variants contrôlés par les auteurs, `gwas_qced.var.gz`.
- L'effet du fichier est celui de l'allèle de la colonne `ALLELE1`. Si cet allèle est A, on change le signe
  de l'effet pour le ramener à C.
- Si le variant manque au fichier ou à la liste, le test 1 est « non lu ». Aucun variant de remplacement n'est prévu.

Les tests 2 et 3 ne se lisent que sur une analyse où le typage HLA est imputé pour les cas et les témoins ensemble.
Un chiffre tiré de l'analyse actuelle de DecodeME est rapporté comme un constat « à confirmer » :
le test reste « non lu ».

Un test sans chiffre est « non lu » : pas de réponse, ou allèle absent de l'analyse.

Le fichier public de DecodeME donne les variants un par un, pas les allèles HLA : seul le test 1 s'y lit.
Les statistiques de 23andMe ne sont ouvertes qu'à des chercheurs agréés, sous contrat.

## 4. La puissance, calculée avant les données

`python3 analyses/P16/puissance.py`. Seuil : p inférieur à 0,05 / 4. L'effet à retrouver est celui
de l'étude d'origine, pris tel quel.

| Test | Puissance | Hypothèse sur la fréquence de l'allèle le moins fréquent |
| --- | --- | --- |
| 1 | 93 à 99 % | De 20 à 40 % |
| 2 | 63 à 100 % | De 1 à 5 % |
| 3 | 56 à 85 % | De 10 à 20 % |
| 4 | 100 % | 23,2 %, donnée par DecodeME |

Les tests 1 à 3 dépendent d'une fréquence que les articles ne donnent pas. La puissance d'un test lu
se recalcule avec le même programme : la fréquence de l'allèle et les effectifs sont ceux du fichier
ou de la réponse, l'effet reste celui de l'étude d'origine. Jamais l'effet observé.

## 5. La règle de décision, fixée avant ces données

Chaque test lu reçoit une lecture. On s'arrête à la première ligne dont la condition est remplie.

| Résultat du test | Lecture |
| --- | --- |
| Effet dans le sens attendu, et p inférieur à 0,0125 | Le test passe |
| Effet dans le sens opposé, et p inférieur à 0,0125 | Résultat contraire |
| Puissance recalculée d'au moins 80 % | Le test échoue |
| Puissance recalculée sous 80 % | Non informatif |

Puis la piste se lit sur l'ensemble des tests lus, de la même façon.

| Les tests lus donnent | Lecture pour la piste |
| --- | --- |
| Au moins un test qui passe, aucun résultat contraire | Piste soutenue pour les allèles qui passent |
| Au moins un test qui passe, et au moins un résultat contraire | Résultat partagé : soutenue pour les uns, contredite pour les autres |
| Aucun test qui passe ; au moins un échec ou un résultat contraire | Aucun allèle commun détecté parmi ceux qui ont été lus, pour des effets de la taille publiée |
| Aucun test lu, ou tous non informatifs | Non conclu |

Si le test 4 passe, la fiche le dit avec deux réserves. Son sens attendu vient de l'analyse de DecodeME
que ses auteurs veulent refaire. Et DQA1*05:01 appartient à l'haplotype 8.1, dont 23andMe a déjà vu deux allèles :
le résultat vaudrait pour l'haplotype, pas pour cet allèle seul.

Conséquence pour le registre : une ligne dans la fiche P16, quel que soit le résultat. Le niveau reste C
tant qu'un allèle partagé n'est pas retrouvé par une troisième étude.

## 6. Limites connues d'avance

- Les cas sont déclarés par les participants dans les deux études.
- Les témoins ne sont pas de même nature : personnes infectées sans COVID long d'un côté, population générale de l'autre.
- L'étude de 23andMe réunit trois ascendances, DecodeME une seule. La région HLA varie beaucoup
  selon l'origine géographique : un écart peut venir de la composition des groupes.
- DecodeME ne teste que les allèles de fréquence supérieure à 1 %. DRB1*11:04 peut ne pas y figurer.
- Le rapprochement de la section 2 a été fait avant l'écriture du plan.
- Les effets attendus sont petits. Un premier résultat surestime souvent l'effet : la puissance réelle est plus basse,
  et un échec ne prouve pas l'absence d'un effet plus faible.
- Quatre tests ne couvrent pas la région. Un allèle partagé ailleurs ne serait pas vu.

## Modifications

Aucune à ce jour.
