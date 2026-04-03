# Labo 1 — GitHub et tests unitaires

Ce dépôt contient les fichiers du Labo 1 du cours *Advanced Python (2BA)*.

## Contenu du projet

- `utils.py` : implémentation des fonctions `fact`, `roots` et `integrate`
- `test_utils.py` : tests unitaires fournis pour valider les fonctions
- `main.py` et `galaxy.py` : fichiers utilisés pour l’exercice de débogage
- `.github/workflows/test.yml` : configuration GitHub Actions pour exécuter automatiquement les tests
- `.gitignore` : fichiers à ignorer dans le dépôt

## Travail réalisé

- Création et configuration d’un dépôt GitHub
- Mise en place d’un workflow GitHub Actions pour lancer les tests à chaque push
- Implémentation correcte des fonctions demandées dans `utils.py`
- Passage de tous les tests unitaires en local et via GitHub Actions
- Débogage de `main.py` et `galaxy.py` (3 bugs identifiés et corrigés grâce au débogueur VS Code)

## Exécuter les tests

Dans un terminal, à la racine du projet :

pytest


Tous les tests doivent passer.

## Lancer le programme principal

main.py


Cela exécute le code lié aux galaxies (après correction des bugs).

## Auteur

Nicolas Vannuffel — 2BA Ingénieur industriel - Electronique, ECAM.
