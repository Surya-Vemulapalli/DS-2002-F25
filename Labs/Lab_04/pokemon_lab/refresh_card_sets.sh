#!/bin/bash

set -e

echo "Refreshing all card sets in card set lookup"

for FILE in "card_set_lookup"/*; do
    SET_ID=$(basename "$FILE" .json)
    echo "updating set"
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" > "$FILE"
    echo "Written into $FILE"
done

echo "All cards have been refreshed"