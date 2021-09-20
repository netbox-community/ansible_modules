#!/usr/bin/env bash

# Usage: ./hacking/make-docs.sh

# Run build, which will remove previously installed versions
./hacking/build.sh

# Install new built version
ansible-galaxy collection install netbox-netbox-*.tar.gz -f

# Run antisbull-docs now
antsibull-docs collection --use-current --squash-hierarchy --dest-dir docs/plugins/ netbox.netbox