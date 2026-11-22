# longClauvid

Recherche ouverte et traçable sur le COVID long, l'encéphalomyélite myalgique (EM/SFC)
et les syndromes post-infectieux. Le dépôt repère des pistes sous-exploitées,
les confronte entre elles et les simule avant qu'une équipe clinique ne les teste.

> **Ce dépôt produit des hypothèses classées, pas des traitements.**
> Rien ici n'est un avis médical. Plusieurs candidats cités sont des médicaments
> à risque sérieux, à n'utiliser que dans un essai clinique.

## Contenu

| Dossier | Rôle |
| --- | --- |
| `PROTOCOLE.md` | Les sept phases, leurs critères de passage, les règles de traçabilité et de fiabilité |
| `JOURNAL.md` | Chaque décision, avec son motif et les options écartées |
| `registre/` | Sources, pistes, endotypes et hypothèses, un fichier par hypothèse |
| `outils/valider_registre.py` | Refuse une hypothèse sans prédiction réfutable ou une affirmation sans source |
| `simulateurs/niveau1/` | Cohorte virtuelle : quel plan d'essai peut voir un effet limité à un sous-groupe |
| `simulateurs/niveau2/` | Modèle mécaniste à deux états stables : le piège métabolique IDO de Kashi 2019 |
| `verifier.py` | Lance tous les contrôles du dépôt |

## Démarrer

```bash
pip install -r requirements.txt
python3 verifier.py                              # tous les contrôles
python3 outils/valider_registre.py               # le registre seul
python3 simulateurs/niveau1/simulateur_endotypes.py
python3 simulateurs/niveau2/piege_ido.py
```

## Où en est le protocole

| Phase | État |
| --- | --- |
| 0. Cadrage | Registre ouvert le 2026-11-22 : 7 hypothèses, 14 pistes, 5 endotypes, 61 sources |
| 1. Cartographie | À faire : la revue actuelle est ciblée, pas systématique |
| 2. Détection | À faire |
| 3. Confrontation | À faire |
| 4. Simulation | Niveaux 1 et 2 construits ; niveau 3 à faire |
| 5. Validation | À faire |
| 6. Passage clinique | Exige une équipe habilitée et un comité d'éthique |

## Résultats à ce jour

- **Niveau 1.** Un essai tout-venant de 200 patients ne détecte qu'une fois sur cinq
  un traitement très efficace chez 20 % des patients ; un biomarqueur imparfait porte
  cette chance à 77 %. Détail : `simulateurs/niveau1/RESULTATS.md`.
- **Niveau 2.** Le modèle de Kashi 2019 est reproduit aux arrondis publiés près.
  Avec ses paramètres, on entre dans le piège en quelques semaines et on en sort
  en mois ou en années. Détail : `simulateurs/niveau2/RESULTATS.md`.

## Règles du dépôt

1. Une affirmation = une source dans `registre/sources.yaml`, avec sa date de lecture.
2. Une décision = une entrée dans `JOURNAL.md`, avec son motif.
3. Une hypothèse ne se supprime pas : son statut change, son historique s'allonge.
4. Un résultat négatif se consigne comme un résultat positif.
5. `python3 verifier.py` doit passer avant chaque commit.

Le document de cadrage (état des lieux, pistes, typologies de patients) se trouve ici :
<https://claude.ai/artifact/VtWerHyfRm7zbinLBKjyba>
