# Lecture des résumés retenus par la carte : trois pistes

Faite le 2026-11-23 pour les trois pistes les plus denses de [CARTE.md](CARTE.md). Quinze lecteurs, des programmes
d'intelligence artificielle d'un modèle moins coûteux, ont lu 477 résumés en suivant `outils/consigne-lecteur.md`,
déposée avant la lecture. Les décomptes viennent de `python3 analyses/cartographie/lots.py controler`.

Un décompte n'est pas une preuve, et un résumé n'est pas un article. Rien ici n'est un avis médical.

## Ce que les termes avaient retenu, et ce qui porte vraiment sur la piste

| Piste | Résumés lus | Objet principal | Mesuré parmi d'autres choses | Cité en passant | Mesures chez des patients ou essais, pertinents |
| --- | --- | --- | --- | --- | --- |
| P01, auto-anticorps | 141 | 68 | 37 | 34 | 77 |
| P08, fibrine et complément | 169 | 52 | 71 | 46 | 86 |
| P14, antigène viral persistant | 167 | 41 | 22 | 104 | 35 |

Deux lectures de P01 sont hors de la grille de la consigne et ne sont pas comptées dans les trois colonnes du milieu.

- **La carte surestimait P14.** Sur 167 résumés retenus par ses termes, 104 ne citent la persistance virale qu'en passant,
  et 87 sont des revues. Trente-cinq études la mesurent ou la testent chez des patients.
- **P01 et P08 sont réellement denses** : 77 et 86 études de mesure ou essais pertinents.
- **Un quart à deux tiers de bruit selon la piste** : 24 % pour P01, 27 % pour P08, 62 % pour P14.
  Un décompte par termes ne se lit donc pas d'une piste à l'autre.

## Relations extraites

327 relations, chacune avec une citation ; toutes les citations sont retrouvées mot pour mot dans leur résumé.

| Piste | Relations | Soutient | Contredit | Neutre | Verbes les plus fréquents |
| --- | --- | --- | --- | --- | --- |
| P01 | 132 | 84 | 33 | 15 | associated_with 42, increased_in 32, causes 16, not_associated_with 15 |
| P08 | 145 | 122 | 11 | 12 | associated_with 54, increased_in 44, decreased_in 17, causes 12 |
| P14 | 50 | 32 | 10 | 8 | associated_with 26, not_associated_with 6 |

Un quart des relations de P01 vont contre la piste, contre 8 % pour P08. Ce chiffre dépend du champ « sens »,
qui est le moins fiable de la lecture (voir plus bas) : il indique où regarder, il ne pèse pas la piste.

## Précision, sur un échantillon relu

Trente relations tirées au sort (graine fixée dans le script) ont été relues par le modèle principal, contre leur citation.

| Jugement | Relations |
| --- | --- |
| La relation dit ce que dit la citation | 27 |
| Elle ne le dit pas | 3 |

Les trois erreurs : une hausse écrite alors que l'écart n'est pas significatif (p = 0,17) ; une association générale
tirée de la description d'un seul patient ; une relation dont la citation ne nomme pas le sujet.

Vingt-sept sur trente font 90 %, le seuil du protocole, avec une marge d'erreur large : de 74 % à 97 % pour un échantillon
de cette taille (intervalle de Wilson à 95 %, calculé à la main). **Le critère de passage n'est pas établi.** Le protocole
demande une relecture à la main ; celle-ci est faite par un programme, du même type que les lecteurs.

Le champ « sens » est moins fiable que la relation : dans l'échantillon, deux baisses du complément sont notées
« soutient » sans que le résumé le justifie. Cinq relations sur trente portent sur le COVID-19 aigu, pas sur le COVID long.

## Défauts relevés par les lecteurs

- **Un terme mal choisi.** « complement » ramène aussi le verbe anglais « to complement » : au moins cinq faux positifs dans P08.
- **Des doublons dans la bibliothèque** : 12 références sur 477 sont enregistrées deux fois.
- **La consigne range les méta-analyses avec les revues**, donc sans relation, alors qu'elles rapportent des mesures groupées.
- **Il manque un verbe**, « détecté dans » : les lecteurs l'ont remplacé par `associated_with`, ce qui gonfle ce verbe.
- **P14 mélange trois objets** : l'antigène, l'ARN viral et les anticorps. Plusieurs études retenues ne mesurent pas l'antigène.
- **Des résumés tronqués** ou réduits à une phrase : le type et la pertinence viennent alors du titre.

Ces défauts sont laissés tels quels dans les décomptes : les termes et la consigne ne se corrigent pas après la lecture.
Ils sont à corriger avant de lire une autre piste.

## Limites

- Les lecteurs ne lisent que des résumés, et la bibliothèque couvre le COVID long, pas l'EM/SFC d'avant 2020.
- Aucun graphe n'est encore construit : les entités ne sont pas normalisées, « fibrinogen » et « fibrin » restent deux noms.
- Les fichiers des lecteurs restent dans `cache/cartographie/`, hors du dépôt : ils contiennent les résumés.
  Seuls ces décomptes entrent au dépôt.

## Refaire

```bash
python3 outils/bibliotheque_apresj20.py telecharger
python3 analyses/cartographie/lots.py preparer P08 P14 P01
# un lecteur par lot, avec outils/consigne-lecteur.md
python3 analyses/cartographie/lots.py controler
python3 analyses/cartographie/lots.py echantillon 30
```
