#!/usr/bin/env bash

# Print commands as they're run
set -x

PATH_TO_INVENTORIES="$( dirname "${BASH_SOURCE[0]}" )/files"

# OUTPUT_DIR is set by ansible-test
# OUTPUT_INVENTORY_JSON is only set if running hacking/update_test_inventories.sh to update the test diff data
if [ ! -z "$OUTPUT_INVENTORY_JSON" ]
then
    OUTPUT_DIR="$OUTPUT_INVENTORY_JSON"
fi

echo OUTPUT_DIR="$OUTPUT_DIR"

RESULT=0

for INVENTORY in "$PATH_TO_INVENTORIES"/*.yml
do
    NAME="$(basename "$INVENTORY")"
    NAME_WITHOUT_EXTENSION="${NAME%.yml}"

    # Run through python.py just to make sure we've definitely got the coverage environment set up
    # Just running ansible-inventory directly may not actually find the right one in PATH
    OUTPUT_JSON="$OUTPUT_DIR/$NAME_WITHOUT_EXTENSION.json"
    python.py `which ansible-inventory` -vvvv --list --inventory "$INVENTORY" --output="$OUTPUT_JSON"

    # Compare the output
    if ! ./compare_inventory_json.py "$PATH_TO_INVENTORIES/$NAME_WITHOUT_EXTENSION.json" "$OUTPUT_JSON"
    then
        # Returned non-zero status
        RESULT=1
    fi

done

exit $RESULT
