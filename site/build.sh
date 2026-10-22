#!/bin/sh
set -eu
cd "$(dirname "$0")"
media=../assets/06_prototipos/media
rm -rf public/media
mkdir -p public/guia public/media
cp ../assets/06_prototipos/PROTOTIPO_fluxo_highlights.html public/index.html
cp ../assets/06_prototipos/GUIA_simulacao.html public/guia/index.html
# só o manifesto e os MP4/JPG que ele referencia; nada mais da pasta de mídia vai para o site
cp "$media/manifest.json" public/media/
for f in $(grep -oE '"(src|poster)": *"media/[^"]+\.(mp4|jpg)"' "$media/manifest.json" | sed -E 's/.*"media\/([^"]+)"/\1/'); do
  cp "$media/$f" public/media/
done
