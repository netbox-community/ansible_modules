# Copyright (c) 2018 Remy Leone
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: nb_inventory
    plugin_type: inventory
    author:
        - Remy Leone (@sieben)
        - Anthony Ruhier (@Anthony25)
        - Nikhil Singh Baliyan (@nikkytub)
        - Sander Steffann (@steffann)
    short_description: NetBox inventory source
    description:
        - Get inventory hosts from NetBox
    extends_documentation_fragment:
        - constructed
        - inventory_cache
    options:
        plugin:
            description: token that ensures this is a source file for the 'netbox' plugin.
            required: True
            choices: ['netbox.netbox.nb_inventory']
        api_endpoint:
            description: Endpoint of the NetBox API
            required: True
            env:
                - name: NETBOX_API
        validate_certs:
            description:
                - Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.
            default: True
            type: boolean
        config_context:
            description:
                - If True, it adds config_context in host vars.
                - Config-context enables the association of arbitrary data to devices and virtual machines grouped by
                  region, site, role, platform, and/or tenant. Please check official netbox docs for more info.
            default: False
            type: boolean
        flatten_config_context:
            description:
                - If config_context is enabled, by default it's added as a host var named config_context.
                - If flatten_config_context is set to True, the config context variables will be added directly to the host instead.
            default: False
            type: boolean
            version_added: "0.2.1"
        flatten_custom_fields:
            description:
                - By default, host custom fields are added as a dictionary host var named custom_fields.
                - If flatten_custom_fields is set to True, the fields will be added directly to the host instead.
            default: False
            type: boolean
            version_added: "0.2.1"
        token:
            required: False
            description:
              - NetBox API token to be able to read against NetBox.
              - This may not be required depending on the NetBox setup.
            env:
                # in order of precedence
                - name: NETBOX_TOKEN
                - name: NETBOX_API_KEY
        plurals:
            description:
                - If True, all host vars are contained inside single-element arrays for legacy compatibility. Group names will be plural (ie. "sites_mysite" instead of "site_mysite")
            default: True
            type: boolean
            version_added: "0.2.1"
        interfaces:
            description:
                - If True, it adds the device or virtual machine interface information in host vars.
            default: False
            type: boolean
            version_added: "0.1.7"
        services:
            description:
                - If True, it adds the device or virtual machine services information in host vars.
            default: True
            type: boolean
            version_added: "0.2.0"
        group_by:
            description: Keys used to create groups. The 'plurals' option controls which of these are valid.
            type: list
            choices:
                - sites
                - site
                - tenants
                - tenant
                - racks
                - rack
                - tags
                - tag
                - device_roles
                - role
                - device_types
                - device_type
                - manufacturers
                - manufacturer
                - platforms
                - platform
                - region
                - cluster
                - cluster_type
                - cluster_group
            default: []
        group_names_raw:
            description: Will not add the group_by choice name to the group names
            default: False
            type: boolean
            version_added: "0.2.0"
        query_filters:
            description: List of parameters passed to the query string for both devices and VMs (Multiple values may be separated by commas)
            type: list
            default: []
        device_query_filters:
            description: List of parameters passed to the query string for devices (Multiple values may be separated by commas)
            type: list
            default: []
        vm_query_filters:
            description: List of parameters passed to the query string for VMs (Multiple values may be separated by commas)
            type: list
            default: []
        timeout:
            description: Timeout for Netbox requests in seconds
            type: int
            default: 60
        compose:
            description: List of custom ansible host vars to create from the device object fetched from NetBox
            default: {}
            type: dict
"""

EXAMPLES = """
# netbox_inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i netbox_inventory.yml

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
validate_certs: True
config_context: False
group_by:
  - device_roles
query_filters:
  - role: network-edge-router

# Query filters are passed directly as an argument to the fetching queries.
# You can repeat tags in the query string.

query_filters:
  - role: server
  - tag: web
  - tag: production

# See the NetBox documentation at https://netbox.readthedocs.io/en/latest/api/overview/
# the query_filters work as a logical **OR**
#
# Prefix any custom fields with cf_ and pass the field value with the regular NetBox query string

query_filters:
  - cf_foo: bar

# NetBox inventory plugin also supports Constructable semantics
# You can fill your hosts vars using the compose option:

