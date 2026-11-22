# Lot 1 : que disent les échantillons déjà collectés ?

Plan d'analyse déposé le 2026-11-22. La date du commit fait foi. Toute modification ultérieure
s'écrit en bas de ce fichier, avec sa date et son motif.

**Vérification faite, aucune des quatre paires n'a de mesure conjointe publiée. Deux peuvent
avancer sans nouveau dosage, en croisant des données déjà mesurées. Les deux autres exigent
un laboratoire, donc une équipe partenaire.**

> Ce plan ne produit aucun avis médical. Il dit quelles données demander,
> et comment les lire une fois reçues.

> Un résultat publié a été lu avant l'écriture de ce plan. Il est rapporté en section 2
> comme un constat, pas comme un test. La règle de la section 5 ne vaut que pour
> les données qui n'ont pas encore été vues.

## 1. Les quatre questions

| Paire | Question | Mesures à croiser sur les mêmes personnes |
| --- | --- | --- |
| H4 et H5 | La surreprésentation des femmes tient-elle à l'antigène ou aux hormones ? | Antigène plasmatique, sexe, statut hormonal |
| H2 et H4 | Le signal interféron s'entretient-il seul ? | Signature interféron, antigène plasmatique |
| H1 et H4 | Le complément est-il activé par des anticorps ou par un antigène ? | Complément terminal, antigène plasmatique, fixation des IgG |
| H1 et H2 | Anticorps ou interféron : lequel désigne le bon traitement ? | Fixation des IgG, signature interféron, réponse au traitement |

## 2. Ce que la vérification a montré

| Paire | Ce qui existe | Ce qui manque |
| --- | --- | --- |
| H4 et H5 | L'antigène par sexe dans une cohorte de 171 personnes ; l'antigène chez 706 personnes, analysé avec un ajustement sur le sexe | La fréquence par sexe chez les 706 ; le statut hormonal |
| H2 et H4 | Des sous-groupes à signature interféron dans une cohorte ; l'antigène chez 706 personnes ; plusieurs auteurs communs aux deux études | Savoir si des participants sont communs, puis le tableau croisé |
| H1 et H4 | Le complément dosé dans deux cohortes, à Zurich et à Cardiff ; l'antigène dosé dans d'autres | Les deux dosages sur les mêmes plasmas |
| H1 et H2 | Plasma et cellules sanguines conservés par l'essai REVERSE-LC | Une biobanque confirmée côté daratumumab ; la mesure de la fixation des IgG |

