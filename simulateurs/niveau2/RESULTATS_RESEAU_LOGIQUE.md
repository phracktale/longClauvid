# Niveau 2 bis : réseaux logiques à plusieurs variables

État du 2026-11-22, produit par `python3 reseau_logique.py` (graine 20261122, 10 000 tirages).

**Le moteur est construit et vérifié. Le modèle de Craddock 2015 n'est pas reproduit :
la liste de ses interactions n'existe que dans une figure, que nous n'avons pas pu lire.**

> Les deux réseaux ci-dessous sont des démonstrations sans valeur biologique.
> Ils vérifient le moteur ; ils ne disent rien d'un traitement.

## 1. Le moteur

Un réseau est une liste de nœuds qui s'activent ou se freinent. Chaque nœud vaut
-1 (bas), 0 (normal) ou 1 (haut). À chaque pas, un seul nœud bouge d'un cran,
tiré au sort parmi ceux qui ne sont pas à leur valeur visée. Une intervention
décale d'un cran les nœuds traités. Comme le tirage compte, chaque question
est simulée 10 000 fois.

## 2. Résultats des démonstrations

### Cause et conséquence : l'ordre décide du résultat

Une cause s'entretient seule ; une conséquence est entretenue par la cause et par elle-même.
Départ : les deux sont hautes.

| Traitement | Retour à l'état sain |
| --- | --- |
| Freiner la cause, puis la conséquence | 100 % |
| Freiner la conséquence, puis la cause | 0 % |
| Freiner les deux en même temps | 100 % |

Traitée en premier, la conséquence est rallumée par la cause. Quand la cause est enfin
freinée, la conséquence s'entretient déjà seule : le réseau reste dans un état intermédiaire.
C'est une propriété de ce formalisme, pas un résultat biologique.

### La bascule : le moteur tire bien au sort

Deux nœuds se freinent l'un l'autre. Départ : les deux sont hauts, sans intervention.

| État final (a, b) | Simulé | Calculé à la main |
| --- | --- | --- |
| (0, 0) | 49,6 % | 50 % |
| (-1, 1) | 25,2 % | 25 % |
| (1, -1) | 25,1 % | 25 % |

## 3. Ce qui manque pour reproduire Craddock 2015

| Élément | Où il se trouve dans l'article | État |
| --- | --- | --- |
| Dynamique : un nœud à la fois, un cran, tirage au sort | Texte | Fait |
| Intervention : le nœud traité est décalé d'un cran | Texte, équation 4 à vérifier | Fait |
| Nœuds | Sept nœuds traitables nommés dans le texte : ACTH, CORT, GR, IIR, Th1Cyt, Th2Cyt, TEST. Liste complète dans la figure 2 | Incomplet |
| Interactions (qui active ou freine qui) | Figure 2 seulement | Manquant |
| Règle donnant la valeur visée d'un nœud | Équation 2, en image | Manquant : règle du vote, provisoire |
| États stables publiés, nœud par nœud | Absents du texte | Manquant |

Pages consultées le 2026-11-22 :

- PubMed Central (PMC4508058) : page bloquée par un contrôle anti-robot.
- PLOS ONE : texte lu, sans les équations ni les figures, qui sont des images.
- Europe PMC : requête refusée pour limite de débit.
- Article d'origine du réseau (Craddock et al. 2014, doi:10.1371/journal.pone.0084839) : non lu.

## 4. Les résultats publiés à retrouver

Relevés dans le texte de la page PLOS ONE ; à revérifier sur le PDF avant toute comparaison.

| Traitement simulé dans l'article | Retour à l'état sain |
| --- | --- |
| Une seule cible | Aucun retour robuste |
| Un seul temps, deux cibles : freiner GR et Th1Cyt | environ 37 % |
| Un seul temps, quatre cibles : ACTH, CORT, GR et Th1Cyt | environ 57 % |
| Deux temps : Th1Cyt, puis GR | environ 40 % |
| Deux cycles (quatre temps) | environ 63 % |
| Quatre cycles (huit temps) | jusqu'à 86 % |

Le texte ne donne pas de résultat pour l'ordre inverse, GR puis Th1Cyt.
C'est le premier calcul à faire une fois le réseau chargé.

## 5. Trois façons de débloquer

1. Relever la figure 2 à la main, puis faire revérifier la saisie par une seconde personne.
   Le plus simple : le réseau tient en quelques dizaines de flèches.
2. Demander le fichier du modèle aux auteurs. Le plus fiable, mais le délai est inconnu.
3. Repartir de l'article d'origine de 2014, qui décrit la construction du réseau.
   À faire de toute façon pour relever la règle de mise à jour.

## 6. Conséquence pour le registre

- **H6 (état stable alternatif).** Le formalisme montre qu'un effet d'ordre est possible
  dans un réseau à plusieurs états stables. Il ne dit pas encore lequel, ni pour quelles cibles.
- **Contrôle de reproduction.** Une fois le réseau chargé, le moteur doit retrouver
  les six chiffres du tableau ci-dessus avant d'être utilisé pour une question nouvelle.
