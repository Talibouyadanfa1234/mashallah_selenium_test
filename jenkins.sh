#!/bin/bash

set -e

echo "🧪 Lancement de Jenkins Test Script"

python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate sur Windows

pip install --upgrade pip
pip install -r requirements.txt

# 👇 Rendre les modules visibles
export PYTHONPATH=$(pwd)

mkdir -p reports

pytest tests/ --browser=chrome --headless \
  --html=reports/report.html \
  --self-contained-html \
  -v --capture=tee-sys
