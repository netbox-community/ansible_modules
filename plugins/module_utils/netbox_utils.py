# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@fragmentedpacket) <mikhail.yohman@gmail.com>
# Copyright: (c) 2018, David Gomez (@amb1s1) <david.gomez@networktocode.com>
# Copyright: (c) 2020, Nokia, Tobias Groß (@toerb) <tobias.gross@nokia.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Import necessary packages
import traceback
import re
import json
from itertools import chain

from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils._text import to_native
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.basic import AnsibleModule, missing_required_lib, _load_params
from ansible.module_utils.urls import open_url

PYNETBOX_IMP_ERR = None
try:
    import pynetbox
    import requests

    HAS_PYNETBOX = True
except ImportError:
    PYNETBOX_IMP_ERR = traceback.format_exc()
    HAS_PYNETBOX = False

# Used to map endpoints to applications dynamically
API_APPS_ENDPOINTS = dict(
    circuits=[
        "circuits",
        "circuit_types",
        "circuit_terminations",
        "providers",
        "provider_networks",
    ],
    dcim=[
        "cables",
        "console_ports",
        "console_port_templates",
        "console_server_ports",
        "console_server_port_templates",
        "device_bays",
        "device_bay_templates",
        "devices",
        "device_roles",
        "device_types",
        "front_ports",
        "front_port_templates",
        "interfaces",
        "interface_templates",
        "inventory_items",
        "inventory_item_roles",
        "locations",
        "manufacturers",
        "module_types",
        "platforms",
        "power_feeds",
        "power_outlets",
        "power_outlet_templates",
        "power_panels",
        "power_ports",
        "power_port_templates",
        "racks",
        "rack_groups",
        "rack_roles",
        "rear_ports",
        "rear-ports",
        "rear_port_templates",
        "regions",
        "sites",
        "site_groups",
        "virtual_chassis",
    ],
    extras=[
        "config_contexts",
        "tags",
        "custom_fields",
        "custom_links",
        "export_templates",
        "journal_entries",
        "webhooks",
    ],
    ipam=[
        "aggregates",
        "asns",
        "fhrp_groups",
        "fhrp_group_assignments",
        "ip_addresses",
        "l2vpns",
        "l2vpn_terminations",
        "prefixes",
        "rirs",
        "roles",
        "route_targets",
        "service_templates",
        "vlans",
        "vlan_groups",
        "vrfs",
        "services",
    ],
    secrets=[],
    tenancy=["tenants", "tenant_groups", "contacts", "contact_groups", "contact_roles"],
    virtualization=[
        "cluster_groups",
        "cluster_types",
        "clusters",
        "virtual_machines",
    ],
    wireless=["wireless_lans", "wireless_lan_groups", "wireless_links"],
)

# Used to normalize data for the respective query types used to find endpoints
QUERY_TYPES = dict(
    asn="asn",
    circuit="cid",
    circuit_termination="circuit",
    circuit_type="slug",
    cluster="name",
    cluster_group="slug",
    cluster_type="slug",
    config_context="name",
    contact_group="name",
    contact_role="name",
    custom_field="name",
    custom_link="name",
    device="name",
    device_role="slug",
    device_type="slug",
    export_targets="name",
    export_template="name",
    fhrp_groups="group_id",
    fhrp_group_assignments="id",
    group="slug",
    installed_device="name",
    inventory_item_role="name",
    import_targets="name",
    l2vpn="name",
    l2vpn_termination="id",
    location="slug",
    manufacturer="slug",
    module_type="model",
    nat_inside="address",
    nat_outside="address",
    parent_contact_group="name",
    parent_location="slug",
    parent_region="slug",
    parent_site_group="slug",
    parent_tenant_group="slug",
    parent_wireless_lan_group="slug",
    power_panel="name",
    power_port="name",
    power_port_template="name",
    platform="slug",
    prefix_role="slug",
    primary_ip="address",
    primary_ip4="address",
    primary_ip6="address",
    provider="slug",
    provider_network="name",
    rack="name",
    rack_group="slug",
    rack_role="slug",
    rear_port="name",
    rear_port_template="name",
    region="slug",
    rir="slug",
    route_targets="name",
    service_templates="name",
    slug="slug",
    site="slug",
    site_group="slug",
    tenant="slug",
    tenant_group="slug",
    time_zone="timezone",
    virtual_chassis="name",
    virtual_machine="name",
    virtual_machine_role="slug",
    vlan="name",
    vlan_group="slug",
    vlan_role="name",
    vrf="name",
    webhook="name",
    wireless_lan="ssid",
    wireless_lan_group="slug",
)

# Specifies keys within data that need to be converted to ID and the endpoint to be used when queried
CONVERT_TO_ID = {
    "assigned_object": "assigned_object",
    "bridge": "interfaces",
    "circuit": "circuits",
    "circuit_type": "circuit_types",
    "circuit_termination": "circuit_terminations",
    "circuits.circuittermination": "circuit_terminations",
    "cluster": "clusters",
    "clusters": "clusters",
    "cluster_group": "cluster_groups",
    "cluster_groups": "cluster_groups",
    "cluster_type": "cluster_types",
    "cluster_types": "cluster_types",
    "config_context": "config_contexts",
    "contact_groups": "contact_groups",
    "dcim.consoleport": "console_ports",
    "dcim.consoleserverport": "console_server_ports",
    "dcim.frontport": "front_ports",
    "dcim.interface": "interfaces",
    "dcim.powerfeed": "power_feeds",
    "dcim.poweroutlet": "power_outlets",
    "dcim.powerport": "power_ports",
    "dcim.rearport": "rear_ports",
    "device": "devices",
    "device_role": "device_roles",
    "device_type": "device_types",
    "device_types": "device_types",
    "export_targets": "route_targets",
    "group": "tenant_groups",
    "import_targets": "route_targets",
    "installed_device": "devices",
    "interface": "interfaces",
    "interface_a": "interfaces",
    "interface_b": "interfaces",
    "interface_template": "interface_templates",
    "ip_addresses": "ip_addresses",
    "ipaddresses": "ip_addresses",
    "location": "locations",
    "lag": "interfaces",
    "manufacturer": "manufacturers",
    "master": "devices",
    "nat_inside": "ip_addresses",
    "nat_outside": "ip_addresses",
    "platform": "platforms",
    "parent_contact_group": "contact_groups",
    "parent_location": "locations",
    "parent_interface": "interfaces",
    "parent_inventory_item": "inventory_items",
    "parent_vm_interface": "interfaces",
    "parent_region": "regions",
    "parent_site_group": "site_groups",
    "parent_tenant_group": "tenant_groups",
    "parent_wireless_lan_group": "wireless_lan_groups",
    "platforms": "platforms",
    "power_panel": "power_panels",
    "power_port": "power_ports",
    "power_port_template": "power_port_templates",
    "prefix_role": "roles",
    "primary_ip": "ip_addresses",
    "primary_ip4": "ip_addresses",
    "primary_ip6": "ip_addresses",
    "provider": "providers",
    "provider_network": "provider_networks",
    "rack": "racks",
    "rack_group": "rack_groups",
    "rack_role": "rack_roles",
    "region": "regions",
    "regions": "regions",
    "rear_port": "rear_ports",
    "rear_port_template": "rear_port_templates",
    "rir": "rirs",
    "roles": "device_roles",
    "route_targets": "route_targets",
    # Just a placeholder as scope can be several different types including sites.
    "scope": "sites",
    "services": "services",
    "service_templates": "service_templates",
    "site": "sites",
    "site_groups": "site_groups",
    "site_group": "site_groups",
    "sites": "sites",
    "tags": "tags",
    "tagged_vlans": "vlans",
    "tenant": "tenants",
    "tenants": "tenants",
    "tenant_group": "tenant_groups",
    "tenant_groups": "tenant_groups",
    "termination_a": "interfaces",
    "termination_b": "interfaces",
    "untagged_vlan": "vlans",
    "virtual_chassis": "virtual_chassis",
    "virtual_machine": "virtual_machines",
    "virtual_machine_role": "device_roles",
    "vm_bridge": "interfaces",
    "vlan": "vlans",
    "vlan_group": "vlan_groups",
    "vlan_role": "roles",
    "vrf": "vrfs",
    "wireless_lan": "wireless_lans",
    "wireless_lan_group": "wireless_lan_groups",
    "wireless_link": "wireless_links",
}

