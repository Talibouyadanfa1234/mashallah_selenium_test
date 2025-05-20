#!/bin/bash

echo "📦 Installation des dépendances..."
pip install -r requirements.txt

echo "🚀 Lancement des tests Selenium..."
pytest tests/ --html=report.html --self-contained-html

echo "✅ Rapport généré : report.html"
