# Piste B005 : refaire la comparaison de 2026 en tenant compte de l'âge et du sexe

Plan écrit le 2026-11-24, **avant** tout calcul sur les dosages. Rien ici n'est un avis médical.

## Pourquoi

L'étude de 2026 ([PMID 42205163](https://pubmed.ncbi.nlm.nih.gov/42205163/)) trouve un indice de la voie
de la noradrénaline plus bas dans le liquide céphalo-rachidien des patients que chez des volontaires sains.
La relecture du 2026-11-24 a relevé trois manques (`registre/banque.yaml`, piste B005, champs `relecture.complement`
et `relecture.attaque_apres_lecture`) :

- les volontaires sains sont plus âgés que les patients EM/SFC, et l'article ne rapporte pas d'ajustement sur l'âge ;
- le sexe diffère entre les groupes ; l'article dit l'avoir vérifié, sans montrer les données ;
- le DOPAC seul, bas dans l'étude de 2024, n'est pas donné en 2026.

Les auteurs publient leurs données individuelles avec leur code :
<https://github.com/lillianaregawi/Central-NE-Pathway-Index-Scripts>, version `8684a2f` du 2026-02-20.
Le classeur compte 122 personnes et donne l'âge, le sexe, le groupe, les médicaments et chaque dosage.
Il n'est pas copié dans ce dépôt : le dépôt des auteurs n'a pas de licence.

## Ce que j'ai déjà vu des données

Avant d'écrire ce plan, j'ai lu le dictionnaire du classeur, les effectifs par groupe, l'âge par groupe,
et la liste des médicaments. J'ai affiché les quatre premières lignes du tableau pour connaître ses colonnes,
sans relever les dosages. Je n'ai calculé aucune moyenne ni aucun écart sur les dosages.
Les écarts publiés, eux, sont connus : ils sont dans l'article.

## Étape 0 : retrouver les chiffres publiés

Analyse de variance de l'indice (`CSF_NE_DHPG_MHPG`) par groupe, puis test de Tukey, comme dans le script des auteurs.
Attendu : −15,9 pour l'EM/SFC, −9,62 pour le COVID long, −19,4 pour la maladie de Parkinson, en pmol/mL,
par rapport aux volontaires sains ; effectifs dosés 36, 15, 30 et 32.

Si ces chiffres ne sont pas retrouvés à 0,1 près, l'analyse s'arrête et l'écart est rapporté.

## Étape 1 : le test principal

Une régression linéaire : indice ~ groupe + âge + sexe, avec les volontaires sains pour référence.
Elle porte sur trois groupes : volontaires sains, EM/SFC, COVID long. Le groupe Parkinson est laissé de côté
dans ce test, parce qu'il est bien plus âgé (64 ans en moyenne) et pèserait sur la pente de l'âge.

Deux écarts sont lus : EM/SFC et COVID long, chacun contre les volontaires sains. Deux tests, donc un seuil
de 0,025 chacun, et un intervalle de confiance à 97,5 %.

| Résultat | Lecture |
| --- | --- |
| L'intervalle ajusté exclut zéro, du côté négatif | L'écart résiste à l'ajustement sur l'âge et le sexe |
| L'intervalle ajusté contient zéro | L'écart publié ne résiste pas à cet ajustement, dans ces données |

Dans les deux cas le résultat est descriptif. Ce sont les mêmes patients et la même équipe : résister à l'ajustement
ne vaut pas réplication, et le niveau de la piste ne monte pas. Si l'écart de l'EM/SFC ne résiste pas,
la décision de la piste est à revoir, avec un contradicteur.

## Étape 2 : analyses de sensibilité, descriptives

Elles ne décident de rien. Chacune est rapportée, quel que soit son résultat.

1. Le même modèle avec les quatre groupes.
2. Le même modèle sans les dix patients qui prenaient un médicament agissant sur la noradrénaline,
   avec le compte de ces patients par groupe.
3. Le même modèle pour chaque dosage seul : MHPG, DHPG, noradrénaline, DOPAC, DOPA, HVA, dopamine.
   C'est ici que se lit le DOPAC.
4. Dans le COVID long, le même modèle en séparant les patients avec et sans malaise post-effort.

L'étape 2 fait beaucoup de comparaisons, sans correction : une valeur de p isolée n'y prouve rien.

## Limites connues d'avance

- Un seul centre, de petits groupes, des volontaires sains venus de plusieurs protocoles.
- L'ajustement suppose un effet linéaire de l'âge, estimé sur une centaine de personnes au plus.
- Les valeurs manquantes sont celles des auteurs : prélèvement insuffisant ou pic parasite. Elles sont laissées manquantes.
- Les patients EM/SFC sont très probablement ceux de l'étude de 2024.

## Refaire

```bash
git clone https://github.com/lillianaregawi/Central-NE-Pathway-Index-Scripts.git cache/b005-code
python3 analyses/banque/B005/reanalyse.py "cache/b005-code/Supplementary File 1 Indiv. Data.xlsx"
```
