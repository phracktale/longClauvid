# Piste P15 : la demande aux auteurs de l'étude de 2019

État au 2026-11-22 : **une lettre envoyée.** Elle est partie de la boîte du projet,
sur instruction du porteur du projet, une fois le travail fusionné. Aucune adresse électronique n'est reprise ici.

| Destinataire | Ce qui est demandé | État |
| --- | --- | --- |
| Auteur correspondant de l'étude de 2019 | Les cinq bibliothèques de témoins sains de la première série ont-elles été préparées autrement ? L'écart tient-il sans elles ? | Envoyée le 2026-11-22 |

L'adresse est publiée par l'[article](https://pubmed.ncbi.nlm.nih.gov/31088495/).
Le constat que la lettre soumet aux auteurs est dans [RESULTATS.md](RESULTATS.md).
L'auteur correspondant et son adresse ont été relevés dans la copie de l'article déposée à PubMed Central.
La lettre est partie telle qu'elle est écrite ici, avec son nom à la place de « [corresponding author] ».

## Lettre à l'auteur correspondant

Objet : Your 2019 monocyte RNA-seq data (GSE130353): rRNA content in five control libraries

```text
Dear Dr [corresponding author],

I maintain longClauvid, an open, source-traceable registry of hypotheses on long COVID and ME/CFS (https://github.com/phracktale/longClauvid). I am an independent software developer, not a clinician or a researcher, and part of the registry was drafted with an AI assistant; every claim in it links to its source.

Your 2019 study reports much lower expression of MT-RNR1 and MT-RNR2 in monocytes of QFS and CFS patients than in healthy controls. The registry lists humanin and MOTS-c as a lead, so I re-read the per-gene files you deposited (GSE130353), with an analysis plan written before opening them.

What I see: the library numbers form two series of twenty (12461 to 12480, and 13120 to 13139), with five libraries per group in each. In the first series, the five healthy-control libraries (HC13, HC16, HC20, HC24, HC25) have 0.5% to 7.6% of their mapped fragments on four rRNA features: MT-RNR1, MT-RNR2, and the 18S and 28S pseudogenes ENSG00000225840 and ENSG00000226958. The median library has 0.02%. In the second series no group stands out, and the patient-control difference in MT-RNR1 and MT-RNR2 is absent.

I also looked for the same difference in three other public datasets (PBMC and whole blood; 41 patients and 47 controls with ME/CFS or long COVID): I do not see it there.

My questions: were these five libraries prepared differently, for example without rRNA removal or in a separate batch? And does the difference hold in your hands when the analysis is restricted to the second series, or adjusted for residual rRNA?

I may well be misreading the files. The plan, the code and the per-library table are public (in French): https://github.com/phracktale/longClauvid/blob/main/analyses/P15/RESULTATS.md. If I am wrong, I will correct the registry at once.

Thank you for depositing the data: it is what made this check possible.

[name]
```

## Journal des envois

Une ligne par envoi ou par réponse : date, destinataire, ce qui a été répondu.

| Date | Destinataire | Événement |
| --- | --- | --- |
| 2026-11-22 | Auteur correspondant de l'étude de 2019 | Lettre rédigée, en attente de relecture |
| 2026-11-22 | Auteur correspondant de l'étude de 2019 | Lettre envoyée, à l'adresse que publie l'article de 2019 |
