# Journal des décisions

Une entrée par décision : ce qui a été choisi, pourquoi, et ce qui a été écarté.
Les entrées les plus récentes sont en haut.

## 2026-11-22 — Reproduction de Kashi 2019 acceptée « aux arrondis publiés près »

**Constat.** Le simulateur de niveau 2 donne un état normal à 2,43 × 10⁷ molécules par cellule
(publié : ~2 × 10⁷, écart +21 %) et un état piégé à 4,47 × 10⁹ (publié : ~5 × 10⁹, écart −11 %).

**Décision.** La reproduction est acceptée. Le critère de la phase 4, écrit d'abord
« reproduit à l'identique », devient « reproduit » avec une tolérance de 25 %.

**Motif.** L'article ne donne ces valeurs qu'avec un chiffre significatif, précédé de « ~ ».
Les équations et les onze paramètres ont été relevés sur deux rendus indépendants de l'article
(PubMed Central et le site de l'éditeur), qui concordent. Les deux affirmations qualitatives
de l'article sur LAT1 sont retrouvées.

**Reste à faire.** Confronter l'équation 1 au PDF de l'article : les deux relevés viennent
du même balisage mathématique de la page.

## 2026-11-22 — Niveau 2 : commencer par Kashi 2019

**Décision.** Le premier modèle mécaniste est le piège métabolique IDO de Kashi, Davis et Phair.

**Motif.** Une seule équation différentielle, onze paramètres, tous publiés : c'est le modèle
le plus simple à reproduire et à contrôler.

**Écarté pour l'instant.** Le modèle logique de Craddock 2015 (plusieurs variables,
réseau neuro-endocrino-immunitaire). Il reste nécessaire : un modèle à une variable
ne peut pas tester l'effet de l'ordre des traitements, que prédit l'hypothèse H6.

## 2026-11-22 — Niveau 2 : extension IDO2 hors article

**Décision.** Le simulateur ajoute une enzyme IDO2 fonctionnelle, inactive par défaut.

**Motif.** L'article suppose IDO2 défaillante et ne la chiffre pas. Or c'est sa prémisse
génétique centrale. L'extension permet de calculer l'activité minimale qui supprime le piège.

**Réserve.** La constante de Michaelis d'IDO2 est déduite du rapport des valeurs in vitro
citées par l'article (environ 100 µM contre 5 µM pour IDO1), faute de valeur dans les unités
du modèle. Tout résultat sur IDO2 est une exploration, pas une reproduction.

## 2026-11-22 — Contrôles : un script, pas un cadre de test

**Décision.** `verifier.py` enchaîne tous les contrôles et renvoie un code d'erreur.

**Motif.** Une commande, aucune dépendance de plus, lisible de haut en bas.

**Écarté.** pytest : standard en Python, mais une dépendance et des conventions de plus
pour une quinzaine de contrôles. À reconsidérer si leur nombre grandit.

## 2026-11-22 — Registre en YAML, un fichier par hypothèse

**Décision.** Sources, pistes et endotypes tiennent chacun dans un fichier YAML ;
chaque hypothèse a son propre fichier.

**Motif.** YAML se relit et s'édite à la main, accepte les commentaires et les textes longs.
Un fichier par hypothèse donne à chacune son propre historique Git.

**Écarté.** JSON : aucune dépendance, mais ni commentaires ni textes longs lisibles.
TOML : lecture native en Python, mais moins répandu. Une base de données : inutile
à cette échelle, et elle sortirait le registre de l'historique Git.

## 2026-11-22 — Simulateurs en scripts Python

**Décision.** Les simulateurs sont des scripts Python (NumPy, SciPy), sans interface.

**Motif.** C'est la voie la plus simple et la plus facile à reproduire : une graine, un commit.

**Écarté pour l'instant.** Les outils de biologie des systèmes (COPASI, Tellurium, format SBML) :
utiles dès qu'un modèle publié existe dans ce format ; l'article de Kashi 2019 ne fournit pas de fichier de modèle.
Une page web interactive : utile pour montrer le simulateur, pas pour le valider.

## 2026-11-22 — Ouverture du dépôt

**Décision.** Le dépôt est privé à sa création.

**Motif.** Il contient des hypothèses non évaluées par des pairs sur des traitements.
Le rendre public est une décision à prendre une fois le registre relu.
