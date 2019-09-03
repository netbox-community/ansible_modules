[![Build Status](https://travis-ci.org/FragmentedPacket/netbox_modules.svg?branch=master)](https://travis-ci.org/FragmentedPacket/netbox_modules) 
# Netbox modules for Ansible using Ansible Collections 

**THIS IS A WIP DUE TO COLLECTIONS BEING IN TECH REVIEW CURRENTLY (Ansible 2.8) BUT WILL BE UPDATED AS NECESSARY AS COLLECTIONS MATURES**

TODO:
- ~~initial build and changes to properly import module_utils~~
- Add testing to a CI (Travis?) and existing unit tests
  - ~~Initial unit tests~~
  - ~~Test different Python versions (3.6/3.7)~~
  - Local testing using Tox
  - Test currently supported versions of Ansible
- ~~Add documentation on how to use to README~~
- Add documentation on how to contribute to collection

## Requirements
- Ansible 2.9+
  - Or run Ansible via source
- Python 3.6+

## Existing Modules

 - netbox_device
 - netbox_interface
 - netbox_ip_address
 - netbox_prefix
 - netbox_site

## How to Use
- Install via Mazer
  - `mazer install fragmentedpacket.netbox_modules`
- Follow Ansible instructions to use the collection:
  - [https://docs.ansible.com/ansible/devel/dev_guide/collections_tech_preview.html#using-collections](https://docs.ansible.com/ansible/devel/dev_guide/collections_tech_preview.html#using-collections)

#### Example playbook
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
**Will be updated with diagram and more information needed to contribute**

If looking to contribute before this is updated, please review the code and hopefully it is enough to get started on adding new modules and how the new modules should be structured.

#### Testing

 1. Please update `tests/unit/module_utils/test_netbox_base_class.py` if editing anything within the base class that needs to be tested.
 2. Run `black .` within the base directory for black formatting as it's required for tests to pass
 3. Check necessary dependencies defined within `.travis.yml` for now if you're wanting to test locally