Sources : [cohorte de 171 personnes](https://medrxiv.org/content/10.1101/2023.10.24.23297114.full.pdf),
[étude des 706](https://pure.psu.edu/en/publications/measurement-of-circulating-viral-antigens-post-sars-cov-2-infecti/),
[signature interféron](https://pmc.ncbi.nlm.nih.gov/articles/PMC10252177),
[complément à Zurich](https://pubmed.ncbi.nlm.nih.gov/38236961/),
[complément à Cardiff](https://www.medrxiv.org/content/10.1101/2023.10.26.23297597v1.full),
[REVERSE-LC](https://www.sctweb.org/presentations/2026/INVITED_SESSION_16_Jason_Liang.pdf),
[pilote du daratumumab](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1607353/full).

### Le constat déjà publié

Dans la cohorte LIINC, l'antigène n'est pas plus fréquent chez les femmes. Le rapport
de prévalence des hommes aux femmes est de 1,68, avec un intervalle de confiance à 95 %
de 0,93 à 3,04. Sur 171 personnes, 42 portaient un antigène détectable.

Ce constat va contre la prédiction tirée de H4 pour le biais féminin. Il ne soutient pas H5
pour autant : le statut hormonal n'y est pas rapporté.

### Les portes d'accès

| Collection | Contenu | Accès |
| --- | --- | --- |
| RECOVER, cohortes adulte, pédiatrique et autopsique | Plus de 1,4 million d'échantillons : sang, salive, urine, tissus | Proposition d'étude annexe, examinée chaque mois par un comité ; un financement indépendant est attendu |
| RECOVER, données agrégées | Les trois cohortes | Portail public, sans compte |
| LIINC, université de Californie à San Francisco | 50 000 échantillons : plasma, sérum, cellules sanguines | Collaboration avec l'équipe, qui affiche une politique de partage large |
| Essai REVERSE-LC | Plasma, cellules sanguines, liquide céphalorachidien, à plusieurs dates | Fermé jusqu'à la fin de l'essai |

Sources : [études annexes de RECOVER](https://recovercovid.org/ancillary),
[biobanque de RECOVER](https://recovercovid.org/news/over-14-million-biosamples-available-recovers-biorepository-support-long-covid-research),
[LIINC, politique de partage](https://polybio.org/projects/support-of-the-long-term-impact-of-infection-with-novel-coronavirus-liinc-program-a-clinical-core-to-facilitate-long-covid-collaborative-research/),
[LIINC, taille de la biobanque](https://cdn.clinicaltrials.gov/large-docs/88/NCT06161688/Prot_SAP_000.pdf).

Conséquence pour le registre : il désignait les prélèvements de l'essai RECOVER-VITAL.
La page des études annexes ne cite que les trois cohortes, pas les essais. Les fiches sont corrigées.

## 3. Deux sous-lots

| Sous-lot | Paires | Ce qu'il demande | Qui peut le faire |
| --- | --- | --- | --- |
| 1a, sans nouveau dosage | H4 et H5, H2 et H4 | Deux tableaux de chiffres agrégés, tirés de données déjà mesurées | Les auteurs des études, sur simple demande |
| 1b, avec dosage | H1 et H4, H1 et H2 | Le complément terminal sur des plasmas déjà typés pour l'antigène ; la fixation des IgG | Une équipe habilitée, par une étude annexe ou une collaboration |

Ce projet n'a ni laboratoire ni habilitation. Il peut instruire le sous-lot 1a et rédiger
la question du sous-lot 1b ; il ne peut pas le conduire.

## 4. Les données demandées pour le sous-lot 1a

Des chiffres agrégés suffisent. Aucune donnée individuelle n'est demandée.

1. Dans l'étude des 706 personnes : par sexe, le nombre de personnes testées
   et le nombre de porteurs d'antigène. Par statut hormonal aussi, s'il a été relevé.
2. Si des participants sont communs aux deux études : un tableau à deux entrées,
   sous-groupe inflammatoire (interféron de type I, de type II, aucun) et antigène détecté ou non.

## 5. La règle de décision, fixée avant ces données

| Paire | Situation | Lecture |
| --- | --- | --- |
| H4 et H5 | Antigène plus fréquent chez les femmes : rapport de prévalence dont l'intervalle de confiance à 95 % exclut 1 | La prédiction de H4 est vérifiée dans cette étude |
| H4 et H5 | Intervalle qui inclut 1, ou antigène plus fréquent chez les hommes | La prédiction de H4 n'est pas vérifiée ; H5 reste sans test, faute de statut hormonal |
| H2 et H4 | Signature interféron aussi fréquente sans antigène : différence dont l'intervalle inclut 0 | La prédiction de H2 est vérifiée : le signal existe sans antigène détectable |
| H2 et H4 | Signature concentrée chez les porteurs d'antigène : rapport de prévalence dont l'intervalle exclut 1 | La prédiction de H4 est vérifiée |
| Les deux | Moins de 20 porteurs d'antigène dans le tableau | Non informatif |

Pour les statuts du registre : ces données sont observationnelles et prises à une seule date.
Elles sont de niveau C et ne changent aucun statut. Une prédiction non vérifiée dans deux cohortes
indépendantes est inscrite comme telle dans la fiche de l'hypothèse.

## 6. Limites connues d'avance

- Le constat sur le sexe a été lu avant l'écriture du plan.
- Le dosage de l'antigène a des faux positifs : 5 témoins sur 250 prélevés avant la pandémie étaient positifs.
- Le sexe n'est pas le statut hormonal. Aucune des études lues ne rapporte ce dernier.
- Le recoupement des participants entre les deux études est une supposition, tirée des listes d'auteurs.
- Deux articles n'ont été lus que par extraits : l'étude des 706 et celle de la signature interféron.
- Une absence de détection de l'antigène dans le sang ne dit rien de sa présence dans les tissus.

## Modifications

### 2026-11-22, après l'envoi des demandes : une précision sur la paire H2 et H4

La première page de l'article sur la signature interféron a pu être lue. La cohorte compte
55 patients, recrutés dans une étude de Seattle. Aucune donnée n'a été reçue.

Conséquence : le seuil de 20 porteurs d'antigène de la section 5 risque de ne pas être atteint.
Le croisement serait alors non informatif. Le seuil n'est pas abaissé pour l'accueillir.

Source : [article](https://www.nature.com/articles/s41467-023-38682-4.pdf).
