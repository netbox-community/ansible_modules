#!/usr/bin/env bash

# Usage: ./hacking/local-test.sh
set -euo pipefail

# shellcheck disable=SC2317
cleanup_tests() {
    popd >/dev/null 2>&1 || true
    rm -rf "${COLLECTION_TMP_DIR}/ansible_collections"
}

: "${COLLECTION_TMP_DIR:=.}"

# Run build, which will remove previously installed versions
./hacking/build.sh

# Install new built version
ansible-galaxy collection install netbox-netbox-*.tar.gz \
    --force \
    --collections-path "$COLLECTION_TMP_DIR"


trap cleanup_tests EXIT INT TERM

# You can now cd into the installed version and run tests
mkdir -p "${COLLECTION_TMP_DIR}"
pushd "${COLLECTION_TMP_DIR}/ansible_collections/netbox/netbox/" >/dev/null || exit 1
ansible-test units -v --python 3.13
ansible-test sanity --requirements -v --python 3.13 --skip-test pep8 plugins/

