# Niveau 2 bis : le réseau de Craddock et l'ordre des traitements

Résultats du 2026-11-22, produits par `python3 craddock_2015.py`
(graine 20261122, 10 000 tirages par traitement, environ une minute).

**Le réseau de Craddock est reproduit : ses cinq états stables publiés sont retrouvés,
et eux seuls. Dans ce modèle, l'ordre décide : freiner les cytokines Th1 puis le récepteur
du cortisol ramène à l'état sain une fois sur quatre ; l'ordre inverse, jamais.
Les taux publiés, eux, ne sont retrouvés qu'en partie.**

> Ce modèle a été construit pour la maladie de la guerre du Golfe, chez l'homme.
> Il n'a pas été validé pour le COVID long ni pour l'EM/SFC.
> Les « traitements » sont des décalages de nœuds dans un modèle, pas des médicaments.

## 1. Le modèle

Quatorze nœuds, chacun bas, normal ou haut, relient trois systèmes : l'axe du stress
(CRH, ACTH, cortisol, son récepteur GR et le récepteur activé GRD), l'axe sexuel
(GnRH, LH/FSH, testostérone) et une immunité simplifiée (cellules et cytokines innées,
Th1 et Th2). Trente-neuf flèches disent qui active ou freine qui.

| Élément | Source | Comment il a été obtenu |
| --- | --- | --- |
| Les 39 flèches | Figure 2 de Craddock 2015 | Relevé à la main sur la figure agrandie |
| La règle de calcul | Équation 2 et tables 1 à 3 de Craddock 2014 | Lue dans le PDF |
| Le tirage au sort, un nœud à la fois | Texte de Craddock 2015 | Lu dans le PDF |
| Les états stables publiés | Figure 2 de Craddock 2014 | Lue dans le PDF |

## 2. Ce qui est reproduit

### Les cinq états stables, exactement

Les 4 782 969 états possibles ont tous été essayés. Cinq sont stables, les cinq publiés.

| État | Ce qui s'écarte de la normale |
| --- | --- |
| SS0, l'état sain | Rien |
| SS1 | Récepteur du cortisol haut (GR, GRD), ACTH basse |
| SS2 | Immunité basculée vers Th2 |
| SS3 | SS1 et SS2 à la fois |
| SS4, l'état malade | Cortisol et son récepteur hauts, immunité Th1 haute, Th2 basse, testostérone basse |

C'est aussi le contrôle du relevé : une flèche mal lue aurait presque sûrement changé ces états.

### Une anomalie entre les deux articles

La figure du réseau n'est pas la même en 2014 et en 2015, alors que l'article de 2015
la présente comme une reproduction. Deux entrées du nœud T1Cell diffèrent : en 2014,
le cortisol le freine et les cytokines Th1 ne l'activent pas. Avec la figure de 2014,
on ne trouve que quatre états stables : l'état malade disparaît. Seule la figure de 2015
est compatible avec les résultats publiés en 2014. Elle est retenue ici.

### Les conclusions qualitatives de l'article

| Affirmation de l'article | Ici |
| --- | --- |
| Aucune cible seule ne ramène à l'état sain | Confirmé : 0 % pour les 14 traitements à une cible |
| Freiner les cytokines Th1 mène à l'état SS1, récepteur haut et ACTH basse | Confirmé, une fois sur deux ; sinon retour à l'état malade |
| Freiner ensuite le récepteur ramène à l'état sain | Confirmé, une fois sur deux à partir de SS1 |
| Répéter le cycle augmente le taux | Confirmé : 25 %, puis 51 % après deux cycles |

## 3. L'effet d'ordre

Départ : l'état malade. Chaque intervention décale sa cible d'un cran, comme l'écrit
l'équation 4 de l'article.

| Traitement | Retour à l'état sain |
| --- | --- |
| Cytokines Th1, puis récepteur du cortisol | 25 % |
| Récepteur du cortisol, puis cytokines Th1 | 0 % |
| Les deux en même temps | 12 % |

