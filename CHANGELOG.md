# Changelog

## v0.2.3

### Documentation

- [#226](https://github.com/netbox-community/ansible_modules/issues/226) - Fix indentation in README to prevent syntax error
- [#180](https://github.com/netbox-community/ansible_modules/issues/180) - Fix documentation errors when using ansible-lint `validate-modules`

### Enchancements
- [#216](https://github.com/netbox-community/ansible_modules/issues/216) - Allows private key to be passed in to `validate_certs` within modules
- [#187](https://github.com/netbox-community/ansible_modules/issues/187) - Adds `discovered` field to `netbox_inventory_item`
- [#219](https://github.com/netbox-community/ansible_modules/pull/219) - Adds `tenant` field to `netbox_cluster`
- [#215](https://github.com/netbox-community/ansible_modules/issues/215) - Adds `query_params` to all modules to allow users to define the `query_params`
- [#238](https://github.com/netbox-community/ansible_modules/pull/238) - Better error handling if read-only token is provided for modules. Updated README as well to say that a `write-enabled` token is required

### Bug Fixes
- [#214](https://github.com/netbox-community/ansible_modules/issues/214) - Fixes bug in inventory plugin that fails if there are either no virtual machines, but devices defined in NetBox or vice versa from failing when `fetch_all` is set to `False`
- [#228](https://github.com/netbox-community/ansible_modules/issues/228) - Fixes bug in `netbox_prefix` failing when using `check_mode`
- [#231](https://github.com/netbox-community/ansible_modules/issues/231) - Normalize any string values that are passed in via Jinja into an integer within the `_normalize_data` method

### New Modules
- [#235](https://github.com/netbox-community/ansible_modules/pull/235) - `netbox_power_feed`
- [#235](https://github.com/netbox-community/ansible_modules/pull/235) - `netbox_power_outlet`
- [#235](https://github.com/netbox-community/ansible_modules/pull/235) - `netbox_power_outlet_template`
- [#235](https://github.com/netbox-community/ansible_modules/pull/235) - `netbox_power_panel`
- [#235](https://github.com/netbox-community/ansible_modules/pull/235) - `netbox_power_port`
- [#235](https://github.com/netbox-community/ansible_modules/pull/235) - `netbox_power_port_template`
- [#236](https://github.com/netbox-community/ansible_modules/pull/236) - `netbox_console_port`
- [#236](https://github.com/netbox-community/ansible_modules/pull/236) - `netbox_console_port_template`
- [#236](https://github.com/netbox-community/ansible_modules/pull/236) - `netbox_console_server_port`
- [#236](https://github.com/netbox-community/ansible_modules/pull/236) - `netbox_console_server_port_template`
- [#237](https://github.com/netbox-community/ansible_modules/pull/237) - `netbox_front_port`
- [#237](https://github.com/netbox-community/ansible_modules/pull/237) - `netbox_front_port_template`
- [#237](https://github.com/netbox-community/ansible_modules/pull/237) - `netbox_rear_port`
- [#237](https://github.com/netbox-community/ansible_modules/pull/237) - `netbox_rear_port_template`


## V0.2.2

### Enhancements

- [#211](https://github.com/netbox-community/ansible_modules/issues/211) - Changed `validate_certs` to `raw` to allow private keys to be passed in

### Bug Fixes

- [#208](https://github.com/netbox-community/ansible_modules/issues/208) - Added `type` to `ALLOWED_QUERY_PARAMS` for interface searches
- [#201](https://github.com/netbox-community/ansible_modules/issues/201) - Added `interfaces` to `ALLOWED_QUERY_PARAMS` for ip addresses searches
- [#221](https://github.com/netbox-community/ansible_modules/pull/221) - Remove `rack` as a choice when createing virtual machines

## v0.2.1

### Enhancements

- [#141](https://github.com/netbox-community/ansible_modules/issues/141) - Added option to change host_vars to singular rather than having single element lists
- [#190](https://github.com/netbox-community/ansible_modules/pull/190) - Added 21" width to netbox_rack
- [#188](https://github.com/netbox-community/ansible_modules/issues/188) - Added cluster, cluster_type, and cluster_group to group_by option in inventory plugin
- [#193](https://github.com/netbox-community/ansible_modules/issues/193) - Added option to flatten `config_context` and `custom_fields` 

### Bug Fixes

- [#193](https://github.com/netbox-community/ansible_modules/issues/193) - Added `type` to `netbox_device_interface` and deprecation notice for `form_factor`
- [#202](https://github.com/netbox-community/ansible_modules/pull/202) - Fixes inventory performance issues, properly shows virtual chassis masters. Also fixes the following #142, #143, #199, #200

## v0.2.0

### Breaking Changes

- [#139](https://github.com/netbox-community/ansible_modules/issues/139) - Change `ip-addresses` key in netbox inventory plugin to `ip_addresses`.

### Bug Fixes
- [#45](https://github.com/netbox-community/ansible_modules/issues/45) - Allow integers to be passed in via Jinja string to properly convert back to integer
- [#158](https://github.com/netbox-community/ansible_modules/issues/158) - Removed choices within argument_spec for `mode` in `netbox_device_interface` and `netbox_vm_interface`. This allows the API to return any error if an invalid choice is selected for `mode`.
- [#151](https://github.com/netbox-community/ansible_modules/issues/151) - Fixed dict iteration error for Python3.8
- [#167](https://github.com/netbox-community/ansible_modules/issues/167) - Updated rack width choices for latest NetBox version
- [#166](https://github.com/netbox-community/ansible_modules/issues/166) - Properly find LAG if defined just as a string rather than dictionary with the relevant data
- [#174](https://github.com/netbox-community/ansible_modules/issues/174) - Allow services to be created with a different protocol

### Enhancements

- [#136](https://github.com/netbox-community/ansible_modules/pull/136) - Added `raw_output` option to netbox lookup plugin to return the exact output from the API with no doctoring
- [#105](https://github.com/netbox-community/ansible_modules/issues/105) - Added `update_vc_child` option to netbox_device_interface to allow child interfaces to be updated if device specified is the master device within the virtual chassis
- [#143](https://github.com/netbox-community/ansible_modules/pull/143) - Added `services` option to the netbox inventory to allow users to toggle whether services are included or not
- [#138](https://github.com/netbox-community/ansible_modules/issues/138) - Added `group_names_raw` option to the netbox inventory to allow users have the group names be the slug rather than prepending the group name with the type
- [#170](https://github.com/netbox-community/ansible_modules/issues/170) - Add `custom_fields` to `netbox_virtual_machine`
- [#140](https://github.com/netbox-community/ansible_modules/issues/140) - Add `device_query_filters` and `vm_query_filters` to allow users to specify query filters for the specific type
- [#183](https://github.com/netbox-community/ansible_modules/issues/183) - Remove token from being required for nb_lookup as some NetBox setups don't require authorization for GET functions
- [#177](https://github.com/netbox-community/ansible_modules/issues/177) - Remove token from being required for nb_inventory as some NetBox setups don't require authorization for GET functions

### Ansible Core Related Changes

- [#124](https://github.com/netbox-community/ansible_modules/issues/124) - Added netbox_interface from Ansible core, but the module is deprecated in favor of netbox_device_interface and netbox_vm_interface

### Thanks for the following contributors!

- @DouglasHeriot
- @toerb
- @malbertus
- @ThomasADavis
- @Duck-dave
- @Jamboon-beurre
- @smolz
- @Yannis100
- @jqueuniet
- @ignatenkobrain
- @pugnacity
- @martink2

## v0.1.10

### Bug Fixes

- [#129](https://github.com/netbox-community/ansible_modules/pull/129) - Updated inventory plugin name from netbox.netbox.netbox to netbox.netbox.nb_inventory

### Thanks to the following contributors!

@smolz

## v0.1.9

### Overview

This version has a few breaking changes due to new namespace and collection name. I felt it necessary to change the name of the lookup plugin and inventory plugin just not to have a non descriptive namespace call to use them. Below is an example:
`netbox.netbox.netbox` would be used for both inventory plugin and lookup plugin, but in different contexts so no collision will arise, but confusion will.

I renamed the lookup plugin to `nb_lookup` so it will be used with the FQCN `netbox.netbox.nb_lookup`.

The inventory plugin will now be called within an inventory file by `netbox.netbox.nb_inventory`

### Bug Fixes

- [#120](https://github.com/netbox-community/ansible_modules/pull/120) - Update netbox_tenant and netbox_tenant_group to use slugs for searching (available since NetBox 2.6). Added slug options to netbox_site, netbox_tenant, netbox_tenant_group

## v.1.8

### Bug Fixes

- [#114](https://github.com/netbox-community/ansible_modules/issues/114) - If interface existed already, caused traceback and crashed playbook

## v.1.7

### New Features

- [#58](https://github.com/netbox-community/ansible_modules/issues/58) - Added fetching services for devices in Netbox Inventory Plugin
- [#62](https://github.com/netbox-community/ansible_modules/issues/62) - Change lookups to property for subclassing of inventory plugin
- [#60](https://github.com/netbox-community/ansible_modules/issues/60) - Added option for interfaces and IP addresses of interfaces to be fetched via inventory plugin

### Bug Fixes

- [#95](https://github.com/netbox-community/ansible_modules/issues/95) - Updated _to_slug to follow same constructs NetBox uses
- [#105](https://github.com/netbox-community/ansible_modules/issues/105) - Properly create interface on correct device when in a VC
- [#106](https://github.com/netbox-community/ansible_modules/issues/106) - Assigning to parent log now finds LAG interface type dynamically rather than set statically in code
- [#107](https://github.com/netbox-community/ansible_modules/issues/107) - Create device with empty string to assign the device a UUID
- [#63](https://github.com/netbox-community/ansible_modules/issues/63) - If query_filters supplied are not allowed for either device or VM lookups, or no valid query filters, it will not attempt to fetch from devices or VMs. This should prevent devices or VMs from being fetched that do not meet the query_filters specified.

### Thanks to following contributors!

@TawR1024
@tkspuk
@Jamboon-beurre
@ignatakenkobrain
@ollybee
@loganbest
@ChrisPortman
@mkeetman
@tyler-8


## v0.1.6

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
