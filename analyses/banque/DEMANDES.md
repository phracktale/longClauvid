# Piste B002 : deux demandes aux auteurs d'études déjà faites dans le COVID long

État au 2026-11-23 : **aucune lettre envoyée.** Ce sont deux brouillons, à relire par le porteur du projet.
Une lettre part de la boîte du projet, après cette relecture ; l'envoi se consigne en bas de ce fichier.
Aucune adresse électronique n'est reprise ici.

La piste B002 n'est pas promue : elle reste en banque, vérifiée, au niveau C. Ces demandes ne testent rien.
Elles disent seulement si le test peut se faire sur des données qui existent déjà.

| Destinataire | Ce qui est demandé | État |
| --- | --- | --- |
| Auteur correspondant de la lipidomique de 2024 ([PMID 38368647](https://pubmed.ncbi.nlm.nih.gov/38368647/)) | Les plasmalogènes font-ils partie des lipides mesurés ? Un groupe de personnes rétablies ou non infectées existe-t-il ? | Brouillon |
| Auteur correspondant de l'étude multi-omique de 2025 ([PMID 40842862](https://pubmed.ncbi.nlm.nih.gov/40842862/)) | Les plasmalogènes sont-ils mesurés par la métabolomique ? Dans quel sens varient-ils ? | Brouillon |

## Pourquoi ces deux questions

Le signal de la piste vient d'une étude de 2022 sur l'EM/SFC ([PMID 35887252](https://pubmed.ncbi.nlm.nih.gov/35887252/)) :
deux plasmalogènes plus bas chez les patientes, avec de petits écarts et un taux de fausses découvertes admis à 15 %.
La relecture contradictoire du 2026-11-22 a relevé deux choses dans les copies locales :

- le résumé de l'étude de 2024 compare des patients symptomatiques et asymptomatiques après le COVID-19,
  sans nommer de groupe rétabli ni de plasmalogènes ;
- l'étude de 2025 décrit un métabolisme des lipides éthers renforcé dans deux sous-groupes de patients.
  Ce résultat vient des voies enrichies, pas d'un dosage des plasmalogènes : le sens reste à lire sur les lipides eux-mêmes.

Le détail est dans `registre/banque.yaml`, piste B002, champ `relecture.attaque`.

## Lettre à l'auteur correspondant de la lipidomique de 2024

Objet : Your 2024 lipidomics study in post-COVID patients: were plasmalogens among the measured lipids?

```text
Dear Dr [corresponding author],

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One lead in the registry comes from a 2022 metabolomics study in ME/CFS (PMID 35887252), which reported slightly lower plasma plasmalogens in women with ME/CFS. As far as I can find, nobody has checked this in long COVID. Your 2024 study (untargeted plasma lipidomics, 147 post-COVID patients, nearly 400 polar lipids) may already hold the answer. I could only read its abstract.

Two questions:

1. Were ether-linked phospholipids, in particular PE and PC plasmalogens, among the lipids you quantified? If so, did they differ between your symptomatic and asymptomatic groups, and in which direction?
2. Did the study include people who had fully recovered, or people never infected, measured on the same platform?

A one-line answer would already help: it tells me whether this lead can be tested on existing data or needs new measurements. I am not asking for individual-level data.

If I have misread your abstract, please tell me and I will correct the registry.

Thank you for your time.

[name]
```

## Lettre à l'auteur correspondant de l'étude multi-omique de 2025

Objet : Your 2025 multi-omics study of long COVID subgroups: direction of plasmalogen levels

```text
Dear Dr [corresponding author],

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

One lead in the registry comes from a 2022 metabolomics study in ME/CFS (PMID 35887252), which reported slightly lower plasma plasmalogens in women with ME/CFS. Your 2025 study reports enhanced glycerophospholipid and ether lipid metabolism in the multisystemic and musculoskeletal subgroups of long COVID. At the pathway level this points the other way, which matters for the lead.

Two questions:

1. Does your metabolomics dataset include individual plasmalogen species (PE or PC plasmalogens)? If so, are their levels higher, lower or unchanged in these two subgroups, relative to your comparison groups?
2. Are the plasmalogen values among the processed data in your supplementary tables, so that I can read them myself rather than take your time?

A one-line answer would already help. I am not asking for individual-level data.

If I have misread your paper, please tell me and I will correct the registry.

Thank you for your time, and for depositing the data.

[name]
```

## Journal des envois

Aucun envoi à ce jour.
