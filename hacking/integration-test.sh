#!/usr/bin/env bash
#
# Integration Test Runner
#
# Runs integration tests against a running NetBox Docker instance
#
# Usage: ./hacking/integration-test.sh [TARGET] [OPTIONS]
#
# Targets:
#   v4.3, v4.4, v4.5       - Main module tests (default: v4.5)
#   inventory-v4.3         - Inventory plugin tests
#   regression-v4.3        - Regression tests
#   all-v4.3               - Run all tests for a version (modules + inventory + regression)
#
# Options:
#   --list                 - List available test targets
#   --help                 - Show this help
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
COLLECTION_TMP_DIR="${COLLECTION_TMP_DIR:-/tmp/test-collections}"
DEFAULT_TARGET="v4.5"

show_help() {
    cat << 'EOF'
Integration Test Runner for NetBox Ansible Collection

Usage: ./hacking/integration-test.sh [TARGET] [OPTIONS]

TARGETS:
  Module Tests:
    v4.0, v4.1, v4.2, v4.3, v4.4, v4.5  - Main module tests (91 modules)

  Inventory Tests:
    inventory-v4.0, inventory-v4.1, inventory-v4.2, inventory-v4.3, inventory-v4.4, inventory-v4.5
    Tests the NetBox inventory plugin against expected JSON output

  Regression Tests:
    regression-v4.0, regression-v4.1, regression-v4.2, regression-v4.3, regression-v4.4, regression-v4.5
    Tests for specific bug fixes (referenced by GitHub issues)

  Combined:
    all-v4.3               - Run modules + inventory + regression for v4.3
    all-v4.4               - Run modules + inventory + regression for v4.4
    all-v4.5               - Run modules + inventory + regression for v4.5

OPTIONS:
  --list                 - List available test targets
  --help, -h             - Show this help

PREREQUISITES:
  1. NetBox Docker must be running on localhost:32768
     See tests/netbox-docker/ for docker-compose overrides per version.

  2. Test data must be populated:
     python tests/integration/netbox-deploy.py

EXAMPLES:
  # Run main module tests for v4.3
  ./hacking/integration-test.sh v4.3

  # Run inventory tests for v4.3
  ./hacking/integration-test.sh inventory-v4.3

  # Run ALL tests for v4.3 (modules + inventory + regression)
  ./hacking/integration-test.sh all-v4.3
EOF
}

list_targets() {
    echo "Available integration test targets:"
    echo ""
    echo "Module Tests:"
    for dir in "$REPO_DIR"/tests/integration/targets/v4.*/; do
        if [ -d "$dir" ]; then
            basename "$dir"
        fi
    done | sort -V
    echo ""
    echo "Inventory Tests:"
    for dir in "$REPO_DIR"/tests/integration/targets/inventory-v4.*/; do
        if [ -d "$dir" ]; then
            basename "$dir"
        fi
    done | sort -V
    echo ""
    echo "Regression Tests:"
    for dir in "$REPO_DIR"/tests/integration/targets/regression-v4.*/; do
        if [ -d "$dir" ]; then
            basename "$dir"
        fi
    done | sort -V
}

setup_collection() {
    echo "================================"
    echo "Setting up collection for testing"
    echo "================================"

    cd "$REPO_DIR"

    # Load NetBox token if available (e.g. for versions requiring v2 tokens)
    if [ -f "/tmp/netbox-token.env" ]; then
        echo "Loading NETBOX_TOKEN from /tmp/netbox-token.env"
        source /tmp/netbox-token.env
        export NETBOX_TOKEN
        echo "✓ Token loaded: ${NETBOX_TOKEN:0:20}..."
    elif [ -n "${NETBOX_TOKEN:-}" ]; then
        echo "✓ Using NETBOX_TOKEN from environment: ${NETBOX_TOKEN:0:20}..."
        export NETBOX_TOKEN
    else
        echo "ℹ No NETBOX_TOKEN found (using default v1 token fallback)"
    fi

    # Build and install the collection
    ./hacking/build.sh

    # Install the netbox collection
    ansible-galaxy collection install netbox-netbox-*.tar.gz \
        --force \
        --collections-path "$COLLECTION_TMP_DIR"

    # Install test dependencies (community.general for json_query filter)
    echo "Installing integration test dependencies..."
    ansible-galaxy collection install community.general \
        --force \
        --collections-path "$COLLECTION_TMP_DIR"
}

run_test() {
    local target="$1"

    cd "$COLLECTION_TMP_DIR/ansible_collections/netbox/netbox/" || exit 1

    echo ""
    echo "================================"
    echo "Running integration tests: $target"
    echo "================================"

    if [ -n "${NETBOX_TOKEN:-}" ]; then
        echo "Using NETBOX_TOKEN: ${NETBOX_TOKEN:0:20}..."
        echo -n "$NETBOX_TOKEN" > /tmp/.netbox_test_token
        chmod 600 /tmp/.netbox_test_token
        export NETBOX_TOKEN

        if [[ "$target" == inventory-* ]]; then
            local config_file="$COLLECTION_TMP_DIR/ansible_collections/netbox/netbox/tests/integration/targets/$target/runme_config"
            local version="${target#inventory-}"
            cat > "$config_file" << EOF
export NETBOX_TOKEN="$NETBOX_TOKEN"
export NETBOX_VERSION="$version"
EOF
        fi
    fi

    ansible-test integration -v --color yes --requirements "$target"
}

run_all_tests() {
    local version="$1"

    cd "$COLLECTION_TMP_DIR/ansible_collections/netbox/netbox/" || exit 1

    local targets=("$version")

    if [ -d "$REPO_DIR/tests/integration/targets/inventory-$version" ]; then
        targets+=("inventory-$version")
    fi

    if [ -d "$REPO_DIR/tests/integration/targets/regression-$version" ]; then
        targets+=("regression-$version")
    fi

    echo ""
    echo "================================"
    echo "Running ALL integration tests for $version"
    echo "Targets: ${targets[*]}"
    echo "================================"

    if [ -n "${NETBOX_TOKEN:-}" ]; then
        echo "Using NETBOX_TOKEN: ${NETBOX_TOKEN:0:20}..."
        echo -n "$NETBOX_TOKEN" > /tmp/.netbox_test_token
        chmod 600 /tmp/.netbox_test_token
        export NETBOX_TOKEN
    fi

    for target in "${targets[@]}"; do
        echo ""
        echo "--- Running: $target ---"
        ansible-test integration -v --color yes --requirements "$target"
    done
}

TARGET="${1:-$DEFAULT_TARGET}"

case "$TARGET" in
    --help|-h|help)
        show_help
        exit 0
        ;;
    --list|list)
        list_targets
        exit 0
        ;;
    all-v*)
        VERSION="${TARGET#all-}"
        setup_collection
        run_all_tests "$VERSION"
        ;;
    *)
        setup_collection
        run_test "$TARGET"
        ;;
esac
