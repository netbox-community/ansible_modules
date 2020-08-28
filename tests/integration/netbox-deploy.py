#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import pynetbox

# NOTE: If anything depends on specific versions of NetBox, can check INTEGRATION_TESTS in env
# os.environ["INTEGRATION_TESTS"]


# Set nb variable to connect to Netbox and use the veriable in future calls
nb = pynetbox.api("http://localhost:32768", "0123456789abcdef0123456789abcdef01234567")


# ORDER OF OPERATIONS FOR THE MOST PART

## Create TENANTS
tenants = [{"name": "Test Tenant", "slug": "test-tenant"}]
created_tenants = nb.tenancy.tenants.create(tenants)
### Test Tenant to be used later on
test_tenant = nb.tenancy.tenants.get(slug="test-tenant")


## Create TENANT GROUPS
tenant_groups = [{"name": "Test Tenant Group", "slug": "test-tenant-group"}]
created_tenant_groups = nb.tenancy.tenant_groups.create(tenant_groups)


## Create Regions
regions = [
    {"name": "Test Region", "slug": "test-region"},
    {"name": "Parent Region", "slug": "parent-region"},
    {"name": "Other Region", "slug": "other-region"},
]
created_regions = nb.dcim.regions.create(regions)
### Region variables to be used later on
parent_region = nb.dcim.regions.get(slug="parent-region")
test_region = nb.dcim.regions.get(slug="test-region")

### Create relationship between regions
test_region.parent = parent_region
test_region.save()


## Create SITES and register variables
sites = [
    {
        "name": "Test Site",
        "slug": "test-site",
        "tenant": test_tenant.id,
        "region": test_region.id,
    },
    {"name": "Test Site2", "slug": "test-site2"},
]
created_sites = nb.dcim.sites.create(sites)
### Site variables to be used later on
test_site = nb.dcim.sites.get(slug="test-site")
test_site2 = nb.dcim.sites.get(slug="test-site2")


## Create VRFs
vrfs = [{"name": "Test VRF", "rd": "1:1"}]
created_vrfs = nb.ipam.vrfs.create(vrfs)


## Create PREFIXES
prefixes = [
    {"prefix": "192.168.100.0/24", "site": test_site2.id},
    {"prefix": "10.10.0.0/16"},
]
created_prefixes = nb.ipam.prefixes.create(prefixes)


## Create VLAN GROUPS
vlan_groups = [
    {
        "name": "Test Vlan Group",
        "slug": "test-vlan-group",
        "site": test_site.id,
        "tenant": test_tenant.id,
    }
]
created_vlan_groups = nb.ipam.vlan_groups.create(vlan_groups)
## VLAN Group variables to be used later on
test_vlan_group = nb.ipam.vlan_groups.get(slug="test-vlan-group")


## Create VLANS
vlans = [
    {"name": "Wireless", "vid": 100, "site": test_site.id},
    {"name": "Data", "vid": 200, "site": test_site.id},
    {"name": "VoIP", "vid": 300, "site": test_site.id},
    {
        "name": "Test VLAN",
        "vid": 400,
        "site": test_site.id,
        "tenant": test_tenant.id,
        "group": test_vlan_group.id,
    },
]
created_vlans = nb.ipam.vlans.create(vlans)


## Create IPAM Roles
ipam_roles = [{"name": "Network of care", "slug": "network-of-care"}]
create_ipam_roles = nb.ipam.roles.create(ipam_roles)


## Create Manufacturers
manufacturers = [
    {"name": "Cisco", "slug": "cisco"},
    {"name": "Arista", "slug": "arista"},
    {"name": "Test Manufactuer", "slug": "test-manufacturer"},
]
created_manufacturers = nb.dcim.manufacturers.create(manufacturers)
### Manufacturer variables to be used later on
cisco_manu = nb.dcim.manufacturers.get(slug="cisco")
arista_manu = nb.dcim.manufacturers.get(slug="arista")


## Create Device Types
device_types = [
    {"model": "Cisco Test", "slug": "cisco-test", "manufacturer": cisco_manu.id},
    {"model": "Arista Test", "slug": "arista-test", "manufacturer": arista_manu.id},
    {
        "model": "Nexus Parent",
        "slug": "nexus-parent",
        "u_height": 0,
        "manufacturer": cisco_manu.id,
        "subdevice_role": True,
    },
    {
        "model": "Nexus Child",
        "slug": "nexus-child",
        "u_height": 0,
        "manufacturer": cisco_manu.id,
        "subdevice_role": False,
    },
    {"model": "1841", "slug": "1841", "manufacturer": cisco_manu.id,},
]
created_device_types = nb.dcim.device_types.create(device_types)
### Device type variables to be used later on
cisco_test = nb.dcim.device_types.get(slug="cisco-test")
arista_test = nb.dcim.device_types.get(slug="arista-test")
nexus_parent = nb.dcim.device_types.get(slug="nexus-parent")
nexus_child = nb.dcim.device_types.get(slug="nexus-child")

