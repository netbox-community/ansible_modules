# Changelog

## v0.1.6`

### New Features
- [#84](https://github.com/netbox-community/ansible_modules/issues/84) - Add dns_name to netbox_ip_address
- [#83](https://github.com/netbox-community/ansible_modules/issues/83) - Add region and region_id to query_filter for Netbox Inventory plugin

### Bug Fixes
- [#85](https://github.com/netbox-community/ansible_modules/issues/85) - Fixed vlan searching with vlan_group for netbox_prefix
- [#67](https://github.com/netbox-community/ansible_modules/issues/67) - Removed static choices from netbox_utils and now pulls the choices for each endpoint from the Netbox API at call time

### Thanks to following contributors!
@vsvetlov
@pugnacity
@DavidRobbNZ
@ThomasADavis

## v0.1.5

### Bug Fixes
- [#68](https://github.com/netbox-community/ansible_modules/issues/68) - Add argument specs for every module to validate data passed in (Fixes some idempotency issues)(POSSIBLE BREAKING CHANGE)
- [#76](https://github.com/netbox-community/ansible_modules/issues/76) - Allow name updates to manufacturers
- [#77](https://github.com/netbox-community/ansible_modules/issues/77) - Builds slug for netbox_device_type from model which is now required and slug is optional. Model will be slugified if slug is not provided (BREAKING CHANGE)
- [#78](https://github.com/netbox-community/ansible_modules/issues/78) - netbox_ip_address: If no address has no CIDR notation, it will convert it into a /32 and pass to Netbox. (Fixes idempotency cidr notation is not provided)
- [#80](https://github.com/netbox-community/ansible_modules/issues/80) - Fail module with proper exception when connection to Netbox API cannot be established
- [#81](https://github.com/netbox-community/ansible_modules/issues/81) - netbox_device_interface: Lag no longer has to be a dictionary and the value of the key can be the name of the LAG

### New Modules / Plugins
- [#70](https://github.com/netbox-community/ansible_modules/issues/70) - netbox_service
- [#54](https://github.com/netbox-community/ansible_modules/issues/54) - Netbox Inventory Plugin

### Thanks to following contributors!
@loganbest
@FurryJulie
@TawR1024
@ignatenkobrain
@mechanomancy


## v0.1.4
Updated documentation for moving repos to Netbox Community Github Organization

## v0.1.3

### Bug Fixes
- [#52](https://github.com/netbox-community/ansible_modules/issues/52) - Add error handling for invalid key_file for lookup plugin

### Documentation
- [#51](https://github.com/netbox-community/ansible_modules/issues/51) - Update lookup plugin documentation for decryption of secrets

## v0.1.2

### Bug Fixes
- [#47](https://github.com/netbox-community/ansible_modules/issues/47) - Allow endpoint choices to be an integer of the choice rather than attempting to dynamically determine the choice ID

## v0.1.1

### Bug Fixes

- [#40](https://github.com/netbox-community/ansible_modules/issues/40) - Fixed issue with netbox_vm_interface where it would fail if different virtual machine had the same interface name
- [#40](https://github.com/netbox-community/ansible_modules/issues/40) - Updated netbox_ip_address to find interfaces on virtual machines correctly

## v0.1.0

### Breaking Changes

- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Changed role to prefix_role in netbox_prefix.py
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Changed group to tenant_group in netbox_tenant.py
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Renamed netbox_interface to netbox_device_interface
- [#24](https://github.com/netbox-community/ansible_modules/issues/24) - Module failures when required fields arent provided

### New Modules / Plugins

- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_device_role
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_device_type
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_ipam_role
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_manufacturer
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_platform
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_rack
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_rack_group
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_rack_role
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_vlan_group
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_vlan
- [#9](https://github.com/netbox-community/ansible_modules/issues/9) - Added netbox_vrf
- [#12](https://github.com/netbox-community/ansible_modules/issues/12) - Added netbox_rir
- [#14](https://github.com/netbox-community/ansible_modules/issues/14) - Added netbox_aggregate
- [#14](https://github.com/netbox-community/ansible_modules/issues/14) - Added netbox_services
- [#15](https://github.com/netbox-community/ansible_modules/issues/15) - Added netbox_region
- [#15](https://github.com/netbox-community/ansible_modules/issues/15) - Added netbox_device_bay
- [#15](https://github.com/netbox-community/ansible_modules/issues/15) - Added netbox_inventory_item
- [#26](https://github.com/netbox-community/ansible_modules/issues/26) - Added netbox lookup plugin
- [#16](https://github.com/netbox-community/ansible_modules/issues/16) - Added netbox_virtual_machine
- [#16](https://github.com/netbox-community/ansible_modules/issues/16) - Added netbox_vm_interface
- [#16](https://github.com/netbox-community/ansible_modules/issues/16) - Added netbox_cluster_type
- [#16](https://github.com/netbox-community/ansible_modules/issues/16) - Added netbox_cluster_group
- [#16](https://github.com/netbox-community/ansible_modules/issues/16) - Added netbox_cluster
- [#17](https://github.com/netbox-community/ansible_modules/issues/17) - Added netbox_provider
- [#17](https://github.com/netbox-community/ansible_modules/issues/17) - Added netbox_circuit
- [#17](https://github.com/netbox-community/ansible_modules/issues/17) - Added netbox_circuit_type
- [#17](https://github.com/netbox-community/ansible_modules/issues/17) - Added netbox_circuit_termination

### Bug Fixes

### Enhancements

- [#10](https://github.com/netbox-community/ansible_modules/issues/10) - Add primary_ip4/6 to netbox_ip_address
