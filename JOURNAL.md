# Journal des décisions

Une entrée par décision : ce qui a été choisi, pourquoi, et ce qui a été écarté.
Les entrées les plus récentes sont en haut.

## 2026-11-24 — B005 et B019 : deux articles lus en entier, deux pistes gardées au niveau C

**Fait.** Le porteur du projet a fourni les deux articles. Le modèle principal les a lus ; un contradicteur par piste
a attaqué la lecture. Les deux avis sont « tient en partie », et toutes les citations sont retrouvées.

**B005.** Recentrée sur la noradrénaline : l'indice de cette voie est plus bas chez les patients, celui de la dopamine est normal.
Les patients EM/SFC sont très probablement ceux de 2024 : la piste reste sans réplication hors du NIH.
Trois constats de ma lecture étaient faux ou trop forts ; le contradicteur les a corrigés, dont une affirmation des auteurs
reprise sans contrôle.

**B019.** Le signal d'avant la maladie est porté par l'IL-13 et l'IL-6 ; l'IL-5 n'est qu'en tendance.

**Choix.** Les titres et les champs écrits au dépôt des deux pistes ne sont pas réécrits : la relecture les corrige
dans son propre champ. Écarté : les réécrire d'office, ce qui effacerait la trace de ce qui avait été déposé.
La réécriture est proposée au porteur du projet.

## 2026-11-24 — Quatre travaux faits sans attendre de réponse

**Modèle de Craddock.** La règle soumise à l'auteur est essayée : un frein de deux crans, une stimulation d'un cran.
Elle rend 11 lignes sur 12 de la figure 5 à 2 points près, contre 8 pour deux crans partout et 0 pour un cran.
La douzième ligne demande l'inverse pour le même nœud : aucune règle simple ne rend les douze.

**Erratum de 2014.** Retrouvé à la seconde recherche, par les liens de correction de PubMed. L'article a deux errata ;
le second remplace la figure du réseau, « qui contenait un certain nombre d'erreurs ». Cela confirme ce que disait l'auteur.
La figure corrigée n'a pas été relue arête par arête. La première recherche avait cherché par nom d'auteur :
les errata sont signés par la revue.

**Contrôle automatique.** Le dépôt n'en avait aucun côté GitHub. Un fichier lance désormais `verifier.py`
à chaque demande de fusion. Choix : un seul travail, sans donnée extérieure.

**Dépôt citable.** `CITATION.cff` et `.zenodo.json` sont ajoutés. L'auteur déclaré est « Projet longClauvid » :
la règle du projet exclut le nom du porteur du projet. L'identifiant DOI demande encore de relier le dépôt à Zenodo
et de publier une version : c'est un geste du porteur du projet.

**Constat.** Les articles de B005 et de B019 sont gratuits pour une personne et refusés aux programmes.

## 2026-11-24 — B009 : l'auteur a envoyé son article, la piste est gardée au niveau C

**Fait.** L'auteur de l'étude de 2017 a envoyé son article le jour de la demande, sans condition.
Le modèle principal l'a lu ; un contradicteur a attaqué la décision. Toutes ses citations sont retrouvées.

**Constat.** La vasopressine est plus basse chez 18 patients que chez 15 témoins, p = 0,02. L'aldostérone l'est aussi.
L'essai de desmopressine porte sur 10 patients, sans placebo.

**Décision.** La piste sort de « à vérifier » : gardée au niveau C, sur l'étude de 2017 seule.

**Erreur du décideur, relevée par le contradicteur.** Le statut avait d'abord été motivé par « deux études portent
le même signal, et l'une est lue en entier ». C'est faux : l'étude de 2026 ne le porte pas, sa copeptine est normale.
Le statut tient quand même, pour une raison plus simple : l'étude qui porte le signal est lue en entier.

**Corrigé.** « Les deux mesures de 2026 se contredisent » : elles viennent de patients différents.
« Financement public japonais » : l'article ne nomme qu'une subvention ; le reste venait de la mémoire du lecteur.

**Constat.** Une seule piste reste à vérifier, B023.

## 2026-11-24 — Règle de lecture des réponses reçues

**Décision du porteur du projet.** Quand il signale une réponse arrivée dans la boîte du projet, le programme la lit,
sauf s'il dit « sous condition ». Une réponse qu'il n'a pas signalée ne se lit pas.

**Motif.** La boîte est connectée au programme, et une réponse peut poser une condition, comme celle de P17.
Seul le porteur du projet, qui l'a lue, sait si elle en pose une. La règle évite de lui reposer la question à chaque réponse.

## 2026-11-23 — Brave-LC prévoit une visite après l'arrêt de la naltrexone

**Fait.** L'équipe de l'essai a répondu à la demande du lot 2. Le porteur du projet a autorisé la lecture de la réponse.
Le traitement s'arrête vers le jour 112 ; une visite est prévue vers le jour 180, pour mesurer la persistance de l'effet.

**Correction.** Le plan du lot 2, la confrontation des hypothèses 6 et 7 et le document de cadrage écrivaient
qu'aucune évaluation après l'arrêt n'avait été trouvée. La correction est datée dans les trois fichiers ; dans le plan,
elle est en bas, et la règle de décision n'est pas modifiée.

**Conséquence.** La visite a lieu environ 68 jours après l'arrêt. La règle du lot exige un écart qui persiste
au moins trois mois : la visite sera descriptive, et la paire des hypothèses 6 et 7 ne revient pas dans le lot.

**Réserve.** La source est un courriel, pas un document public. Elle est à confirmer quand le protocole sera déposé
au registre, ce que l'équipe annonce. « Non trouvé » avait été écrit après la lecture de la seule fiche de registre.

**Écarté.** Assouplir la règle des trois mois pour faire entrer cette visite : une règle déposée ne se corrige pas
quand une donnée arrive.

## 2026-11-23 — Modèle de Craddock : l'article de 2021 est lu, une seconde lettre est rédigée

**Fait.** L'article de 2021 indiqué par l'auteur est lu pour ses passages de méthode et de résultats sur les traitements.
Le compte rendu est à la section 4 ter de `simulateurs/niveau2/RESULTATS_RESEAU_LOGIQUE.md`.

**Constat.** La règle y est écrite : un cran par pas de temps, tant que le traitement est appliqué, et le traitement est maintenu.
Le taux rapporté est celui du meilleur traitement trouvé par un algorithme génétique : un taux choisi parce qu'il est le plus haut
surestime le taux réel. C'était l'une des deux causes avancées pour l'écart aux taux de 2015.

