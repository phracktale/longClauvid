# Registre des hypothèses

Ouvert le 2026-11-22. Le registre est la mémoire du projet : ce qui est affirmé,
sur quelle source, et ce qui pourrait le réfuter.

| Fichier | Contenu |
| --- | --- |
| `sources.yaml` | Chaque page consultée : adresse, type, date de lecture |
| `pistes.yaml` | Les 17 pistes sous-exploitées, avec leur niveau de preuve ; les trois dernières viennent de la banque |
| `endotypes.yaml` | Les 5 typologies de patients, leurs marqueurs et les candidats à tester |
| `transpositions.yaml` | Les 11 transpositions : ce qu'une maladie mieux maîtrisée apprend sur un processus partagé |
| `confrontations.yaml` | Les 21 confrontations : pour chaque paire d'hypothèses, la mesure qui les départage |
| `hypotheses/` | Une fiche par hypothèse |

## Une fiche d'hypothèse

```yaml
id: H1
titre: Une phrase qui affirme quelque chose
statut: ouverte            # ouverte | soutenue | affaiblie | réfutée | abandonnée
creee_le: 2026-11-22
endotype: E1               # ou null
pistes: [P01, P02]         # les pistes du registre qu'elle relie
sources: [fluge-2025]      # sources en plus de celles des pistes

enonce: Ce que l'hypothèse affirme, et ce qu'elle explique.
prediction: Ce qu'on doit observer si elle est vraie.
refutation: Ce qui, observé, la rendrait fausse.

test:
  donnees: Sur quels échantillons ou quelles données.
  methode: Comment.
  faisabilite: Ce qui existe déjà, ce qui manque.

historique:
  - date: 2026-11-22
    evenement: Création.
```

## Une fiche de transposition

```yaml
- id: T01
  nom: "Maladie de référence : ce qu'on y fait"
  processus: Le processus biologique partagé.
  maladie: La maladie de référence.
  maitrise: rémission        # guérison | rémission | contrôle | prévention | échec
  levier: Ce qui agit sur le processus dans la maladie de référence.
  preuve: Ce que le levier y a montré, chiffres à l'appui.
  deja_tente: Ce qui a été essayé dans le COVID long ou l'EM/SFC, échecs compris.
  lecon: Ce que la transposition change pour nos hypothèses.
  prochain_test: Le test qui trancherait.
  niveau: B                  # preuve du processus dans nos maladies, échelle A à D
  liens: [P14, H4, E4]       # pistes, hypothèses et endotypes concernés
  sources: [vih-rio-2026]
```

## Une fiche de confrontation

```yaml
- paire: [H1, H4]
  question: La question qui oppose les deux hypothèses.
  mesure: Ce qu'on mesure, et sur quoi.
  si_premiere: Ce qu'on observe si H1 est à l'œuvre.
  si_seconde: Ce qu'on observe si c'est H4.
  acces: échantillons existants   # ou : suivi d'essais | nouvelle collecte
  donnees: Où la mesure est possible.
  sources: [recover-vital-nih]   # facultatif
```

## Règles

1. Pas de fiche sans `prediction` ni `refutation` : le validateur la refuse.
2. Une fiche ne se supprime pas. Si l'hypothèse tombe, son statut passe à `réfutée`
   et l'historique dit pourquoi.
3. Chaque résultat qui touche une hypothèse ajoute une ligne à son historique,
   qu'il aille dans son sens ou non.
4. Une source n'entre dans `sources.yaml` qu'après avoir été lue.
   Les sources des transpositions ont été lues sous forme de résumé ou d'extrait :
   leur lecture intégrale est un travail de la phase 1.
5. Pas de transposition sans `deja_tente` : le validateur la refuse.
6. Chaque paire d'hypothèses a sa confrontation, avec deux prédictions différentes.
   Une hypothèse ajoutée au registre exige donc ses confrontations avec toutes les autres.

## La banque d'hypothèses à vérifier

`banque.yaml` reçoit les pistes proposées par les agents de recherche. Ce n'est pas le registre :
une entrée y reste « à vérifier » tant que ses sources n'ont pas été rouvertes par quelqu'un d'autre.
Les règles sont dans `PROTOCOLE.md`.

Une piste relue porte un champ `relecture` : ce qui a été lu, les corrections, le résultat du test
« inexplorée » et la décision. Ce champ prime sur le texte déposé, qui n'est pas réécrit.
Une piste qui a été écartée y porte aussi l'avis de son contradicteur et le motif d'origine.
Le compte rendu de la relecture du 2026-11-22 est dans `analyses/banque/RELECTURE.md`.

## Valider

```bash
python3 outils/valider_registre.py
```

## Origine des fiches actuelles

Les sept hypothèses sont des croisements formulés dans le document de cadrage
du 2026-11-22. Aucune n'a été évaluée par des pairs.
