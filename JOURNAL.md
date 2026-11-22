# Journal des décisions

Une entrée par décision : ce qui a été choisi, pourquoi, et ce qui a été écarté.
Les entrées les plus récentes sont en haut.

## 2026-11-22 — Lot 2 : cinq demandes sur six envoyées

**Fait.** Cinq lettres sont parties : Bergen, REVERSE-LC, outSMART-LC, rapamycine, Craddock.
Quatre l'ont été après la mise en ligne du plan corrigé. La première, à Bergen, a été envoyée
par le porteur du projet ; elle ne dépend pas des cases corrigées. La sixième, pour Brave-LC,
attend un contact.

**Décision.** Le texte des lettres est déposé dans `analyses/lot-2/LETTRES.md`, sans signature
ni adresse : la formulation d'une demande peut orienter la réponse, elle fait partie du dossier.
Une absence de réponse se constate à partir du 2027-01-22.

**Limite.** La lettre à Craddock est partie à son adresse actuelle, à l'université de Waterloo,
et non à celle de l'article de 2015.

## 2026-11-22 — Lot 2 : trois corrections après une seconde lecture des sources

**Constat.** En cherchant les destinataires des demandes, trois cases du tableau de vérification
se sont révélées fausses ou incomplètes. REVERSE-LC a une visite à 12 mois, six mois après
l'arrêt. AER002 est suivi jusqu'à un an, pas trois mois. L'essai qui suit l'étude
de la rapamycine prévoit un retrait randomisé.

**Cause.** La première vérification s'appuyait sur une seule page par essai : une fiche
de registre illisible, une fiche qui ne liste que les critères principaux, un résumé d'article.

**Décision.** Corriger le plan en bas de fichier, avec date et motif, sans toucher à la règle
de décision. Une case « non trouvé » ou « aucun » ne s'écrit plus qu'après une seconde source.

**Conséquence.** Trois essais en cours ou prévus comportent un suivi après l'arrêt. Le lot 2
est plus prometteur que ne le disait l'entrée suivante ; sa composition ne change pas.

## 2026-11-22 — Lot 2 retenu en premier ; la vérification en retire une paire

**Décision du porteur du projet.** Instruire d'abord le lot 2 : ce que deviennent
les répondeurs après l'arrêt du traitement.

**Fait.** Plan d'analyse déposé avant toute donnée (`analyses/lot-2/PLAN.md`) : données
demandées, repère d'arrêt par traitement, règle de décision. Six demandes prêtes,
aucune envoyée (`analyses/lot-2/DEMANDES.md`).

**Constat.** La vérification essai par essai corrige l'estimation de l'entrée suivante.
Les deux essais de la naltrexone s'arrêtent à 16 semaines, sans évaluation après l'arrêt :
la paire H6 et H7 passe en « nouvelle collecte ». Huit paires sur vingt et une, et non neuf,
se tranchent sans nouveau prélèvement. Un seul traitement, le daratumumab, a publié
un suivi après l'arrêt.

**Choix.** Demander des chiffres agrégés plutôt que des données individuelles : plus simples
à fournir, et suffisants pour la règle de décision. Prendre un repère biologique plutôt
qu'un délai fixe pour le daratumumab et l'anticorps, dont l'effet dure plus que le médicament.

**Écarté.** Conclure sur le pilote du daratumumab : son résultat va dans le sens de H6,
mais H1 le prédit aussi, et l'essai est ouvert, sans critère de réponse fixé d'avance.

## 2026-11-22 — Phase 3 : vingt et une confrontations, classées par accès aux données

**Décision.** Une fiche par paire d'hypothèses dans `registre/confrontations.yaml` : la question,
la mesure, ce qu'on observe selon l'hypothèse à l'œuvre, et l'accès aux données.
Le validateur exige les 21 paires, avec deux prédictions différentes par paire.

**Constat, corrigé par l'entrée précédente.** Quatre paires se tranchent sur du sang déjà conservé, cinq sur le suivi d'essais
après l'arrêt du traitement, douze demandent une nouvelle collecte. Les hypothèses 3, 5 et 7
ne se confrontent aux autres qu'avec une nouvelle collecte, sauf face à l'hypothèse 6.

**Écarté.** Classer les mesures par nombre de paires tranchées : chaque hypothèse apporte
son marqueur dans ses six paires, le classement est plat par construction. Traiter
les hypothèses comme exclusives : plusieurs peuvent être vraies chez des patients différents.

**Réserve.** La phase 3 n'est pas franchie. Le critère automatique passe, mais les fiches
viennent d'un seul rédacteur, sans relecture contradictoire. L'accès aux données est estimé
d'après le registre, pas confirmé auprès des équipes d'essais.

## 2026-11-22 — Craddock 2015 : réseau reproduit, taux publiés retrouvés en partie

**Constat.** Les deux articles ont pu être lus en PDF, figures comprises. Le réseau relevé
sur la figure 2 de 2015, avec la règle de 2014, redonne exactement les cinq états stables
publiés. La figure de 2014 diffère sur deux flèches et perd l'état malade.

**Décisions.**

- Retenir la figure de 2015 : elle seule est compatible avec les états publiés.
- Lire un traitement comme l'écrit l'équation 4 de l'article : un décalage d'un cran.
  Donner la lecture « deux crans » à côté, parce qu'elle seule retrouve la figure 5.
