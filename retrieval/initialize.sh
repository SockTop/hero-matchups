#!/bin/bash

set -eu

DOTABUFF_URL="https://www.dotabuff.com"

if [ ! -d .dotabuff-content ]; then
    mkdir .dotabuff-content
    mkdir .dotabuff-content/heroes
fi

curl -s ${DOTABUFF_URL}/heroes > .dotabuff-content/heroes/content

for hero in $(python ${PWD}/retrieval/fetch-hero-list.py); do
    echo "Fetching matchups for ${hero}"
    
    mkdir .dotabuff-content/heroes/${hero}

    curl -s ${DOTABUFF_URL}/heroes/${hero}/matchups > .dotabuff-content/heroes/${hero}/matchups

done

python ${PWD}/retrieval/generate-hero-matrix.py

rm -r .dotabuff-content