## Create Device Roles
device_roles = [
    {"name": "Core Switch", "slug": "core-switch", "color": "aa1409", "vm_role": False},
    {
        "name": "Test VM Role",
        "slug": "test-vm-role",
        "color": "e91e63",
        "vm_role": True,
    },
    {
        "name": "Test VM Role 1",
        "slug": "test-vm-role-1",
        "color": "e91e65",
        "vm_role": True,
    },
]
created_device_roles = nb.dcim.device_roles.create(device_roles)
### Device role variables to be used later on
core_switch = nb.dcim.device_roles.get(slug="core-switch")


## Create Rack Groups
rack_groups = [
    {"name": "Test Rack Group", "slug": "test-rack-group", "site": test_site.id},
    {"name": "Parent Rack Group", "slug": "parent-rack-group", "site": test_site.id},
]
created_rack_groups = nb.dcim.rack_groups.create(rack_groups)

### Create Rack Group Parent relationship
created_rack_groups[0].parent = created_rack_groups[1]
created_rack_groups[0].save()

## Create Rack Roles
rack_roles = [{"name": "Test Rack Role", "slug": "test-rack-role", "color": "4287f5"}]
created_rack_roles = nb.dcim.rack_roles.create(rack_roles)

## Create Racks
racks = [
    {
        "name": "Test Rack Site 2",
        "site": test_site2.id,
        "role": created_rack_roles[0].id,
    },
    {"name": "Test Rack", "site": test_site.id, "group": created_rack_groups[0].id},
]
created_racks = nb.dcim.racks.create(racks)
test_rack = nb.dcim.racks.get(name="Test Rack")  # racks don't have slugs
test_rack_site2 = nb.dcim.racks.get(name="Test Rack Site 2")


## Create Devices
devices = [
    {
        "name": "test100",
        "device_type": cisco_test.id,
        "device_role": core_switch.id,
        "site": test_site.id,
        "local_context_data": {"ntp_servers": ["pool.ntp.org"]},
    },
    {
        "name": "TestDeviceR1",
        "device_type": cisco_test.id,
        "device_role": core_switch.id,
        "site": test_site.id,
        "rack": test_rack.id,
    },
    {
        "name": "R1-Device",
        "device_type": cisco_test.id,
        "device_role": core_switch.id,
        "site": test_site2.id,
        "rack": test_rack_site2.id,
    },
    {
        "name": "Test Nexus One",
        "device_type": nexus_parent.id,
        "device_role": core_switch.id,
        "site": test_site.id,
    },
    {
        "name": "Test Nexus Child One",
        "device_type": nexus_child.id,
        "device_role": core_switch.id,
        "site": test_site.id,
    },
]
created_devices = nb.dcim.devices.create(devices)
### Device variables to be used later on
test100 = nb.dcim.devices.get(name="test100")

# Create VC, assign member, create initial interface
created_vcs = nb.dcim.virtual_chassis.create({"master": 4})
nexus_child = nb.dcim.devices.get(5)
nexus_child.update({"virtual_chassis": 1, "vc_position": 1})
nexus = nb.dcim.devices.get(4)
nexus.update({"vc_position": 0})
nexus_interfaces = [
    {"device": nexus.id, "name": "Ethernet1/1", "type": 1000},
    {"device": nexus_child.id, "name": "Ethernet2/1", "type": 1000},
]
created_nexus_interfaces = nb.dcim.interfaces.create(nexus_interfaces)

## Create Interfaces
dev_interfaces = [
    {"name": "GigabitEthernet1", "device": test100.id, "type": 1000},
    {"name": "GigabitEthernet2", "device": test100.id, "type": 1000},
]
created_interfaces = nb.dcim.interfaces.create(dev_interfaces)
## Interface variables to be used later on
test100_gi1 = nb.dcim.interfaces.get(name="GigabitEthernet1", device_id=1)
test100_gi2 = nb.dcim.interfaces.get(name="GigabitEthernet2", device_id=1)


## Create IP Addresses
ip_addresses = [
    {"address": "172.16.180.1/24", "interface": test100_gi1.id},
    {"address": "2001::1:1/64", "interface": test100_gi2.id},
    {"address": "172.16.180.11/24", "interface": created_nexus_interfaces[0].id},
    {"address": "172.16.180.12/24", "interface": created_nexus_interfaces[1].id},
    {"address": "172.16.180.254/24"},
]
created_ip_addresses = nb.ipam.ip_addresses.create(ip_addresses)


