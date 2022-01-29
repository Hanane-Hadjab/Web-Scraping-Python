#!/bin/bash
debut=$(date +%s)
echo "Démarrage ...................."
base_url="http://example.python-scraping.com/"
for i in {0..25}; do
  curl "$base_url/places/default/index/$i" > tmp.html
  default="/places/default/view/"
  manna=$(cat tmp.html | grep -oP '(?<=href="/places/default/view/)(.*?)(?=\"|$(.*)\")')
  for line in $manna; do
    curl "$base_url$default$line" >tmp2.html
    html2text tmp2.html | awk "/Area|Tld|Population|Capital|Country/" | sort --ignore-case > tmphanane.txt ;
    mm=$(tail -1 tmphanane.txt)
    sed  "s/[^$mm]$/;/g" tmphanane.txt |  awk -F ':' '{print $NF}' | xargs >>result.txt
  done
done
echo "FIN"
fin=$(date +%s)
duree=$(( $fin - $debut ))
echo "$duree secondes"
