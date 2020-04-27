#!/usr/bin/env bash

# Stop on failure - if unit tests fail the inventory will not be updated
set -e

# Usage overview (see Contributing.md for more detail):
# - Run netbox with the netbox-docker project
# - Fill with test data, run ./tests/integration/netbox-deploy.py
# - Run ./hacking/update_test_inventories.sh
# - Manually verify the diff of new JSON is correct, to prevent introducing a regression.

# Install locally
export ANSIBLE_COLLECTIONS_PATHS=.
export OUTPUT_INVENTORY_JSON=tests/integration/targets/inventory/files

# Remove local cache
rm -rf /tmp/inventory_netbox/

# Clean and install the built collection
./hacking/local-test.sh

# Run the same script used by integration tests, but save the results
./tests/integration/targets/inventory/runme.sh