## Create RIRs
rirs = [{"name": "Example RIR", "slug": "example-rir"}]
created_rirs = nb.ipam.rirs.create(rirs)

## Create Cluster Group
cluster_groups = [{"name": "Test Cluster Group", "slug": "test-cluster-group"}]
created_cluster_groups = nb.virtualization.cluster_groups.create(cluster_groups)
test_cluster_group = nb.virtualization.cluster_groups.get(slug="test-cluster-group")

## Create Cluster Type
cluster_types = [{"name": "Test Cluster Type", "slug": "test-cluster-type"}]
created_cluster_types = nb.virtualization.cluster_types.create(cluster_types)
test_cluster_type = nb.virtualization.cluster_types.get(slug="test-cluster-type")

## Create Cluster
clusters = [
    {
        "name": "Test Cluster",
        "type": test_cluster_type.id,
        "group": test_cluster_group.id,
        "site": test_site.id,
    },
    {"name": "Test Cluster 2", "type": test_cluster_type.id,},
]
created_clusters = nb.virtualization.clusters.create(clusters)
test_cluster = nb.virtualization.clusters.get(name="Test Cluster")
test_cluster2 = nb.virtualization.clusters.get(name="Test Cluster 2")

## Create Virtual Machine
virtual_machines = [
    {"name": "test100-vm", "cluster": test_cluster.id},
    {"name": "test101-vm", "cluster": test_cluster.id},
    {"name": "test102-vm", "cluster": test_cluster.id},
    {"name": "test103-vm", "cluster": test_cluster.id},
    {"name": "test104-vm", "cluster": test_cluster2.id},
    {"name": "Test VM With Spaces", "cluster": test_cluster2.id},
]
created_virtual_machines = nb.virtualization.virtual_machines.create(virtual_machines)
test100_vm = nb.virtualization.virtual_machines.get(name="test100-vm")
test101_vm = nb.virtualization.virtual_machines.get(name="test101-vm")
test_spaces_vm = nb.virtualization.virtual_machines.get(name="Test VM With Spaces")

## Create Virtual Machine Interfaces
virtual_machines_intfs = [
    # Create test100-vm intfs
    {"name": "Eth0", "virtual_machine": test100_vm.id},
    {"name": "Eth1", "virtual_machine": test100_vm.id},
    {"name": "Eth2", "virtual_machine": test100_vm.id},
    {"name": "Eth3", "virtual_machine": test100_vm.id},
    {"name": "Eth4", "virtual_machine": test100_vm.id},
    # Create test101-vm intfs
    {"name": "Eth0", "virtual_machine": test101_vm.id},
    {"name": "Eth1", "virtual_machine": test101_vm.id},
    {"name": "Eth2", "virtual_machine": test101_vm.id},
    {"name": "Eth3", "virtual_machine": test101_vm.id},
    {"name": "Eth4", "virtual_machine": test101_vm.id},
    # Create Test VM With Spaces intfs
    {"name": "Eth0", "virtual_machine": test_spaces_vm.id},
    {"name": "Eth1", "virtual_machine": test_spaces_vm.id},
]
created_virtual_machines_intfs = nb.virtualization.interfaces.create(
    virtual_machines_intfs
)


## Create Services
services = [
    {"device": test100.id, "name": "ssh", "port": 22, "protocol": "tcp"},
    {
        "device": test100.id,
        "name": "http",
        "port": 80,
        "protocol": "tcp",
        "ipaddresses": [created_ip_addresses[0].id, created_ip_addresses[1].id],
    },
    {"device": nexus.id, "name": "telnet", "port": 23, "protocol": "tcp"},
    {
        "virtual_machine": test_spaces_vm.id,
        "name": "ssh",
        "port": 22,
        "protocol": "tcp",
    },
]
created_services = nb.ipam.services.create(services)


## Create Circuit Provider
providers = [{"name": "Test Provider", "slug": "test-provider"}]
created_providers = nb.circuits.providers.create(providers)
test_provider = nb.circuits.providers.get(slug="test-provider")

## Create Circuit Type
circuit_types = [{"name": "Test Circuit Type", "slug": "test-circuit-type"}]
created_circuit_types = nb.circuits.circuit_types.create(circuit_types)
test_circuit_type = nb.circuits.circuit_types.get(slug="test-circuit-type")

## Create Circuit
circuits = [
    {"cid": "Test Circuit", "provider": test_provider.id, "type": test_circuit_type.id}
]
created_circuits = nb.circuits.circuits.create(circuits)