**Fait.** Une seconde lettre à l'auteur est rédigée, non envoyée. Elle lui signale l'écart qu'il demande à connaître :
les taux publiés se retrouvent si un frein va à la valeur extrême et une stimulation d'un seul cran. Elle demande
la référence de l'erratum de 2014, et s'il autorise à citer son indication sur l'essai non publié.

**Réserve.** L'article de 2021 porte sur un autre réseau, plus grand : il éclaire la règle, pas les taux de 2015.

## 2026-11-23 — Modèle de Craddock : l'auteur a répondu, le code n'existe plus

**Fait.** L'auteur correspondant de l'article de 2015 a répondu. Le porteur du projet a dit que la réponse
ne porte aucune restriction ; le programme l'a lue.

**Constat.** Le code de simulation n'est plus disponible. Les traitements de 2015 sont appliqués à un seul instant,
puis relâchés : c'est ce que fait le simulateur. Un traitement peut déplacer un nœud d'un cran ou de deux, et la réponse
ne dit pas quelle définition a servi aux figures. Pour l'auteur, des taux proches suffisent, le procédé étant aléatoire.

**Lecture.** Avec un cran, l'écart aux taux publiés atteint 33 points : l'aléa n'explique pas cela. Avec deux crans,
8 lignes sur 12 sont à 2 points près. Les figures n'utilisent donc pas la lecture à un cran que donne l'équation de l'article.
C'est une déduction du projet, pas une confirmation de l'auteur.

**Non vérifié.** L'auteur attribue la différence entre les figures de 2014 et de 2015 à un erratum de 2014.
Une première recherche ne l'a pas retrouvé.

**Écarté.** Reprendre l'indication qu'il donne sur les résultats d'un essai non publié : il la dit non publique,
et un résultat confié avant publication n'entre pas au dépôt. Sa lettre ne pose pourtant aucune condition.

**Suite.** Lire l'article de 2021 qu'il indique, où le traitement est maintenu pendant une durée optimisée.

## 2026-11-23 — P17 : une réponse sous embargo, que le programme ne lit pas

**Fait.** L'auteur correspondant de la prépublication de P17 a répondu au porteur du projet. Il demande que ses données
ne soient pas données à une IA, ni rendues publiques avant la publication de son étude. Le porteur du projet l'a rapporté ;
le programme n'a ouvert ni le message ni ses pièces jointes.

**Décision.** Rien de cette réponse n'entre dans le dépôt. Le programme ne lit pas ce fil. La réponse du porteur
du projet confirme les deux engagements et pose deux questions : l'usage des données après publication, et l'emploi
d'un modèle à poids ouverts tournant sur sa machine avant.

**Constat.** La boîte du projet est connectée au programme. Une réponse confiée sous condition s'y trouve donc
à sa portée : c'est au porteur du projet de la sortir de la boîte. Le relevé des réponses ne peut plus se faire
en lisant tous les fils sans distinction.

**Écarté.** Lire le message pour consigner précisément ce qui est permis : ce serait faire ce que l'auteur refuse.

## 2026-11-23 — B004 et B016 : articles lus en entier, deux pistes gardées, un niveau baisse

**Fait.** Le porteur du projet a téléchargé les deux articles, en accès libre pour une personne et refusés aux programmes.
Le modèle principal les a lus ; un contradicteur a attaqué chaque décision. Toutes les citations sont retrouvées.

**Décision, B004.** Gardée comme hypothèse théorique, niveau D. L'effet est montré chez 12 cyclistes entraînés,
après neuf heures d'effort, et il a disparu le lendemain. Aucun patient n'est étudié.

**Décision, B016.** Gardée, niveau ramené de B à C. Le texte confirme 1,75 et 1,12, et montre un rapport de 0,91
dans un réseau quand l'ajustement change. La seule confirmation indépendante est une enquête déclarée des deux côtés.

**Motif, pour le niveau de B016.** Deux cohortes suffisent à la lettre pour le niveau B. La même lecture à la lettre
avait été refusée pour B018 : une confirmation qui ne tient pas seule ne relève pas un niveau.

**Écarté.** Écarter B016 comme signal probablement artefactuel : la grille le permettrait, pour un doute aux questions 5 et 9.
L'association de l'analyse principale est de même sens dans trois jeux de données, et une mise à l'écart de cette piste
a déjà été levée une fois. Elle est gardée, avec ses réserves écrites.

**Erreurs du décideur, relevées par les contradicteurs.** « Disparaît » pour un renversement de sens ; « ne dit rien
du traitement » alors qu'une analyse a été faite et non rapportée ; « aucune source ne mesure le canal chez des patients »,
trop large. Deux constats de la première contradiction de B004 tombent aussi.

**Constat.** Il ne reste que deux pistes à vérifier, B009 et B023 : trois articles sous abonnement, demandés à leurs auteurs.

## 2026-11-23 — B008 : l'article lu en entier ne dose le D-lactate chez aucun patient

**Fait.** Le porteur du projet a téléchargé l'article de 2009, que le site de la revue refuse aux programmes.
Le modèle principal l'a lu ; un contradicteur a ensuite attaqué la décision. Toutes ses citations sont retrouvées.

**Constat.** L'étude compte des bactéries dans les selles de 108 patients choisis pour leurs troubles digestifs,
contre 177 témoins définis par ce qu'ils déclarent. Elle dose le D-lactate dans le milieu de culture de trois souches,
jamais chez un patient. Un compte est mille fois plus haut chez les patients, et deux pourcentages du texte ne se retrouvent
pas avec les moyennes du tableau.

**Décision.** La piste sort de « à vérifier ». Elle est gardée comme hypothèse théorique, au niveau D au lieu de C.
Le signal de 2009 est probablement artefactuel : la piste n'est pas gardée sur sa foi.

**Corrigé après contradiction.** « Un dosage suffirait à réfuter » : le D-lactate fluctue. « Aucun essai enregistré » :
l'essai de 2018 l'est au registre australien et néo-zélandais, qui n'avait pas été interrogé. Et un constat du lecteur,
sur le métier d'un laboratoire, venait de sa mémoire et non de l'article.

**Réserve.** Le lecteur et le décideur sont ici le même programme. C'est le contradicteur qui a relevé l'erreur de mémoire.

**Fait.** Une troisième demande de copie est partie, pour B023, à l'adresse d'établissement que PubMed publie
pour le dernier auteur dans un autre article. C'est la dix-huitième demande.

## 2026-11-23 — Deux demandes de copie aux auteurs, pour B009

**Fait.** Sur instruction du porteur du projet, une copie des deux articles qui portent la piste B009 a été demandée
à leurs auteurs, de la boîte du projet. Ce sont les seizième et dix-septième demandes.

