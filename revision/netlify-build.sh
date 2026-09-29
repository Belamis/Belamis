#!/bin/sh
# Prépare le dossier publié par Netlify : uniquement les fichiers du site (pas les sources Python ni les brouillons).
set -e
cd "$(dirname "$0")"
rm -rf dist
mkdir -p dist/data dist/assets
cp index.html style.css prefs.js app.js raphael.js auth.js config.js revise.js panels.js _headers dist/
cp data/francais.js data/maths.js data/epreuve2.js data/mayotte.js data/revisions.js data/notions.js dist/data/
cp assets/transition.mp3 dist/assets/
echo "Site prêt dans revision/dist"
