#!/bin/bash
# Ordner "thumbs" anlegen
mkdir -p thumbs

# Bilder in Thumbnails konvertieren
for bild in *.png
do
 convert "$bild" -resize 260x180 "thumbs/$bild"
done