L'ordre inverse n'est pas chiffré dans l'article ; ce 0 % est un calcul de ce dépôt.

Pourquoi l'ordre compte, dans ce modèle :

1. Dans l'état malade, les cytokines Th1 tiennent le cortisol haut, et le cortisol
   tient le récepteur haut.
2. Freiner le récepteur en premier ne tient pas : le cortisol, toujours haut,
   le rallume aussitôt.
3. Freiner les cytokines d'abord fait retomber le cortisol une fois sur deux.
   Le récepteur reste alors verrouillé haut par sa propre boucle : c'est l'état SS1.
4. Freiner le récepteur à ce moment-là casse la boucle une fois sur deux.

Les deux en même temps font moins bien que la suite : le freinage du récepteur
doit tenir le temps que le cortisol retombe, ce qui arrive rarement.

## 4. Ce qui n'est pas reproduit : les taux publiés

L'article écrit qu'un traitement décale sa cible d'un cran. Avec cette lecture,
aucun taux publié n'est retrouvé. Si un nœud freiné descend de deux crans,
la figure 5 est retrouvée pour 8 lignes sur 12, à moins de 2 points.

### Figure 5 de l'article : un seul temps, plusieurs cibles

| Cibles (− freiné, + stimulé) | Publié | 1 cran | 2 crans |
| --- | --- | --- | --- |
| GR−, T1Cyt− | 37,06 % | 12,4 % | 37,2 % |
| GR−, T2Cyt+ | 7,99 % | 0,0 % | 7,8 % |
| CORT−, GR−, T1Cyt− | 56,50 % | 24,4 % | 55,2 % |
| ACTH−, GR−, T1Cyt− | 38,08 % | 12,2 % | 37,8 % |
| GR−, T1Cyt−, TEST+ | 38,06 % | 12,2 % | 24,3 % |
| GR−, IIR−, T1Cyt− | 37,56 % | 12,1 % | 37,8 % |
| GR−, T1Cyt−, T2Cyt+ | 37,48 % | 12,6 % | 29,3 % |
| ACTH−, CORT−, GR−, T1Cyt− | 57,32 % | 24,6 % | 55,8 % |
| CORT−, GR−, IIR−, T1Cyt− | 56,97 % | 24,7 % | 56,0 % |
| CORT−, GR−, T1Cyt−, TEST+ | 56,31 % | 25,0 % | 38,1 % |
| CORT−, GR−, T1Cyt−, T2Cyt+ | 56,16 % | 25,2 % | 43,8 % |
| ACTH+, CORT−, GR−, T1Cyt− | 46,63 % | 16,5 % | 47,4 % |

Les quatre lignes mal retrouvées contiennent une hausse de TEST ou de T2Cyt.
Elles le sont à 1 point près si cette hausse ne vaut qu'un cran, mais alors
la deuxième ligne ne l'est plus. Aucune lecture unique ne retrouve les douze lignes.

### Figure 6 de l'article : suites d'interventions

| Suite | Publié | 1 cran | 2 crans |
| --- | --- | --- | --- |
| T1Cyt, GR | 40 % | 25,1 % | 56,3 % |
| T1Cyt, GR, GR | 52 % | 37,5 % | 70,3 % |
| T1Cyt, GR, T1Cyt, GR | 63 % | 50,9 % | 84,5 % |
| T1Cyt, GR, T1Cyt, GR, GR | 73 % | 62,6 % | 91,9 % |

Les taux publiés tombent entre les deux lectures. Deux causes possibles, non départagées :

- La façon exacte dont le code des auteurs applique un traitement n'est pas décrite
  assez précisément pour être refaite à l'identique.
- Ces taux sortent d'un algorithme qui garde le meilleur de milliers d'essais bruités :
  le meilleur score observé surestime le taux réel.