ENDPOINT_NAME_MAPPING = {
    "aggregates": "aggregate",
    "asns": "asn",
    "cables": "cable",
    "circuit_terminations": "circuit_termination",
    "circuit_types": "circuit_type",
    "circuits": "circuit",
    "clusters": "cluster",
    "cluster_groups": "cluster_group",
    "cluster_types": "cluster_type",
    "config_contexts": "config_context",
    "console_ports": "console_port",
    "console_port_templates": "console_port_template",
    "console_server_ports": "console_server_port",
    "console_server_port_templates": "console_server_port_template",
    "contacts": "contact",
    "contact_groups": "contact_group",
    "contact_roles": "contact_role",
    "custom_fields": "custom_field",
    "custom_links": "custom_link",
    "device_bays": "device_bay",
    "device_bay_templates": "device_bay_template",
    "devices": "device",
    "device_roles": "device_role",
    "device_types": "device_type",
    "export_templates": "export_template",
    "fhrp_groups": "fhrp_group",
    "fhrp_group_assignments": "fhrp_group_assignment",
    "front_ports": "front_port",
    "front_port_templates": "front_port_template",
    "journal_entries": "journal_entry",
    "interfaces": "interface",
    "interface_templates": "interface_template",
    "inventory_items": "inventory_item",
    "inventory_item_roles": "inventory_item_role",
    "ip_addresses": "ip_address",
    "l2vpns": "l2vpn",
    "l2vpn_terminations": "l2vpn_termination",
    "locations": "location",
    "manufacturers": "manufacturer",
    "module_types": "module_type",
    "platforms": "platform",
    "power_feeds": "power_feed",
    "power_outlets": "power_outlet",
    "power_outlet_templates": "power_outlet_template",
    "power_panels": "power_panel",
    "power_ports": "power_port",
    "power_port_templates": "power_port_template",
    "prefixes": "prefix",
    "providers": "provider",
    "provider_networks": "provider_network",
    "racks": "rack",
    "rack_groups": "rack_group",
    "rack_roles": "rack_role",
    "rear_ports": "rear_port",
    "rear-ports": "rearport",
    "rear_port_templates": "rear_port_template",
    "regions": "region",
    "rirs": "rir",
    "roles": "role",
    "route_targets": "route_target",
    "service_templates": "service_template",
    "services": "services",
    "sites": "site",
    "site_groups": "site_group",
    "tags": "tags",
    "tenants": "tenant",
    "tenant_groups": "tenant_group",
    "virtual_chassis": "virtual_chassis",
    "virtual_machines": "virtual_machine",
    "vlans": "vlan",
    "vlan_groups": "vlan_group",
    "vrfs": "vrf",
    "webhooks": "webhook",
    "wireless_lans": "wireless_lan",
    "wireless_lan_groups": "wireless_lan_group",
    "wireless_links": "wireless_link",
}

