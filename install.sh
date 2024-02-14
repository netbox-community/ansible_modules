#!/bin/bash

rm netbox-netbox-3.16.0.tar.gz
ansible-galaxy collection build .
ansible-galaxy collection install -f netbox-netbox-3.16.0.tar.gz