#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p public/guia
cp ../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html public/index.html
cp ../assets/06_prototipos/GUIA_simulacao.html public/guia/index.html
