#!/bin/bash

set -e

read -p "TCG Card Set ID: " SET_ID

if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

echo "Fetching data from $SET_ID. "

curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" > card_set_lookup/$SET_ID.json

echo "Success."