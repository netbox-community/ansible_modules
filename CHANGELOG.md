# Changelog

## v0.1.2

### Bug Fixes
- [#47](https://github.com/FragmentedPacket/netbox_modules/issues/47) - Allow endpoint choices to be an integer of the choice rather than attempting to dynamically determine the choice ID

## v0.1.1

### Bug Fixes

- [#40](https://github.com/FragmentedPacket/netbox_modules/issues/40) - Fixed issue with netbox_vm_interface where it would fail if different virtual machine had the same interface name
- [#40](https://github.com/FragmentedPacket/netbox_modules/issues/40) - Updated netbox_ip_address to find interfaces on virtual machines correctly

## v0.1.0

### Breaking Changes

- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Changed role to prefix_role in netbox_prefix.py
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Changed group to tenant_group in netbox_tenant.py
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Renamed netbox_interface to netbox_device_interface
- [#24](https://github.com/FragmentedPacket/netbox_modules/issues/24) - Module failures when required fields arent provided

### New Modules / Plugins

- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_device_role
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_device_type
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_ipam_role
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_manufacturer
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_platform
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_rack
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_rack_group
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_rack_role
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_vlan_group
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_vlan
- [#9](https://github.com/FragmentedPacket/netbox_modules/issues/9) - Added netbox_vrf
- [#12](https://github.com/FragmentedPacket/netbox_modules/issues/12) - Added netbox_rir
- [#14](https://github.com/FragmentedPacket/netbox_modules/issues/14) - Added netbox_aggregate
- [#14](https://github.com/FragmentedPacket/netbox_modules/issues/14) - Added netbox_services
- [#15](https://github.com/FragmentedPacket/netbox_modules/issues/15) - Added netbox_region
- [#15](https://github.com/FragmentedPacket/netbox_modules/issues/15) - Added netbox_device_bay
- [#15](https://github.com/FragmentedPacket/netbox_modules/issues/15) - Added netbox_inventory_item
- [#26](https://github.com/FragmentedPacket/netbox_modules/issues/26) - Added netbox lookup plugin
- [#16](https://github.com/FragmentedPacket/netbox_modules/issues/16) - Added netbox_virtual_machine
- [#16](https://github.com/FragmentedPacket/netbox_modules/issues/16) - Added netbox_vm_interface
- [#16](https://github.com/FragmentedPacket/netbox_modules/issues/16) - Added netbox_cluster_type
- [#16](https://github.com/FragmentedPacket/netbox_modules/issues/16) - Added netbox_cluster_group
- [#16](https://github.com/FragmentedPacket/netbox_modules/issues/16) - Added netbox_cluster
- [#17](https://github.com/FragmentedPacket/netbox_modules/issues/17) - Added netbox_provider
- [#17](https://github.com/FragmentedPacket/netbox_modules/issues/17) - Added netbox_circuit
- [#17](https://github.com/FragmentedPacket/netbox_modules/issues/17) - Added netbox_circuit_type
- [#17](https://github.com/FragmentedPacket/netbox_modules/issues/17) - Added netbox_circuit_termination

### Bug Fixes

### Enhancements

- [#10](https://github.com/FragmentedPacket/netbox_modules/issues/10) - Add primary_ip4/6 to netbox_ip_address
