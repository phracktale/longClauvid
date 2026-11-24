# Piste B005 : résultats de la réanalyse des données de l'étude de 2026

Calcul du 2026-11-24, selon [`PLAN.md`](PLAN.md), déposé avant le calcul. Script : [`reanalyse.py`](reanalyse.py).
Données : le classeur publié par les auteurs, version `8684a2f` de leur dépôt. Rien ici n'est un avis médical.

**En une phrase :** l'écart publié résiste à l'ajustement sur l'âge et le sexe, pour l'EM/SFC comme pour le COVID long.
C'est un résultat descriptif, sur les mêmes patients : il ne vaut pas réplication, et le niveau de la piste reste C.

## Étape 0 : les chiffres publiés sont retrouvés

Écart de l'indice de la voie de la noradrénaline aux volontaires sains, en pmol/mL, sans ajustement (test de Tukey).

| Groupe | Dosés | Écart recalculé | Intervalle à 95 % | Écart publié |
| --- | --- | --- | --- | --- |
| Volontaires sains | 36 | référence | | |
| EM/SFC | 15 | −15,89 | −26,12 à −5,65 | −15,9 |
| COVID long | 30 | −9,62 | −17,85 à −1,39 | −9,62 |
| Maladie de Parkinson | 32 | −19,39 | −27,48 à −11,30 | −19,4 |

Parmi les personnes dosées, l'âge moyen est de 50,1 ans chez les volontaires sains, 37,3 ans dans l'EM/SFC
et 43,9 ans dans le COVID long. Les femmes font 33 %, 60 % et 67 % de ces groupes.

## Étape 1 : le test principal

Régression de l'indice sur le groupe, l'âge et le sexe, sans le groupe Parkinson. Seuil de 0,025 par test.

| Groupe | Dosés | Écart ajusté | Intervalle à 97,5 % | p |
| --- | --- | --- | --- | --- |
| EM/SFC | 15 | −13,16 | −22,71 à −3,61 | 0,0023 |
| COVID long | 30 | −8,75 | −16,33 à −1,17 | 0,0101 |

Les deux intervalles excluent zéro, du côté négatif : selon le plan, **l'écart résiste à l'ajustement**.
L'ajustement le réduit un peu : de 15,9 à 13,2 pour l'EM/SFC, de 9,6 à 8,8 pour le COVID long.
La pente de l'âge est de 0,26 pmol/mL par an, à la limite du seuil (p = 0,0245) :
elle rend compte de cette baisse, sans plus.

## Étape 2 : sensibilité

Descriptif, sans correction : une valeur de p isolée n'y prouve rien. Intervalles à 95 %.

**2.1 Avec les quatre groupes.** EM/SFC −14,96 (−23,25 à −6,66) ; COVID long −9,56 (−16,14 à −2,97) ;
maladie de Parkinson −21,05 (−27,82 à −14,27).

**2.2 Sans les patients sous médicament agissant sur la noradrénaline.** Ils sont dix : quatre dans l'EM/SFC,
six dans le COVID long, aucun chez les volontaires sains. L'article ne donnait pas cette répartition.

| Groupe | Dosés | Écart ajusté | Intervalle à 95 % | p |
| --- | --- | --- | --- | --- |
| EM/SFC | 11 | −11,68 | −21,45 à −1,92 | 0,020 |
| COVID long | 24 | −6,52 | −13,79 à +0,75 | 0,078 |

Sans eux, l'écart de l'EM/SFC tient. Celui du COVID long garde son sens et bouge peu, de −8,75 à −6,52 ;
avec 24 patients au lieu de 30, il est moins précis et son intervalle contient zéro.

**2.3 Chaque dosage seul**, ajusté sur l'âge et le sexe.

| Dosage | EM/SFC | COVID long |
| --- | --- | --- |
| MHPG | −10,57 (−17,00 à −4,14) | −7,16 (−12,27 à −2,05) |
| DHPG | −2,85 (−5,10 à −0,60) | −2,07 (−3,85 à −0,28) |
| Noradrénaline | −0,23 (−0,51 à +0,06) | +0,14 (−0,08 à +0,37) |
| DOPAC | −0,43 (−0,85 à −0,01) | −0,06 (−0,39 à +0,27) |
| DOPA | −0,51 (−1,15 à +0,14) | −0,10 (−0,61 à +0,41) |
| HVA | −17,49 (−68,51 à +33,53) | +32,72 (−7,78 à +73,22) |
| Dopamine | −0,03 (−0,11 à +0,06) | +0,01 (−0,06 à +0,08) |

