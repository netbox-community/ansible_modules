import pynetbox

nb = pynetbox.api("http://localhost:32768", "0123456789abcdef0123456789abcdef01234567")
tenants = [{"name": "Test Tenant", "slug": "test-tenant"}]
created_tenants = nb.tenancy.tenants.create(tenants)
tenant_groups = [{"name": "Test Tenant Group", "slug": "test-tenant-group"}]
created_tenant_groups = nb.tenancy.tenant_groups.create(tenant_groups)
tenant = nb.tenancy.tenants.get(slug="test-tenant")
sites = [
    {"name": "Test Site", "slug": "test-site", "tenant": tenant.id},
    {"name": "Test Site2", "slug": "test-site2"},
]
created_sites = nb.dcim.sites.create(sites)
test_site = nb.dcim.sites.get(slug="test-site")
test_site2 = nb.dcim.sites.get(slug="test-site2")
prefixes = [
    {"prefix": "192.168.100.0/24", "site": test_site2.id},
    {"prefix": "10.10.0.0/16"},
]
created_prefixes = nb.ipam.prefixes.create(prefixes)
regions = [{"name": "Test Region", "slug": "test-region"}]
created_regions = nb.dcim.regions.create(regions)
vrfs = [{"name": "Test VRF", "rd": "1:1"}]
created_vrfs = nb.ipam.vrfs.create(vrfs)
vlan_groups = [
    {
        "name": "Test Vlan Group",
        "slug": "test-vlan-group",
        "site": test_site.id,
        "tenant": tenant.id,
    }
]
created_vlan_groups = nb.ipam.vlan_groups.create(vlan_groups)
vlan_group = nb.ipam.vlan_groups.get(slug="test-vlan-group")
vlans = [
    {"name": "Wireless", "vid": 100, "site": test_site.id},
    {"name": "Data", "vid": 200, "site": test_site.id},
    {"name": "VoIP", "vid": 300, "site": test_site.id},
    {
        "name": "Test VLAN",
        "vid": 400,
        "site": test_site.id,
        "tenant": tenant.id,
        "group": vlan_group.id,
    },
]
created_vlans = nb.ipam.vlans.create(vlans)
ipam_roles = [{"name": "Network of Care", "slug": "network-of-care"}]
create_ipam_roles = nb.ipam.roles.create(ipam_roles)
manufacturers = [
    {"name": "Cicsco", "slug": "cisco"},
    {"name": "Arista", "slug": "arista"},
]
created_manufacturers = nb.dcim.manufacturers.create(manufacturers)
cisco_manu = nb.dcim.manufacturers.get(slug="cisco")
arista_manu = nb.dcim.manufacturers.get(slug="arista")
device_types = [
    {"model": "Cisco Test", "slug": "cisco-test", "manufacturer": cisco_manu.id},
    {"model": "Arista Test", "slug": "arista-test", "manufacturer": arista_manu.id},
]
created_device_types = nb.dcim.device_types.create(device_types)
device_roles = [
    {"name": "Core Switch", "slug": "core-switch", "color": "aa1409", "vm_role": False}
]
created_device_roles = nb.dcim.device_roles.create(device_roles)
site_two = nb.dcim.sites.get(slug="test-site2")
racks = [{"name": "Test Rack", "slug": "test-rack", "site": site_two.id}]
created_racks = nb.dcim.racks.create(racks)
device_type = nb.dcim.device_types.get(slug="cisco-test")
device_role = nb.dcim.device_roles.get(slug="core-switch")
devices = [
    {
        "name": "test100",
        "device_type": device_type.id,
        "device_role": device_role.id,
        "site": test_site.id,
    },
    {
        "name": "TestDeviceR1",
        "device_type": device_type.id,
        "device_role": device_role.id,
        "site": test_site.id,
    },
    {
        "name": "R1-Device",
        "device_type": device_type.id,
        "device_role": device_role.id,
        "site": test_site.id,
    },
]
created_devices = nb.dcim.devices.create(devices)
device = nb.dcim.devices.get(name="test100")
interfaces = [
    {"name": "GigabitEthernet1", "device": device.id, "form_factor": 1000},
    {"name": "GigabitEthernet2", "device": device.id, "form_factor": 1000},
]
created_interfaces = nb.dcim.interfaces.create(interfaces)
