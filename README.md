[![Build Status](https://travis-ci.com/netbox-community/ansible_modules.svg?branch=devel)](https://travis-ci.com/netbox-community/ansible_modules)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Netbox modules for Ansible using Ansible Collections

## Requirements

- Netbox 2.5+
- **pynetbox 4.1.0+**
- Python 3.6+
- Ansible 2.9+

## Existing Modules

- netbox_aggregate
- netbox_circuit
- netbox_circuit_termination
- netbox_circuit_type
- netbox_cluster
- netbox_cluster_group
- netbox_cluster_type
- netbox_device_bay
- netbox_device_interface
- netbox_device_role
- netbox_device_type
- netbox_device
- netbox_inventory_item
- netbox_ip_address
- netbox_ipam_role
- netbox_manufacturer
- netbox_platform
- netbox_prefix
- netbox_provider
- netbox_rack_group
- netbox_rack_role
- netbox_rack
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

## Netbox Plugins

- netbox lookup plugin
- netbox inventory plugin (0.1.5)

## How to Use

- Install via Galaxy
  - `ansible-galaxy collection install netbox_community.ansible_modules`
- Install via source
  - `git clone git@github.com:netbox-community/ansible_modules.git`
  - `cd ansible_modules`
  - `ansible-galaxy collection build .`
  - `ansible-galaxy collection install netbox_community-ansible_modules-X.X.X.tar.gz`
    - Can add `-p` to provide a different path other than the default path, but it must be within your `ansible.cfg` or provided via an environment variable.

### Example playbooks

Using the **collections** at the play level

```yaml
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False
  collections:
    - netbox_community.ansible_modules

  tasks:
    - name: Create device within Netbox with only required information
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
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create device within Netbox with only required information
      netbox_community.ansible_modules.netbox_device:
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
- name: Create device within Netbox with only required information
  netbox_community.ansible_modules.netbox_device:
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
- name: Create device within Netbox with only required information
  collections:
    - netbox_community.ansible_modules:
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
        query_result: "{{ query('netbox_community.ansible_modules.netbox', 'sites', api_endpoint='http://localhost:32768', token='0123456789abcdef0123456789abcdef01234567') }}"
```

## How to Contribute

Please read ![Contributing](CONTRIBUTING.md)