**Constat.** Pour les deux autres articles sous abonnement, B008 et B023, PubMed ne publie aucune adresse,
et les pages de la revue et de l'éditeur refusent les programmes. Les demandes ne sont pas parties.

**Écarté.** Deviner une adresse à partir du nom et de l'établissement d'un auteur : une adresse se prend
dans une source officielle, ou la lettre ne part pas.

**Choix.** La copie reçue ne sera pas versée au dépôt : la lettre s'y engage.

## 2026-11-23 — Cartographie : 477 résumés lus pour trois pistes

**Fait.** Quinze lecteurs, d'un modèle moins coûteux, ont lu les résumés retenus pour P01, P08 et P14, avec une consigne
déposée avant la lecture. Ils rendent 327 relations ; toutes leurs citations sont retrouvées mot pour mot.
Le compte rendu est dans `analyses/cartographie/LECTURE.md`.

**Constat.** La carte par termes surestimait la piste de l'antigène persistant : 104 résumés sur 167 ne la citent
qu'en passant, et 35 études la mesurent ou la testent chez des patients. Les auto-anticorps et la fibrine sont réellement
denses, avec 77 et 86 études. Un décompte par termes ne se compare donc pas d'une piste à l'autre.

**Précision.** Sur 30 relations tirées au sort et relues par le modèle principal, 27 disent ce que dit leur citation.
C'est le seuil de 90 % du protocole, avec une marge de 74 % à 97 % : le critère n'est pas établi, et la relecture
n'a pas été faite à la main par une personne.

**Choix.** Laisser les défauts dans les décomptes : un terme qui ramène le verbe « to complement », des doublons,
un verbe manquant, les méta-analyses rangées avec les revues. Ils sont listés et se corrigent avant la piste suivante.

**Écarté.** Construire le graphe maintenant : les entités ne sont pas normalisées, et la précision n'est pas acquise.

## 2026-11-23 — B002 : les deux lettres sont parties

**Fait.** Après le « bon pour envoi » du porteur du projet, les deux lettres sont parties de la boîte du projet,
telles qu'elles étaient déposées. Ce sont les quatorzième et quinzième demandes.

**Choix.** Quand un article donne plusieurs adresses, écrire à l'adresse d'établissement du dernier auteur.
Les adresses viennent de PubMed et du texte d'Europe PMC. Aucun nom ni adresse n'entre dans le dépôt.

## 2026-11-23 — Le programme fusionne lui-même ses demandes de fusion

**Décision du porteur du projet.** Le programme est autorisé à fusionner ses demandes de fusion sans redemander,
pour travailler de façon autonome. La règle est écrite dans `REPRISE.md`, section 2.

**Conditions.** Les contrôles passent sur le dernier commit ; la demande ne contient que le travail de la session ;
rien n'y attend une décision. Un envoi de lettre, une promotion ou une mise à l'écart gardent leur accord préalable.

**Constat.** Le dépôt n'a pas de contrôle automatique côté GitHub : « fusionnées automatiquement, une fois les contrôles
passés » voulait dire que le programme lance `verifier.py` puis fusionne. La fusion se fait avec un commit de fusion ;
le rebasage est abandonné, parce qu'il oblige à forcer la mise à jour de la branche.

## 2026-11-23 — P16 : la lettre repart, vers l'auteur correspondant de DecodeME

**Fait.** Sur instruction du porteur du projet, la lettre sur les allèles DRB1*11:04 et DQA1*03:01 est partie
de la boîte du projet vers l'auteur correspondant de la prépublication, à l'université. C'est la treizième demande.

**Choix.** Des trois auteurs correspondants, écrire au chercheur : les deux autres représentent les patients
et une association. L'adresse vient du fichier source de la prépublication. Aucun nom ni adresse n'entre dans le dépôt.

**Choix.** Dire dès la première phrase pourquoi la lettre arrive par cette voie : la boîte générale ne répond pas,
et la procédure d'accès vise des données individuelles.

## 2026-11-23 — DecodeME : la demande d'accès n'est pas ouverte au projet

**Constat.** La page d'accès de DecodeME ne propose pas de formulaire en ligne, mais un dossier à envoyer à un comité.
Sa politique écarte d'emblée un demandeur qui n'est pas employé par un établissement scientifique capable de signer
un contrat avec l'université d'Édimbourg. Le dossier vise les données individuelles et les échantillons.

**Conséquence.** Les tests 2 et 3 de P16 ne seront pas lus par cette voie. Ils ne demandent qu'un chiffre par allèle.

**Écarté.** Remplir le dossier malgré tout : le projet n'a ni établissement, ni avis éthique, ni financement à déclarer,
et la politique dit que le projet d'un demandeur non admissible n'est pas lu.

**Suite.** Trois voies sont notées dans `analyses/P16/DEMANDES.md`. La moins coûteuse : la même lettre, adressée
à l'auteur correspondant de la prépublication plutôt qu'à la boîte générale. Elle attend la décision du porteur du projet.

## 2026-11-23 — Cartographie : un premier pas, par un script

**Fait.** `analyses/cartographie/cartographie.py` compte, pour chaque piste du registre et de la banque, les références
de la bibliothèque #ApresJ20 dont le titre ou le résumé contient ses termes. La carte est dans `analyses/cartographie/CARTE.md`.
Sur 10 466 références, 8 432 ont un résumé, et 1 258 sont retenues par au moins une piste.

**Constat.** Trois pistes du registre sont denses : fibrine et complément (177 références), antigène persistant (175),
auto-anticorps (147). Six pistes ont quatre références ou moins : WASF3, SMPDL3B, humanine, pyruvate déshydrogénase,
cibinétide, RyR1. C'est le troisième critère d'une piste sous-exploitée, mesuré pour la première fois.
Les 9 208 références hors carte sont surtout de la clinique : définition, soins, enfants, rééducation.

**Choix.** Un script et aucun agent : des décomptes sur une copie locale, sans requête ni lecture par un modèle.
Les termes sont écrits dans le script, et ceux de la banque sont repris du test « inexplorée ».
Seuls des décomptes entrent au dépôt ; les titres et les résumés restent hors dépôt.

**Écarté.** Extraire tout de suite les relations entre entités : il faut lire 1 258 résumés et mesurer la précision
sur un échantillon relu à la main. Ce sera fait piste par piste.

