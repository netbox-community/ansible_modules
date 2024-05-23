#!/usr/bin/env bash

# Usage: ./hacking/local-test.sh

# Run build, which will remove previously installed versions
./hacking/build.sh

# Install new built version
ansible-galaxy collection install netbox-netbox-*.tar.gz -p .

# You can now cd into the installed version and run tests
(cd ansible_collections/netbox/netbox/ && ansible-test units -v --python 3.10 && ansible-test sanity --requirements -v --python 3.10 --skip-test pep8 plugins/)
rm -rf ansible_collections
