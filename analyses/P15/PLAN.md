# Piste P15 : la baisse d'expression de 2019 est-elle un artefact de préparation ?

Plan d'analyse déposé le 2026-11-22. La date du commit fait foi. Toute modification ultérieure
s'écrit en bas de ce fichier, avec sa date et son motif. Avant ce dépôt, le plan a été relu par un relecteur
qui n'en est pas l'auteur, puis corrigé : la consigne est dans `outils/consigne-relecteur-de-plan.md`,
le compte rendu dans `JOURNAL.md`.

**Le premier test de la piste ne demande aucun laboratoire : les données d'expression de l'étude de 2019
sont publiques. Elles n'ont pas été ouvertes. Avant de les ouvrir, ce plan fixe ce qu'on y mesurera
et comment on le lira.**

> Ce plan ne produit aucun avis médical. Il dit quelles données lire, et comment les lire.

> Des résultats publiés et des métadonnées ont été lus avant l'écriture de ce plan. Ils sont rapportés
> en section 2 comme des constats, pas comme des tests. La règle de la section 5 ne vaut que pour
> les données d'expression, qui n'ont pas encore été vues.

## 1. La question

L'étude de 2019 trouve l'expression de deux gènes très abaissée dans les monocytes des patients :
MT-RNR2, qui contient l'humanine, et MT-RNR1, qui contient MOTS-c. Deux lectures s'opposent.

| Lecture | Ce qu'elle dit | Ce qu'elle prédit dans les données |
| --- | --- | --- |
| Biologique | Les mitochondries des patients transcrivent moins ces deux gènes | L'écart est propre aux gènes mitochondriaux |
| Technique | Le retrait de l'ARN ribosomique a été plus efficace dans les bibliothèques des patients | L'écart touche aussi les ARN ribosomiques du reste de la cellule, et les suit d'une bibliothèque à l'autre |

MT-RNR1 et MT-RNR2 sont les gènes des deux ARN ribosomiques de la mitochondrie, 12S et 16S.
Les deux peptides sont de petits cadres de lecture à l'intérieur de ces gènes : dans des données d'expression,
on ne peut pas séparer le peptide de l'ARN ribosomique qui le porte.

## 2. Ce qui a été lu avant ce plan

| Constat | Source |
| --- | --- |
| Écarts publiés entre patients et témoins sains : de 4,4 à 5,2 log2 pour les deux gènes, soit de 21 à 37 fois, sur 10 personnes par groupe | Article de 2019 |
| Le troisième gène le plus abaissé chez les patients est AC010970.2, à 3,8 log2. C'est un pseudogène de l'ARN ribosomique 18S, celui du cytoplasme | Article de 2019 ; base Ensembl |
| Les bibliothèques ont été préparées sur de l'ARN total, avec un retrait de l'ARN ribosomique | Fiche des échantillons, base GEO |
| Les peptides eux-mêmes ne diffèrent pas dans le sang ; l'humanine ne baisse que dans des cellules stimulées en culture | Article de 2019 |
| 40 bibliothèques : 10 témoins sains, 10 patients EM/SFC, 10 patients atteints de fatigue après fièvre Q, 10 témoins infectés sans fatigue | Fiche des échantillons, base GEO |
| Les numéros de bibliothèque forment deux séries de vingt. Chaque série compte cinq bibliothèques par groupe : la série n'est pas confondue avec le groupe | Noms des fichiers, base GEO |
| Dans chaque série, les numéros se suivent groupe par groupe : patients de la fièvre Q, patients EM/SFC, témoins infectés, témoins sains | Noms des fichiers, base GEO |
| Les fichiers déposés viennent du programme MMSEQ. Les lectures ont été alignées sur l'annotation Ensembl 68 du génome humain | Fiche des échantillons, base GEO |

Les trois gènes les plus abaissés sont donc tous des ARN ribosomiques ou leur pseudogène,
dans des bibliothèques dont on a retiré l'ARN ribosomique. Ce constat oriente vers la lecture technique.
Il ne la prouve pas : c'est pour cela que le test est écrit.