**Réserve.** Un terme dans un résumé ne dit pas que l'étude porte sur la piste : « interferon » ou « IL-13 » ramènent
des panels de cytokines. La bibliothèque couvre le COVID long, pas l'EM/SFC d'avant 2020. Deux contrôles sont dans le script :
un terme inventé ne trouve rien, le nom de la maladie trouve plus de la moitié des références.

## 2026-11-23 — Les cinq nouvelles pistes relues et contredites : quatre gardées, une à vérifier

**Fait.** Chacune des cinq pistes a eu un relecteur, le test « inexplorée », puis un contradicteur : un défenseur
pour la piste écartée, un attaquant pour chacune des trois gardées. Sur 148 affirmations, 117 sont confirmées.
Toutes les citations sont retrouvées mot pour mot.

**Décision.**

- Ferroptose (B022) : d'abord écartée, puis gardée au niveau D. La source ne contredit pas la ferroptose,
  elle ne la teste pas : l'inhibiteur n'y est essayé que sur la prolifération.
- SLC7A11 (B023) : à vérifier. L'étude qui porte le signal n'est lue que par son résumé (PMID 38310391).
- Diarrhée aux acides biliaires (B024) : gardée au niveau D. Un cas d'un mois, sans marqueur dosé.
- Acides biliaires dans l'EM/SFC (B025) : gardée au niveau C pour la baisse de 2017 ; le mécanisme n'a pas de donnée.
- HIF-2α et érythropoïétine (B026) : gardée au niveau C, sur un appui mince.

**Motif, pour B022.** La mise à l'écart répétait l'erreur faite pour l'orexine : écrire « la source va contre »
là où elle ne mesure pas. Le contradicteur l'a relevée, et la même suite est donnée.

**Écarté.**

- Écarter B024 ou B026 pour un doute à la question 9 de la grille : il porte sur un diagnostic présumé
  ou des critères non écrits, pas sur une mesure déclarée des deux côtés.
- Garder « retrouvée par deux équipes » pour B025 : la seconde étude n'en dit qu'une phrase, dans son résumé.

**Réserve.** Quatre des cinq pistes sont de niveau D ou tiennent à une seule petite étude. Aucune n'a de test prêt.
Le dépôt n'ajoute pas de piste solide : il dit que ces trois zones sont presque vides de mesures chez les patients.

## 2026-11-23 — Trois zones non couvertes explorées : cinq pistes déposées, aucune relue

**Fait.** Trois agents de recherche, un par zone, ont suivi `outils/consigne-chercheur.md`, déposée avant leur départ.
Ils ont déposé cinq pistes, intégrées à la banque au statut « à vérifier » : B022 et B023 pour la ferroptose,
B024 et B025 pour les acides biliaires, B026 pour l'hypoxie et la voie HIF. Le contrôle à l'intégration est formel :
champs présents, chaque source avec son adresse et son mode de lecture. Aucune source n'a été rouverte.

**Écarté par les agents, d'après leurs comptes rendus.** Ferroptose : la peroxydation des lipides après l'effort,
pour un signal ancien et trois résultats nuls ; la coenzyme Q10, déjà essayée sans sélection des patients ;
le sélénium et le fer, déjà en banque. Hypoxie : l'oxygène hyperbare, dont les essais sont enregistrés ;
les variants d'altitude, sans donnée ; HIF-1α, connu par des revues seulement. Ces motifs ne sont pas sourcés
dans le dépôt : ils évitent de refaire la recherche, ils ne prouvent rien.

**Limites déclarées.** Presque toutes les sources sont lues par leur résumé ; deux textes intégraux seulement.
Europe PMC a renvoyé des erreurs sur plusieurs requêtes. Les recherches sont ciblées, non systématiques.

**Constat.** La consigne des deux premiers agents n'avait pas été conservée. Celle-ci est écrite d'après le protocole
et la forme des 21 premières pistes ; elle limite chaque agent à trois pistes.

## 2026-11-23 — B002 : deux lettres rédigées, non envoyées

**Fait.** Deux brouillons de lettre sont déposés dans `analyses/banque/DEMANDES.md`, pour les auteurs de la lipidomique
de 2024 et de l'étude multi-omique de 2025. Chacune pose deux questions : les plasmalogènes ont-ils été mesurés,
et par rapport à quel groupe ?

**Choix.** Demander une réponse d'une ligne plutôt que des données : la question est de savoir si le test de la piste
peut se faire sur l'existant. La seconde lettre dit que le résultat publié va, au niveau des voies, à l'inverse de la piste.

**Réserve.** L'étude de 2024 n'est lue que par son résumé. Rien ne part sans la relecture du porteur du projet.

## 2026-11-22 — Les quinze pistes gardées ont été attaquées : une repasse « à vérifier », un niveau baisse

**Fait.** Chacune des quinze pistes gardées a eu un contradicteur, chargé de l'attaquer. Sa consigne,
`outils/consigne-contradicteur-piste-gardee.md`, a été déposée avant sa lecture : celle du dépôt ne faisait que défendre
une piste écartée. Un avis « ne tient pas », quatorze « tient en partie », aucun « tient ». Les 158 arguments
et 233 des 237 faits contrôlés portent une citation ; toutes sont retrouvées mot pour mot. Quatre faits « non trouvés »
n'en portent pas : une absence ne se cite pas.

**Constat.** Sur les 237 faits des relectures, 195 sont confirmés, 19 sont inexacts et 3 sont contredits.
Six phrases trop fortes venaient du décideur lui-même, comme pour les mises à l'écart. Aucun des quinze tests proposés
n'est prêt : il manque un seuil, un sens attendu ou un jeu de données dont l'existence soit montrée.

**Décision.**

- Canal RyR1 du muscle (B004) : statut ramené de « vérifiée » à « à vérifier ». Le résultat qui porte la piste
  vient d'un article de 2008 lu par son seul résumé (PMID 18268335).
- Hypermobilité articulaire (B018) : niveau ramené de B à C. Deux des « trois équipes » n'en font qu'une,
  et les deux études indépendantes mesurent un diagnostic codé, pas l'hypermobilité.
- Les treize autres pistes gardent leur statut et leur niveau. Neuf décisions sont reformulées, les deux ci-dessus comprises ;
  six sont maintenues telles quelles.

**Motif.** La règle du résumé seul avait été appliquée de façon inégale : B008, B009 et B016 attendaient pour la raison
qui vaut pour B004. Pour B018, la même lecture avait ramené B013 à C : deux études qui ne mesurent pas la même chose
ne se répliquent pas.

**Choix.** La décision d'origine reste dans chaque piste, à côté de l'avis du contradicteur, dans le champ `relecture.attaque`.
Le décideur a vérifié lui-même, dans les copies locales, les constats qui changent un statut ou un niveau.

