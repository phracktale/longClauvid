# Registre des hypothèses

Ouvert le 2026-11-22. Le registre est la mémoire du projet : ce qui est affirmé,
sur quelle source, et ce qui pourrait le réfuter.

| Fichier | Contenu |
| --- | --- |
| `sources.yaml` | Chaque page consultée : adresse, type, date de lecture |
| `pistes.yaml` | Les 14 pistes sous-exploitées, avec leur niveau de preuve |
| `endotypes.yaml` | Les 5 typologies de patients, leurs marqueurs et les candidats à tester |
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

## Règles

1. Pas de fiche sans `prediction` ni `refutation` : le validateur la refuse.
2. Une fiche ne se supprime pas. Si l'hypothèse tombe, son statut passe à `réfutée`
   et l'historique dit pourquoi.
3. Chaque résultat qui touche une hypothèse ajoute une ligne à son historique,
   qu'il aille dans son sens ou non.
4. Une source n'entre dans `sources.yaml` qu'après avoir été lue.

## Valider

```bash
python3 outils/valider_registre.py
```

## Origine des fiches actuelles

Les sept hypothèses sont des croisements formulés dans le document de cadrage
du 2026-11-22. Aucune n'a été évaluée par des pairs.
