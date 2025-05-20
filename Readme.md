# 📦 Projet de Tests Automatisés avec Selenium, Pytest, Docker & Jenkins

Ce projet implémente une architecture de test complète incluant Selenium Grid, Pytest, Jenkins CI/CD et la génération de rapports HTML.

## 🗂️ Structure du projet

project/
├── pages/ ← Objets de page (PageObject)
├── tests/ ← Fichiers de tests pytest
├── utils/ ← Fonctions communes (driver, etc.)
├── .env ← URL du site (ex: BASE_URL)
├── config.py ← Chargement des variables d’environnement
├── requirements.txt ← Dépendances Python
├── jenkins.sh ← Script d'exécution utilisé par Jenkins
├── Jenkinsfile ← Pipeline Jenkins (déclenchement, test, archive)
├── docker-compose.yml ← Infrastructure Selenium Grid (hub + node)
└── report.html ← Rapport de test généré avec pytest-html


## 🚀 Fonctionnalités principales

- Exécution des tests via Selenium Grid (Docker)
- Support multi-navigateurs (Chrome, Firefox…)
- Intégration continue via Jenkins (pipeline + webhook GitHub)
- Génération automatique d’un rapport HTML avec `pytest-html`

## 🛠️ Installation rapide

1. Cloner le repo :
   ```bash
   git clone <url-du-repo>
   cd project/