**Écarté.**

- Suivre le contradicteur sur la question 9 de la grille pour B013 et B017 : la maladie y est déclarée par la personne,
  mais le génotype et les marqueurs du sang sont mesurés. La règle vise une mesure déclarée des deux côtés.
- Ramener B007 et B019 à « à vérifier » : une de leurs deux sources n'est lue que par son résumé, mais l'autre,
  lue en entier, porte le même signal. C'est la limite de la règle, écrite comme telle dans le compte rendu.
- Réécrire les titres, les énoncés et les tests, comme les contradicteurs le demandent : le texte déposé ne se réécrit pas.
  Un test se réécrit dans un plan d'analyse, au moment de promouvoir la piste.
- Modifier les pistes P15 à P17 du registre : leurs fiches disent déjà l'essentiel de ce que l'attaque relève.
  Révisé le 2026-11-23 pour P15, par décision du porteur du projet : la fiche précise que les deux groupes
  de patients ne sont pas comparés l'un à l'autre, et que les prélèvements des témoins sont anciens.
  Le porteur du projet a aussi validé le niveau C de B018.

**Incident.** Les quinze contradicteurs écrivaient leurs fichiers de travail dans le même dossier temporaire.
Deux scripts du même nom se sont écrasés : le fichier de B002 n'était pas sur le disque alors que son auteur le disait écrit.
Il a été réécrit avec les mêmes faits et les mêmes arguments, une citation étant raccourcie ; le contrôle des citations
a été refait sur les quinze fichiers. Désormais chaque agent nomme ses fichiers de travail d'après sa piste.

**Réserve.** Le contradicteur est un programme du même type que le relecteur et le décideur, d'un modèle moins coûteux.
Une consigne d'attaque pousse à trouver : aucun avis n'est « tient ». Les constats qui ne changent ni statut ni niveau
reposent sur le contrôle mot pour mot de leur citation, pas sur une seconde lecture.

## 2026-11-22 — Quatre lettres envoyées pour les pistes promues

**Fait.** Sur instruction du porteur du projet, les quatre lettres sont parties de la boîte du projet,
une fois le travail fusionné : à l'auteur correspondant de l'étude de 2019 (P15), à l'équipe de DecodeME
et à l'auteur correspondant de l'étude de 23andMe (P16), à l'auteur correspondant de la prépublication
de randomisation mendélienne (P17). Chaque envoi est inscrit au journal des envois de sa piste.

**Choix.** Ne prendre les destinataires que dans des sources officielles : la copie de l'article à PubMed Central,
le fichier source de la prépublication par l'interface de medRxiv, la page d'accès de DecodeME,
le texte de la prépublication. Aucun nom et aucune adresse de destinataire n'entrent dans le dépôt.

**Contrôle.** Avant l'envoi : les trois liens des lettres répondent sur la branche principale ; les allèles
que les lettres disent absents des prépublications y ont été cherchés une dernière fois, sans résultat.

**Constat.** Une réponse automatique est arrivée de la boîte de DecodeME dans la minute : elle s'adresse d'abord
aux participants de l'étude et prévient qu'elle ne pourra pas répondre aux messages reçus. Sa page d'accès
prévoit un formulaire de demande pour les chercheurs. Les tests 2 et 3 de P16 pourraient ne jamais être lus
par cette voie.

**Réserve.** L'adresse de l'auteur de 2019 date de la publication. Aucun message d'erreur n'était revenu
au moment du relevé, fait dans les minutes qui ont suivi l'envoi.

## 2026-11-22 — Décisions du porteur du projet sur les pistes promues

**Décision.** Le résultat d'expression de 2019 n'est plus cité comme un appui de la piste P15.

**Motif.** L'écart vient de cinq bibliothèques de témoins sains chargées d'ARN ribosomique, et il n'est pas retrouvé
dans trois autres jeux de données. La règle déposée rendait « indécidable » et ne permettait pas ce retrait :
c'est une décision, notée comme telle en bas du plan et dans la fiche.

**Conséquence.** La piste P15 ne repose plus que sur les vésicules extracellulaires du COVID long,
un résultat d'une seule équipe sur un sous-groupe de patients. Elle reste au niveau C.

**Décision.** La piste P17 reste au registre, bien que son premier test ne soit pas faisable aujourd'hui.

**Écarté.** La renvoyer en banque, puisqu'elle avait été promue pour un test qui ne peut pas se faire.

**Décision.** Les quatre lettres partent une fois ce travail fusionné : leurs liens pointent vers la branche principale.

## 2026-11-22 — P15 : le signal de 2019 n'est pas retrouvé chez d'autres personnes

**Fait.** La section 6 du plan de P15 a été appliquée aux jeux de données publics retenus. Trois se lisent :
EM/SFC après une infection (12 patients, 15 témoins), COVID long dans les cellules mononucléées (11 et 12),
COVID long dans le sang total (18 et 20).

**Résultat.** Lecture fixée par le plan : signal non retrouvé chez d'autres personnes. L'écart d'expression
des deux gènes est de +0,01, de −0,19 et de +0,35 log2 ; la borne basse des trois intervalles reste au-dessus
de −1 log2. L'écart publié en 2019 était de −4,4 à −5,2 log2.

**Constat.** Quatre des sept jeux retenus ne se lisent pas : deux n'ont pas les deux gènes dans leurs fichiers,
deux n'ont déposé aucune estimation. L'indicateur technique ne se calcule dans aucun des trois jeux lus.

**Choix.** Fixer les listes de gènes de chaque jeu avant de lire les écarts, par une commande à part.

**Écarté.** Réaligner les lectures brutes des deux jeux sans estimation déposée, 223 bibliothèques :
le plan ne l'engage pas, et trois lectures concordantes suffisent à la règle.

**Réserve.** Aucun des trois jeux ne porte sur des monocytes isolés, ni sur la fatigue après fièvre Q.
Un écart plus petit que 1 log2 n'y est pas exclu.

**Suite.** La décision sur l'appui de 2019 revient au porteur du projet. Les trois éléments vont dans le même sens :
une règle qui rend « indécidable », une description qui montre cinq bibliothèques à part,
et trois autres jeux de données sans écart.

## 2026-11-22 — Premiers tests des pistes promues : P15 indécidable, le test 1 de P16 échoue

**Fait.** Les deux tests qui ne demandaient qu'un fichier public ont été lancés après le dépôt des plans.