ALLOWED_QUERY_PARAMS = {
    "aggregate": set(["prefix", "rir"]),
    "asn": set(["asn"]),
    "assigned_object": set(["name", "device", "virtual_machine"]),
    "bridge": set(["name", "device"]),
    "circuit": set(["cid"]),
    "circuit_type": set(["slug"]),
    "circuit_termination": set(["circuit", "term_side"]),
    "circuits.circuittermination": set(["circuit", "term_side"]),
    "cluster": set(["name", "type"]),
    "cluster_group": set(["slug"]),
    "cluster_type": set(["slug"]),
    "config_context": set(
        [
            "name",
            "regions",
            "site_groups",
            "sites",
            "roles",
            "device_types",
            "platforms",
            "cluster_types",
            "cluster_groups",
            "clusters",
            "tenant_groups",
            "tenants",
            "tags",
        ]
    ),
    "console_port": set(["name", "device"]),
    "console_port_template": set(["name", "device_type"]),
    "console_server_port": set(["name", "device"]),
    "console_server_port_template": set(["name", "device_type"]),
    "contact": set(["name", "group"]),
    "contact_group": set(["name"]),
    "contact_role": set(["name"]),
    "custom_field": set(["name"]),
    "custom_link": set(["name"]),
    "dcim.consoleport": set(["name", "device"]),
    "dcim.consoleserverport": set(["name", "device"]),
    "dcim.frontport": set(["name", "device", "rear_port"]),
    "dcim.interface": set(["name", "device", "virtual_machine"]),
    "dcim.powerfeed": set(["name", "power_panel"]),
    "dcim.poweroutlet": set(["name", "device"]),
    "dcim.powerport": set(["name", "device"]),
    "dcim.rearport": set(["name", "device"]),
    "device_bay": set(["name", "device"]),
    "device_bay_template": set(["name", "device_type"]),
    "device": set(["name"]),
    "device_role": set(["slug"]),
    "device_type": set(["slug"]),
    "export_template": set(["name"]),
    "fhrp_group": set(
        ["id", "group_id", "interface_type", "device", "virtual_machine"]
    ),
    "fhrp_group_assignment": set(["group", "interface_type", "interface_id"]),
    "front_port": set(["name", "device", "rear_port"]),
    "front_port_template": set(["name", "device_type", "rear_port"]),
    "installed_device": set(["name"]),
    "interface": set(["name", "device", "virtual_machine"]),
    "interface_a": set(["name", "device"]),
    "interface_b": set(["name", "device"]),
    "interface_template": set(["name", "device_type"]),
    "inventory_item": set(["name", "device"]),
    "inventory_item_role": set(["name"]),
    "ip_address": set(["address", "vrf", "device", "interface", "assigned_object"]),
    "ip_addresses": set(["address", "vrf", "device", "interface", "assigned_object"]),
    "ipaddresses": set(
        ["address", "vrf", "device", "interface", "assigned_object", "virtual_machine"]
    ),
    "l2vpn": set(["name"]),
    "l2vpn_termination": set(
        ["l2vpn", "assigned_object_type", "interface_id", "vlan_id", "vminterface_id"]
    ),
    "lag": set(["name"]),
    "location": set(["name", "slug", "site"]),
    "module_type": set(["model"]),
    "manufacturer": set(["slug"]),
    "master": set(["name"]),
    "nat_inside": set(["vrf", "address"]),
    "parent_contact_group": set(["name"]),
    "parent_location": set(["slug"]),
    "parent_interface": set(["name"]),
    "parent_inventory_item": set(["name", "device"]),
    "parent_vm_interface": set(["name"]),
    "parent_region": set(["slug"]),
    "parent_site_group": set(["slug"]),
    "parent_tenant_group": set(["slug"]),
    "platform": set(["slug"]),
    "power_feed": set(["name", "power_panel"]),
    "power_outlet": set(["name", "device"]),
    "power_outlet_template": set(["name", "device_type"]),
    "power_panel": set(["name", "site"]),
    "power_port": set(["name", "device"]),
    "power_port_template": set(["name", "device_type"]),
    "prefix": set(["prefix", "vrf"]),
    "primary_ip4": set(["address", "vrf"]),
    "primary_ip6": set(["address", "vrf"]),
    "provider": set(["slug"]),
    "provider_network": set(["name"]),
    "rack": set(["name", "site", "location"]),
    "rack_group": set(["slug"]),
    "rack_role": set(["slug"]),
    "region": set(["slug"]),
    "rear_port": set(["name", "device"]),
    "rear_port_template": set(["name", "device_type"]),
    "rir": set(["slug"]),
    "role": set(["slug"]),
    "route_target": set(["name"]),
    "services": set(["device", "virtual_machine", "name", "port", "protocol"]),
    "service_template": set(["name"]),
    "site": set(["slug", "name"]),
    "site_group": set(["slug"]),
    "tags": set(["slug"]),
    "tagged_vlans": set(["group", "name", "site", "vid", "vlan_group", "tenant"]),
    "tenant": set(["slug"]),
    "tenant_group": set(["slug"]),
    "termination_a": set(["name", "device", "virtual_machine"]),
    "termination_b": set(["name", "device", "virtual_machine"]),
    "untagged_vlan": set(["group", "name", "site", "vid", "vlan_group", "tenant"]),
    "virtual_chassis": set(["name", "master"]),
    "virtual_machine": set(["name", "cluster"]),
    "vm_bridge": set(["name"]),
    "vlan": set(["group", "name", "site", "tenant", "vid", "vlan_group"]),
    "vlan_group": set(["name", "slug", "site", "scope"]),
    "vrf": set(["name", "tenant"]),
    "webhook": set(["name"]),
    "wireless_lan": set(["ssid"]),
    "wireless_lan_group": set(["name"]),
    "wireless_link": set(["interface_a", "interface_b"]),
}

QUERY_PARAMS_IDS = set(
    [
        "circuit",
        "cluster",
        "device",
        "group",
        "interface",
        "location",
        "rir",
        "vrf",
        "site",
        "scope",
        "tenant",
        "type",
        "virtual_machine",
        "rack",
    ]
)

REQUIRED_ID_FIND = {
    "cables": set(["status", "type", "length_unit"]),
    "circuits": set(["status"]),
    "console_ports": set(["type"]),
    "console_port_templates": set(["type"]),
    "console_server_ports": set(["type"]),
    "console_server_port_templates": set(["type"]),
    "devices": set(["status", "face"]),
    "device_types": set(["subdevice_role"]),
    "front_ports": set(["type"]),
    "front_port_templates": set(["type"]),
    "interfaces": set(["form_factor", "mode", "type"]),
    "interface_templates": set(["type"]),
    "ip_addresses": set(["status", "role"]),
    "prefixes": set(["status"]),
    "power_feeds": set(["status", "type", "supply", "phase"]),
    "power_outlets": set(["type", "feed_leg"]),
    "power_outlet_templates": set(["type", "feed_leg"]),
    "power_ports": set(["type"]),
    "power_port_templates": set(["type"]),
    "racks": set(["status", "outer_unit", "type"]),
    "rear_ports": set(["type"]),
    "rear_port_templates": set(["type"]),
    "services": set(["protocol"]),
    "sites": set(["status"]),
    "virtual_machines": set(["status", "face"]),
    "vlans": set(["status"]),
}

# This is used to map non-clashing keys to NetBox API compliant keys to prevent bad logic in code for similar keys but different modules
CONVERT_KEYS = {
    "assigned_object": "assigned_object_id",
    "scope": "scope_id",
    "circuit_type": "type",
    "cluster_type": "type",
    "cluster_group": "group",
    "contact_group": "group",
    "fhrp_group": "group",
    "parent_contact_group": "parent",
    "parent_location": "parent",
    "parent_interface": "parent",
    "parent_inventory_item": "parent",
    "parent_vm_interface": "parent",
    "parent_region": "parent",
    "parent_site_group": "parent",
    "parent_tenant_group": "parent",
    "parent_wireless_lan_group": "parent",
    "power_port_template": "power_port",
    "prefix_role": "role",
    "rack_group": "group",
    "rack_role": "role",
    "rear_port_template": "rear_port",
    "rear_port_template_position": "rear_port_position",
    "site_group": "group",
    "tenant_group": "group",
    "termination_a": "termination_a_id",
    "termination_b": "termination_b_id",
    "virtual_machine_role": "role",
    "vlan_role": "role",
    "vlan_group": "group",
    "vm_bridge": "bridge",
    "wireless_lan_group": "group",
}

# This is used to dynamically convert name to slug on endpoints requiring a slug
SLUG_REQUIRED = {
    "circuit_types",
    "cluster_groups",
    "cluster_types",
    "contact_groups",
    "contact_roles",
    "device_roles",
    "device_types",
    "inventory_item_roles",
    "ipam_roles",
    "l2vpns",
    "locations",
    "rack_groups",
    "rack_roles",
    "regions",
    "rirs",
    "roles",
    "sites",
    "site_groups",
    "tags",
    "tenants",
    "tenant_groups",
    "manufacturers",
    "platforms",
    "providers",
    "vlan_groups",
    "wireless_lan_groups",
}

SCOPE_TO_ENDPOINT = {
    "dcim.location": "locations",
    "dcim.rack": "racks",
    "dcim.region": "regions",
    "dcim.site": "sites",
    "dcim.sitegroup": "site_groups",
    "virtualization.cluster": "clusters",
    "virtualization.clustergroup": "cluster_groups",
}

