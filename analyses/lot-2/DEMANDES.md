# Lot 2 : les demandes aux équipes

État au 2026-11-22 au soir : **les six demandes sont parties ; une réponse automatique, aucune réponse sur le fond.**
Les lettres partent au nom du porteur du projet, qui les relit avant l'envoi.
Leur texte est dans [LETTRES.md](LETTRES.md), sans signature ni adresse.

Les adresses ne sont pas recopiées ici : la section « Destinataires » renvoie aux pages qui les publient.

| Destinataire | Essai | Ce qui est demandé | État |
| --- | --- | --- | --- |
| Équipe de l'hôpital universitaire Haukeland, Bergen | Pilote du daratumumab et ResetME | La fixation des IgG aux neurones sensitifs peut-elle être mesurée sur les sérums du suivi (15 à 21 mois) ? ResetME publiera-t-il la réponse par bras jusqu'à la 72e semaine ? | Envoyée (déclaré le 2026-11-22) |
| Équipe de REVERSE-LC, université Vanderbilt | Baricitinib | Les résultats de la visite à 12 mois, six mois après l'arrêt, seront-ils publiés par bras ? Une signature interféron est-elle mesurée ? | Envoyée le 2026-11-22 |
| Équipe d'outSMART-LC, université de Californie à San Francisco | AER002 | L'antigène plasmatique a-t-il été dosé avant et après la perfusion ? Que deviennent, sur un an, les patients devenus négatifs ? | Envoyée le 2026-11-22 |
| Auteurs de l'étude sur la rapamycine | Étude ouverte, puis essai avec retrait randomisé | Le retrait randomisé est-il en cours, et ses résultats seront-ils publiés par bras ? Que deviennent les patients qui ont arrêté ? | Envoyée le 2026-11-22 |
| Équipe de Brave-LC | Naltrexone | Une évaluation est-elle prévue après les 16 semaines ? Sinon, peut-elle être ajoutée ? | Envoyée le 2026-11-22 ; réponse le 2026-11-23 : oui, une visite est prévue vers le jour 180 |
| Auteurs de Craddock et al. 2015 | Modèle logique | Le code de simulation, pour retrouver les taux publiés (voir `simulateurs/niveau2/RESULTATS_RESEAU_LOGIQUE.md`) | Envoyée le 2026-11-22 |

L'ordre conseillé est celui du tableau : la première demande porte sur des sérums déjà
conservés et un essai en cours, c'est celle qui peut répondre le plus tôt.

## Destinataires

Recherche du 2026-11-22. Une adresse publiée dans un article peut être périmée :
celle de Craddock, imprimée en 2015, est celle de son ancien poste.

| Demande | Destinataire | Page qui publie l'adresse |
| --- | --- | --- |
| Daratumumab | Øystein Fluge, hôpital universitaire Haukeland | [Article du pilote](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1607353/full), ligne « Correspondence » |
| REVERSE-LC | E. Wesley Ely, investigateur principal, université Vanderbilt | [Fiche de l'université](https://wag.app.vanderbilt.edu/PublicPage/Faculty/Details/29490) |
| outSMART-LC | Michael J. Peluso, investigateur principal, université de Californie à San Francisco | [Article de 2021](https://escholarship.org/uc/item/0qt7x5rj), ligne « Correspondence » |
| Rapamycine | David Kaufman, Avik Roy et C. Gunnar Gottschalk, auteurs correspondants | [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12538759/) |
| Brave-LC | Contact central de l'essai | [Fiche du registre](https://clinicaltrials.gov/study/NCT07916259) |
| Craddock 2015 | Travis Craddock, aujourd'hui à l'université de Waterloo | [Annuaire de l'université](https://uwaterloo.ca/biology/contacts/travis-craddock) |

## Lettre type

À adapter à chaque destinataire : la question précise est dans le tableau.

> Subject: A question on off-treatment follow-up in [trial name]
>
> Dear Dr [name],
>
> I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID
> and ME/CFS (https://github.com/phracktale/longClauvid). I am not a clinician or an academic
> researcher, and part of the registry was drafted with an AI assistant; every claim in it
> links to its source.
>
> One hypothesis in the registry is that the illness is an alternative stable state:
> responders should stay improved after the drug is gone. Your trial is one of the few
> that can test this. My question:
>
> [the specific question from the table]
>
> Aggregate numbers would be enough: responders per arm at end of treatment, and how many
> still respond 3, 6 and 12 months later. The analysis plan, written before any data,
> is public: https://github.com/phracktale/longClauvid/blob/main/analyses/lot-2/PLAN.md
>
> If this is already planned or published, a pointer to it would fully answer my question.
>
> Thank you for your work on this illness.
>
> [name]

## Journal des envois

Une ligne par envoi ou par réponse : date, destinataire, ce qui a été répondu.
Une absence de réponse après deux mois se consigne aussi : à partir du 2027-01-22
pour les envois ci-dessous.

| Date | Destinataire | Événement |
| --- | --- | --- |
| 2026-11-22 | Øystein Fluge, daratumumab | Envoi déclaré par le porteur du projet |
| 2026-11-22 | E. Wesley Ely, REVERSE-LC | Lettre envoyée |
| 2026-11-22 | Michael J. Peluso, outSMART-LC | Lettre envoyée |
| 2026-11-22 | David Kaufman, Avik Roy et C. Gunnar Gottschalk, rapamycine | Lettre envoyée |
| 2026-11-22 | Travis Craddock, modèle logique | Lettre envoyée à son adresse actuelle |
| 2026-11-22 | Équipe de Brave-LC | Lettre envoyée au contact central de l'essai, relevé sur sa fiche de registre |
| 2026-11-23 | Équipe de Brave-LC | Réponse sur le fond, lue avec l'accord du porteur du projet : le traitement s'arrête à la visite 7, vers le jour 112 ; une visite 8, vers le jour 180, mesure la persistance de l'effet après l'arrêt. Le protocole complet doit être déposé au registre. Détail : bas de `PLAN.md` |
| 2026-11-23 | Travis Craddock, modèle logique | Réponse sur le fond, lue avec l'accord du porteur du projet : le code n'est plus disponible ; les traitements de 2015 sont appliqués à un seul instant puis relâchés ; un cran ou deux, les deux définitions existent. Détail : `simulateurs/niveau2/RESULTATS_RESEAU_LOGIQUE.md`, section 4 bis |
| 2026-11-22 | Michael J. Peluso, outSMART-LC | Réponse automatique : réponses retardées par un déplacement. Rien sur le fond |
| 2026-11-22 | Relevé de la boîte du projet | Aucune autre réponse. La lettre à Bergen, envoyée par le porteur du projet, n'apparaît pas dans cette boîte : ni son envoi ni une réponse n'ont pu y être contrôlés |
