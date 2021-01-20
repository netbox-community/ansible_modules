![Devel CI Status](https://github.com/netbox-community/ansible_modules/workflows/All%20CI%20related%20tasks/badge.svg?branch=devel)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![Release](https://img.shields.io/github/v/release/netbox-community/ansible_modules)

# NetBox modules for Ansible using Ansible Collections

We have moved this collection to a different namespace and collection name on Ansible Galaxy. The new versions will be at `netbox.netbox`.

To keep the code simple, we only officially support the two latest releases of NetBox and don't guarantee backwards compatibility beyond that. We do try and keep these breaking changes to a minimum, but sometimes changes to NetBox's API cause us to have to make breaking changes.

## Requirements

- NetBox 2.6+ or the two latest NetBox releases
- Python 3.6+
- Python modules: **pynetbox 5.0.4+**
- Ansible 2.9+
- NetBox write-enabled token when using modules or read-only token for `nb_lookup/nb_inventory`

We have a new docs site live that can be found [here](https://netbox-ansible-collection.readthedocs.io/en/latest/).
