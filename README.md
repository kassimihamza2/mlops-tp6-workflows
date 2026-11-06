# MLOps TP06 — Automatisation des workflows MLOps

## Présentation
Ce projet porte sur l'automatisation des workflows MLOps dans le cadre du module Déploiement d'IA (5IASD — EMSI, année 2026-2027).

## Technologies
- Python
- DVC
- Prefect
- MLflow
- Git et GitHub
- GitHub Actions
- Scikit-learn

## Fonctionnalités
- Reproduction automatisée du pipeline DVC
- Lecture et validation des métriques du modèle
- Validation du F1-score selon un seuil défini
- Notification après validation du modèle
- Planification des workflows avec Prefect
- Vérification automatique de la qualité via GitHub Actions

## Structure
- flow_mlops.py : workflow Prefect
- planifier.py : planification
- dvc.yaml : pipeline DVC
- params.yaml : paramètres et seuil de validation
- verifier_qualite.py : contrôle qualité
- .github/workflows/ : intégration continue

## Auteur
Hamza Kassimi
EMSI Rabat — 5AISDR-G6

## Note
Projet académique adapté à partir d'un projet de référence collaboratif.
