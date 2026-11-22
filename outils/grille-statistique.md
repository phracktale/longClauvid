# Grille de relecture statistique d'une piste

Dix questions, à poser dans l'ordre. Pour chacune : ce qu'il faut regarder dans la source, et ce qui doit faire douter.
Aucune piste n'est un avis médical. Une association n'est pas une cause.

| # | Question | Ce qu'il faut regarder | Ce qui doit faire douter |
| --- | --- | --- | --- |
| 1 | D'où vient le chiffre ? | La source a été ouverte. Elle donne un effectif, une taille d'effet et un intervalle de confiance. | Un communiqué ou un résumé seul. Un pourcentage sans intervalle. Un chiffre cité de mémoire. |
| 2 | Combien de personnes portent le signal ? | Le plus petit groupe de la comparaison : nombre d'exposés, nombre de malades parmi eux. | Moins de 30 personnes ou moins de 20 événements dans ce groupe, même si la cohorte est immense. |
| 3 | Le signal a-t-il été retrouvé ailleurs ? | Une seconde cohorte, par une autre équipe, avec un effet de même sens. | La même équipe ou les mêmes données deux fois. Un effet de sens opposé ailleurs. Un échec de réplication dans une étude assez puissante. |
| 4 | Combien de choses ont été testées ? | Le nombre de comparaisons, la correction appliquée, un plan déposé avant les données. | Une analyse de sous-groupe faite après coup. Un p proche de 0,05 parmi des dizaines de tests. Aucun décompte des tests. |
| 5 | La taille de l'effet est-elle croyable ? | L'effet brut et l'effet ajusté. L'effet dans chaque base. | Un risque divisé par plus de deux par un produit courant. Un effet qui change de sens après ajustement. Deux bases qui donnent 1,1 et 1,8. |
| 6 | La cause peut-elle être l'effet ? | La date de la mesure par rapport au début de la maladie. | Un prélèvement fait une fois la maladie déclarée. Une maladie qui change l'alimentation, l'activité ou les traitements. |
| 7 | Les groupes se ressemblaient-ils au départ ? | Les facteurs d'ajustement. La raison de la prescription. La valeur E. | Des exposés plus suivis, plus riches ou en meilleure santé. Pas d'ajustement sur le poids ou la gravité. Une valeur E sous 1,5. |
| 8 | Le temps est-il bien compté ? | Le jour où le suivi commence, et le jour où l'exposition est connue. | « A reçu le médicament à un moment du suivi » : il fallait survivre sans maladie jusque-là. Aucune mention du temps immortel. |
| 9 | La maladie est-elle bien mesurée ? | La définition du cas : critères, code de diagnostic, auto-déclaration. La fréquence obtenue. | Un code fourre-tout comme « malaise et fatigue ». Une fréquence dix fois plus haute qu'attendu. Une mesure auto-déclarée des deux côtés. |
| 10 | Qu'est-ce qui la réfuterait, et est-elle vraiment inexplorée ? | Un test écrit avant les données, avec un seuil et un jeu de données nommé. Les recherches faites dans les registres d'essais. Les risques du candidat. | Aucun seuil. « Non trouvé » écrit comme « inexistant ». Un essai déjà enregistré. Un danger non examiné. |

## Lire le résultat

- Chaque case « doute » cochée se note en une phrase dans le champ `risques` de la piste.
- Un doute aux questions 5, 8 ou 9 suffit à classer le signal comme probablement artefactuel tant qu'une contre-analyse n'est pas faite.
- Niveau du protocole : A s'il est retrouvé par des équipes indépendantes (question 3), B pour une étude solide ou deux cohortes, C pour une seule équipe ou une étude non contrôlée, D sans donnée.
- Tout calcul de puissance ou d'effectif se fait en code, avec ses hypothèses écrites.

Exemples tirés de la banque : effet invraisemblable (question 5), antibiotiques à Taïwan ; échec de réplication malgré la puissance (question 3), FOXP4 ; causalité inverse (question 6), biomarqueurs d'UK Biobank.
