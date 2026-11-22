# Niveau 1 : quel plan d'essai peut voir un effet limité à un sous-groupe

Résultats du 2026-11-22, produits par `python3 simulateur_endotypes.py`
(graine 20261122, 20 000 essais simulés par case).

**Un essai tout-venant de 200 patients ne détecte qu'une fois sur cinq un traitement
très efficace chez 20 % des patients. Un biomarqueur imparfait porte cette chance à 77 %.**

## Puissance par plan d'essai

| Part de répondeurs | Essai tout-venant, 200 patients | Patients requis pour 80 % de puissance | Essai enrichi, 200 inclus (patients dépistés) | Série N-de-1, 60 patients : effet moyen / hétérogénéité |
| --- | --- | --- | --- | --- |
| 10 % | 8 % | 5 048 | 39 % (770) | 24 % / 38 % |
| 20 % | 20 % | 1 290 | 77 % (625) | 66 % / 70 % |
| 30 % | 38 % | 582 | 93 % (527) | 92 % / 85 % |
| 50 % | 77 % | 212 | 99 % (400) | 100 % / 93 % |

Chaque pourcentage est une puissance : la probabilité que l'essai détecte l'effet au seuil de 5 %.

## Hypothèses

- Effet de 0,8 écart-type chez les répondeurs, nul chez les autres.
- Biomarqueur de sensibilité et de spécificité 80 %.
- N-de-1 : trois paires de périodes par patient, bruit intra-patient de 0,5 écart-type.
  Avec un bruit de 0,8, la détection d'hétérogénéité tombe entre 15 % et 42 %.

## Lecture

- L'essai tout-venant dilue l'effet : il faudrait 1 290 patients, et non 200,
  pour un sous-groupe de 20 %.
- Un biomarqueur même imparfait change l'ordre de grandeur, au prix de 625 patients dépistés.
- La série N-de-1 est le seul plan qui distingue « petit effet chez tous » de « fort effet
  chez certains ». Elle exige un traitement à effet rapide et réversible.

## Contrôles

Avec un effet nul, le simulateur donne 2,6 %, 2,5 % et 4,9 % de faux positifs
pour 2,5 %, 2,5 % et 5 % attendus. La formule analytique recoupe la simulation à un point près.

## Limites

Le simulateur suppose un effet en tout ou rien et des endotypes exclusifs.
La réalité est plus continue : un patient a un profil sur plusieurs axes.
