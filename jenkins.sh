#!/bin/bash

set -e

echo "🧪 Lancement de Jenkins Test Script"



# 👇 Rendre les modules visibles
export PYTHONPATH=$(pwd)

mkdir -p reports

pytest tests/ --browser=chrome \
  --html=reports/report.html \
  --self-contained-html \
  -v --capture=tee-sys
