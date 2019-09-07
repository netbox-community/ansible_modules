[![Build Status](https://travis-ci.org/FragmentedPacket/netbox_modules.svg?branch=master)](https://travis-ci.org/FragmentedPacket/netbox_modules) 
# Netbox modules for Ansible using Ansible Collections 

**THIS IS A WIP DUE TO COLLECTIONS BEING IN TECH REVIEW CURRENTLY (Ansible 2.8) BUT WILL BE UPDATED AS NECESSARY AS COLLECTIONS MATURES**

## Todo

- ~~initial build and changes to properly import module_utils~~
- Add testing to Travis CI
  - ~~Initial unit tests~~
  - ~~Test different Python versions (3.6/3.7)~~
  - ~~Integration testing against at least two versions of Netbox~~
  - Local testing using Tox
  - Test currently supported versions of Ansible
- ~~Add documentation on how to use to README~~
- ~~Add documentation on how to contribute to collection~~

## Requirements

- Netbox 2.5+
- pynetbox 4.0.6+
- Python 3.6+
- Ansible 2.9+
  - Or run Ansible via source

## Existing Modules

- netbox_device
- netbox_device_interface
- netbox_ip_address
- netbox_prefix
- netbox_site
- netbox_tenant
- netbox_tenant_group

## How to Use

- Install via Mazer
  - `mazer install fragmentedpacket.netbox_modules`
- Follow Ansible instructions to use the collection
  - [https://docs.ansible.com/ansible/devel/dev_guide/collections_tech_preview.html#using-collections](https://docs.ansible.com/ansible/devel/dev_guide/collections_tech_preview.html#using-collections)

### Example playbook

```yaml
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False
  collections:
    - fragmentedpacket.netbox_modules

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

## How to Contribute

The structure of the Netbox modules attempts to follow the layout of the Netbox API by having a module_util for each application (`dcim, ipam, tenancy, etc`) that inherits from a base module (`NetboxModule - netbox_utils.py`) and then implements the specific endpoints within the correct application module.

ex. Add logic for adding devices under netbox_dcim.py or ip addresses under netbox_ipam.py

In turn when creating the actual modules, we're just calling a single function and passing in the Ansible Module and the endpoint. This means all the logic is within the specific application's module_util module and a lot of the logic should be the same for most endpoints since it is a basic operation of using the desired state of the endpoint and then either making sure it exists, updating it if it does exist, or removing it. There may be some special logic for other endpoints, but it should be minimal.

(Ansible Module) netbox_{{ endpoint }} -> (Module Util) netbox_{{ application }} -> (Module Util) netbox_utils

### Testing

 1. Please update `tests/unit/module_utils/test_netbox_base_class.py` if editing anything within the base class that needs to be tested.
 2. Please add or update an existing play to test the new Netbox module for integration testing within `tests/integration/integration-tests.yml`
 3. Run `black .` within the base directory for black formatting as it's required for tests to pass
 4. Check necessary dependencies defined within `.travis.yml` for now if you're wanting to test locally