Sources : [article de 2019](https://pubmed.ncbi.nlm.nih.gov/31088495/),
[série GSE130353](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130353),
[AC010970.2 dans Ensembl](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225840),
[MT-RNR1](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211459),
[MT-RNR2](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000210082),
[format des fichiers MMSEQ](https://github.com/eturro/mmseq#step-4-obtain-expression-estimates).

## 3. Les données

| Jeu | Contenu | Accès |
| --- | --- | --- |
| GSE130353 | Une estimation d'expression par gène et par bibliothèque, 40 fichiers | Public, sans compte |
| [Annotation Ensembl 68](https://ftp.ensembl.org/pub/release-68/gtf/homo_sapiens/), génome humain GRCh37 | Le type et le chromosome de chaque gène | Publique |

L'annotation a été lue avant ce plan, pour fixer les listes de gènes. Elle ne contient aucune mesure.

## 4. Ce qui sera mesuré, par bibliothèque

Tout se calcule sur les estimations déposées, sans les recalculer depuis les lectures brutes.

Unité : pour chaque gène, l'estimation d'expression du fichier (colonne `log_mu`, un logarithme népérien),
ramenée à l'échelle linéaire. Un gène que le fichier marque comme non observé compte pour zéro.

| Ensemble de gènes | Définition dans Ensembl 68 | Gènes |
| --- | --- | --- |
| Gènes codants du noyau | Type `protein_coding`, hors chromosome MT | 22 045 |
| Gènes codants de la mitochondrie | Type `protein_coding`, chromosome MT | 13 |
| ARN ribosomiques de la mitochondrie | MT-RNR1 (ENSG00000211459) et MT-RNR2 (ENSG00000210082) | 2 |
| ARN ribosomiques 18S et 28S du cytoplasme | Les deux pseudogènes qui portent leur nom : RN18S1 (ENSG00000225840, appelé ensuite AC010970.2) et RN28S1 (ENSG00000226958) | 2 |
| ARN ribosomiques 5S et 5,8S | Type `rRNA` | 558 |

Dans l'annotation de 2012, aucun autre gène ne porte le nom des ARN 18S et 28S :
c'est sur ces deux pseudogènes que leurs lectures sont attendues.

| Mesure | Définition |
| --- | --- |
| N | Somme des gènes codants du noyau |
| A, le signal publié | log2 de (MT-RNR1 + MT-RNR2) / N |
| B, l'indicateur technique | log2 de (RN18S1 + RN28S1) / N |
| D, les autres transcrits de la mitochondrie | log2 de (somme des 13 gènes codants de la mitochondrie) / N |
| E, décrit sans entrer dans la règle | log2 de (somme des ARN 5S et 5,8S) / N |

Si une somme vaut zéro dans une bibliothèque, on la remplace par la moitié de la plus petite valeur non nulle
de cette somme dans les 40 bibliothèques. Si RN18S1 et RN28S1 valent zéro partout, B ne se calcule pas :
la lecture est « indécidable ». Si MT-RNR1 et MT-RNR2 manquent, rien ne se lit.

Deux comparaisons, chacune de 10 contre 10 : patients EM/SFC contre témoins sains, patients atteints de fatigue
après fièvre Q contre témoins sains. Pour chaque mesure, l'écart est la moyenne des patients moins la moyenne
des témoins. Il est donné avec son intervalle de confiance à 95 % (test de Welch). La règle porte sur l'écart,
pas sur l'intervalle. Un écart négatif veut dire : plus bas chez les patients.

Le lien entre A et B se mesure à groupe égal : on retire à chaque valeur la moyenne de son groupe,
sur les 40 bibliothèques. Deux nombres en sortent, qui servent aux deux comparaisons :

- la corrélation de rang (Spearman) : A suit-il B d'une bibliothèque à l'autre ?
- la pente de A sur B (moindres carrés) : de combien A bouge quand B bouge de 1 log2.

L'écart corrigé est l'écart de A moins la pente multipliée par l'écart de B. C'est ce qui reste de l'écart de A
une fois retiré ce que l'indicateur technique permet de prévoir. Il est donné pour chaque comparaison.

Les témoins infectés sans fatigue sont décrits de la même façon, sans entrer dans la règle.

Contrôle négatif : dix gènes de ménage, fixés ici : ACTB, GAPDH, B2M, PPIA, RPLP0, TBP, HPRT1, PGK1, GUSB, YWHAZ.
Pour chacun, on calcule log2 de (gène / N), puis l'écart entre patients et témoins. La médiane de ces dix écarts
doit être strictement sous 0,5 log2 en valeur absolue. Sinon la normalisation est invalide pour cette comparaison.

## 5. La règle de décision, fixée avant ces données

Elle se lit comparaison par comparaison. On s'arrête à la première étape dont la condition est remplie.

| Étape | Condition | Lecture |
| --- | --- | --- |
| 1 | Le contrôle négatif échoue | Illisible |
| 2 | L'écart de A est au-dessus de −2 log2 | Signal non reproduit sur les données déposées |
| 3 | L'écart de A n'a pas le même signe dans les deux séries de bibliothèques | Indécidable |
| 4 | Écart de B de −2 log2 ou plus bas, et corrélation d'au moins 0,5 | Signal probablement artefactuel, tant qu'une contre-analyse n'est pas faite : les bibliothèques des patients ont aussi moins d'ARN ribosomique du cytoplasme, et A suit cet indicateur |
| 5 | Écart de B au-dessus de −1 log2, et écart corrigé de −2 log2 ou plus bas | Signal non expliqué par le retrait de l'ARN ribosomique |
| 6 | Tout autre cas | Indécidable |

À l'étape 3, l'écart se calcule dans chaque série sur cinq patients et cinq témoins. Seul le signe compte ;
un écart nul compte comme un signe différent.

Quand la lecture est « non expliqué », D la précise, sans entrer dans la suite : si l'écart de D est de −1 log2
ou plus bas, tous les transcrits de la mitochondrie baissent ; sinon la baisse est propre à ses ARN ribosomiques.

| Les deux comparaisons donnent | Lecture d'ensemble | Conséquence pour le registre |
| --- | --- | --- |
| « Non reproduit » ou « artefactuel », dans n'importe quelle combinaison | Appui perdu | La piste P15 perd son appui de 2019. Elle ne repose plus que sur les vésicules extracellulaires du COVID long. Une ligne le dit dans la fiche |
| Deux fois « non expliqué » | Appui gardé | La piste garde son appui de 2019, au niveau C. Ce n'est pas une réplication : ce sont les mêmes personnes |
| Tout autre cas | Indécidable | Une ligne le dit dans la fiche, avec les deux lectures. Rien d'autre ne change |

Aucun de ces résultats ne change un niveau de preuve à la hausse.

Le programme `arn_ribosomique.py`, déposé avec ce plan, applique cette règle. Il a été éprouvé sur des données
inventées : `python3 analyses/P15/arn_ribosomique.py essai`.

## 6. Ensuite, sur d'autres jeux de données

Une réplication demande d'autres personnes. Un jeu de données entre dans l'analyse s'il remplit quatre critères,
fixés ici :

1. des cellules du sang humain ;
2. un séquençage d'ARN en vrac, pas cellule par cellule ;
3. au moins 10 patients EM/SFC ou COVID long et 10 témoins. Un témoin est une personne sans la maladie, infectée ou non ;
4. une expression disponible pour MT-RNR1, MT-RNR2 et les 13 gènes codants de la mitochondrie.
   Ce critère se vérifie à l'ouverture du fichier, sur les noms de gènes, avant tout calcul.

Sept jeux remplissent les trois premiers critères, d'après leurs fiches dans la base GEO, lues le 2026-11-22.
Leurs données d'expression n'ont pas été ouvertes.

| Jeu | Maladie, cellules | Patients / témoins | Préparation, d'après la fiche | Estimations déposées |
| --- | --- | --- | --- | --- |
| [GSE128078](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128078) | EM/SFC, sang total | 14 / 11 | Retrait des ARN ribosomiques 12S, 16S, 18S et 28S | Par isoforme |
| [GSE251872](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251872) | EM/SFC après une infection, cellules mononucléées | 12 / 15 | Kit « TruSeq Stranded Total RNA » | Par gène |
| [GSE227375](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE227375) | EM/SFC, cellules mononucléées | 35 / 34 | Kit « TruSeq Stranded Total RNA » | Aucune : lectures brutes seules |
| [GSE270045](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270045) | EM/SFC après COVID, sang total | 19 / 17 | Kit « TruSeq RNA v2 », sélection non précisée | Comptages |
| [GSE226260](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE226260) | COVID long, sang total | 52 / 51 prélèvements | ARN polyadénylés | Comptages |
| [GSE251849](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251849) | COVID long, cellules mononucléées | 11 / 12 | Kit « SMART-Seq v4 », sélection non précisée | Comptages |
| [GSE224615](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE224615) | COVID long, cellules mononucléées | 23 / 13 | ARN polyadénylés | Aucune : liste des gènes différentiels seule |

Règles propres à ces jeux, fixées ici :

- Quand une personne a plusieurs prélèvements, on prend le plus ancien d'après la fiche.
  À défaut de date ou de rang, celui dont le numéro d'échantillon est le plus petit.
- A, D et N se calculent comme en section 4, sur l'annotation du jeu. B se calcule sur tous les gènes
  dont le nom commence par RN18S, RN28S, RN45S, RNA18S, RNA28S ou RNA45S. Si aucun gène ne correspond,
  B ne se calcule pas.
- Chaque jeu donne une comparaison, patients contre témoins, lue par la règle de la section 5, contrôle négatif
  compris. L'étape 3 ne s'y applique pas. La corrélation et la pente se calculent sur les bibliothèques du jeu
  qui entrent dans la comparaison.
- Un jeu préparé par sélection des ARN polyadénylés se lit à part : le retrait de l'ARN ribosomique n'y joue pas.
  Seules les étapes 1 et 2 s'y lisent : passé ces deux étapes, le signal y est dit « présent ».
- Un jeu sans estimation déposée demande de réaligner les lectures brutes. Ce travail n'est pas engagé par ce plan.
- Un jeu est « lu » s'il remplit le critère 4 et passe le contrôle négatif.

On s'arrête à la première ligne dont la condition est remplie.

| Résultat sur l'ensemble des jeux lus | Lecture |
| --- | --- |
| Au moins un jeu donne « non expliqué », ou un signal « présent » pour un jeu d'ARN polyadénylés | Signal retrouvé chez d'autres personnes. Une ligne le dit dans la fiche P15 |
| Au moins deux jeux lus, et tous donnent « non reproduit » ou « artefactuel » | Signal non retrouvé chez d'autres personnes. Une ligne le dit dans la fiche P15 |
| Tout autre cas | Non conclu |

Les autres séries de la requête ne remplissent pas les critères : pas de groupe témoin dans la fiche (GSE267625,
GSE222253), moins de 10 témoins (GSE297499, GSE268212), moins de 20 échantillons (GSE350411),
du muscle (GSE245661), de l'ARN circulant hors des cellules (GSE293840), un séquençage cellule par cellule
(GSE334857, GSE286325), ou une autre question que la comparaison de patients et de témoins.

## 7. Limites connues d'avance

- Les constats de la section 2 ont été lus avant l'écriture du plan, et orientent déjà vers la lecture technique.
- Dix personnes par groupe : seuls de grands écarts sont lisibles. Les seuils de 2 et de 1 log2 sont larges à dessein.
- Le plan teste le signal publié, de 4 à 5 log2. Un écart réel mais plus petit que 2 log2 ne serait pas retenu.
- La fiche des échantillons ne dit pas si le retrait de l'ARN ribosomique visait aussi celui de la mitochondrie.
  Si ce n'était pas le cas, A ne suivrait pas B, et la règle ne conclurait pas à l'artefact.
- B est une mesure bruitée. La pente en est sous-estimée, et la correction avec elle. C'est pourquoi
  la lecture « artefactuel » ne repose pas sur l'écart corrigé, et pourquoi la lecture « non expliqué »
  demande aussi que B lui-même ne baisse pas.
- B ne voit que ce qui touche à la fois les ARN ribosomiques du cytoplasme et ceux de la mitochondrie.
  Un défaut propre au retrait des seconds ne serait pas vu.
- Un ARN dégradé, ou un ordre de préparation confondu avec le groupe à l'intérieur d'une série,
  ne seraient pas vus non plus.
- B repose sur deux pseudogènes courts. RN18S1 est porté par le chromosome Y dans l'annotation ;
  les lectures de l'ARN 18S peuvent s'y aligner quel que soit le sexe, qui n'est pas dans les métadonnées.
  Si elles s'alignent ailleurs, B les manque.
- Les estimations déposées viennent d'un alignement de 2019 sur une annotation de 2012.
  Un écart lié à cet alignement ne serait pas vu.
- Une lecture « technique » dit que ce jeu de données ne montre rien. Elle ne dit pas que l'humanine
  et MOTS-c sont normaux chez les patients.

Requête de la section 6, dans la base GEO : séries humaines de séquençage d'ARN dont le texte contient
« chronic fatigue syndrome », « myalgic encephalomyelitis », « long covid », « post-acute sequelae »
ou « post-covid ». 76 séries ; 56 citent le sang ou des cellules du sang dans leur titre ou leur résumé.
Les fiches d'échantillons de quinze d'entre elles ont été lues.

## Modifications

Aucune à ce jour.
