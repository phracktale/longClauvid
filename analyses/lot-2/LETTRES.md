# Lot 2 : les lettres

Textes du 2026-11-22, tels quels. La signature est remplacée par « [name] »
et aucune adresse électronique n'est reprise.
La formulation d'une demande peut orienter la réponse : elle fait partie du dossier.

| Lettre | État |
| --- | --- |
| REVERSE-LC, outSMART-LC, rapamycine, modèle logique | Envoyées le 2026-11-22 |
| Brave-LC | Prête, non envoyée : aucun contact trouvé |
| Bergen, daratumumab | Envoyée par le porteur du projet, dans la version ci-dessous |

## Daratumumab : Øystein Fluge

Texte proposé au porteur du projet, qui l'a envoyé lui-même ; il a pu le retoucher avant l'envoi.

Objet : Off-treatment follow-up in the daratumumab pilot and ResetME: two questions

```text
Dear Dr Fluge,

I maintain longClauvid, an open registry of hypotheses on ME/CFS and long COVID in which every claim links to its source (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant.

One hypothesis in the registry is that the illness is an alternative stable state: responders should stay improved after the treatment effect has worn off. Your pilot is the only published study I found that follows responders long enough to test this: five of six stayed improved for 12 to 24 months while serum IgG rose again.

The long-lived plasma cell explanation predicts the same result, so I have two questions.

1. Could IgG binding to sensory neurons, or another functional readout of pathogenic IgG, be measured in the stored follow-up sera (15 to 21 months)? Binding back with patients still well would favour a state change. Binding still absent would favour the plasma cell explanation.

2. Will ResetME report response by arm up to week 72? Aggregate numbers would be enough: responders per arm at the end of treatment, and how many still respond once IgG has returned to baseline.

The analysis plan, written before any data, is public:
https://github.com/phracktale/longClauvid/blob/main/analyses/lot-2/PLAN.md

If any of this is already planned or published, a pointer would fully answer my question.

Thank you for your work on this illness.

[name]
```

## REVERSE-LC : E. Wesley Ely

Objet : REVERSE-LC: will the 12-month visit be reported by arm?

```text
Dear Dr Ely,

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One hypothesis in the registry is that the illness is an alternative stable state. If so, responders should stay improved after the drug is gone. REVERSE-LC is one of the few trials that can test this: the project page describes visits at enrollment, 6 months and 12 months, the last one six months after the end of treatment.

I have two questions about what is planned, not about unblinded data:

1. Will the 12-month results be reported by arm, including how many 6-month responders are still responders at 12 months?
2. Is an interferon or inflammatory signature measured at baseline, so that a durable response can be related to it?

The analysis plan, written before any data, is public (in French): https://github.com/phracktale/longClauvid/blob/main/analyses/lot-2/PLAN.md

If this is already in the protocol or the statistical analysis plan, a pointer to it would fully answer my question.

Thank you for running this trial.

[name]
```

## outSMART-LC : Michael J. Peluso

Objet : outSMART-LC (AER002): plasma antigen over the one-year follow-up

```text
Dear Dr Peluso,

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

Two hypotheses in the registry make different predictions about outSMART-LC. If persistent antigen drives the illness, symptoms should follow antigen. If the illness is an alternative stable state, clearing antigen may not be enough. A single infusion followed for up to one year is a rare opportunity to tell them apart, whatever the primary result.

My questions:

1. Was SARS-CoV-2 antigen measured in plasma before and after the infusion?
2. If so, could aggregate counts be published or shared: per arm, how many participants were antigen-positive at baseline, how many became negative, and how the symptoms of those participants evolved up to one year?

Aggregate numbers are enough; I am not asking for participant-level data. The analysis plan, written before any data, is public (in French): https://github.com/phracktale/longClauvid/blob/main/analyses/lot-2/PLAN.md

If this is already published or planned, a pointer to it would fully answer my question.

Thank you for your work on this illness.

[name]
```

## Rapamycine : David Kaufman, Avik Roy et C. Gunnar Gottschalk

Objet : Rapamycin in ME/CFS: the randomized withdrawal phase

```text
Dear David Kaufman, Avik Roy and Gunnar Gottschalk,

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One hypothesis in the registry is that the illness is an alternative stable state. If so, responders should stay improved after the drug is gone. Your article describes the design that tests exactly this: after 90 days of rapamycin, participants are randomized to continue the drug or to receive placebo for 60 days.

My questions:

1. Is this withdrawal phase part of NCT06257420, and is it under way?
2. Will its results be reported by arm: among responders at day 90, how many are still responders 60 days later on placebo and on rapamycin?
3. In the published study, do you know what happened to the participants who stopped rapamycin, in particular whether those who had improved kept their improvement?

Aggregate numbers are enough. The analysis plan, written before any data, is public (in French): https://github.com/phracktale/longClauvid/blob/main/analyses/lot-2/PLAN.md

If this is already planned or published, a pointer to it would fully answer my question.

Thank you for your work on this illness.

[name]
```

## Modèle logique : Travis Craddock

Objet : Reproducing Craddock et al. 2015 (PLoS ONE): treatment rule and code

```text
Dear Dr Craddock,

I maintain longClauvid, an open registry of hypotheses on long COVID and ME/CFS. I am an independent software developer, not a researcher, and part of the work was drafted with an AI assistant.

I reimplemented the 14-node male HPA-HPG-immune network of your 2015 PLoS ONE paper on remission in Gulf War Illness. The code and the results (in French) are here: https://github.com/phracktale/longClauvid/tree/main/simulateurs/niveau2

What reproduces:
- exactly the five published stable states, out of 4,782,969;
- the qualitative conclusions: no single target returns the system to health; lowering Th1 cytokines and then GR does, in 25% of 10,000 runs; the reverse order never does.

What does not: the success rates of Figures 5 and 6. With a one-level shift per intervention my rates are lower. With a two-level shift, 8 of the 12 rows of Figure 5 match within 2 points, and Figure 6 falls between the two readings.

One more observation: the network figure differs between the 2014 and 2015 papers at the T1Cell node. In 2014 cortisol inhibits it and Th1 cytokines do not activate it. Only the 2015 version gives the published illness state.

Three questions:

1. Does an intervention shift a node by one level, or set it to -1 or +1? Is it held while the network settles, or released at once?
2. Is the simulation code available?
3. Has NCT04254627 (etanercept, then mifepristone) reported results?

Thank you for this model. The order-of-treatment idea is central to one of the registry's hypotheses.

[name]
```

## Brave-LC : équipe du protocole (non envoyée)

Objet : Brave-LC: is an assessment planned after the 16 weeks of naltrexone?

```text
To the Brave-LC protocol team,

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One hypothesis in the registry is that the illness is an alternative stable state. If so, participants who improve should stay improved after the drug is gone. If low-dose naltrexone only works while it is taken, the improvement should fade. The registry entry for Brave-LC (NCT07916259) describes a 16-week course, and I could not find an assessment after the last dose.

My questions:

1. Is an off-treatment assessment planned after week 16?
2. If not, could one be considered, even a single questionnaire a few weeks after the last dose? It would let the trial tell a lasting improvement from an effect that needs the drug.

If this is already in the protocol, a pointer to it would fully answer my question.

Thank you for running a trial for children and young adults.

[name]
```
