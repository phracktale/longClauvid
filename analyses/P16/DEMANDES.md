# Piste P16 : les demandes aux équipes

État au 2026-11-22 : **deux lettres envoyées.** Elles sont parties de la boîte du projet,
sur instruction du porteur du projet, une fois le travail fusionné. Aucune adresse électronique n'est reprise ici.

| Destinataire | Ce qui est demandé | Test du plan | État |
| --- | --- | --- | --- |
| Équipe de DecodeME, université d'Édimbourg | Les résultats de DRB1*11:04 et de DQA1*03:01 dans l'étude de l'EM/SFC, par copie de l'allèle | 2 et 3 | Envoyée le 2026-11-22 |
| Auteur correspondant de l'étude de 23andMe | Le résultat de DQA1*05:01 dans l'étude du COVID long, par copie de l'allèle | 4 | Envoyée le 2026-11-22 |

Le test 1 ne demande rien : il se lit dans le fichier public de DecodeME. Voir [PLAN.md](PLAN.md).

L'adresse de l'équipe de DecodeME est publiée par sa [page d'accès](https://institute-genetics-cancer.ed.ac.uk/decodeme-the-worlds-largest-mecfs-study/researcher-access).
Cette page prévoit, pour les chercheurs, un formulaire de demande d'accès : c'est peut-être la seule voie
qui obtienne une réponse.
Pour 23andMe, l'auteur correspondant et son adresse ont été relevés dans le fichier source de la
[prépublication](https://www.medrxiv.org/content/10.1101/2024.10.07.24315052v1), par l'interface de medRxiv.
La lettre est partie telle qu'elle est écrite ici, avec son nom à la place de « [corresponding author] ».

## Lettre à l'équipe de DecodeME

Objet : Two HLA allele results from the DecodeME GWAS: DRB1*11:04 and DQA1*03:01

```text
Dear DecodeME team,

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One entry asks whether the two illnesses share an HLA allele. The 23andMe long COVID GWAS reports HLA-DRB1*11:04 (OR 1.18) and HLA-DQA1*03:01 (OR 0.95); your preprint reports HLA-DQA1*05:01. I could not find the first two alleles in your preprint, and the public summary statistics are variant-level.

My question: could you share, or point me to, the association results for HLA-DRB1*11:04 and HLA-DQA1*03:01 in DecodeME: allele frequency in cases and in controls, per-allele (additive) odds ratio and two-sided p value? If you have re-run the HLA analysis with alleles imputed jointly for cases and controls, as your preprint announces, those are the results to use. If one of the two alleles was below your 1% frequency filter and was not tested, that is a useful answer too.

I am not asking for participant-level data. The analysis plan, with the decision rule written before seeing these numbers, is public (in French): https://github.com/phracktale/longClauvid/blob/main/analyses/P16/PLAN.md

If this is already published, a pointer to it would fully answer my question.

Thank you for your work on this illness.

[name]
```

## Lettre à l'auteur correspondant de l'étude de 23andMe

Objet : One HLA allele in your long COVID GWAS: DQA1*05:01

```text
Dear Dr [corresponding author],

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One entry asks whether the two illnesses share an HLA allele. Your preprint reports HLA-DRB1*11:04, C*07:01, B*08:01 and DQA1*03:01 for long COVID. The DecodeME study of ME/CFS reports HLA-DQA1*05:01, less frequent in cases (21.7% versus 23.2%). I could not find DQA1*05:01 in your preprint.

My question: could you share, or point me to, the association result for HLA-DQA1*05:01 in your long COVID GWAS: allele frequency in cases and in controls, per-allele (additive) odds ratio and two-sided p value, in the multi-ancestry meta-analysis and, if available, in participants of European ancestry?

I am not asking for participant-level data, and I understand that the full summary statistics are shared under agreement. One number would be enough. The analysis plan, with the decision rule written before seeing it, is public (in French): https://github.com/phracktale/longClauvid/blob/main/analyses/P16/PLAN.md

If this is already published, a pointer to it would fully answer my question.

Thank you for your work on this illness.

[name]
```

## Journal des envois

Une ligne par envoi ou par réponse : date, destinataire, ce qui a été répondu.

| Date | Destinataire | Événement |
| --- | --- | --- |
| 2026-11-22 | Les deux destinataires | Lettres rédigées, en attente de relecture |
| 2026-11-22 | Équipe de DecodeME | Lettre envoyée, à l'adresse de contact de sa page d'accès |
| 2026-11-22 | Auteur correspondant de l'étude de 23andMe | Lettre envoyée, à l'adresse que publie la prépublication |
| 2026-11-22 | Équipe de DecodeME | Réponse automatique, dans la minute : la boîte s'adresse d'abord aux participants et prévient qu'elle ne pourra pas répondre aux messages reçus. Rien sur le fond |
| 2026-11-23 | Équipe de DecodeME | Voie de la demande d'accès lue et écartée : voir ci-dessous |
| 2026-11-23 | Auteur correspondant de la prépublication de DecodeME | Même lettre envoyée, sur instruction du porteur du projet. Un paragraphe d'ouverture dit que la boîte générale ne répond pas et que la procédure d'accès vise des données individuelles. L'adresse vient du fichier source de la prépublication, par l'interface de medRxiv ; des trois auteurs correspondants, c'est celui de l'université |

## La demande d'accès de DecodeME n'est pas ouverte au projet

Lu le 2026-11-23 sur la [page d'accès](https://institute-genetics-cancer.ed.ac.uk/decodeme-the-worlds-largest-mecfs-study/researcher-access/data-access-policy-and-application-form) :
ce n'est pas un formulaire en ligne. C'est un document à remplir et à envoyer par courriel à un comité d'accès,
avec une politique d'accès en huit points (version 3).

- Le demandeur doit être employé par un établissement scientifique, universitaire ou commercial, dont le service
  juridique peut signer un contrat de transfert de données avec l'université d'Édimbourg. Un demandeur qui ne remplit pas
  cette condition est écarté sans que son projet soit lu.
- Le dossier demande un curriculum vitæ et des publications, un projet de deux pages, un plan d'analyse,
  un financement, un avis éthique et un plan d'association des patients.
- Il vise les données individuelles et les échantillons. Le formulaire rappelle que les statistiques résumées
  sont en accès libre : c'est le fichier déjà lu pour le test 1, qui donne les variants un par un, pas les allèles HLA.

Le porteur du projet, développeur indépendant, ne remplit pas la première condition. Les tests 2 et 3 ne demandent
d'ailleurs qu'un chiffre par allèle, pas des données individuelles : cette voie n'est pas faite pour eux.

Ce qui reste possible :

1. Écrire à l'auteur correspondant de la prépublication de DecodeME, et non à la boîte générale. Même lettre. Fait le 2026-11-23.
2. Attendre l'analyse HLA que les auteurs disent vouloir refaire, avec un typage imputé pour les cas et les témoins ensemble.
3. Passer par une personne employée d'un établissement de recherche, qui ferait la demande en son nom.

