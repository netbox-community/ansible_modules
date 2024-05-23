#!/usr/bin/env bash

set -o xtrace # Print commands as they're run
set -o errexit # abort on nonzero exitstatus
set -o nounset # abort on unbound variable
set -o pipefail # don't hide errors within pipes

# Directory of this script
SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"
RUNME_CONFIG="$SCRIPT_DIR/runme_config"
INVENTORIES_DIR="$SCRIPT_DIR/files"

# Load runme_config, if exists - the only way to pass environment when run through ansible-test
if [[ -f "$RUNME_CONFIG" ]]
then
    source "$RUNME_CONFIG"
fi

declare -a COMPARE_OPTIONS # empty array

# Check if NETBOX_VERSION has been set by runme_config, and if so, pass to compare_inventory_json.py
if [[ "${NETBOX_VERSION:-}" == "v3.5" ]]
then
    COMPARE_OPTIONS+=(--netbox-version "${NETBOX_VERSION}")
fi

# OUTPUT_DIR is set by ansible-test
# OUTPUT_INVENTORY_JSON is only set if running hacking/update_test_inventories.sh to update the test diff data
if [[ -n "${OUTPUT_INVENTORY_JSON:-}" ]]
then
    OUTPUT_DIR="$OUTPUT_INVENTORY_JSON"

    # Clean up JSON fields we don't want to store and compare against in tests (creation times, etc.)
    COMPARE_OPTIONS+=(--write)
fi

echo OUTPUT_DIR="$OUTPUT_DIR"

inventory () {
    if [[ -n "${OUTPUT_INVENTORY_JSON:-}" ]]
    then
        # Running for the purpose of updating test data
        ansible-inventory "$@"
    else
        # Running inside ansible-test
        # Run through python.py just to make sure we've definitely got the coverage environment set up
        # Just running ansible-inventory directly may not actually find the right one in PATH
        python.py "$(command -v ansible-inventory)" "$@"
    fi
}


RESULT=0

for INVENTORY in "$INVENTORIES_DIR"/*.yml
do
    NAME="$(basename "$INVENTORY")"
    NAME_WITHOUT_EXTENSION="${NAME%.yml}"

    OUTPUT_JSON="$OUTPUT_DIR/$NAME_WITHOUT_EXTENSION.json"
    inventory -vvvv --list --inventory "$INVENTORY" --output="$OUTPUT_JSON"

    # Compare the output
    if ! "$SCRIPT_DIR/compare_inventory_json.py" "${COMPARE_OPTIONS[@]}" "$INVENTORIES_DIR/$NAME_WITHOUT_EXTENSION.json" "$OUTPUT_JSON"
    then
        # Returned non-zero status
        RESULT=1
    fi

done

exit $RESULT