**Résultat, P15.** Lecture fixée d'avance : indécidable. L'écart publié en 2019 se retrouve sur les 40 bibliothèques,
−3,1 et −2,6 log2. Mais il vient tout entier d'une des deux séries de bibliothèques ; dans l'autre,
il est de +0,6 et de +0,3 log2. La règle prévoyait ce cas et le lit « indécidable ».

**Constat après coup, P15.** Cinq bibliothèques de témoins sains, toutes dans la première série, ont de 0,5 à 7,6 %
de leurs lectures sur l'ARN ribosomique, mitochondrie et cytoplasme réunis. La médiane des 40 bibliothèques
est de 0,02 %. L'écart oppose ces cinq bibliothèques à toutes les autres, témoins infectés compris.
Ce constat n'était pas dans le plan : il vaut moins qu'un test.

**Résultat, P16.** Le test 1 échoue. Le variant le plus associé au COVID long, rs9273363, n'est pas associé
à l'EM/SFC dans DecodeME : rapport de cotes de 0,996 (de 0,970 à 1,023) pour l'allèle C, p = 0,79,
avec 98 % de puissance pour l'effet publié de 1,06. Les tests 2 à 4 ne sont pas lus.

**Choix.** Ne pas changer la règle de P15 après coup. Si l'étape de l'artefact avait été placée avant celle
des deux séries, la lecture aurait été « probablement artefactuel ». L'ordre a été fixé avant les données : il reste.
La fiche P15 reçoit une ligne ; son niveau ne change pas.

**Choix.** Écrire aux auteurs de l'étude de 2019 avant de conclure : eux seuls savent comment ces cinq bibliothèques
ont été préparées. La lettre est prête, non envoyée.

**Écarté.** Retirer de la fiche P15 l'appui de 2019 sur la foi de la description : la règle déposée
ne le permet pas, et la décision revient au porteur du projet.

**Réserve.** P15 : la réplication sur d'autres personnes, que le plan prévoit sur sept jeux de données,
n'est pas faite. P16 : un test lu sur quatre.

**Suite.** Trois décisions pour le porteur du projet : l'appui de 2019 pour P15, le maintien de P17 au registre,
l'envoi des quatre lettres. Puis la réplication de P15 sur les autres jeux de données.

## 2026-11-22 — Plans d'analyse des trois pistes promues ; le test de P17 n'est pas faisable

**Fait.** Un plan d'analyse est déposé pour P15, P16 et P17, avant l'ouverture de toute donnée d'expression
et de toute statistique résumée. Chacun rapporte comme des constats ce qui avait déjà été lu :
articles, fiches d'échantillons, annotation, notice des fichiers.

**Constat, P15.** Les trois gènes les plus abaissés de l'étude de 2019 sont des ARN ribosomiques
ou leur pseudogène, dans des bibliothèques dont on a retiré l'ARN ribosomique. Le plan oppose donc
une lecture technique à la lecture biologique, et fixe l'indicateur qui les départage :
les ARN 18S et 28S du cytoplasme.

**Constat, P17.** Le test promis à la promotion n'est pas faisable aujourd'hui. Aucun jeu de cas public
et indépendant ne dépasse 18 % de puissance ; il faudrait environ 16 400 cas. Le résultat d'origine
n'avait lui-même que 79 % de puissance pour son propre effet. Le plan fixe la règle pour le jour
où les données existeront. Le porteur du projet décide si la piste reste au registre.

**Choix.** Faire relire chaque plan avant son dépôt par un relecteur qui n'en est pas l'auteur,
avec une consigne publiée : `outils/consigne-relecteur-de-plan.md`. Les trois avis étaient « à corriger » :
31 remarques, dont des résultats que la règle ne classait pas, des bornes qui se chevauchaient
et un allèle d'effet non fixé. Les règles ont été réécrites avant le dépôt. Aucune donnée n'était ouverte.

**Choix, P15.** Le programme d'analyse est déposé avec le plan. Sa règle est éprouvée sur des données inventées
dans `verifier.py` : elle sait rendre « artefactuel », « non expliqué », « indécidable » et « illisible ».

**Écarté.**

- P15 : conclure à l'artefact sur l'écart de A corrigé de l'indicateur technique. La pente qui sert
  à corriger est sous-estimée quand l'indicateur est bruité : un artefact franc aurait été lu « indécidable ».
  L'écart corrigé est donné, et ne sert qu'à la lecture « non expliqué ».
- P16 : prévoir un variant de remplacement si rs9273363 manque au fichier public. Il faudrait savoir
  quel allèle du remplaçant voyage avec l'allèle C. Le test serait alors « non lu ».
- P17 : refaire l'analyse sur le COVID long, à 45 % de puissance, ou sur les deux jeux publics réunis, à 18 %.
  Un résultat nul n'y voudrait rien dire.

**Corrections.** Le premier relevé des séries de la base GEO n'en avait lu que 60 sur 76 ; les seize manquantes
contenaient deux jeux de données sur l'EM/SFC. « De vingt à trente-cinq fois » devient « de 21 à 37 fois »
dans la fiche P15 et dans la relecture de B011 : 2 puissance 5,2 vaut 37. Une source s'ajoute au registre
pour l'haplotype 8.1, cité par le plan de P16.

**Réserve.** Trois lettres sont prêtes, aucune n'est partie : elles attendent la relecture du porteur du projet.
L'auteur correspondant de l'étude de 23andMe reste à relever sur la page de la prépublication.
Les relecteurs des plans sont des programmes ; une personne du métier verrait autre chose.

**Suite.** Ouvrir les données de l'étude de 2019 et lire le fichier public de DecodeME, selon les plans.

## 2026-11-22 — Trois pistes promues au registre ; la recherche de PHOTOCOV est abandonnée

**Décision du porteur du projet.** Promouvoir au registre les trois pistes vérifiées dont le premier test
ne demande aucun laboratoire. Abandonner la recherche de l'étude PHOTOCOV, introuvable sous ce nom.

**Fait.** Trois pistes entrent au registre, au niveau C : P15, humanine et MOTS-c (B011) ; P16, région HLA
commune aux deux maladies (B013) ; P17, nombre de copies d'ADN mitochondrial (B020). Neuf sources les accompagnent.
Les entrées de la banque passent à « promue » et gardent leur relecture.

**Choix.** Écrire chaque piste à partir de la relecture, et non du texte déposé : P15 s'appuie d'abord
sur le résultat des vésicules extracellulaires, que le déposant n'avait pas trouvé.

**Réserve.** Aucune des trois n'a eu de contradicteur chargé de l'attaquer. P17 repose sur une prépublication
sans intervalle de confiance, et les mesures directes ne la confirment pas toutes : elle est promue
pour son test, pas pour sa solidité.