- Laisser le réseau se stabiliser entre deux interventions, au lieu des délais fixes
  de l'article : plus simple, et le résultat ne dépend plus d'un réglage.
- Annoncer une reproduction des états stables et de l'effet d'ordre, pas des taux.

**Écarté.** Ajuster la lecture du traitement ligne par ligne jusqu'à retrouver chaque taux :
ce serait régler le simulateur sur le résultat attendu. Chercher les taux exacts par
l'algorithme génétique de l'article : inutile tant que l'application d'un traitement
n'est pas tranchée.

**Réserve.** Le relevé de la figure est manuel, sans seconde lecture indépendante.
Le contrôle est indirect : les cinq états stables publiés sont retrouvés.

**Conséquence.** Cette entrée remplace la suivante.

## 2026-11-22 — Remplacée — Craddock 2015 : le moteur est construit, la reproduction attend la figure 2

**Constat.** Dans l'article, la liste des interactions du réseau n'existe que dans la figure 2,
et la règle de mise à jour que dans des équations en image. La page PubMed Central est bloquée
par un contrôle anti-robot ; la page PLOS ONE donne le texte sans équations ni figures.

**Décision.** Construire le moteur avec ce que le texte décrit (trois valeurs par nœud,
un nœud à la fois, tirage au sort, intervention d'un cran), le vérifier sur deux réseaux
calculables à la main, et ne pas annoncer de reproduction. La règle donnant la valeur visée
d'un nœud est provisoire (un vote) et isolée dans une seule fonction.

**Écarté.** Reconstituer le réseau de mémoire ou d'après d'autres articles : invérifiable,
et contraire à la règle « une affirmation = une source lue ».

**Reste à faire.** Relever la figure 2 et l'équation 2, charger le réseau, puis retrouver
les six taux publiés avant toute question nouvelle. Détail :
`simulateurs/niveau2/RESULTATS_RESEAU_LOGIQUE.md`.

## 2026-11-22 — Nouvel axe : les transpositions depuis des maladies mieux maîtrisées

**Décision.** La phase 2 reçoit une seconde source de pistes : partir des maladies qu'on sait
guérir, contrôler ou prévenir et qui partagent un processus biologique avec nos pistes.
Première série de onze fiches dans `registre/transpositions.yaml`, dont trois sur le VIH.

**Motif.** Ces maladies apportent des leviers, des marqueurs et des plans d'essai déjà éprouvés.

**Choix.** Le degré de maîtrise se dit en cinq mots (guérison, rémission, contrôle, prévention,
échec) : le VIH est contrôlé et prévenu, pas guéri, et cela ne se transpose pas comme
une guérison. Le champ `deja_tente` est obligatoire : plusieurs transpositions ont déjà été
essayées dans le COVID long, et ont échoué chez des patients non sélectionnés.

**Écarté.** Ranger les transpositions parmi les pistes : elles ne remplissent pas les mêmes
critères. Une seule fiche par maladie : le VIH porte trois processus distincts.

**Réserve.** Les 50 sources ajoutées ont été lues sous forme de résumé ou d'extrait,
pas intégralement. La phase 1 doit les relire et interroger les registres d'essais.
Le niveau attribué à chaque transposition est un jugement de ce dépôt, non évalué par des pairs.

## 2026-11-22 — Licences : MIT pour le code, CC BY 4.0 pour le reste

**Décision.** Le code Python est sous licence MIT (`LICENSE`). Le registre, les documents,
les résultats et la figure sont sous licence Creative Commons Attribution 4.0
(`LICENSES/CC-BY-4.0.txt`).

**Motif.** Les résultats doivent pouvoir être utilisés. Sans licence, un dépôt public
ne donne à personne le droit de réutiliser son contenu. Ces deux licences autorisent
toute réutilisation, y compris commerciale, à la seule condition de citer la source :
la citation préserve la traçabilité.

**Écarté.** CC0 : aucune obligation de citer, donc une chaîne de sources qui peut se perdre.
GPL-3.0 et CC BY-SA 4.0 : l'obligation de rediffuser sous la même licence freine
la réutilisation par d'autres équipes.

**Réserve.** Le titulaire est désigné collectivement : « Les contributeurs de longClauvid ».
Une partie du contenu a été rédigée avec un assistant d'intelligence artificielle ;
la protection de ce contenu par le droit d'auteur varie selon les pays. Les licences
disent l'intention : laisser réutiliser. Cette entrée n'est pas un avis juridique.

## 2026-11-22 — Le dépôt est public

**Décision.** Le dépôt est public, et le document de cadrage y est publié
(`docs/cadrage.md`), sans nom d'auteur.

**Motif.** Les résultats doivent pouvoir être utilisés.

**Conséquence.** Cette entrée remplace « Ouverture du dépôt », plus bas, qui prévoyait
un dépôt privé. Les avertissements restent en tête du README, des fiches d'endotypes
et des résultats du niveau 2 : hypothèses non évaluées par des pairs, aucun avis médical.

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

**Remplacée** le jour même par l'entrée « Le dépôt est public ».

**Décision.** Le dépôt est privé à sa création.

**Motif.** Il contient des hypothèses non évaluées par des pairs sur des traitements.
Le rendre public est une décision à prendre une fois le registre relu.