NETBOX_ARG_SPEC = dict(
    netbox_url=dict(type="str", required=True),
    netbox_token=dict(type="str", required=True, no_log=True),
    state=dict(required=False, default="present", choices=["present", "absent"]),
    query_params=dict(required=False, type="list", elements="str"),
    validate_certs=dict(type="raw", default=True),
    cert=dict(type="raw", required=False),
)


class NetboxModule(object):
    """
    Initialize connection to NetBox, sets AnsibleModule passed in to
    self.module to be used throughout the class
    :params module (obj): Ansible Module object
    :params endpoint (str): Used to tell class which endpoint the logic needs to follow
    :params nb_client (obj): pynetbox.api object passed in (not required)
    """

    def __init__(self, module, endpoint, nb_client=None):
        self.module = module
        self.state = self.module.params["state"]
        self.check_mode = self.module.check_mode
        self.endpoint = endpoint
        query_params = self.module.params.get("query_params")

        if not HAS_PYNETBOX:
            self.module.fail_json(
                msg=missing_required_lib("pynetbox"), exception=PYNETBOX_IMP_ERR
            )
        # These should not be required after making connection to NetBox
        url = self.module.params["netbox_url"]
        token = self.module.params["netbox_token"]
        ssl_verify = self.module.params["validate_certs"]
        cert = self.module.params["cert"]

        # Attempt to initiate connection to NetBox
        if nb_client is None:
            self.nb = self._connect_netbox_api(url, token, ssl_verify, cert)
        else:
            self.nb = nb_client
            try:
                self.version = self.nb.version
                try:
                    self.full_version = self.nb.status().get("netbox-version")
                except Exception:
                    # For NetBox versions without /api/status endpoint
                    self.full_version = f"{self.version}.0"
            except AttributeError:
                self.module.fail_json(msg="Must have pynetbox >=4.1.0")

        # if self.module.params.get("query_params"):
        #    self._validate_query_params(self.module.params["query_params"])

        # These methods will normalize the regular data
        cleaned_data = self._remove_arg_spec_default(module.params["data"])
        norm_data = self._normalize_data(cleaned_data)
        choices_data = self._change_choices_id(self.endpoint, norm_data)
        data = self._find_ids(choices_data, query_params)
        self.data = self._convert_identical_keys(data)

    def _version_check_greater(self, greater, lesser, greater_or_equal=False):
        """Determine if first argument is greater than second argument.

        Args:
            greater (str): decimal string
            lesser (str): decimal string
        """
        g_major, g_minor = greater.split(".")
        l_major, l_minor = lesser.split(".")

        # convert to ints
        g_major = int(g_major)
        g_minor = int(g_minor)
        l_major = int(l_major)
        l_minor = int(l_minor)

        # If major version is higher then return true right off the bat
        if g_major > l_major:
            return True
        elif greater_or_equal and g_major == l_major and g_minor >= l_minor:
            return True
        # If major versions are equal, and minor version is higher, return True
        elif g_major == l_major and g_minor > l_minor:
            return True

        return False

    def _connect_netbox_api(self, url, token, ssl_verify, cert):
        try:
            session = requests.Session()
            session.verify = ssl_verify
            if cert:
                session.cert = tuple(i for i in cert)
            nb = pynetbox.api(url, token=token)
            nb.http_session = session
            try:
                self.version = nb.version
                try:
                    self.full_version = nb.status().get("netbox-version")
                except Exception:
                    # For NetBox versions without /api/status endpoint
                    self.full_version = f"{self.version}.0"
            except AttributeError:
                self.module.fail_json(msg="Must have pynetbox >=4.1.0")
            except Exception:
                self.module.fail_json(
                    msg="Failed to establish connection to NetBox API"
                )
            return nb
        except Exception:
            self.module.fail_json(msg="Failed to establish connection to NetBox API")

    def _nb_endpoint_get(self, nb_endpoint, query_params, search_item):
        try:
            response = nb_endpoint.get(**query_params)
        except pynetbox.RequestError as e:
            self._handle_errors(msg=e.error)
        except ValueError:
            self._handle_errors(
                msg="More than one result returned for %s" % (search_item)
            )

        return response

    def _validate_query_params(self, query_params):
        """
        Validate query_params that are passed in by users to make sure
        they're valid and return error if they're not valid.
        """
        invalid_query_params = []

        app = self._find_app(self.endpoint)
        nb_app = getattr(self.nb, app)
        nb_endpoint = getattr(nb_app, self.endpoint)
        # Fetch the OpenAPI spec to perform validation against
        base_url = self.nb.base_url
        junk, endpoint_url = nb_endpoint.url.split(base_url)
        response = open_url(base_url + "/docs/?format=openapi")
        try:
            raw_data = to_text(response.read(), errors="surrogate_or_strict")
        except UnicodeError:
            self._handle_errors(
                msg="Incorrect encoding of fetched payload from NetBox API."
            )

        try:
            openapi = json.loads(raw_data)
        except ValueError:
            self._handle_errors(msg="Incorrect JSON payload returned: %s" % raw_data)

        valid_query_params = openapi["paths"][endpoint_url + "/"]["get"]["parameters"]

        # Loop over passed in params and add to invalid_query_params and then fail if non-empty
        for param in query_params:
            if param not in valid_query_params:
                invalid_query_params.append(param)

        if invalid_query_params:
            self._handle_errors(
                "The following query_params are invalid: {0}".format(
                    ", ".join(invalid_query_params)
                )
            )

    def _handle_errors(self, msg):
        """
        Returns message and changed = False
        :params msg (str): Message indicating why there is no change
        """
        if msg:
            self.module.fail_json(msg=msg, changed=False)

    def _build_diff(self, before=None, after=None):
        """Builds diff of before and after changes"""
        return {"before": before, "after": after}

    def _convert_identical_keys(self, data):
        """
        Used to change non-clashing keys for each module into identical keys that are required
        to be passed to pynetbox
        ex. rack_role back into role to pass to NetBox
        Returns data
        :params data (dict): Data dictionary after _find_ids method ran
        """
        temp_dict = dict()
        if self._version_check_greater(self.version, "2.7", greater_or_equal=True):
            if data.get("form_factor"):
                temp_dict["type"] = data.pop("form_factor")
        for key in data:
            if self.endpoint == "power_panels" and key == "rack_group":
                temp_dict[key] = data[key]
            elif key in CONVERT_KEYS:
                # This will keep the original key for keys in list, but also convert it.
                if key in ("assigned_object", "scope"):
                    temp_dict[key] = data[key]
                new_key = CONVERT_KEYS[key]
                temp_dict[new_key] = data[key]
            else:
                temp_dict[key] = data[key]

        return temp_dict

    def _remove_arg_spec_default(self, data):
        """Used to remove any data keys that were not provided by user, but has the arg spec
        default values
        """
        new_dict = dict()
        for k, v in data.items():
            if isinstance(v, dict):
                v = self._remove_arg_spec_default(v)
                new_dict[k] = v
            elif v is not None:
                new_dict[k] = v

        return new_dict

    def _get_query_param_id(self, match, data):
        """Used to find IDs of necessary searches when required under _build_query_params
        :returns id (int) or data (dict): Either returns the ID or original data passed in
        :params match (str): The key within the user defined data that is required to have an ID
        :params data (dict): User defined data passed into the module
        """
        if isinstance(data.get(match), int):
            return data[match]
        else:
            endpoint = CONVERT_TO_ID[match]
            app = self._find_app(endpoint)
            nb_app = getattr(self.nb, app)
            nb_endpoint = getattr(nb_app, endpoint)

            query_params = {QUERY_TYPES.get(match): data[match]}
            result = self._nb_endpoint_get(nb_endpoint, query_params, match)

            if result:
                return result.id
            else:
                return data

    def _build_query_params(
        self, parent, module_data, user_query_params=None, child=None
    ):
        """
        :returns dict(query_dict): Returns a query dictionary built using mappings to dynamically
        build available query params for NetBox endpoints
        :params parent(str): This is either a key from `_find_ids` or a string passed in to determine
        which keys in the data that we need to use to construct `query_dict`
        :params module_data(dict): Uses the data provided to the NetBox module
        :params child(dict): This is used within `_find_ids` and passes the inner dictionary
        to build the appropriate `query_dict` for the parent
        """
        # This is to change the parent key to use the proper ALLOWED_QUERY_PARAMS below for termination searches.
        if parent == "termination_a" and module_data.get("termination_a_type"):
            parent = module_data["termination_a_type"]
        elif parent == "termination_b" and module_data.get("termination_b_type"):
            parent = module_data["termination_b_type"]
        elif parent == "scope":
            parent = ENDPOINT_NAME_MAPPING[SCOPE_TO_ENDPOINT[module_data["scope_type"]]]

        query_dict = dict()
        if user_query_params:
            query_params = set(user_query_params)
        else:
            query_params = ALLOWED_QUERY_PARAMS.get(parent)

        if child:
            matches = query_params.intersection(set(child.keys()))
        else:
            matches = query_params.intersection(set(module_data.keys()))

        for match in matches:
            if match in QUERY_PARAMS_IDS:
                if child:
                    query_id = self._get_query_param_id(match, child)
                else:
                    query_id = self._get_query_param_id(match, module_data)

                if parent == "vlan_group" and match == "site":
                    query_dict.update({match: query_id})
                else:
                    query_dict.update({match + "_id": query_id})
            else:
                if child:
                    value = child.get(match)
                else:
                    value = module_data.get(match)
                query_dict.update({match: value})

        if user_query_params:
            # This is to skip any potential changes using module_data when the user
            # provides user_query_params
            pass

        elif parent == "prefix" and module_data.get("parent"):
            query_dict.update({"prefix": module_data["parent"]})

        elif parent == "parent_interface" and module_data.get("device"):
            if not child:
                query_dict["name"] = module_data.get("parent_interface")

            if isinstance(module_data.get("device"), int):
                query_dict.update({"device_id": module_data.get("device")})
            else:
                query_dict.update({"device": module_data.get("device")})

        elif parent == "parent_vm_interface" and module_data.get("virtual_machine"):
            if not child:
                query_dict["name"] = module_data["parent_vm_interface"]

        elif parent == "vm_bridge" and module_data.get("virtual_machine"):
            if not child:
                query_dict["name"] = module_data["vm_bridge"]
                query_dict["virtual_machine_id"] = module_data["virtual_machine"]

        elif parent == "lag":
            if not child:
                query_dict["name"] = module_data["lag"]
            intf_type = self._fetch_choice_value(
                "Link Aggregation Group (LAG)", "interfaces"
            )
            query_dict.update({"form_factor": intf_type})
            if isinstance(module_data["device"], int):
                query_dict.update({"device_id": module_data["device"]})
            else:
                query_dict.update({"device": module_data["device"]})

        elif parent == "ip_addresses":
            if isinstance(module_data["device"], int):
                query_dict.update({"device_id": module_data["device"]})
            else:
                query_dict.update({"device": module_data["device"]})

        elif (
            parent == "ip_address"
            and "assigned_object" in matches
            and module_data.get("assigned_object_type")
        ):
            if module_data["assigned_object_type"] == "virtualization.vminterface":
                query_dict.update(
                    {"vminterface_id": module_data.get("assigned_object_id")}
                )
            elif module_data["assigned_object_type"] == "dcim.interface":
                query_dict.update(
                    {"interface_id": module_data.get("assigned_object_id")}
                )

        elif parent == "virtual_chassis":
            query_dict.update({"master": self.module.params["data"].get("master")})

        elif parent == "rear_port" and self.endpoint == "front_ports":
            if isinstance(module_data.get("rear_port"), str):
                rear_port = {
                    "device_id": module_data.get("device"),
                    "name": module_data.get("rear_port"),
                }
                query_dict.update(rear_port)

        elif parent == "rear_port_template" and self.endpoint == "front_port_templates":
            if isinstance(module_data.get("rear_port_template"), str):
                rear_port_template = {
                    "devicetype_id": module_data.get("device_type"),
                    "name": module_data.get("rear_port_template"),
                }
                query_dict.update(rear_port_template)

        elif parent == "power_port" and self.endpoint == "power_outlets":
            if isinstance(module_data.get("power_port"), str):
                power_port = {
                    "device_id": module_data.get("device"),
                    "name": module_data.get("power_port"),
                }
                query_dict.update(power_port)

        elif (
            parent == "power_port_template"
            and self.endpoint == "power_outlet_templates"
        ):
            if isinstance(module_data.get("power_port_template"), str):
                power_port_template = {
                    "devicetype_id": module_data.get("device_type"),
                    "name": module_data.get("power_port_template"),
                }
                query_dict.update(power_port_template)
        elif parent == "l2vpn_termination":
            query_param_mapping = {
                "dcim.interface": "interface_id",
                "ipam.vlan": "vlan_id",
                "virtualization.vminterface": "vminterface_id",
            }
            query_key = query_param_mapping[module_data.get("assigned_object_type")]
            query_dict.update(
                {
                    "l2vpn_id": query_dict.pop("l2vpn"),
                    query_key: module_data.get("assigned_object_id"),
                }
            )
        elif "_template" in parent:
            if query_dict.get("device_type"):
                query_dict["devicetype_id"] = query_dict.pop("device_type")

        if not query_dict:
            provided_kwargs = child.keys() if child else module_data.keys()
            acceptable_query_params = (
                user_query_params if user_query_params else query_params
            )
            self._handle_errors(
                f"One or more of the kwargs provided are invalid for {parent}, provided kwargs: {', '.join(sorted(provided_kwargs))}. Acceptable kwargs: {', '.join(sorted(acceptable_query_params))}"
            )

        query_dict = self._convert_identical_keys(query_dict)
        return query_dict

    def _fetch_choice_value(self, search, endpoint):
        app = self._find_app(endpoint)
        nb_app = getattr(self.nb, app)
        nb_endpoint = getattr(nb_app, endpoint)
        try:
            endpoint_choices = nb_endpoint.choices()
        except ValueError:
            self._handle_errors(
                msg="Failed to fetch endpoint choices to validate against. This requires a write-enabled token. Make sure the token is write-enabled. If looking to fetch only information, use either the inventory or lookup plugin."
            )

        choices = list(chain.from_iterable(endpoint_choices.values()))

        for item in choices:
            if item["display_name"].lower() == search.lower():
                return item["value"]
            elif item["value"] == search.lower():
                return item["value"]
        self._handle_errors(
            msg="%s was not found as a valid choice for %s" % (search, endpoint)
        )

    def _change_choices_id(self, endpoint, data):
        """Used to change data that is static and under _choices for the application.
        ex. DEVICE_STATUS
        :returns data (dict): Returns the user defined data back with updated fields for _choices
        :params endpoint (str): The endpoint that will be used for mapping to required _choices
        :params data (dict): User defined data passed into the module
        """
        if REQUIRED_ID_FIND.get(endpoint):
            required_choices = REQUIRED_ID_FIND[endpoint]
            for choice in required_choices:
                if data.get(choice):
                    if isinstance(data[choice], int):
                        continue
                    choice_value = self._fetch_choice_value(data[choice], endpoint)
                    data[choice] = choice_value

        return data

    def _find_app(self, endpoint):
        """Dynamically finds application of endpoint passed in using the
        API_APPS_ENDPOINTS for mapping
        :returns nb_app (str): The application the endpoint lives under
        :params endpoint (str): The endpoint requiring resolution to application
        """
        nb_app = None
        for k, v in API_APPS_ENDPOINTS.items():
            if endpoint in v:
                nb_app = k

        if nb_app:
            return nb_app
        else:
            raise Exception(f"{endpoint} not found in API_APPS_ENDPOINTS")

    def _find_ids(self, data, user_query_params):
        """Will find the IDs of all user specified data if resolvable
        :returns data (dict): Returns the updated dict with the IDs of user specified data
        :params data (dict): User defined data passed into the module
        """
        for k, v in data.items():
            if k in CONVERT_TO_ID:
                if (
                    not self._version_check_greater(
                        self.version, "2.9", greater_or_equal=True
                    )
                    and k == "tags"
                ) or (self.endpoint == "config_contexts" and k == "tags"):
                    continue
                if k == "termination_a":
                    endpoint = CONVERT_TO_ID[data.get("termination_a_type")]
                elif k == "termination_b":
                    endpoint = CONVERT_TO_ID[data.get("termination_b_type")]
                elif k == "assigned_object":
                    endpoint = "interfaces"
                elif k == "scope":
                    # Determine endpoint name for scope ID resolution
                    endpoint = SCOPE_TO_ENDPOINT[data["scope_type"]]
                else:
                    endpoint = CONVERT_TO_ID[k]
                search = v
                app = self._find_app(endpoint)
                nb_app = getattr(self.nb, app)
                nb_endpoint = getattr(nb_app, endpoint)

                if isinstance(v, dict):
                    if (k == "interface" or k == "assigned_object") and v.get(
                        "virtual_machine"
                    ):
                        nb_app = getattr(self.nb, "virtualization")
                        nb_endpoint = getattr(nb_app, endpoint)
                    query_params = self._build_query_params(k, data, child=v)
                    query_id = self._nb_endpoint_get(nb_endpoint, query_params, k)
                elif isinstance(v, list):
                    id_list = list()
                    for list_item in v:
                        if k in (
                            "regions",
                            "sites",
                            "roles",
                            "device_types",
                            "platforms",
                            "cluster_groups",
                            "contact_groups",
                            "tenant_groups",
                            "tenants",
                            "tags",
                        ) and isinstance(list_item, str):
                            temp_dict = {"slug": self._to_slug(list_item)}
                        elif isinstance(list_item, dict):
                            norm_data = self._normalize_data(list_item)
                            temp_dict = self._build_query_params(
                                k, data, child=norm_data
                            )
                        # If user passes in an integer, add to ID list to id_list as user
                        # should have passed in a tag ID
                        elif isinstance(list_item, int):
                            id_list.append(list_item)
                            continue
                        else:
                            temp_dict = {QUERY_TYPES.get(k, "q"): list_item}

                        query_id = self._nb_endpoint_get(nb_endpoint, temp_dict, k)
                        if query_id:
                            id_list.append(query_id.id)
                        else:
                            self._handle_errors(msg="%s not found" % (list_item))
                else:
                    if k in [
                        "lag",
                        "parent_interface",
                        "rear_port",
                        "rear_port_template",
                        "power_port",
                        "power_port_template",
                    ]:
                        query_params = self._build_query_params(
                            k, data, user_query_params
                        )
                    elif k == "scope":
                        query_params = {
                            QUERY_TYPES.get(
                                ENDPOINT_NAME_MAPPING[endpoint], "q"
                            ): search
                        }
                    elif k == "parent_vm_interface":
                        nb_app = getattr(self.nb, "virtualization")
                        nb_endpoint = getattr(nb_app, endpoint)
                        query_params = self._build_query_params(
                            k, data, user_query_params
                        )
                    elif k == "vm_bridge":
                        nb_app = getattr(self.nb, "virtualization")
                        nb_endpoint = getattr(nb_app, endpoint)
                        query_params = self._build_query_params(
                            k, data, user_query_params
                        )
                    else:
                        query_params = {QUERY_TYPES.get(k, "q"): search}
                    query_id = self._nb_endpoint_get(nb_endpoint, query_params, k)

                if isinstance(v, list):
                    data[k] = id_list
                elif isinstance(v, int):
                    pass
                elif query_id:
                    data[k] = query_id.id
                else:
                    self._handle_errors(msg="Could not resolve id of %s: %s" % (k, v))

        return data

    def _to_slug(self, value):
        """
        :returns slug (str): Slugified value
        :params value (str): Value that needs to be changed to slug format
        """
        if value is None:
            return value
        elif isinstance(value, int):
            return value
        else:
            removed_chars = re.sub(r"[^\-\.\w\s]", "", value)
            convert_chars = re.sub(r"[\-\.\s]+", "-", removed_chars)
            return convert_chars.strip().lower()

    def _normalize_data(self, data):
        """
        :returns data (dict): Normalized module data to formats accepted by NetBox searches
        such as changing from user specified value to slug
        ex. Test Rack -> test-rack
        :params data (dict): Original data from NetBox module
        """
        for k, v in data.items():
            if isinstance(v, dict):
                if v.get("id"):
                    try:
                        data[k] = int(v["id"])
                    except (ValueError, TypeError):
                        pass
                else:
                    for subk, subv in v.items():
                        sub_data_type = QUERY_TYPES.get(subk, "q")
                        if sub_data_type == "slug":
                            data[k][subk] = self._to_slug(subv)
            else:
                if k == "scope":
                    data_type = QUERY_TYPES.get(
                        ENDPOINT_NAME_MAPPING[SCOPE_TO_ENDPOINT[data["scope_type"]]],
                        "q",
                    )
                else:
                    data_type = QUERY_TYPES.get(k, "q")
                if data_type == "slug":
                    data[k] = self._to_slug(v)
                elif data_type == "timezone":
                    if " " in v:
                        data[k] = v.replace(" ", "_")
            if k == "description":
                data[k] = v.strip()

            if k == "mac_address":
                data[k] = v.upper()

        # We need to assign the correct type for the assigned object so the user doesn't have to worry about this.
        # We determine it by whether or not they pass in a device or virtual_machine
        if data.get("assigned_object"):
            if data["assigned_object"].get("device"):
                data["assigned_object_type"] = "dcim.interface"
            if data["assigned_object"].get("virtual_machine"):
                data["assigned_object_type"] = "virtualization.vminterface"

        return data

    def _create_netbox_object(self, nb_endpoint, data):
        """Create a NetBox object.
        :returns tuple(serialized_nb_obj, diff): tuple of the serialized created
        NetBox object and the Ansible diff.
        """
        if self.check_mode:
            nb_obj = data
        else:
            try:
                nb_obj = nb_endpoint.create(data)
            except pynetbox.RequestError as e:
                self._handle_errors(msg=e.error)

        diff = self._build_diff(before={"state": "absent"}, after={"state": "present"})
        return nb_obj, diff

    def _delete_netbox_object(self):
        """Delete a NetBox object.
        :returns diff (dict): Ansible diff
        """
        if not self.check_mode:
            try:
                self.nb_object.delete()
            except pynetbox.RequestError as e:
                self._handle_errors(msg=e.error)

        diff = self._build_diff(before={"state": "present"}, after={"state": "absent"})
        return diff

    def _update_netbox_object(self, data):
        """Update a NetBox object.
        :returns tuple(serialized_nb_obj, diff): tuple of the serialized updated
        NetBox object and the Ansible diff.
        """
        serialized_nb_obj = self.nb_object.serialize()
        if "custom_fields" in serialized_nb_obj:
            custom_fields = serialized_nb_obj.get("custom_fields", {})
            shared_keys = custom_fields.keys() & data.get("custom_fields", {}).keys()
            serialized_nb_obj["custom_fields"] = {
                key: custom_fields[key]
                for key in shared_keys
                if custom_fields[key] is not None
            }

        updated_obj = serialized_nb_obj.copy()
        updated_obj.update(data)

        if serialized_nb_obj.get("tags") and data.get("tags"):
            serialized_nb_obj["tags"] = set(serialized_nb_obj["tags"])
            updated_obj["tags"] = set(data["tags"])

        # Ensure idempotency for site on older netbox versions
        version_pre_30 = self._version_check_greater("3.0", self.version)
        if (
            serialized_nb_obj.get("latitude")
            and data.get("latitude")
            and version_pre_30
        ):
            updated_obj["latitude"] = str(data["latitude"])
        if (
            serialized_nb_obj.get("longitude")
            and data.get("longitude")
            and version_pre_30
        ):
            updated_obj["longitude"] = str(data["longitude"])

        # Ensure idempotency for virtual machine on older netbox versions
        version_pre_211 = self._version_check_greater("2.11", self.version)
        if serialized_nb_obj.get("vcpus") and data.get("vcpus"):
            if version_pre_211:
                updated_obj["vcpus"] = int(data["vcpus"])
            else:
                updated_obj["vcpus"] = float(data["vcpus"])

        # Ensure idempotency for cable on netbox versions later than 3.3
        version_post_33 = self._version_check_greater(self.version, "3.3", True)
        if (
            serialized_nb_obj.get("a_terminations")
            and serialized_nb_obj.get("b_terminations")
            and data.get("a_terminations")
            and data.get("b_terminations")
            and version_post_33
        ):

            def _convert_termination(termination):
                object_app = self._find_app(termination.endpoint.name)
                object_name = ENDPOINT_NAME_MAPPING[termination.endpoint.name]
                return {
                    "object_id": termination.id,
                    "object_type": f"{object_app}.{object_name}",
                }

            serialized_nb_obj["a_terminations"] = list(
                map(_convert_termination, self.nb_object.a_terminations)
            )
            serialized_nb_obj["b_terminations"] = list(
                map(_convert_termination, self.nb_object.b_terminations)
            )

        if serialized_nb_obj == updated_obj:
            return serialized_nb_obj, None
        else:
            data_before, data_after = {}, {}
            for key in data:
                try:
                    if serialized_nb_obj[key] != updated_obj[key]:
                        data_before[key] = serialized_nb_obj[key]
                        data_after[key] = updated_obj[key]
                except KeyError:
                    if key == "form_factor":
                        msg = "form_factor is not valid for NetBox 2.7 onward. Please use the type key instead."
                    else:
                        msg = (
                            "%s does not exist on existing object. Check to make sure valid field."
                            % (key)
                        )

                    self._handle_errors(msg=msg)

            if not self.check_mode:
                self.nb_object.update(data)
                updated_obj = self.nb_object.serialize()

            diff = self._build_diff(before=data_before, after=data_after)
            return updated_obj, diff

    def _ensure_object_exists(self, nb_endpoint, endpoint_name, name, data):
        """Used when `state` is present to make sure object exists or if the object exists
        that it is updated
        :params nb_endpoint (pynetbox endpoint object): This is the nb endpoint to be used
        to create or update the object
        :params endpoint_name (str): Endpoint name that was created/updated. ex. device
        :params name (str): Name of the object
        :params data (dict): User defined data passed into the module
        """
        if not self.nb_object:
            self.nb_object, diff = self._create_netbox_object(nb_endpoint, data)
            self.result["msg"] = "%s %s created" % (endpoint_name, name)
            self.result["changed"] = True
            self.result["diff"] = diff
        else:
            self.nb_object, diff = self._update_netbox_object(data)
            if self.nb_object is False:
                self._handle_errors(
                    msg="Request failed, couldn't update device: %s" % name
                )
            if diff:
                self.result["msg"] = "%s %s updated" % (endpoint_name, name)
                self.result["changed"] = True
                self.result["diff"] = diff
            else:
                self.result["msg"] = "%s %s already exists" % (endpoint_name, name)

    def _ensure_object_absent(self, endpoint_name, name):
        """Used when `state` is absent to make sure object does not exist
        :params endpoint_name (str): Endpoint name that was created/updated. ex. device
        :params name (str): Name of the object
        """
        if self.nb_object:
            diff = self._delete_netbox_object()
            self.result["msg"] = "%s %s deleted" % (endpoint_name, name)
            self.result["changed"] = True
            self.result["diff"] = diff
        else:
            self.result["msg"] = "%s %s already absent" % (endpoint_name, name)

    def run(self):
        """
        Must be implemented in subclasses
        """
        raise NotImplementedError