**Suite.** Un plan d'analyse se dépose avant toute donnée, comme pour les lots 1 et 2.

## 2026-11-22 — Relecture contradictoire : deux mises à l'écart sur cinq ne tiennent pas

**Fait.** Chacune des cinq pistes écartées a eu un contradicteur, chargé de la défendre contre son motif.
Un motif tient, quatre tiennent en partie. Les 74 faits contrôlés et les 36 arguments portent une citation ;
toutes sont retrouvées mot pour mot.

**Constat.** Quatre motifs sur cinq contenaient une phrase trop forte ou inexacte, écrite par le décideur
lui-même. « La source le contredit », pour l'orexine, généralisait un seul des deux modèles animaux.
« Pas retrouvé », pour la grossesse, valait pour une cohorte trop petite pour exclure l'effet.
« Probablement artefactuel », pour l'apnée du sommeil, ignorait qu'une autre équipe retrouve l'association.

**Décision.**

- Orexine (B003) : mise à l'écart levée. La piste est sans donnée chez les patients, pas contredite.
  Elle est gardée au niveau D, comme l'autre hypothèse théorique de la banque (B004).
- Apnée du sommeil (B016) : mise à l'écart levée. Elle reste « à vérifier », faute du texte de l'article.
- FOXP4 (B014), grossesse (B015), antibiotiques (B021) : mises à l'écart maintenues, motifs reformulés.

**Motif.** La même situation avait été jugée de deux façons. Pour l'hypermobilité, deux façons de mesurer
qui donnent le même sens levaient en partie le doute de la question 9. Pour l'apnée du sommeil, non.
La contradiction a fait voir l'écart.

**Choix.** Le motif d'origine reste dans chaque piste, à côté de l'avis du contradicteur :
une erreur du décideur se consigne comme une autre.

**Écarté.** Suivre l'avis du contradicteur sans le peser : il défend, il ne décide pas. Trois mises à l'écart
tiennent malgré ses objections.

**Réserve.** Seules les mises à l'écart ont été contredites. Les quinze pistes gardées n'ont pas eu
de contradicteur chargé de les attaquer.

## 2026-11-22 — Relevé des réponses ; l'étude PHOTOCOV reste introuvable

**Fait.** La boîte du projet a été relevée le soir même des envois. Une réponse automatique est arrivée,
pour outSMART-LC : réponses retardées par un déplacement. Aucune réponse sur le fond aux sept lettres
parties de cette boîte. La lettre à Bergen, envoyée par le porteur du projet, n'y apparaît pas :
ni son envoi ni une réponse n'ont pu être contrôlés.

**Constat.** Aucune étude nommée PHOTOCOV n'a été trouvée : ni dans ClinicalTrials.gov, ni dans le registre
européen des essais, ni dans Europe PMC, ni par une recherche sur le web, y compris sous d'autres orthographes.
Ce « non trouvé » repose sur quatre sources. Il ne dit pas que l'étude n'existe pas : il manque son nom complet,
son promoteur ou sa ville.

## 2026-11-22 — La fiche T03 était fausse : la metformine a été testée sur un COVID long installé

**Constat.** La remarque du statisticien est confirmée, et dépassée. L'essai REVIVE (NCT06128967) est terminé :
399 adultes fatigués depuis 90 jours à 24 mois, publié en mai 2026, rétracté puis republié en novembre 2026.
Son bras metformine a été arrêté pour futilité après un changement de dose ; son résultat est jugé non concluant.
Un second essai randomisé, coréen, donne 14 jours de metformine à 132 adultes : pas mieux que le placebo.

**Décision.** Corriger la fiche T03 dans son texte, avec la date et le renvoi à cette entrée : une fiche du registre
ne doit pas garder une phrase fausse. La leçon de la fiche tient : la fenêtre utile précède la maladie.

**Fait.** Dans le même essai, la fluvoxamine réduit la fatigue contre placebo. Le résultat touche l'hypothèse 2,
qui passe par la sérotonine : une ligne s'ajoute à son historique. Son statut ne change pas, parce que l'essai
ne mesure pas la sérotonine et ne sélectionne pas ses patients.

**Cause.** La fiche s'appuyait sur des synthèses de la prévention. Aucun registre d'essais n'avait été interrogé
sur le traitement d'un COVID long installé.

**Réserve.** Les deux essais sont lus par leur résumé. L'avis de rétractation n'a pas pu être lu : le site
de la revue refuse les programmes. La version republiée corrige au moins les fréquences d'événements indésirables.

## 2026-11-22 — Relecture de la banque : quatorze pistes vérifiées, cinq écartées, deux en attente

**Révisée** le soir même par l'entrée « Relecture contradictoire » : quinze vérifiées, trois écartées, trois en attente.

**Fait.** Les 21 pistes ont été relues contre leurs sources. Le compte rendu est dans
`analyses/banque/RELECTURE.md`, le détail dans le champ `relecture` de chaque piste.

**Constat.** Les chiffres recopiés étaient presque toujours exacts : 27 affirmations fausses sur 537.
Le point faible était ailleurs. Pour 16 pistes, le test « inexplorée » a fait remonter une étude que la fiche
ne citait pas ; pour sept, une phrase de la fiche était fausse. Sept niveaux de preuve baissent, un monte
(six après la relecture contradictoire).

**Choix de méthode.**

- Copier d'abord les sources en local, par les interfaces officielles de PubMed, PubMed Central, medRxiv
  et ClinicalTrials.gov : 150 sources, dont 74 en texte intégral. La relecture se fait ensuite sans requête.
- Un relecteur par piste, d'un modèle moins coûteux, avec une consigne publiée. Il rend une citation
  par affirmation ; un programme recherche chaque citation mot pour mot. Toutes sont retrouvées.
- Le modèle principal décide, après avoir vérifié lui-même les constats qui changent un statut.
- Le texte déposé n'est pas réécrit : la relecture s'ajoute, et prime.
- « Vérifiée » exige que la source qui porte le signal soit lue en entier. Deux pistes restent donc
  « à vérifier » : leurs études ne sont accessibles que par leur résumé.

**Décision d'interprétation.** Les questions 5, 8 et 9 de la grille classent un signal comme probablement
artefactuel. Elles sont écrites pour l'épidémiologie. Pour une étude de laboratoire, elles n'ont été retenues
que dans leur sens strict. Appliquées à la lettre, elles auraient écarté presque toute la banque.

**Écarté.**

