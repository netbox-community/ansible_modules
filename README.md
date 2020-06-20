[![Build Status](https://travis-ci.com/netbox-community/ansible_modules.svg?branch=devel)](https://travis-ci.com/netbox-community/ansible_modules)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![Release](https://img.shields.io/github/v/release/netbox-community/ansible_modules)

# NetBox modules for Ansible using Ansible Collections

We have moved this collection to a different namespace and collection name on Ansible Galaxy. The new versions will be at `netbox.netbox`.

To keep the code simple, we only officially support the two latest releases of NetBox and don't guarantee backwards compatibility beyond that. We do try and keep these breaking changes to a minimum, but sometimes changes to NetBox's API cause us to have to make breaking changes.

## Requirements

- NetBox 2.6+ or the two latest NetBox releases
- **pynetbox 4.2.5+**
- Python 3.6+
- Ansible 2.9+
- NetBox write-enabled token

## Existing Modules

- netbox_aggregate
- netbox_circuit
- netbox_circuit_termination
- netbox_circuit_type
- netbox_cluster
- netbox_cluster_group
- netbox_cluster_type
- netbox_console_port
- netbox_console_port_template
- netbox_console_server_port
- netbox_console_server_port_template
- netbox_device_bay
- netbox_device_interface
- netbox_device_role
- netbox_device_type
- netbox_device
- netbox_front_port
- netbox_front_port_template
- netbox_inventory_item
- netbox_ip_address
- netbox_ipam_role
- netbox_manufacturer
- netbox_platform
- netbox_power_feed
- netbox_power_outlet
- netbox_power_outlet_template
- netbox_power_panel
- netbox_power_port
- netbox_power_port_template
- netbox_prefix
- netbox_provider
- netbox_rack_group
- netbox_rack_role
- netbox_rack
- netbox_rear_port
- netbox_rear_port_template
- netbox_region
- netbox_rir
- netbox_site
- netbox_service
- netbox_tenant_group
- netbox_tenant
- netbox_virtual_machine
- netbox_vm_interface
- netbox_vlan_group
- netbox_vlan
- netbox_vrf

## NetBox Plugins

- netbox lookup plugin
- netbox inventory plugin (0.1.5)

## How to Use

- Install via Galaxy
  - `ansible-galaxy collection install netbox.netbox`
- Install via source
  - `git clone git@github.com:netbox-community/ansible_modules.git`
  - `cd ansible_modules`
  - `ansible-galaxy collection build .`
  - `ansible-galaxy collection install netbox-netbox-X.X.X.tar.gz`
    - Can add `-p` to provide a different path other than the default path, but it must be within your `ansible.cfg` or provided via an environment variable.

### Example playbooks

Using the **collections** at the play level

```yaml
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False
  collections:
    - netbox.netbox

  tasks:
    - name: Create device within NetBox with only required information
      netbox_device:
        netbox_url: http://netbox-demo.org:32768
        netbox_token: 0123456789abcdef0123456789abcdef01234567
        data:
          name: Test66
          device_type: Cisco Test
          device_role: Core Switch
          site: Test Site
          status: Staged
        state: present
```

Using the **collections** at the task level

```yaml
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create device within NetBox with only required information
      netbox.netbox.netbox_device:
        netbox_url: http://netbox-demo.org:32768
        netbox_token: 0123456789abcdef0123456789abcdef01234567
        data:
          name: Test66
          device_type: Cisco Test
          device_role: Core Switch
          site: Test Site
          status: Staged
        state: present
```

Using the **collections** in a role's task files

```yaml
---
- name: Create device within NetBox with only required information
  netbox.netbox.netbox_device:
    netbox_url: http://netbox-demo.org:32768
    netbox_token: 0123456789abcdef0123456789abcdef01234567
    data:
      name: Test66
      device_type: Cisco Test
      device_role: Core Switch
      site: Test Site
      status: Staged
    state: present

OR

---
- name: Create device within NetBox with only required information
  collections:
    - netbox.netbox
  netbox_device:
    netbox_url: http://netbox-demo.org:32768
    netbox_token: 0123456789abcdef0123456789abcdef01234567
    data:
      name: Test66
      device_type: Cisco Test
      device_role: Core Switch
      site: Test Site
      status: Staged
    state: present
```

Using the **collections** lookup plugin at the task level

```yaml
- name: "TEST NETBOX_LOOKUP"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: "NETBOX_LOOKUP 1: Lookup returns exactly two sites"
      assert:
        that: "{{ query_result|count }} == 3"
      vars:
        query_result: "{{ query('nb_lookup', 'sites', api_endpoint='http://localhost:32768', token='0123456789abcdef0123456789abcdef01234567') }}"
```

### Using **nb_inventory** Within AWX/Tower

This will cover the basic usage of the NetBox inventory plugin within this collection.

1. Define `collections/requirements.yml` within a Git project.
    1. AWX/Tower will download the collection on each run. This can be handled differently or excluded if storing Ansible Collections on the AWX/Tower box.
    2. Define `inventory.yml` in Git project that adheres to inventory plugin structure.
2. Add Git project to AWX/Tower as a project.
3. Create inventory and select `source from project`.
    1. Select the AWX/Tower project from Step 2
    2. Select the `inventory.yml` file in the project from Step 1.1
    3. Click `Save` and sync source.

## How to Contribute

Please read ![Contributing](CONTRIBUTING.md)