class NetboxAnsibleModule(AnsibleModule):
    """
    Creating this due to needing to override some functionality to provide required_together, required_if
    and will be able to override more in the future.
    This is due to the NetBox modules having the module arguments within a key in the argument spec, using suboptions rather than
    having all module arguments within the regular argument spec.

    Didn't want to change that functionality of the NetBox modules as its disruptive and we're required to send a specific payload
    to the NetBox API
    """

    def __init__(
        self,
        argument_spec,
        bypass_checks=False,
        no_log=False,
        mutually_exclusive=None,
        required_together=None,
        required_one_of=None,
        add_file_common_args=False,
        supports_check_mode=False,
        required_if=None,
        required_by=None,
    ):
        # Sets each check to None so they are not run in AnsibleModule
        super().__init__(
            argument_spec,
            bypass_checks=False,
            no_log=False,
            mutually_exclusive=None,
            required_together=None,
            required_one_of=None,
            add_file_common_args=False,
            supports_check_mode=supports_check_mode,
            required_if=None,
        )

        # Quick fix to support ansible-core 2.11
        #
        # Load the params manually as the self.params already have the defaults set
        params = _load_params()

        # Run each check manually providing the params
        if mutually_exclusive:
            self._check_mutually_exclusive(mutually_exclusive, param=params)

        if required_together:
            self._check_required_together(required_together, param=params)

        if required_one_of:
            self._check_required_one_of(required_one_of, param=params)

        if required_if:
            self._check_required_if(required_if, param=params)

    def _check_mutually_exclusive(self, spec, param=None):
        if param is None:
            param = self.params

        try:
            self.check_mutually_exclusive(spec, param)
        except TypeError as e:
            msg = to_native(e)
            if self._options_context:
                msg += " found in %s" % " -> ".join(self._options_context)
            self.fail_json(msg=msg)

    def check_mutually_exclusive(self, terms, module_parameters):
        """Check mutually exclusive terms against argument parameters
        Accepts a single list or list of lists that are groups of terms that should be
        mutually exclusive with one another
        :arg terms: List of mutually exclusive module parameters
        :arg module_parameters: Dictionary of module parameters
        :returns: Empty list or raises TypeError if the check fails.
        """

        results = []
        if terms is None:
            return results

        for check in terms:
            count = self.count_terms(check, module_parameters["data"])
            if count > 1:
                results.append(check)

        if results:
            full_list = ["|".join(check) for check in results]
            msg = "parameters are mutually exclusive: %s" % ", ".join(full_list)
            raise TypeError(to_native(msg))

        return results

    def _check_required_if(self, spec, param=None):
        """ensure that parameters which conditionally required are present"""
        if spec is None:
            return

        if param is None:
            param = self.params

        try:
            self.check_required_if(spec, param)
        except TypeError as e:
            msg = to_native(e)
            if self._options_context:
                msg += " found in %s" % " -> ".join(self._options_context)
            self.fail_json(msg=msg)

    def check_required_if(self, requirements, module_parameters):
        results = []
        if requirements is None:
            return results

        for req in requirements:
            missing = {}
            missing["missing"] = []
            max_missing_count = 0
            is_one_of = False
            if len(req) == 4:
                key, val, requirements, is_one_of = req
            else:
                key, val, requirements = req

            # is_one_of is True at least one requirement should be
            # present, else all requirements should be present.
            if is_one_of:
                max_missing_count = len(requirements)
                missing["requires"] = "any"
            else:
                missing["requires"] = "all"

            if key in module_parameters and module_parameters[key] == val:
                for check in requirements:
                    count = self.count_terms(check, module_parameters["data"])
                    if count == 0:
                        missing["missing"].append(check)
            if len(missing["missing"]) and len(missing["missing"]) >= max_missing_count:
                missing["parameter"] = key
                missing["value"] = val
                missing["requirements"] = requirements
                results.append(missing)

        if results:
            for missing in results:
                msg = "%s is %s but %s of the following are missing: %s" % (
                    missing["parameter"],
                    missing["value"],
                    missing["requires"],
                    ", ".join(missing["missing"]),
                )
                raise TypeError(to_native(msg))

        return results

    def _check_required_one_of(self, spec, param=None):
        if spec is None:
            return

        if param is None:
            param = self.params

        try:
            self.check_required_one_of(spec, param)
        except TypeError as e:
            msg = to_native(e)
            if self._options_context:
                msg += " found in %s" % " -> ".join(self._options_context)
            self.fail_json(msg=msg)

    def check_required_one_of(self, terms, module_parameters):
        """Check each list of terms to ensure at least one exists in the given module
        parameters
        Accepts a list of lists or tuples
        :arg terms: List of lists of terms to check. For each list of terms, at
            least one is required.
        :arg module_parameters: Dictionary of module parameters
        :returns: Empty list or raises TypeError if the check fails.
        """

        results = []
        if terms is None:
            return results

        for term in terms:
            count = self.count_terms(term, module_parameters["data"])
            if count == 0:
                results.append(term)

        if results:
            for term in results:
                msg = "one of the following is required: %s" % ", ".join(term)
                raise TypeError(to_native(msg))

        return results

    def _check_required_together(self, spec, param=None):
        if spec is None:
            return
        if param is None:
            param = self.params

        try:
            self.check_required_together(spec, param)
        except TypeError as e:
            msg = to_native(e)
            if self._options_context:
                msg += " found in %s" % " -> ".join(self._options_context)
            self.fail_json(msg=msg)

    def check_required_together(self, terms, module_parameters):
        """Check each list of terms to ensure every parameter in each list exists
        in the given module parameters
        Accepts a list of lists or tuples
        :arg terms: List of lists of terms to check. Each list should include
            parameters that are all required when at least one is specified
            in the module_parameters.
        :arg module_parameters: Dictionary of module parameters
        :returns: Empty list or raises TypeError if the check fails.
        """

        results = []
        if terms is None:
            return results

        for term in terms:
            counts = [
                self.count_terms(field, module_parameters["data"]) for field in term
            ]
            non_zero = [c for c in counts if c > 0]
            if len(non_zero) > 0:
                if 0 in counts:
                    results.append(term)
        if results:
            for term in results:
                msg = "parameters are required together: %s" % ", ".join(term)
                raise TypeError(to_native(msg))

        return results

    def count_terms(self, terms, module_parameters):
        """Count the number of occurrences of a key in a given dictionary
        :arg terms: String or iterable of values to check
        :arg module_parameters: Dictionary of module parameters
        :returns: An integer that is the number of occurrences of the terms values
        in the provided dictionary.
        """

        if not is_iterable(terms):
            terms = [terms]

        return len(set(terms).intersection(module_parameters))
