![Devel CI Status](https://github.com/netbox-community/ansible_modules/workflows/All%20CI%20related%20tasks/badge.svg?branch=devel)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![Release](https://img.shields.io/github/v/release/netbox-community/ansible_modules)
[![Talk to us: Slack](https://img.shields.io/badge/Slack-blue.svg)](https://netdev-community.slack.com/join/shared_invite/zt-mtts8g0n-Sm6Wutn62q_M4OdsaIycrQ#/shared-invite/email)

# Looking for New Maintainers

We are in search of a few maintainers for this project.  Please see discussion [Looking for maintainers](https://github.com/netbox-community/ansible_modules/discussions/526).  Our previous single maintainer was unable to keep up with the project to the high bar set by @FragmentedPacket.  The reality is that this is not a project that should be held by a single maintainer.  Reach out in the discussion or on our slack if you are interested in helping out.

While we look for maintainers who have shown a willingness to provide inputs/ides, contribute code, and review contributions, the netbox-community team will do its best to maintain this repo in the interim.  Prioritization will given to bug fixes, NetBox compatibility, and Ansible requirements/compatibility.  New features (associated to the project or NetBox core)will be developed as a best effort, but rest assured, no releases will be cut that are not stable and tested.

# NetBox modules for Ansible using Ansible Collections

We have moved this collection to a different namespace and collection name on Ansible Galaxy. The new versions will be at `netbox.netbox`.

To keep the code simple, we only officially support the two latest releases of NetBox and don't guarantee backwards compatibility beyond that. We do try and keep these breaking changes to a minimum, but sometimes changes to NetBox's API cause us to have to make breaking changes.

## Requirements

- NetBox 2.6+ or the two latest NetBox releases
- Python 3.6+
- Python modules:
  - `pynetbox 5.0.4+`
  - `packages` if using Ansible < 2.10, as it's included in Ansible 2.10+
- Ansible 2.9+
- NetBox write-enabled token when using modules or read-only token for `nb_lookup/nb_inventory`

## Docs

Module documentation exists on [netbox-ansible-collection.readthedocs.io](https://netbox-ansible-collection.readthedocs.io/en/latest/).

## Join the discussion

We have a dedicated Slack channel `#ansible` on [netdev-community.slack.com](https://netdev-community.slack.com/join/shared_invite/zt-mtts8g0n-Sm6Wutn62q_M4OdsaIycrQ#/shared-invite/email)
