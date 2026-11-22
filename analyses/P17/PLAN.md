# Piste P17 : peut-on refaire le résultat sur le nombre de copies d'ADN mitochondrial ?

Plan d'analyse déposé le 2026-11-22. La date du commit fait foi. Toute modification ultérieure
s'écrit en bas de ce fichier, avec sa date et son motif. Avant ce dépôt, le plan a été relu par un relecteur
qui n'en est pas l'auteur, puis corrigé : la consigne est dans `outils/consigne-relecteur-de-plan.md`,
le compte rendu dans `JOURNAL.md`.

**Pas aujourd'hui. Aucun jeu de cas public et indépendant n'est assez grand : la puissance irait de 5 à 18 %.
Refaire l'analyse dans ces conditions donnerait un résultat nul, qu'on prendrait à tort pour une réfutation.
Ce plan fixe la règle pour le jour où les données existeront, et dit ce qui peut être demandé d'ici là.**

> Ce plan ne produit aucun avis médical. Un effet génétique sur toute la vie ne dit pas
> qu'une intervention changerait quelque chose chez un malade.

> Le résultat à refaire a été lu avant l'écriture de ce plan. Aucune donnée n'a été ouverte.

## 1. La question

Une prépublication de 2026 applique la randomisation mendélienne aux 15 579 cas de DecodeME.
Un nombre de copies d'ADN mitochondrial génétiquement plus élevé y va avec moins d'EM/SFC :
rapport de cotes d'environ 0,83 par écart type. Le résultat tient-il sur d'autres malades ?

## 2. Ce qui a été lu avant ce plan

| Constat | Source |
| --- | --- |
| Rapport de cotes d'environ 0,83, par la méthode de la variance inverse pondérée ; 84 instruments, statistique F moyenne de 85,5 ; hétérogénéité faible (p = 0,31) | Prépublication |
| Neuf expositions testées ; seuil corrigé à p < 0,0056 | Prépublication |
| Ni l'intervalle de confiance, ni la valeur de p, ni le détail des analyses de sensibilité ne sont dans le texte | Prépublication |
| Le dépôt de résultats complets, liste des instruments comprise, est en accès restreint | Fiche du dépôt Zenodo |
| Pas de corrélation génétique globale entre le nombre de copies et l'EM/SFC | Prépublication |
| Les instruments viennent d'une étude de 465 809 personnes, dont celles de la UK Biobank | Tableau 1 de la prépublication ; étude du nombre de copies, lue en résumé |
| Les témoins de DecodeME viennent de la UK Biobank | Prépublication de DecodeME |
| Contenu en ADN mitochondrial normal dans les cellules du sang de 23 patients EM/SFC | Étude de 2013 |