L'effet d'ordre ne dépend pas de la lecture : l'ordre inverse donne 0 % dans les deux cas.

## 4 bis. Ce que l'auteur a répondu, le 2026-11-23

L'auteur correspondant de l'article a répondu à la lettre du 2026-11-22. Sa réponse n'est pas reprise mot pour mot.

| Question | Sa réponse | Ce que cela change ici |
| --- | --- | --- |
| Un cran, ou la valeur extrême ? | Les deux définitions existent : un traitement peut déplacer un nœud d'un cran ou de deux. Il ne dit pas laquelle a servi aux figures de 2015 | L'ambiguïté de la section 4 reste entière : les deux colonnes du tableau sont des lectures permises |
| Maintenu, ou relâché ? | En 2015, tous les traitements sont appliqués à un seul instant, sur l'état malade, puis le réseau évolue librement | C'est ce que fait le simulateur pour la figure 5 |
| Le code ? | Il n'est plus disponible, après plusieurs déménagements du laboratoire | Les taux publiés ne peuvent pas être refaits à l'identique |
| Des taux un peu différents ? | Attendu, parce que le procédé est aléatoire. Des résultats proches sont, pour lui, cohérents ; un écart grossier serait à lui signaler | Voir ci-dessous |
| La figure de 2014 ? | Selon lui, un erratum de l'article de 2014 corrige une arête mal étiquetée | Retrouvé le 2026-11-24 : l'article de 2014 a deux errata. Le second ([PLoS ONE 2014, 9(6), e100355](https://doi.org/10.1371/journal.pone.0100355)) dit que la figure 1 du réseau contenait « un certain nombre d'erreurs » et la remplace. La figure corrigée est une image, qui n'a pas été relue arête par arête |

Deux choses restent à faire, sans l'auteur :

- **Dire si l'écart est « proche » ou « grossier ».** Avec la lecture à deux crans, 8 lignes sur 12 de la figure 5 sont retrouvées
  à 2 points près. Avec la lecture à un cran, aucune : l'écart atteint 33 points. L'aléa d'un tirage sur 10 000 simulations
  ne fait pas un tel écart. La lecture à un cran, qui est celle de l'équation de l'article, n'est donc pas celle des figures.
- **Lire l'article de 2021 que l'auteur indique** : fait le 2026-11-23, voir la section 4 ter.

L'essai de l'étanercept puis de la mifépristone (NCT04254627) n'a pas de publication. L'auteur a donné une indication
de ses résultats, non publics : elle n'est pas reprise ici.

### La lecture mixte, essayée le 2026-11-24

La seconde lettre à l'auteur lui soumet une règle : un frein va à la valeur extrême, une stimulation ne monte que d'un cran.
Elle est maintenant dans le simulateur (`frein_extreme`, quatrième colonne de la sortie de `craddock_2015.py`).

| Lecture | Lignes de la figure 5 retrouvées à 2 points près | Écart maximal |
| --- | --- | --- |
| Un cran partout | 0 sur 12 | 33 points |
| Deux crans partout | 8 sur 12 | 18 points |
| Frein de deux crans, stimulation d'un cran | 11 sur 12 | 8 points |

La ligne qui résiste est « GR−, T2Cyt+ » : 7,99 % publié, 0,0 % avec la lecture mixte, 7,8 % avec deux crans partout.
Elle demande donc une stimulation de deux crans pour T2Cyt, quand deux autres lignes en demandent un seul pour le même nœud.
Aucune règle simple ne rend les douze lignes. La lecture mixte est la meilleure des trois, sans être confirmée par l'auteur.

## 4 ter. Ce que dit l'article de 2021

L'article que l'auteur indique ([PMID 34445252](https://pubmed.ncbi.nlm.nih.gov/34445252/), en accès libre) a été lu
le 2026-11-23, par ses passages de méthode et de résultats sur les traitements, pas en entier. Il porte sur un réseau plus grand,
qui ajoute la barrière entre le sang et le cerveau : ses taux ne se comparent pas à ceux de 2015.

- **La règle d'un traitement y est écrite sans ambiguïté.** Un traitement vaut −1, 0 ou +1 pour chaque nœud. Tant qu'il est appliqué,
  l'état visé au pas suivant est l'état présent plus cette valeur, borné aux valeurs extrêmes. C'est donc un cran par pas de temps.
- **Un traitement y est maintenu**, d'un pas de début à un pas de fin : par exemple du pas 1 au pas 43. Maintenu plusieurs pas,
  un traitement d'un cran par pas amène le nœud à sa valeur extrême. Cela rapproche les deux lectures de la section 4 :
  « deux crans » en une fois ressemble à « un cran » tenu deux pas.
- **Le taux rapporté est celui du meilleur traitement trouvé.** Un algorithme génétique fait évoluer 1 000 traitements candidats
  pendant 1 000 générations, les classe par leur taux de retour à l'état sain sur 1 000 simulations, et garde le meilleur
  de 100 recherches. Un taux choisi parce qu'il est le plus haut surestime le taux réel : c'était la seconde cause possible
  de la section 4, et l'article décrit bien ce procédé. Il ne chiffre pas ce biais.
- **L'ordre des traitements y est retrouvé, avec une étape de plus** : augmenter la testostérone, puis freiner les cytokines Th1,
  puis bloquer le récepteur du cortisol, avec un recouvrement entre les phases. Ce traitement à trois cibles ramène à l'état sain
  dans 37 % des simulations.
- **Limite dite par les auteurs** : le modèle n'a pas de cinétique. Il dit si une suite d'interventions est logiquement possible,
  pas sa dose ni sa durée réelle.

Conséquence pour l'hypothèse H6 : l'effet d'ordre est retrouvé par la même équipe dans un second modèle. Ce n'est pas
une réplication indépendante, et cela reste un argument de plausibilité.

## 5. Suite donnée par les auteurs

La séquence prédite a été portée en clinique : un essai ouvert de phase 1 sur 20 anciens
combattants teste l'étanercept, un anti-TNF, pendant 12 semaines, puis la mifépristone,
un bloqueur du récepteur du cortisol, pendant une semaine
([NCT04254627](https://clinicaltrials.gov/study/NCT04254627)). Aucun résultat publié
chez l'humain n'a été repéré dans cette revue. Une étude chez la souris rapporte
une baisse de la neuro-inflammation avec la combinaison
([PLOS ONE 2026](https://stacks.cdc.gov/view/cdc/258809/cdc_258809_DS1.pdf)).

## 6. Conséquences pour le registre

- **H6 (état stable alternatif).** Un modèle publié, reproduit ici, contient un effet
  d'ordre net. C'est un argument de plausibilité, pas un test : le statut reste « ouverte ».
  La prédiction reste à vérifier chez des patients.
- **Pour un futur essai.** Le modèle désigne un repère plutôt qu'un délai : ne freiner
  le récepteur qu'une fois l'ACTH retombée à un niveau bas et stable.
- **Demandé à l'auteur, qui a répondu le 2026-11-23.** Le code de simulation n'existe plus : voir la section 4 bis.
  L'incertitude de la section 4 ne sera pas levée par le code.

## 7. Limites

- Le réseau a été relevé à la main sur une figure. Le contrôle est indirect : les cinq
  états stables publiés sont retrouvés. Une seconde lecture indépendante reste à faire.
- Le modèle n'a pas de durées : il dit dans quel ordre les nœuds bougent, pas en combien de temps.
- Entre deux interventions, le réseau retrouve ici un état stable. L'article impose
  des délais fixes de 10 à 50 pas.
- Le modèle féminin de l'article de 2014 n'est pas reproduit.
- Les deux réseaux de démonstration de `reseau_logique.py` servent à contrôler le moteur
  sur des cas calculables à la main. Ils n'ont aucune valeur biologique.