plugin: netbox.netbox.nb_inventory
compose:
  foo: last_updated
  bar: display_name
  nested_variable: rack.display_name
"""

import json
import uuid
from functools import partial
from sys import version as python_version
from threading import Thread
from typing import Iterable
from itertools import chain

from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.module_utils.ansible_release import __version__ as ansible_version
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text
from ansible.module_utils.urls import open_url
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible_collections.ansible.netcommon.plugins.module_utils.compat.ipaddress import (
    ip_interface,
)

# List of parameters fetched from /api/docs/?format=openapi
# Use hacking/get_inventory_query_parameters.py to update this

ALLOWED_DEVICE_QUERY_PARAMETERS = (
    "asset_tag",
    "asset_tag__ic",
    "asset_tag__ie",
    "asset_tag__iew",
    "asset_tag__isw",
    "asset_tag__n",
    "asset_tag__nic",
    "asset_tag__nie",
    "asset_tag__niew",
    "asset_tag__nisw",
    "cluster_id",
    "cluster_id__n",
    "console_ports",
    "console_server_ports",
    "created",
    "created__gte",
    "created__lte",
    "device_bays",
    "device_type_id",
    "device_type_id__n",
    "face",
    "face__n",
    "has_primary_ip",
    "id",
    "id__gt",
    "id__gte",
    "id__in",
    "id__lt",
    "id__lte",
    "id__n",
    "interfaces",
    "is_full_depth",
    "last_updated",
    "last_updated__gte",
    "last_updated__lte",
    "limit",
    "local_context_data",
    "mac_address",
    "mac_address__ic",
    "mac_address__ie",
    "mac_address__iew",
    "mac_address__isw",
    "mac_address__n",
    "mac_address__nic",
    "mac_address__nie",
    "mac_address__niew",
    "mac_address__nisw",
    "manufacturer",
    "manufacturer__n",
    "manufacturer_id",
    "manufacturer_id__n",
    "model",
    "model__n",
    "name",
    "name__ic",
    "name__ie",
    "name__iew",
    "name__isw",
    "name__n",
    "name__nic",
    "name__nie",
    "name__niew",
    "name__nisw",
    "offset",
    "pass_through_ports",
    "platform",
    "platform__n",
    "platform_id",
    "platform_id__n",
    "position",
    "position__gt",
    "position__gte",
    "position__lt",
    "position__lte",
    "position__n",
    "power_outlets",
    "power_ports",
    "q",
    "rack_group_id",
    "rack_group_id__n",
    "rack_id",
    "rack_id__n",
    "region",
    "region__n",
    "region_id",
    "region_id__n",
    "role",
    "role__n",
    "role_id",
    "role_id__n",
    "serial",
    "site",
    "site__n",
    "site_id",
    "site_id__n",
    "status",
    "status__n",
    "tag",
    "tag__n",
    "tenant",
    "tenant__n",
    "tenant_group",
    "tenant_group__n",
    "tenant_group_id",
    "tenant_group_id__n",
    "tenant_id",
    "tenant_id__n",
    "vc_position",
    "vc_position__gt",
    "vc_position__gte",
    "vc_position__lt",
    "vc_position__lte",
    "vc_position__n",
    "vc_priority",
    "vc_priority__gt",
    "vc_priority__gte",
    "vc_priority__lt",
    "vc_priority__lte",
    "vc_priority__n",
    "virtual_chassis_id",
    "virtual_chassis_id__n",
    "virtual_chassis_member",
)

ALLOWED_VM_QUERY_PARAMETERS = (
    "cluster",
    "cluster__n",
    "cluster_group",
    "cluster_group__n",
    "cluster_group_id",
    "cluster_group_id__n",
    "cluster_id",
    "cluster_id__n",
    "cluster_type",
    "cluster_type__n",
    "cluster_type_id",
    "cluster_type_id__n",
    "created",
    "created__gte",
    "created__lte",
    "disk",
    "disk__gt",
    "disk__gte",
    "disk__lt",
    "disk__lte",
    "disk__n",
    "id",
    "id__gt",
    "id__gte",
    "id__in",
    "id__lt",
    "id__lte",
    "id__n",
    "last_updated",
    "last_updated__gte",
    "last_updated__lte",
    "limit",
    "local_context_data",
    "mac_address",
    "mac_address__ic",
    "mac_address__ie",
    "mac_address__iew",
    "mac_address__isw",
    "mac_address__n",
    "mac_address__nic",
    "mac_address__nie",
    "mac_address__niew",
    "mac_address__nisw",
    "memory",
    "memory__gt",
    "memory__gte",
    "memory__lt",
    "memory__lte",
    "memory__n",
    "name",
    "name__ic",
    "name__ie",
    "name__iew",
    "name__isw",
    "name__n",
    "name__nic",
    "name__nie",
    "name__niew",
    "name__nisw",
    "offset",
    "platform",
    "platform__n",
    "platform_id",
    "platform_id__n",
    "q",
    "region",
    "region__n",
    "region_id",
    "region_id__n",
    "role",
    "role__n",
    "role_id",
    "role_id__n",
    "site",
    "site__n",
    "site_id",
    "site_id__n",
    "status",
    "status__n",
    "tag",
    "tag__n",
    "tenant",
    "tenant__n",
    "tenant_group",
    "tenant_group__n",
    "tenant_group_id",
    "tenant_group_id__n",
    "tenant_id",
    "tenant_id__n",
    "vcpus",
    "vcpus__gt",
    "vcpus__gte",
    "vcpus__lt",
    "vcpus__lte",
    "vcpus__n",
)


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "netbox.netbox.nb_inventory"

    def _fetch_information(self, url):
        results = None
        cache_key = self.get_cache_key(url)

        # get the user's cache option to see if we should save the cache if it is changing
        user_cache_setting = self.get_option("cache")

        # read if the user has caching enabled and the cache isn't being refreshed
        attempt_to_read_cache = user_cache_setting and self.use_cache

        # attempt to read the cache if inventory isn't being refreshed and the user has caching enabled
        if attempt_to_read_cache:
            try:
                results = self._cache[cache_key]
                need_to_fetch = False
            except KeyError:
                # occurs if the cache_key is not in the cache or if the cache_key expired
                # we need to fetch the URL now
                need_to_fetch = True
        else:
            # not reading from cache so do fetch
            need_to_fetch = True

        if need_to_fetch:
            self.display.v("Fetching: " + url)
            response = open_url(
                url,
                headers=self.headers,
                timeout=self.timeout,
                validate_certs=self.validate_certs,
            )

            try:
                raw_data = to_text(response.read(), errors="surrogate_or_strict")
            except UnicodeError:
                raise AnsibleError(
                    "Incorrect encoding of fetched payload from NetBox API."
                )

            try:
                results = json.loads(raw_data)
            except ValueError:
                raise AnsibleError("Incorrect JSON payload: %s" % raw_data)

            # put result in cache if enabled
            if user_cache_setting:
                self._cache[cache_key] = results

        return results

    def get_resource_list(self, api_url):
        """Retrieves resource list from netbox API.
         Returns:
            A list of all resource from netbox API.
        """
        if not api_url:
            raise AnsibleError("Please check API URL in script configuration file.")

        hosts_list = []
        # Pagination.
        while api_url:
            self.display.v("Fetching: " + api_url)
            # Get hosts list.
            api_output = self._fetch_information(api_url)
            hosts_list += api_output["results"]
            api_url = api_output["next"]

        # Get hosts list.
        return hosts_list

    @property
    def group_extractors(self):

        # List of group_by options and hostvars to extract
        # Keys are different depending on plurals option
        if self.plurals:
            return {
                "sites": self.extract_site,
                "tenants": self.extract_tenant,
                "racks": self.extract_rack,
                "tags": self.extract_tags,
                "disk": self.extract_disk,
                "memory": self.extract_memory,
                "vcpus": self.extract_vcpus,
                "device_roles": self.extract_device_role,
                "platforms": self.extract_platform,
                "device_types": self.extract_device_type,
                "services": self.extract_services,
                "config_context": self.extract_config_context,
                "manufacturers": self.extract_manufacturer,
                "interfaces": self.extract_interfaces,
                "custom_fields": self.extract_custom_fields,
                "region": self.extract_regions,
                "cluster": self.extract_cluster,
                "cluster_group": self.extract_cluster_group,
                "cluster_type": self.extract_cluster_type,
            }
        else:
            return {
                "site": self.extract_site,
                "tenant": self.extract_tenant,
                "rack": self.extract_rack,
                "tag": self.extract_tags,
                "disk": self.extract_disk,
                "memory": self.extract_memory,
                "vcpus": self.extract_vcpus,
                "role": self.extract_device_role,
                "platform": self.extract_platform,
                "device_type": self.extract_device_type,
                "services": self.extract_services,
                "config_context": self.extract_config_context,
                "manufacturer": self.extract_manufacturer,
                "interfaces": self.extract_interfaces,
                "custom_fields": self.extract_custom_fields,
                "region": self.extract_regions,
                "cluster": self.extract_cluster,
                "cluster_group": self.extract_cluster_group,
                "cluster_type": self.extract_cluster_type,
            }

    def _pluralize(self, extracted_value):
        # If plurals is enabled, wrap in a single-element list for backwards compatibility
        if self.plurals:
            return [extracted_value]
        else:
            return extracted_value

    def extract_disk(self, host):
        return host.get("disk")

    def extract_vcpus(self, host):
        return host.get("vcpus")

    def extract_memory(self, host):
        return host.get("memory")

    def extract_platform(self, host):
        try:
            return self._pluralize(self.platforms_lookup[host["platform"]["id"]])
        except Exception:
            return

    def extract_services(self, host):
        try:
            if self.services:
                url = (
                    self.api_endpoint
                    + "/api/ipam/services/?device="
                    + str(host["name"])
                )
                device_lookup = self._fetch_information(url)
                return device_lookup["results"]
        except Exception:
            return

    def extract_device_type(self, host):
        try:
            return self._pluralize(self.device_types_lookup[host["device_type"]["id"]])
        except Exception:
            return

    def extract_rack(self, host):
        try:
            return self._pluralize(self.racks_lookup[host["rack"]["id"]])
        except Exception:
            return

    def extract_site(self, host):
        try:
            return self._pluralize(self.sites_lookup[host["site"]["id"]])
        except Exception:
            return

    def extract_tenant(self, host):
        try:
            return self._pluralize(self.tenants_lookup[host["tenant"]["id"]])
        except Exception:
            return

    def extract_device_role(self, host):
        try:
            if "device_role" in host:
                return self._pluralize(
                    self.device_roles_lookup[host["device_role"]["id"]]
                )
            elif "role" in host:
                return self._pluralize(self.device_roles_lookup[host["role"]["id"]])
        except Exception:
            return

    def extract_config_context(self, host):
        try:
            if self.flatten_config_context:
                # Don't wrap in an array if we're about to flatten it to separate host vars
                return host["config_context"]
            else:
                return self._pluralize(host["config_context"])
        except Exception:
            return

    def extract_manufacturer(self, host):
        try:
            return self._pluralize(
                self.manufacturers_lookup[host["device_type"]["manufacturer"]["id"]]
            )
        except Exception:
            return

    def extract_primary_ip(self, host):
        try:
            address = host["primary_ip"]["address"]
            return str(ip_interface(address).ip)
        except Exception:
            return

    def extract_primary_ip4(self, host):
        try:
            address = host["primary_ip4"]["address"]
            return str(ip_interface(address).ip)
        except Exception:
            return

    def extract_primary_ip6(self, host):
        try:
            address = host["primary_ip6"]["address"]
            return str(ip_interface(address).ip)
        except Exception:
            return

    def extract_tags(self, host):
        return host["tags"]

    def extract_ipaddresses(self, host):
        try:
            if self.interfaces:
                if "device_role" in host:
                    url = (
                        self.api_endpoint
                        + "/api/ipam/ip-addresses/?limit=0&device_id=%s"
                        % (to_text(host["id"]))
                    )
                elif "role" in host:
                    url = (
                        self.api_endpoint
                        + "/api/ipam/ip-addresses/?limit=0&virtual_machine_id=%s"
                        % (to_text(host["id"]))
                    )
                ipaddress_lookup = self.get_resource_list(api_url=url)

                return ipaddress_lookup
        except Exception:
            return

    def extract_interfaces(self, host):
        try:
            if self.interfaces:
                if "device_role" in host:
                    url = (
                        self.api_endpoint
                        + "/api/dcim/interfaces/?limit=0&device_id=%s"
                        % (to_text(host["id"]))
                    )
                elif "role" in host:
                    url = (
                        self.api_endpoint
                        + "/api/virtualization/interfaces/?limit=0&virtual_machine_id=%s"
                        % (to_text(host["id"]))
                    )
                interface_lookup = self.get_resource_list(api_url=url)

                # Collect all IP Addresses associated with the device
                device_ipaddresses = self.extract_ipaddresses(host)

                # Attach the found IP Addresses record to the interface
                for interface in interface_lookup:
                    interface_ip = [
                        ipaddress
                        for ipaddress in device_ipaddresses
                        if ipaddress["interface"]["id"] == interface["id"]
                    ]
                    interface["ip_addresses"] = interface_ip

                return interface_lookup
        except Exception:
            return

    def extract_custom_fields(self, host):
        try:
            return host["custom_fields"]
        except Exception:
            return

    def extract_regions(self, host):
        # A host may have a site. A site may have a region. A region may have a parent region.
        # Produce a list of regions:
        # - it will be empty if the device has no site, or the site has no region set
        # - it will have 1 element if the site's region has no parent
        # - it will have multiple elements if the site's region has a parent region

        site = host.get("site", None)
        if not isinstance(site, dict):
            # Device has no site
            return []

        site_id = site.get("id", None)
        if site_id is None:
            # Device has no site
            return []

        regions = []
        region_id = self.sites_region_lookup[site_id]

        # Keep looping until the region has no parent
        while region_id is not None:
            region_slug = self.regions_lookup[region_id]
            if region_slug in regions:
                # Won't ever happen - defensively guard against infinite loop
                break
            regions.append(region_slug)

            # Get the parent of this region
            region_id = self.regions_parent_lookup[region_id]

        return regions

    def extract_cluster(self, host):
        try:
            # cluster does not have a slug
            return host["cluster"]["name"]
        except Exception:
            return

    def extract_cluster_group(self, host):
        try:
            return self.clusters_group_lookup[host["cluster"]["id"]]
        except Exception:
            return

    def extract_cluster_type(self, host):
        try:
            return self.clusters_type_lookup[host["cluster"]["id"]]
        except Exception:
            return

    def refresh_platforms_lookup(self):
        url = self.api_endpoint + "/api/dcim/platforms/?limit=0"
        platforms = self.get_resource_list(api_url=url)
        self.platforms_lookup = dict(
            (platform["id"], platform["slug"]) for platform in platforms
        )

    def refresh_sites_lookup(self):
        url = self.api_endpoint + "/api/dcim/sites/?limit=0"
        sites = self.get_resource_list(api_url=url)
        self.sites_lookup = dict((site["id"], site["slug"]) for site in sites)

        def get_region_for_site(site):
            # Will fail if site does not have a region defined in Netbox
            try:
                return (site["id"], site["region"]["id"])
            except Exception:
                return (site["id"], None)

        # Dictionary of site id to region id
        self.sites_region_lookup = dict(
            filter(lambda x: x is not None, map(get_region_for_site, sites))
        )

    def refresh_regions_lookup(self):
        url = self.api_endpoint + "/api/dcim/regions/?limit=0"
        regions = self.get_resource_list(api_url=url)
        self.regions_lookup = dict((region["id"], region["slug"]) for region in regions)

        def get_region_parent(region):
            # Will fail if region does not have a parent region
            try:
                return (region["id"], region["parent"]["id"])
            except Exception:
                return (region["id"], None)

        # Dictionary of region id to parent region id
        self.regions_parent_lookup = dict(
            filter(lambda x: x is not None, map(get_region_parent, regions))
        )

    def refresh_tenants_lookup(self):
        url = self.api_endpoint + "/api/tenancy/tenants/?limit=0"
        tenants = self.get_resource_list(api_url=url)
        self.tenants_lookup = dict((tenant["id"], tenant["slug"]) for tenant in tenants)

    def refresh_racks_lookup(self):
        url = self.api_endpoint + "/api/dcim/racks/?limit=0"
        racks = self.get_resource_list(api_url=url)
        self.racks_lookup = dict((rack["id"], rack["name"]) for rack in racks)

    def refresh_device_roles_lookup(self):
        url = self.api_endpoint + "/api/dcim/device-roles/?limit=0"
        device_roles = self.get_resource_list(api_url=url)
        self.device_roles_lookup = dict(
            (device_role["id"], device_role["slug"]) for device_role in device_roles
        )

    def refresh_device_types_lookup(self):
        url = self.api_endpoint + "/api/dcim/device-types/?limit=0"
        device_types = self.get_resource_list(api_url=url)
        self.device_types_lookup = dict(
            (device_type["id"], device_type["slug"]) for device_type in device_types
        )

    def refresh_manufacturers_lookup(self):
        url = self.api_endpoint + "/api/dcim/manufacturers/?limit=0"
        manufacturers = self.get_resource_list(api_url=url)
        self.manufacturers_lookup = dict(
            (manufacturer["id"], manufacturer["slug"]) for manufacturer in manufacturers
        )

    def refresh_clusters_lookup(self):
        url = self.api_endpoint + "/api/virtualization/clusters/?limit=0"
        clusters = self.get_resource_list(api_url=url)

        def get_cluster_type(cluster):
            # Will fail if cluster does not have a type (required property so should always be true)
            try:
                return (cluster["id"], cluster["type"]["slug"])
            except Exception:
                return (cluster["id"], None)

        def get_cluster_group(cluster):
            # Will fail if cluster does not have a group (group is optional)
            try:
                return (cluster["id"], cluster["group"]["slug"])
            except Exception:
                return (cluster["id"], None)

        self.clusters_type_lookup = dict(
            filter(lambda x: x is not None, map(get_cluster_type, clusters))
        )

        self.clusters_group_lookup = dict(
            filter(lambda x: x is not None, map(get_cluster_group, clusters))
        )

    @property
    def lookup_processes(self):
        return [
            self.refresh_sites_lookup,
            self.refresh_regions_lookup,
            self.refresh_tenants_lookup,
            self.refresh_racks_lookup,
            self.refresh_device_roles_lookup,
            self.refresh_platforms_lookup,
            self.refresh_device_types_lookup,
            self.refresh_manufacturers_lookup,
            self.refresh_clusters_lookup,
        ]

    def refresh_lookups(self):
        thread_list = []
        for p in self.lookup_processes:
            t = Thread(target=p)
            thread_list.append(t)
            t.start()

        for thread in thread_list:
            thread.join()

    def validate_query_parameter(self, parameter, allowed_query_parameters):
        if not (isinstance(parameter, dict) and len(parameter) == 1):
            self.display.warning(
                "Warning query parameters %s not a dict with a single key." % parameter
            )
            return None

        k = tuple(parameter.keys())[0]
        v = tuple(parameter.values())[0]

        if not (k in allowed_query_parameters or k.startswith("cf_")):
            msg = "Warning: %s not in %s or starting with cf (Custom field)" % (
                k,
                allowed_query_parameters,
            )
            self.display.warning(msg=msg)
            return None
        return k, v

    def filter_query_parameters(self, parameters, allowed_query_parameters):
        return filter(
            lambda parameter: parameter is not None,
            # For each element of query_filters, test if it's allowed
            map(
                # Create a partial function with the device-specific list of query parameters
                partial(
                    self.validate_query_parameter,
                    allowed_query_parameters=allowed_query_parameters,
                ),
                parameters,
            ),
        )

    def refresh_url(self):
        device_query_parameters = [("limit", 0)]
        vm_query_parameters = [("limit", 0)]
        device_url = self.api_endpoint + "/api/dcim/devices/?"
        vm_url = self.api_endpoint + "/api/virtualization/virtual-machines/?"

        # Add query_filtes to both devices and vms query, if they're valid
        if isinstance(self.query_filters, Iterable):
            device_query_parameters.extend(
                self.filter_query_parameters(
                    self.query_filters, ALLOWED_DEVICE_QUERY_PARAMETERS
                )
            )

            vm_query_parameters.extend(
                self.filter_query_parameters(
                    self.query_filters, ALLOWED_VM_QUERY_PARAMETERS
                )
            )

        if isinstance(self.device_query_filters, Iterable):
            device_query_parameters.extend(
                self.filter_query_parameters(
                    self.device_query_filters, ALLOWED_DEVICE_QUERY_PARAMETERS
                )
            )

        if isinstance(self.vm_query_filters, Iterable):
            vm_query_parameters.extend(
                self.filter_query_parameters(
                    self.vm_query_filters, ALLOWED_VM_QUERY_PARAMETERS
                )
            )

        # When query_filters is Iterable, and is not empty:
        # - If none of the filters are valid for devices, do not fetch any devices
        # - If none of the filters are valid for VMs, do not fetch any VMs
        # If either device_query_filters or vm_query_filters are set,
        # device_query_parameters and vm_query_parameters will have > 1 element so will continue to be requested
        if self.query_filters and isinstance(self.query_filters, Iterable):
            if len(device_query_parameters) <= 1:
                device_url = None

            if len(vm_query_parameters) <= 1:
                vm_url = None

        # Append the parameters to the URLs
        if device_url:
            device_url = device_url + urlencode(device_query_parameters)
        if vm_url:
            vm_url = vm_url + urlencode(vm_query_parameters)

        # Exclude config_context if not required
        if not self.config_context:
            if device_url:
                device_url = device_url + "&exclude=config_context"
            if vm_url:
                vm_url = vm_url + "&exclude=config_context"

        return device_url, vm_url

    def fetch_hosts(self):
        device_url, vm_url = self.refresh_url()
        if device_url and vm_url:
            return chain(
                self.get_resource_list(device_url), self.get_resource_list(vm_url),
            )
        elif device_url:
            return self.get_resource_list(device_url)
        elif vm_url:
            return self.get_resource_list(vm_url)

    def extract_name(self, host):
        # An host in an Ansible inventory requires an hostname.
        # name is an unique but not required attribute for a device in NetBox
        # We default to an UUID for hostname in case the name is not set in NetBox
        return host["name"] or str(uuid.uuid4())

    def generate_group_name(self, grouping, group):
        if self.group_names_raw:
            return group
        else:
            return "_".join([grouping, group])

    def add_host_to_groups(self, host, hostname):

        # If we're grouping by regions, hosts are not added to region groups
        # - the site groups are added as sub-groups of regions
        # So, we need to make sure we're also grouping by sites if regions are enabled

        if "region" in self.group_by:
            # Make sure "site" or "sites" grouping also exists, depending on plurals options
            if self.plurals and "sites" not in self.group_by:
                self.group_by.append("sites")
            elif not self.plurals and "site" not in self.group_by:
                self.group_by.append("site")

        for grouping in self.group_by:

            # Don't handle regions here - that will happen in main()
            if grouping == "region":
                continue

            if grouping not in self.group_extractors:
                raise AnsibleError(
                    'group_by option "%s" is not valid. (Maybe check the plurals option? It can determine what group_by options are valid)'
                    % grouping
                )

            groups_for_host = self.group_extractors[grouping](host)

            if not groups_for_host:
                continue

            # Make groups_for_host a list if it isn't already
            if not isinstance(groups_for_host, list):
                groups_for_host = [groups_for_host]

            for group_for_host in groups_for_host:
                group_name = self.generate_group_name(grouping, group_for_host)

                # Group names may be transformed by the ansible TRANSFORM_INVALID_GROUP_CHARS setting
                # add_group returns the actual group name used
                transformed_group_name = self.inventory.add_group(group=group_name)
                self.inventory.add_host(group=transformed_group_name, host=hostname)

    def _add_region_groups(self):

        # Mapping of region id to group name
        region_transformed_group_names = dict()

        # Create groups for each region
        for region_id in self.regions_lookup:
            region_group_name = self.generate_group_name(
                "region", self.regions_lookup[region_id]
            )
            region_transformed_group_names[region_id] = self.inventory.add_group(
                group=region_group_name
            )

        # Now that all region groups exist, add relationships between them
        for region_id in self.regions_lookup:
            region_group_name = region_transformed_group_names[region_id]
            parent_region_id = self.regions_parent_lookup.get(region_id, None)
            if (
                parent_region_id is not None
                and parent_region_id in region_transformed_group_names
            ):
                parent_region_name = region_transformed_group_names[parent_region_id]
                self.inventory.add_child(parent_region_name, region_group_name)

        # Add site groups as children of region groups
        for site_id in self.sites_lookup:
            region_id = self.sites_region_lookup.get(site_id, None)
            if region_id is None:
                continue

            region_transformed_group_name = region_transformed_group_names[region_id]

            site_name = self.sites_lookup[site_id]
            site_group_name = self.generate_group_name(
                "sites" if self.plurals else "site", site_name
            )
            # Add the site group to get its transformed name
            # Will already be created by add_host_to_groups - it's ok to call add_group again just to get its name
            site_transformed_group_name = self.inventory.add_group(
                group=site_group_name
            )

            self.inventory.add_child(
                region_transformed_group_name, site_transformed_group_name
            )

    def _fill_host_variables(self, host, hostname):
        for attribute, extractor in self.group_extractors.items():
            extracted_value = extractor(host)

            # Compare with None, not just check for a truth comparison - allow empty arrays, etc to be host vars
            if extracted_value is None:
                continue

            # Special case - all group_by options are single strings, but tag is a list of tags
            # Keep the groups named singular "tag_sometag", but host attribute should be "tags":["sometag", "someothertag"]
            if attribute == "tag":
                attribute = "tags"

            if attribute == "region":
                attribute = "regions"

            # Flatten the dict into separate host vars, if enabled
            if isinstance(extracted_value, dict) and (
                (attribute == "config_context" and self.flatten_config_context)
                or (attribute == "custom_fields" and self.flatten_custom_fields)
            ):
                for key, value in extracted_value.items():
                    self.inventory.set_variable(hostname, key, value)
            else:
                self.inventory.set_variable(hostname, attribute, extracted_value)

        extracted_primary_ip = self.extract_primary_ip(host=host)
        if extracted_primary_ip:
            self.inventory.set_variable(hostname, "ansible_host", extracted_primary_ip)

        extracted_primary_ip4 = self.extract_primary_ip4(host=host)
        if extracted_primary_ip4:
            self.inventory.set_variable(hostname, "primary_ip4", extracted_primary_ip4)

        extracted_primary_ip6 = self.extract_primary_ip6(host=host)
        if extracted_primary_ip6:
            self.inventory.set_variable(hostname, "primary_ip6", extracted_primary_ip6)

    def main(self):
        self.refresh_lookups()
        hosts_list = self.fetch_hosts()

        for host in hosts_list:
            hostname = self.extract_name(host=host)
            self.inventory.add_host(host=hostname)
            self._fill_host_variables(host=host, hostname=hostname)

            strict = self.get_option("strict")

            # Composed variables
            self._set_composite_vars(
                self.get_option("compose"), host, hostname, strict=strict
            )

            # Complex groups based on jinja2 conditionals, hosts that meet the conditional are added to group
            self._add_host_to_composed_groups(
                self.get_option("groups"), host, hostname, strict=strict
            )

            # Create groups based on variable values and add the corresponding hosts to it
            self._add_host_to_keyed_groups(
                self.get_option("keyed_groups"), host, hostname, strict=strict
            )
            self.add_host_to_groups(host=host, hostname=hostname)

        # Create groups for regions, containing the site groups
        if "region" in self.group_by:
            self._add_region_groups()

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path=path)
        self.use_cache = cache

        # Netbox access
        token = self.get_option("token")
        # Handle extra "/" from api_endpoint configuration and trim if necessary, see PR#49943
        self.api_endpoint = self.get_option("api_endpoint").strip("/")
        self.timeout = self.get_option("timeout")
        self.validate_certs = self.get_option("validate_certs")
        self.config_context = self.get_option("config_context")
        self.flatten_config_context = self.get_option("flatten_config_context")
        self.flatten_custom_fields = self.get_option("flatten_custom_fields")
        self.plurals = self.get_option("plurals")
        self.interfaces = self.get_option("interfaces")
        self.services = self.get_option("services")
        self.headers = {
            "User-Agent": "ansible %s Python %s"
            % (ansible_version, python_version.split(" ")[0]),
            "Content-type": "application/json",
        }
        if token:
            self.headers.update({"Authorization": "Token %s" % token})

        # Filter and group_by options
        self.group_by = self.get_option("group_by")
        self.group_names_raw = self.get_option("group_names_raw")
        self.query_filters = self.get_option("query_filters")
        self.device_query_filters = self.get_option("device_query_filters")
        self.vm_query_filters = self.get_option("vm_query_filters")

        self.main()