- Laisser chaque relecteur ouvrir les pages en ligne : plus de requêtes, et des citations impossibles à contrôler.
- Réécrire les fiches : on perdrait ce qui avait été déposé, avec le risque d'ajouter des erreurs.
- Contourner les contrôles anti-robot avec un navigateur piloté : un site qui refuse les programmes a décidé
  de les refuser. Les pages bloquées sont notées bloquées.
- Garder un niveau relevé pour B004 sur la foi d'un résumé de 2003 : la règle vaut aussi dans ce sens.

**Réserve.** Relecteur et déposant sont des programmes du même type, et un seul décideur a tranché.
Ce n'est pas une relecture par des pairs. Une relecture contradictoire des cinq mises à l'écart reste à faire.

## 2026-11-22 — Compte rendu du chercheur en biologie : ce qu'il a écarté

**Fait, corrigé le jour même.** L'agent a encore modifié son fichier après la première intégration.
La banque reprend ici sa version finale : douze pistes, 88 sources. La phrase d'origine disait
à tort que la première version était la finale ; elle avait été écrite avant la comparaison.

**Écarté par l'agent, d'après son compte rendu.** GDF15, pour des résultats contraires ;
les rétrovirus endogènes, pour un essai négatif ; le système glymphatique, déjà exploré.
Non retenus : alpha-tryptasémie, cGAS-STING, horloge circadienne. Ces motifs ne sont pas
sourcés dans le dépôt : ils évitent de refaire la recherche, ils ne prouvent rien.

**Non couvert.** Ferroptose, acides biliaires, hypoxie et HIF, tissu conjonctif.

**Limites déclarées.** PubMed et PubMed Central inaccessibles : résumés lus par un autre site,
un seul texte intégral. Un seul registre d'essais consulté. Recherche ciblée, non systématique.

## 2026-11-22 — Premier dépôt en banque : 21 pistes, aucune relue

**Fait.** Les deux agents ont déposé : douze pistes de biologie (B001 à B012), neuf signaux
statistiques (B013 à B021). Le contrôle à l'intégration est formel : champs présents,
chaque source avec son adresse et son mode de lecture. Aucune source n'a été rouverte.
Toutes les pistes sont « à vérifier ».

**Fait.** Le statisticien a rédigé la grille de relecture (`outils/grille-statistique.md`)
et ses calculs d'effectifs (`analyses/banque/`). Il n'a pas encore relu les pistes de biologie.

**Remarque à vérifier.** Selon le statisticien, l'essai REVIVE teste la metformine sur un COVID
long installé, ce que la fiche T03 ne dit pas.

**Décision du porteur du projet.** Dépenser moins : la bibliothèque #ApresJ20 est copiée une fois,
lentement, par un script ; les recherches se font ensuite sur la copie, sans requête.
Les lectures en nombre iront à un modèle moins coûteux.

**Choix.** Un fichier `REPRISE.md` dit où en est le projet, pour repartir dans une nouvelle
session sans dépendre du fil de la conversation.

**Écarté.** Verser la copie de la bibliothèque au dépôt : c'est le travail de l'association,
on le consulte, on ne le republie pas.

## 2026-11-22 — Deux ressources signalées par le porteur du projet

**Fait.** La bibliothèque Zotero de l'association #ApresJ20 est inscrite aux sources :
douze collections, tenue à jour. Elle servira à tester l'affirmation « inexplorée »
des entrées de la banque.

**Fait.** Les résumés du symposium ANRS MIE du 2026-11-12 sont lus. Deux résultats
préliminaires sont consignés : pas d'excès global d'auto-anticorps dans l'étude CLIIM (H1),
virus infectieux porté par des plaquettes dans une étude de l'Institut Cochin (H4).
Aucun statut ne change.

**Règle rappelée.** Le dépôt est public. Un résultat confié sous embargo n'y entre pas.

## 2026-11-22 — Une banque d'hypothèses à vérifier, alimentée par deux agents

**Décision du porteur du projet.** Envoyer deux agents de recherche sillonner la littérature :
un chercheur en biologie et un statisticien en appui. Ils alimentent une banque d'hypothèses
à vérifier. Le porteur du projet autorise aussi la fusion automatique des demandes de fusion.

**Choix.** La banque est un seul fichier, `registre/banque.yaml`, séparé du registre.
Une entrée y reste « à vérifier » tant que ses sources n'ont pas été rouvertes par quelqu'un
d'autre que le déposant. Les agents écrivent hors du dépôt ; l'intégration est faite à part.

**Écarté.** Un fichier par entrée : plus lourd à relire pour des fiches courtes.
Des tickets GitHub : hors du dépôt, donc hors du contrôle automatique.
Laisser les agents écrire dans le registre : une piste non relue y passerait pour un résultat.

## 2026-11-22 — Lot 1 : les deux demandes sont parties

**Fait.** Les deux demandes de chiffres agrégés sont envoyées, après relecture du porteur
du projet. Huit demandes sont parties au total, aucune réponse n'est arrivée.

**Écart.** La seconde lettre a été adressée aux auteurs correspondants de l'article,
et non aux deux noms relus : seule la formule d'appel a changé.

**Constat.** La cohorte de la signature interféron compte 55 patients. Le seuil de 20 porteurs
d'antigène risque de ne pas être atteint : le croisement serait non informatif. Le seuil,
fixé avant les données, n'est pas abaissé.

## 2026-11-22 — Lot 1 instruit ; lot 2 complété

**Fait, lot 2.** La sixième demande est partie, au contact central de l'essai Brave-LC.
Les demi-vies sont relevées, deux sources chacune. Le repère d'arrêt est toujours atteint
bien avant les visites prévues.

**Constat, lot 2.** Le retrait randomisé de la rapamycine dure 60 jours, soit 43 jours après
le repère. La règle exige trois mois : ce retrait restera descriptif. La règle n'est pas
assouplie pour l'accueillir.

**Constat, lot 1.** Aucune des quatre paires n'a de mesure conjointe publiée. Le registre
désignait les prélèvements de RECOVER-VITAL ; la voie ouverte aux équipes extérieures porte
sur les cohortes, pas sur les essais. Les fiches sont corrigées.

**Choix.** Scinder le lot : 1a croise des données déjà mesurées, par deux demandes de chiffres
agrégés ; 1b exige des dosages, donc une équipe habilitée que le projet n'a pas.

**Réserve.** Un résultat publié a été lu avant l'écriture du plan : dans la cohorte LIINC,
l'antigène n'est pas plus fréquent chez les femmes. Il est consigné comme constat, pas comme
test. La règle de décision ne vaut que pour les données non encore vues.

**Écarté.** Envoyer les deux demandes du lot 1 sans relecture du porteur du projet.

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