Trois lectures :

- L'écart de l'indice vient surtout du MHPG, puis du DHPG. La noradrénaline elle-même ne diffère pas.
- Le DOPAC seul est un peu plus bas dans l'EM/SFC, à la limite (p = 0,043, sans correction), et pas dans le COVID long.
  Cela concorde avec le DOPAC bas de l'étude de 2024, sur des patients très probablement identiques.
- L'indice de la dopamine est une somme dominée par le HVA : 180 pmol/mL en moyenne, contre 1,6 pour le DOPAC.
  Un petit écart du DOPAC ne peut pas s'y voir. « Pas de déficit en dopamine » dit donc plus que les données.
- Les lignes du tableau ne portent pas toutes sur les mêmes personnes : 36 volontaires sains ont un MHPG et un HVA,
  39 ou 40 ont les autres dosages.
- Le sexe pèse sur le DOPAC, plus haut chez les femmes. L'écart du DOPAC dans l'EM/SFC dépend donc de l'ajustement
  sur le sexe, dans des groupes qui comptent 60 % et 33 % de femmes.

**2.4 COVID long, avec et sans malaise post-effort.** Avec malaise, 9 patients : −16,15 (−27,10 à −5,21).
Sans malaise, 12 patients : −5,72 (−14,65 à +3,21). Neuf patients dosés, tous d'un même protocole, n'ont pas de malaise codé et sortent de ce calcul,
comme dans le script des auteurs. L'article compte 13 patients sans malaise ; le classeur en donne 12 dosés.

## Relecture indépendante du calcul, et deux ajouts hors plan

Un second programme a refait le calcul avec son propre code, sans importer le script : il retrouve tous les chiffres
des étapes 1 et 2, et ne trouve pas d'erreur de calcul. Il a corrigé quatre phrases de ce compte rendu,
qui disaient plus que les chiffres ; elles sont réécrites ci-dessus. Relecteur et auteur du calcul sont des programmes du même type.

Deux analyses, **non prévues au plan**, sont ajoutées au script à sa demande. Elles sont descriptives.

| Analyse hors plan | EM/SFC | COVID long |
| --- | --- | --- |
| Indice de la voie de la dopamine, ajusté, intervalle à 95 % | −21,9 (−74,8 à +31,1) | +28,9 (−14,9 à +72,7) |
| Test principal refait sur les rangs, intervalle à 97,5 % | −21,7 rangs (−37,6 à −5,9) | −12,5 rangs (−25,1 à +0,07) |

Sur les rangs, l'écart de l'EM/SFC tient ; celui du COVID long frôle zéro. Le COVID long est donc le moins net des deux.
Le relecteur rapporte aussi, avec son code hors dépôt, qu'aucune personne retirée seule ne fait basculer le résultat.

## Ce que cela change pour la piste

- Le manque relevé à la relecture, l'absence d'ajustement sur l'âge, est comblé : l'écart tient, plus nettement pour l'EM/SFC que pour le COVID long.
- La lecture « la voie de la dopamine est normale » est à nuancer : le DOPAC seul reste un peu bas dans l'EM/SFC.
- Le statut et le niveau ne changent pas : vérifiée, niveau C. Il manque toujours une cohorte hors du NIH.

## Limites

- Mêmes patients, même équipe, même centre que l'article : ce calcul contrôle une analyse, il ne réplique rien.
- Les volontaires sains viennent de plusieurs protocoles ; l'âge et le sexe ne sont pas les seules différences possibles.
- Effet de l'âge supposé linéaire, estimé sur 81 personnes au test principal, et sur 57 à 89 ailleurs.
- L'étape 2 compte une vingtaine de comparaisons, sans correction.
- Le plan a été écrit après lecture de l'article : les écarts bruts étaient connus. Seul l'ajustement était inconnu.
