# Ansible Modules for NetBox

## Description
The NetBox Ansible project provides an Ansible collection for interacting with NetBox, the leading solution for modeling and documenting modern networks. By combining the traditional disciplines of IP address management (IPAM) and datacenter infrastructure management (DCIM) with powerful APIs and extensions, NetBox provides the ideal "source of truth" to power network automation.

This Ansible collection consists of a set of modules to define the intended network state in NetBox, along with plugins to drive automation of the network using data from NetBox.

## Requirements

- You must be running one of the two most recent releases of NetBox
- A NetBox write-enabled API token when using modules or a read-only token for the `nb_lookup` and `nb_inventory` plugins.
- Python 3.10+
- Python modules:
  - pytz
  - pynetbox
- Ansible 2.15+

## Installation

### Python Modules and Ansible
```
pip install pytz
pip install pynetbox
pip install ansible
```

### NetBox Ansible Collection
Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install netbox.netbox
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```
collections:
  - name: netbox.netbox
```

To upgrade the collection to the latest available version, run the following command:
```
ansible-galaxy collection install netbox.netbox --upgrade
```
You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 3.19.1:

```
ansible-galaxy collection install netbox.netbox:==3.19.1
```
See using [Ansible collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections) for more details.

### Other Installation Options

#### Build From Source

Follow these steps to install from source:

1. ``git clone git@github.com:netbox-community/ansible_modules.git``
2. ``cd ansible_modules``
3. ``ansible-galaxy collection build .``
4. ``ansible-galaxy collection install netbox-netbox*.tar.gz``

#### Build From Source (Pull Request)

This is useful to test code within PRs.

1. ``git clone git@github.com:netbox-community/ansible_modules.git``
2. ``cd ansible_modules``
3. ``git fetch origin pull/<pr #>/head:<whatever-name-you-want>``
4. ``git checkout <whatever-name-you-want>``
5. ``ansible-galaxy collection build .``
6. ``ansible-galaxy collection install netbox-netbox*.tar.gz``

**_Note:_** This [GitHub link](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/checking-out-pull-requests-locally) provides detailed information on checking out pull requests locally.

## Use Cases

### Use Case 1 - Define Intended Network State in NetBox
Define the intended state of your network in NetBox, by interacting with the NetBox database to define objects and their associated state in the following ways:

- Make sure objects exit
- Update objects if they do exist
- Remove objects if they do not not exist

For example, to make sure a new aggregate network prefix exists:
```
tasks:
    - name: Create aggregate within NetBox with only required information
      netbox.netbox.netbox_aggregate:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 192.168.0.0/16
          rir: Test RIR
        state: present
```

### Use Case 2 - NetBox as a Dynamic Inventory Source for Ansible
Use the Inventory Plugin to dynamically generate Ansible inventory from device data in NetBox. Use query filters, groups and mappings to tailor the generated inventory to your specific needs.

The following example builds an Ansible inventory that groups devices by `role`, and filters for only devices that have the `network-edge-router` role, have a primary IP address and belong to the `internal` tenant:
```
# netbox_inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i netbox_inventory.yml

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
validate_certs: True
config_context: False
group_by:
  - device_roles
query_filters:
  - role: network-edge-router
device_query_filters:
  - has_primary_ip: 'true'
  - tenant__n: internal
```

### Use Case 3 - Query and Return Elements from NetBox
Use the Lookup plugin to query NetBox and return data to drive network automation, such as lists of devices, device configurations, prefixes and IP addresses etc.

The following example returns a list of devices and their manufacturers, using an API filter to only return devices with the `management` role and the NetBox tag of `Dell`:
```
tasks:
  # query a list of devices
  - name: Obtain list of devices from NetBox
    debug:
      msg: >
        "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
         manufactured by {{ item.value.device_type.manufacturer.name }}"
    loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                    api_endpoint='http://localhost/',
                    api_filter='role=management tag=Dell'),
                    token='<redacted>') }}"

```
## Testing
Tested with Ansible Core v2.15+ Ansible Core versions prior to 2.15 are not supported.

## Contributing
If you would to contribute to the project then you can find out how to get started [here](https://github.com/netbox-community/ansible_modules/blob/devel/CONTRIBUTING.md).

## Support
There are various options to get support for the collection:
-  Search through previous [GitHub Discussions](https://github.com/netbox-community/ansible_modules/discussions) or start a new one.
- Raise a [GitHub Issue](https://github.com/netbox-community/ansible_modules/issues)
- Read the module [documentation](https://netbox-ansible-collection.readthedocs.io/en/latest/)
- Join the discussion on the dedicated `#ansible` Slack Channel on [netdev-community.slack.com](https://netdev-community.slack.com/join/shared_invite/zt-mtts8g0n-Sm6Wutn62q_M4OdsaIycrQ#/shared-invite/email)

Customers of NetBox Labs and Ansible using the officially certified version of the collection can get support via the usual Ansible channels. Escalation to the NetBox Labs support team will be provided as needed.

## Release Notes
The collection release notes and changelog can be found [here](https://github.com/netbox-community/ansible_modules/releases).

## Related Information
Some extra resources you might find useful for both the Ansible collection and for NetBox itself:
- [NetBox Zero to Hero](https://netboxlabs.com/zero-to-hero/) - free 12 part course that takes you from an empty NetBox through to a fully deployed branch site, using the Ansible collection extensively along the way.
- [Network Configuration Assurance with NetBox and Ansible](https://netboxlabs.com/blog/network-configuration-assurance-with-netbox-and-ansible/) - blog post featuring the Inventory plugin being used in a simple network automation use case to compare actual network state Vs intended state as defined in NetBox.
- Official NetBox [documentation](https://docs.netbox.dev/en/stable/).

## License Information
GNU General Public License v3.0 or later.

See [LICENSE](https://github.com/netbox-community/ansible_modules/blob/devel/LICENSE) for the full text of the license.

Link to the license that the collection is published under.