Sources : [prépublication](https://www.researchsquare.com/article/rs-9363637/v2.pdf),
[dépôt Zenodo](https://doi.org/10.5281/zenodo.18198370),
[étude du nombre de copies](https://pubmed.ncbi.nlm.nih.gov/34859289/),
[DecodeME](https://www.medrxiv.org/content/10.1101/2025.08.06.25333109v1.full-text),
[étude de 2013](https://pubmed.ncbi.nlm.nih.gov/23600892/).

## 3. La puissance, calculée avant les données

`python3 analyses/P17/puissance.py`. Les instruments expliquent 1,5 % de la variance du nombre de copies,
d'après leur nombre, leur statistique F et l'effectif de 465 809 personnes. L'effet à retrouver est celui
de la prépublication, pris tel quel.

| Jeu de cas | Cas | Puissance | Remarque |
| --- | --- | --- | --- |
| DecodeME | 15 579 | 79 % | Le jeu d'origine : ce n'est pas une réplication |
| FinnGen, fatigue post-virale | 195 | 5 % | Indépendant, public |
| Pan-UK Biobank, fatigue chronique déclarée | 1 882 | 17 % | Public ; partage la UK Biobank avec les instruments |
| Les deux réunis | 2 077 | 18 % | |
| COVID long, définition large | 6 450 | 45 % | Autre maladie : une extension, pas une réplication |

Il faut environ 16 400 cas, à dix témoins par cas, pour atteindre 80 %. Le résultat d'origine lui-même
n'avait que 79 % de puissance pour son propre effet.

Sources des effectifs : [FinnGen](https://storage.googleapis.com/finngen-public-data-r10/summary_stats/R10_manifest.tsv),
[Pan-UK Biobank](https://pan.ukbb.broadinstitute.org/downloads),
[COVID long](https://pubmed.ncbi.nlm.nih.gov/40399555/).
Méthode : [calcul de puissance pour une issue binaire](https://pubmed.ncbi.nlm.nih.gov/24608958/).

## 4. La règle de décision, fixée avant toute donnée

La puissance est celle que donne le programme du dossier, sans arrondi, pour un rapport de cotes de 0,83
et la variance expliquée qu'il déduit, 1,5 %. Ces deux valeurs ne se changent pas. Les effectifs se relèvent
à nouveau avant chaque décision.

| Situation | Lecture |
| --- | --- |
| Puissance sous 50 % | L'analyse ne se fait pas. Un résultat nul n'y voudrait rien dire |
| Puissance d'au moins 50 %, et sous 80 % | L'analyse se fait comme une exploration, annoncée comme telle. Elle ne change aucune fiche |
| Puissance d'au moins 80 % | L'analyse est un test, si le jeu de cas est indépendant |

Un jeu de cas est indépendant s'il ne contient aucun cas de DecodeME, et si ses cas ne viennent pas
de la UK Biobank, où les instruments ont été en partie trouvés. Sinon l'analyse se lit comme une exploration,
quelle que soit sa puissance.

Quand l'analyse est un test, elle reprend les 84 instruments de la prépublication. L'estimation principale
est la variance inverse pondérée, à effets aléatoires, avec son intervalle de confiance à 95 %.
Elle rend aussi la médiane pondérée et l'ordonnée de la méthode d'Egger.
On s'arrête à la première ligne dont la condition est remplie.

| Résultat du test | Lecture |
| --- | --- |
| L'intervalle de l'ordonnée d'Egger exclut 0 | Non retenu comme réplication : les instruments peuvent agir par une autre voie |
| Intervalle entièrement sous 1, et médiane pondérée sous 1 | Résultat retrouvé. Si l'intervalle ne contient pas 0,83, on écrit : retrouvé, avec un effet plus faible que publié |
| Intervalle entièrement sous 1, et médiane pondérée à 1 ou au-dessus | Non retenu comme réplication : les deux estimations ne concordent pas |
| Intervalle qui contient 1 et 0,83 | Non concluant |
| Tout autre cas : l'intervalle contient 1 sans contenir 0,83, ou il est entièrement au-dessus de 1 | Résultat non retrouvé |

## 5. Ce qui peut se faire d'ici là

| Action | Ce qu'elle apporte | État |
| --- | --- | --- |
| Demander aux auteurs les chiffres absents du texte et la liste des instruments | Intervalle de confiance, valeur de p, analyses de sensibilité, analyse sans chaque instrument à tour de rôle ; de quoi refaire le calcul le jour venu | Lettre prête, non envoyée |
| Attendre une seconde grande étude pangénomique de l'EM/SFC | Le seul vrai test | Aucune repérée |

Refaire l'analyse sur le COVID long ne se fait pas : 45 % de puissance, sous le seuil de la section 4.

La mesure directe est l'autre voie, et elle demande un laboratoire : compter les copies dans des cellules
du sang, à numération égale, chez des patients et des témoins. La seule étude lue n'y voit pas d'écart, sur 23 patients.

Conséquence pour le registre : la fiche P17 dit que son premier test n'est pas faisable aujourd'hui.
La piste a été promue pour ce test. Le porteur du projet décide si elle reste au registre.

## 6. Limites connues d'avance

- La variance expliquée par les instruments est déduite, pas lue : la liste des instruments est dans un dépôt fermé.
- Les instruments et les témoins de DecodeME viennent en partie de la UK Biobank. Ce recouvrement peut biaiser l'estimation d'origine.
- Le nombre de copies mesuré dans le sang dépend de la composition en cellules sanguines, plaquettes comprises.
- Neuf expositions ont été testées dans la prépublication. Elle n'est pas relue par des pairs.
- Un premier résultat surestime souvent l'effet : la puissance réelle est plus basse que celle du tableau.
- L'ordonnée d'Egger exclut 0 une fois sur vingt par hasard : la première ligne de la règle peut écarter un bon résultat.

## Modifications

Aucune à ce jour.
