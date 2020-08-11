#!/usr/bin/env bash

# The only way to pass variables to integration tests - write to a file inside the integration test directory.
# Usage: render_config.sh runme_config.template > runme_config
# Copied from:
# https://www.ansible.com/blog/adding-integration-tests-to-ansible-content-collections
# https://github.com/xlab-si/digital_ocean.digital_ocean/blob/master/tests/utils/render.sh

set -o xtrace # Print commands as they're run
set -o errexit # abort on nonzero exitstatus
set -o nounset # abort on unbound variable
set -o pipefail # don't hide errors within pipes


function main()
{
    readonly template="$1"
    readonly content="$(cat "${template}")"

    eval "echo \"$content\""
}

main "$@"
