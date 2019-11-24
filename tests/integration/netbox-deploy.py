import pynetbox

# Set nb variable to connec to Netbox and use the veriable in future calls
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


## Create SITES and register variables
sites = [
    {"name": "Test Site", "slug": "test-site", "tenant": test_tenant.id},
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


## Create Regions
regions = [{"name": "Test Region", "slug": "test-region"}]
created_regions = nb.dcim.regions.create(regions)


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
]
created_device_roles = nb.dcim.device_roles.create(device_roles)
### Device role variables to be used later on
core_switch = nb.dcim.device_roles.get(slug="core-switch")


## Create Racks
racks = [{"name": "Test Rack", "slug": "test-rack", "site": test_site2.id}]
created_racks = nb.dcim.racks.create(racks)


## Create Rack Groups
rack_groups = [
    {"name": "Test Rack Group", "slug": "test-rack-group", "site": test_site.id}
]
created_rack_groups = nb.dcim.rack_groups.create(rack_groups)


## Create Rack Roles
rack_roles = [{"name": "Test Rack Role", "slug": "test-rack-role", "color": "4287f5"}]
created_rack_roles = nb.dcim.rack_roles.create(rack_roles)


## Create Devices
devices = [
    {
        "name": "test100",
        "device_type": cisco_test.id,
        "device_role": core_switch.id,
        "site": test_site.id,
    },
    {
        "name": "TestDeviceR1",
        "device_type": cisco_test.id,
        "device_role": core_switch.id,
        "site": test_site.id,
    },
    {
        "name": "R1-Device",
        "device_type": cisco_test.id,
        "device_role": core_switch.id,
        "site": test_site.id,
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


## Create Interfaces
interfaces = [
    {"name": "GigabitEthernet1", "device": test100.id, "form_factor": 1000},
    {"name": "GigabitEthernet2", "device": test100.id, "form_factor": 1000},
]
created_interfaces = nb.dcim.interfaces.create(interfaces)
## Interface variables to be used later on
test100_gi1 = nb.dcim.interfaces.get(name="GigabitEthernet1", device_id=1)
test100_gi2 = nb.dcim.interfaces.get(name="GigabitEthernet2", device_id=1)


## Create IP Addresses
ip_addresses = [
    {"address": "172.16.180.1/24", "interface": test100_gi1.id},
    {"address": "2001::1:1/64", "interface": test100_gi2.id},
]
created_ip_addresses = nb.ipam.ip_addresses.create(ip_addresses)

## Create RIRs
rirs = [{"name": "Example RIR", "slug": "example-rir"}]
created_rirs = nb.ipam.rirs.create(rirs)

## Create Cluster Group
cluster_groups = [{"name": "Test Cluster Group", "slug": "test-cluster-group"}]
created_cluster_groups = nb.virtualization.cluster_groups.create(cluster_groups)

## Create Cluster Type
cluster_types = [{"name": "Test Cluster Type", "slug": "test-cluster-type"}]
created_cluster_types = nb.virtualization.cluster_types.create(cluster_types)
test_cluster_type = nb.virtualization.cluster_types.get(slug="test-cluster-type")

## Create Cluster
clusters = [
    {"name": "Test Cluster", "type": test_cluster_type.id, "site": test_site.id}
]
created_clusters = nb.virtualization.clusters.create(clusters)
test_cluster = nb.virtualization.clusters.get(name="Test Cluster")

## Create Virtual Machine
virtual_machines = [{"name": "test100-vm", "cluster": test_cluster.id}]
created_virtual_machines = nb.virtualization.virtual_machines.create(virtual_machines)

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
