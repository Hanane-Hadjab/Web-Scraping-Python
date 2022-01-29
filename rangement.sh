#!/bin/bash
#directory=$(pwd)
if [[ $# = 0 ]]; then
    echo "Veuillez passez un chemin de dossier"
fi
directory=$1
listFiles=$(ls "$directory")
for file in $listFiles; do
  file=$directory"/"$file
  if [ -f "$file" ]; then
    mimetype=$(file --mime-type -b "$file")
    type=$(echo "$mimetype" | sed 's/.*\///')
    dossier=$directory"/Dossier_$type"
    mkdir "$dossier" 2>/dev/null
    mv "$file" "$dossier"
  fi
done
