# Copyright (c) 2018 Remy Leone
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: nb_inventory
    author:
        - Remy Leone (@sieben)
        - Anthony Ruhier (@Anthony25)
        - Nikhil Singh Baliyan (@nikkytub)
        - Sander Steffann (@steffann)
        - Douglas Heriot (@DouglasHeriot)
        - Thore Knickrehm (@tkn2023)
    short_description: NetBox inventory source
    description:
        - Get inventory hosts from NetBox
    extends_documentation_fragment:
        - constructed
        - inventory_cache
    options:
        plugin:
            description: token that ensures this is a source file for the 'netbox' plugin.
            required: true
            choices: ['netbox.netbox.nb_inventory']
        api_endpoint:
            description: Endpoint of the NetBox API
            required: true
            env:
                - name: NETBOX_API
        validate_certs:
            description:
                - Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.
            default: true
            type: boolean
        cert:
            description:
                - Certificate path
            default: false
        key:
            description:
                - Certificate key path
            default: false
        ca_path:
            description:
                - CA path
            default: false
        follow_redirects:
            description:
                - Determine how redirects are followed.
                - By default, I(follow_redirects) is set to uses urllib2 default behavior.
            default: urllib2
            choices: ['urllib2', 'all', 'yes', 'safe', 'none']
        config_context:
            description:
                - If True, it adds config_context in host vars.
                - Config-context enables the association of arbitrary data to devices and virtual machines grouped by
                  region, site, role, platform, and/or tenant. Please check official netbox docs for more info.
            default: false
            type: boolean
        flatten_config_context:
            description:
                - If I(config_context) is enabled, by default it's added as a host var named config_context.
                - If flatten_config_context is set to True, the config context variables will be added directly to the host instead.
            default: false
            type: boolean
            version_added: "0.2.1"
        flatten_local_context_data:
            description:
                - If I(local_context_data) is enabled, by default it's added as a host var named local_context_data.
                - If flatten_local_context_data is set to True, the config context variables will be added directly to the host instead.
            default: false
            type: boolean
            version_added: "0.3.0"
        flatten_custom_fields:
            description:
                - By default, host custom fields are added as a dictionary host var named custom_fields.
                - If flatten_custom_fields is set to True, the fields will be added directly to the host instead.
            default: false
            type: boolean
            version_added: "0.2.1"
        token:
            required: false
            description:
                - NetBox API token to be able to read against NetBox.
                - This may not be required depending on the NetBox setup.
                - You can provide a "type" and "value" for a token if your NetBox deployment is using a more advanced authentication like OAUTH.
                - If you do not provide a "type" and "value" parameter, the HTTP authorization header will be set to "Token", which is the NetBox default
            env:
                # in order of precedence
                - name: NETBOX_TOKEN
                - name: NETBOX_API_KEY
        plurals:
            description:
                - If True, all host vars are contained inside single-element arrays for legacy compatibility with old versions of this plugin.
                - Group names will be plural (ie. "sites_mysite" instead of "site_mysite")
                - The choices of I(group_by) will be changed by this option.
            default: true
            type: boolean
            version_added: "0.2.1"
        virtual_disks:
            description:
                - If True, it adds the virtual disks information in host vars.
            default: false
            type: boolean
            version_added: "3.18.0"
        interfaces:
            description:
                - If True, it adds the device or virtual machine interface information in host vars.
            default: false
            type: boolean
            version_added: "0.1.7"
        site_data:
            description:
                - If True, sites' full data structures returned from Netbox API are included in host vars.
            default: false
            type: boolean
            version_added: "3.5.0"
        prefixes:
            description:
                - If True, it adds the device or virtual machine prefixes to hostvars nested under "site".
                - Must match selection for "site_data", as this changes the structure of "site" in hostvars
            default: false
            type: boolean
            version_added: "3.5.0"
        services:
            description:
                - If True, it adds the device or virtual machine services information in host vars.
            default: true
            type: boolean
            version_added: "0.2.0"
        fetch_all:
            description:
                - By default, fetching interfaces and services will get all of the contents of NetBox regardless of query_filters applied to devices and VMs.
                - When set to False, separate requests will be made fetching interfaces, services, and IP addresses for each device_id and virtual_machine_id.
                - If you are using the various query_filters options to reduce the number of devices, you may find querying NetBox faster with fetch_all set to False.  # noqa: E501
                - For efficiency, when False, these requests will be batched, for example /api/dcim/interfaces?limit=0&device_id=1&device_id=2&device_id=3
                - These GET request URIs can become quite large for a large number of devices. If you run into HTTP 414 errors, you can adjust the max_uri_length option to suit your web server.  # noqa: E501
            default: true
            type: boolean
            version_added: "0.2.1"
        group_by:
            description:
                - Keys used to create groups. The I(plurals) and I(racks) options control which of these are valid.
                - I(rack_group) is supported on NetBox versions 2.10 or lower only
                - I(location) is supported on NetBox versions 2.11 or higher only
            type: list
            elements: str
            choices:
                - sites
                - site
                - location
                - tenants
                - tenant
                - racks
                - rack
                - rack_group
                - rack_role
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
                - site_group
                - cluster
                - cluster_type
                - cluster_group
                - is_virtual
                - services
                - status
                - time_zone
                - utc_offset
                - facility
            default: []
        group_names_raw:
            description: Will not add the group_by choice name to the group names
            default: false
            type: boolean
            version_added: "0.2.0"
        query_filters:
            description:
                - List of parameters passed to the query string for both devices and VMs (Multiple values may be separated by commas).
                - You can also use Jinja2 templates.
            type: list
            elements: str
            default: []
        device_query_filters:
            description:
                - List of parameters passed to the query string for devices (Multiple values may be separated by commas).
                - You can also use Jinja2 templates.
            type: list
            elements: str
            default: []
        vm_query_filters:
            description:
                - List of parameters passed to the query string for VMs (Multiple values may be separated by commas).
                - You can also use Jinja2 templates.
            type: list
            elements: str
            default: []
        timeout:
            description: Timeout for NetBox requests in seconds
            type: int
            default: 60
        max_uri_length:
            description:
                - When fetch_all is False, GET requests to NetBox may become quite long and return a HTTP 414 (URI Too Long).
                - You can adjust this option to be smaller to avoid 414 errors, or larger for a reduced number of requests.
            type: int
            default: 4000
            version_added: "0.2.1"
        virtual_chassis_name:
            description:
                - When a device is part of a virtual chassis, use the virtual chassis name as the Ansible inventory hostname.
                - The host var values will be from the virtual chassis master.
            type: boolean
            default: false
        dns_name:
            description:
                - Force IP Addresses to be fetched so that the dns_name for the primary_ip of each device or VM is set as a host_var.
                - Setting interfaces will also fetch IP addresses and the dns_name host_var will be set.
            type: boolean
            default: false
        ansible_host_dns_name:
            description:
                - If True, sets DNS Name (fetched from primary_ip) to be used in ansible_host variable, instead of IP Address.
            type: boolean
            default: false
        compose:
            description: List of custom ansible host vars to create from the device object fetched from NetBox
            default: {}
            type: dict
        racks:
            description:
                - If False, skip querying the racks for information, which can be slow with great amounts of racks.
                - The choices of I(group_by) will be changed by this option.
            type: boolean
            default: true
            version_added: "3.6.0"
        oob_ip_as_primary_ip:
            description: Use out of band IP as `ansible host`
            type: boolean
            default: false
        rename_variables:
            description:
                - Rename variables evaluated by nb_inventory, before writing them.
                - Each list entry contains a dict with a 'pattern' and a 'repl'.
                - Both 'pattern' and 'repl' are regular expressions.
                - The first matching expression is used, subsequent matches are ignored.
                - Internally `re.sub` is used.
            type: list
            elements: dict
            default: []
        hostname_field:
            description:
                - By default, the inventory hostname is the netbox device name
                - If set, sets the inventory hostname from this field in custom_fields instead
            default: False
        headers:
            description: Dictionary of headers to be passed to the NetBox API.
            default: {}
            env:
                - name: NETBOX_HEADERS
"""

EXAMPLES = """
# netbox_inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i netbox_inventory.yml

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
validate_certs: true
config_context: false
group_by:
  - device_roles
query_filters:
  - role: network-edge-router
device_query_filters:
  - has_primary_ip: 'true'
  - tenant__n: internal
headers:
  Cookie: "{{ auth_cookie }}"

# has_primary_ip is a useful way to filter out patch panels and other passive devices
# Adding '__n' to a field searches for the negation of the value.
# The above searches for devices that are NOT "tenant = internal"

# Query filters are passed directly as an argument to the fetching queries.
# You can repeat tags in the query string.

query_filters:
  - role: server
  - tag: web
  - tag: production

# See the NetBox documentation at https://netbox.readthedocs.io/en/stable/rest-api/overview/
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

# You can use keyed_groups to group on properties of devices or VMs.
# NOTE: It's only possible to key off direct items on the device/VM objects.
plugin: netbox.netbox.nb_inventory
keyed_groups:
  - prefix: status
    key: status.value

# For use in Ansible Tower (AWX) the credential for NetBox will need to expose NETBOX_API
# and NETBOX_TOKEN as environment variables.
# Example Ansible Tower credential Input Configuration:

fields:
  - id: NETBOX_API
    type: string
    label: NetBox Host URL
  - id: NETBOX_TOKEN
    type: string
    label: NetBox API Token
    secret: true
required:
  - NETBOX_API
  - NETBOX_TOKEN

# Example Ansible Tower credential Injector Configuration:

env:
  NETBOX_API: '{{ NETBOX_API }}'
  NETBOX_TOKEN: '{{ NETBOX_TOKEN }}'

# Example of time_zone and utc_offset usage

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
token: <insert token>
validate_certs: true
config_context: true
group_by:
  - site
  - role
  - time_zone
  - utc_offset
device_query_filters:
  - has_primary_ip: 'true'
  - manufacturer_id: 1

# using group by time_zone, utc_offset it will group devices in ansible groups depending on time zone configured on site.
# time_zone gives grouping like:
# - "time_zone_Europe_Bucharest"
# - "time_zone_Europe_Copenhagen"
# - "time_zone_America_Denver"
# utc_offset gives grouping like:
# - "time_zone_utc_minus_7"
# - "time_zone_utc_plus_1"
# - "time_zone_utc_plus_10"

# Example of using a token type

plugin: netbox.netbox.nb_inventory
api_endpoint: http://localhost:8000
token:
  type: Bearer
  value: test123456
"""

import json
import uuid
import math
import os
import re
import datetime
from copy import deepcopy
from functools import partial
from sys import version as python_version
from threading import Thread
from typing import Iterable
from itertools import chain
from collections import defaultdict
from ipaddress import ip_interface


from ansible.constants import DEFAULT_LOCAL_TMP
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.module_utils.ansible_release import __version__ as ansible_version
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text, to_native
from ansible.module_utils.urls import open_url
from ansible.module_utils.six.moves.urllib import error as urllib_error
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.six.moves.urllib.parse import urlparse


try:
    from packaging import specifiers, version
except ImportError as imp_exc:
    PACKAGING_IMPORT_ERROR = imp_exc
else:
    PACKAGING_IMPORT_ERROR = None

try:
    import pytz
except ImportError as imp_exc:
    PYTZ_IMPORT_ERROR = imp_exc
else:
    PYTZ_IMPORT_ERROR = None


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
            try:
                response = open_url(
                    url,
                    headers=self.headers,
                    timeout=self.timeout,
                    validate_certs=self.validate_certs,
                    follow_redirects=self.follow_redirects,
                    client_cert=self.cert,
                    client_key=self.key,
                    ca_path=self.ca_path,
                )
            except urllib_error.HTTPError as e:
                """This will return the response body when we encounter an error.
                This is to help determine what might be the issue when encountering an error.
                Please check issue #294 for more info.
                """
                # Prevent inventory from failing completely if the token does not have the proper permissions for specific URLs
                if e.code == 403:
                    self.display.display(
                        "Permission denied: {0}. This may impair functionality of the"
                        " inventory plugin.".format(url),
                        color="red",
                    )
                    # Need to return mock response data that is empty to prevent any failures downstream
                    return {"results": [], "next": None}

                raise AnsibleError(to_native(e.fp.read()))

            try:
                raw_data = to_text(response.read(), errors="surrogate_or_strict")
            except UnicodeError:
                raise AnsibleError(
                    "Incorrect encoding of fetched payload from NetBox API."
                )

            try:
                results = self.loader.load(raw_data, json_only=True)
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

        resources = []

        # Handle pagination
        while api_url:
            api_output = self._fetch_information(api_url)
            resources.extend(api_output["results"])
            api_url = api_output["next"]

        return resources

    def get_resource_list_chunked(self, api_url, query_key, query_values):
        # Make an API call for multiple specific IDs, like /api/ipam/ip-addresses?limit=0&device_id=1&device_id=2&device_id=3
        # Drastically cuts down HTTP requests comnpared to 1 request per host, in the case where we don't want to fetch_all

        # Make sure query_values is subscriptable
        if not isinstance(query_values, list):
            query_values = list(query_values)

        def query_string(value, separator="&"):
            return separator + query_key + "=" + str(value)

        # Calculate how many queries we can do per API call to stay within max_url_length
        largest_value = str(max(query_values, default=0))  # values are always id ints
        length_per_value = len(query_string(largest_value))
        chunk_size = math.floor((self.max_uri_length - len(api_url)) / length_per_value)

        # Sanity check, for case where max_uri_length < (api_url + length_per_value)
        if chunk_size < 1:
            chunk_size = 1

        if self.api_version in specifiers.SpecifierSet("~=2.6.0"):
            # Issue netbox-community/netbox#3507 was fixed in v2.7.5
            # If using NetBox v2.7.0-v2.7.4 will have to manually set max_uri_length to 0,
            # but it's probably faster to keep fetch_all: true
            # (You should really just upgrade your NetBox install)
            chunk_size = 1

        resources = []

        for i in range(0, len(query_values), chunk_size):
            chunk = query_values[i : i + chunk_size]  # noqa: E203
            # process chunk of size <= chunk_size
            url = api_url
            for value in chunk:
                url += query_string(value, "&" if "?" in url else "?")

            resources.extend(self.get_resource_list(url))

        return resources

    @property
    def group_extractors(self):
        # List of group_by options and hostvars to extract

        # Some keys are different depending on plurals option
        extractors = {
            "disk": self.extract_disk,
            "memory": self.extract_memory,
            "vcpus": self.extract_vcpus,
            "status": self.extract_status,
            "config_context": self.extract_config_context,
            "local_context_data": self.extract_local_context_data,
            "custom_fields": self.extract_custom_fields,
            "region": self.extract_regions,
            "cluster": self.extract_cluster,
            "cluster_group": self.extract_cluster_group,
            "cluster_type": self.extract_cluster_type,
            "cluster_device": self.extract_cluster_device,
            "is_virtual": self.extract_is_virtual,
            "serial": self.extract_serial,
            "asset_tag": self.extract_asset_tag,
            "time_zone": self.extract_site_time_zone,
            "utc_offset": self.extract_site_utc_offset,
            "facility": self.extract_site_facility,
            self._pluralize_group_by("site"): self.extract_site,
            self._pluralize_group_by("tenant"): self.extract_tenant,
            self._pluralize_group_by("tag"): self.extract_tags,
            self._pluralize_group_by("role"): self.extract_device_role,
            self._pluralize_group_by("platform"): self.extract_platform,
            self._pluralize_group_by("device_type"): self.extract_device_type,
            self._pluralize_group_by("manufacturer"): self.extract_manufacturer,
        }

        if self.api_version >= version.parse("2.11"):
            extractors.update(
                {
                    "site_group": self.extract_site_groups,
                }
            )
        if self.racks:
            extractors.update(
                {
                    self._pluralize_group_by("rack"): self.extract_rack,
                    "rack_role": self.extract_rack_role,
                }
            )

            # Locations were added in 2.11 replacing rack-groups.
            if self.api_version >= version.parse("2.11"):
                extractors.update(
                    {
                        "location": self.extract_location,
                    }
                )
            else:
                extractors.update(
                    {
                        "rack_group": self.extract_rack_group,
                    }
                )

        if self.services:
            extractors.update(
                {
                    "services": self.extract_services,
                }
            )
        if self.virtual_disks:
            extractors.update(
                {
                    "virtual_disks": self.extract_virtual_disks,
                }
            )
        if self.interfaces:
            extractors.update(
                {
                    "interfaces": self.extract_interfaces,
                }
            )

        if self.interfaces or self.dns_name or self.ansible_host_dns_name:
            extractors.update(
                {
                    "dns_name": self.extract_dns_name,
                }
            )

        return extractors

    def _pluralize_group_by(self, group_by):
        mapping = {
            "site": "sites",
            "tenant": "tenants",
            "rack": "racks",
            "tag": "tags",
            "role": "device_roles",
            "platform": "platforms",
            "device_type": "device_types",
            "manufacturer": "manufacturers",
        }

        if self.plurals:
            mapped = mapping.get(group_by)
            return mapped or group_by
        else:
            return group_by

    def _pluralize(self, extracted_value):
        # If plurals is enabled, wrap in a single-element list for backwards compatibility
        if self.plurals:
            return [extracted_value]
        else:
            return extracted_value

    def _objects_array_following_parents(
        self, initial_object_id, object_lookup, object_parent_lookup
    ):
        objects = []

        object_id = initial_object_id

        # Keep looping until the object has no parent
        while object_id is not None:
            object_slug = object_lookup[object_id]

            if object_slug in objects:
                # Won't ever happen - defensively guard against infinite loop
                break

            objects.append(object_slug)

            # Get the parent of this object
            object_id = object_parent_lookup[object_id]

        return objects

    def extract_disk(self, host):
        return host.get("disk")

    def extract_vcpus(self, host):
        return host.get("vcpus")

    def extract_status(self, host):
        return host["status"]

    def extract_memory(self, host):
        return host.get("memory")

    def extract_platform(self, host):
        try:
            return self._pluralize(self.platforms_lookup[host["platform"]["id"]])
        except Exception:
            return

    def extract_services(self, host):
        try:
            services_lookup = (
                self.vm_services_lookup
                if host["is_virtual"]
                else self.device_services_lookup
            )

            return list(services_lookup[host["id"]].values())

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

    def extract_rack_group(self, host):
        # A host may have a rack. A rack may have a rack_group. A rack_group may have a parent rack_group.
        # Produce a list of rack_groups:
        # - it will be empty if the device has no rack, or the rack has no rack_group
        # - it will have 1 element if the rack's group has no parent
        # - it will have multiple elements if the rack's group has a parent group

        rack = host.get("rack", None)
        if not isinstance(rack, dict):
            # Device has no rack
            return None

        rack_id = rack.get("id", None)
        if rack_id is None:
            # Device has no rack
            return None

        return self._objects_array_following_parents(
            initial_object_id=self.racks_group_lookup[rack_id],
            object_lookup=self.rack_groups_lookup,
            object_parent_lookup=self.rack_group_parent_lookup,
        )

    def extract_rack_role(self, host):
        try:
            return self.racks_role_lookup[host["rack"]["id"]]
        except Exception:
            return

    def extract_site(self, host):
        try:
            site = self.sites_lookup[host["site"]["id"]]
            if (
                self.prefixes
            ):  # If prefixes have been pulled, attach prefix list to its assigned site
                prefixes = self.prefixes_sites_lookup[site["id"]]
                site["prefixes"] = prefixes
            return self._pluralize(site)
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

    def extract_site_time_zone(self, host):
        try:
            return self.sites_time_zone_lookup[host["site"]["id"]]
        except Exception:
            return

    def extract_site_utc_offset(self, host):
        try:
            return self.sites_utc_offset_lookup[host["site"]["id"]]
        except Exception:
            return

    def extract_site_facility(self, host):
        try:
            return self.sites_facility_lookup[host["site"]["id"]]
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

    def extract_local_context_data(self, host):
        try:
            if self.flatten_local_context_data:
                # Don't wrap in an array if we're about to flatten it to separate host vars
                return host["local_context_data"]
            else:
                return self._pluralize(host["local_context_data"])
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

    def extract_oob_ip(self, host):
        try:
            address = host["oob_ip"]["address"]
            return str(ip_interface(address).ip)
        except Exception:
            return

    def extract_tags(self, host):
        try:
            tag_zero = host["tags"][0]
            # Check the type of the first element in the "tags" array.
            # If a dictionary (NetBox >= 2.9), return an array of tags' slugs.
            if isinstance(tag_zero, dict):
                return list(sub["slug"] for sub in host["tags"])
            # If a string (NetBox <= 2.8), return the original "tags" array.
            elif isinstance(tag_zero, str):
                return host["tags"]
        # If tag_zero fails definition (no tags), return the empty array.
        except Exception:
            return host["tags"]

    def extract_virtual_disks(self, host):
        try:
            virtual_disks_lookup = self.vm_virtual_disks_lookup
            virtual_disks = deepcopy(list(virtual_disks_lookup[host["id"]].values()))

            return virtual_disks
        except Exception:
            return

    def extract_interfaces(self, host):
        try:
            interfaces_lookup = (
                self.vm_interfaces_lookup
                if host["is_virtual"]
                else self.device_interfaces_lookup
            )

            interfaces = deepcopy(list(interfaces_lookup[host["id"]].values()))

            before_netbox_v29 = bool(self.ipaddresses_intf_lookup)
            # Attach IP Addresses to their interface
            for interface in interfaces:
                if before_netbox_v29:
                    interface["ip_addresses"] = list(
                        self.ipaddresses_intf_lookup[interface["id"]].values()
                    )
                else:
                    interface["ip_addresses"] = list(
                        self.vm_ipaddresses_intf_lookup[interface["id"]].values()
                        if host["is_virtual"]
                        else self.device_ipaddresses_intf_lookup[
                            interface["id"]
                        ].values()
                    )
                    interface["tags"] = list(sub["slug"] for sub in interface["tags"])

            return interfaces
        except Exception:
            return

    def extract_custom_fields(self, host):
        try:
            return {
                key: value
                for key, value in host["custom_fields"].items()
                if value is not None
            }
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

        return self._objects_array_following_parents(
            initial_object_id=self.sites_region_lookup[site_id],
            object_lookup=self.regions_lookup,
            object_parent_lookup=self.regions_parent_lookup,
        )

    def extract_site_groups(self, host):
        # A host may have a site. A site may have a site_group. A site_group may have a parent site_group.
        # Produce a list of site_groups:
        # - it will be empty if the device has no site, or the site has no site_group set
        # - it will have 1 element if the site's site_group has no parent
        # - it will have multiple elements if the site's site_group has a parent site_group

        site = host.get("site", None)
        if not isinstance(site, dict):
            # Device has no site
            return []

        site_id = site.get("id", None)
        if site_id is None:
            # Device has no site
            return []

        return self._objects_array_following_parents(
            initial_object_id=self.sites_site_group_lookup[site_id],
            object_lookup=self.site_groups_lookup,
            object_parent_lookup=self.site_groups_parent_lookup,
        )

    def extract_location(self, host):
        # A host may have a location. A location may have a parent location.
        # Produce a list of locations:
        # - it will be empty if the device has no location
        # - it will have 1 element if the device's location has no parent
        # - it will have multiple elements if the location has a parent location

        try:
            location_id = host["location"]["id"]
        except (KeyError, TypeError):
            # Device has no location
            return []

        return self._objects_array_following_parents(
            initial_object_id=location_id,
            object_lookup=self.locations_lookup,
            object_parent_lookup=self.locations_parent_lookup,
        )

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

    def extract_cluster_device(self, host):
        return host.get("device")

    def extract_is_virtual(self, host):
        return host.get("is_virtual")

    def extract_dns_name(self, host):
        # No primary IP assigned
        if not host.get("primary_ip"):
            return None

        before_netbox_v29 = bool(self.ipaddresses_lookup)
        if before_netbox_v29:
            ip_address = self.ipaddresses_lookup.get(host["primary_ip"]["id"])
        else:
            if host["is_virtual"]:
                ip_address = self.vm_ipaddresses_lookup.get(host["primary_ip"]["id"])
            else:
                ip_address = self.device_ipaddresses_lookup.get(
                    host["primary_ip"]["id"]
                )

        # Don"t assign a host_var for empty dns_name
        if ip_address.get("dns_name") == "":
            return None

        return ip_address.get("dns_name")

    def extract_serial(self, host):
        return host.get("serial", None)

    def extract_asset_tag(self, host):
        return host.get("asset_tag", None)

    def refresh_platforms_lookup(self):
        url = self.api_endpoint + "/api/dcim/platforms/?limit=0"
        platforms = self.get_resource_list(api_url=url)
        self.platforms_lookup = dict(
            (platform["id"], platform["slug"]) for platform in platforms
        )

    def refresh_sites_lookup(self):
        # Three dictionaries are created here.
        # "sites_lookup_slug" only contains the slug. Used by _add_site_groups() when creating inventory groups
        # "sites_lookup" contains the full data structure. Most site lookups use this
        # "sites_with_prefixes" keeps track of which sites have prefixes assigned. Passed to get_resource_list_chunked()
        url = self.api_endpoint + "/api/dcim/sites/?limit=0"
        sites = self.get_resource_list(api_url=url)
        # The following dictionary is used for host group creation only,
        # as the grouping function expects a string as the value of each key
        self.sites_lookup_slug = dict((site["id"], site["slug"]) for site in sites)
        if self.site_data or self.prefixes:
            # If the "site_data" option is specified, keep the full data structure presented by the API response.
            # The "prefixes" option necessitates this structure as well as it requires the site object to be dict().
            self.sites_lookup = dict((site["id"], site) for site in sites)
        else:
            # Otherwise, set equal to the "slug only" dictionary
            self.sites_lookup = self.sites_lookup_slug
        # The following dictionary tracks which sites have prefixes assigned.
        self.sites_with_prefixes = set()

        for site in sites:
            if site["prefix_count"] and site["prefix_count"] > 0:
                self.sites_with_prefixes.add(site["slug"])
                # Used by refresh_prefixes()

        def get_region_for_site(site):
            # Will fail if site does not have a region defined in NetBox
            try:
                return (site["id"], site["region"]["id"])
            except Exception:
                return (site["id"], None)

        # Dictionary of site id to region id
        self.sites_region_lookup = dict(map(get_region_for_site, sites))

        def get_site_group_for_site(site):
            # Will fail if site does not have a group defined in NetBox
            try:
                return (site["id"], site["group"]["id"])
            except Exception:
                return (site["id"], None)

        # Dictionary of site id to site_group id
        self.sites_site_group_lookup = dict(map(get_site_group_for_site, sites))

        def get_time_zone_for_site(site):
            # Will fail if site does not have a time_zone defined in NetBox
            try:
                return (site["id"], site["time_zone"].replace("/", "_", 2))
            except Exception:
                return (site["id"], None)

        # Dictionary of site id to time_zone name (if group by time_zone is used)
        if "time_zone" in self.group_by:
            self.sites_time_zone_lookup = dict(map(get_time_zone_for_site, sites))

        def get_utc_offset_for_site(site):
            # Will fail if site does not have a time_zone defined in NetBox
            try:
                utc = round(
                    datetime.datetime.now(pytz.timezone(site["time_zone"]))
                    .utcoffset()
                    .total_seconds()
                    / 60
                    / 60
                )
                if utc < 0:
                    return (site["id"], str(utc).replace("-", "minus_"))
                else:
                    return (site["id"], f"plus_{utc}")
            except Exception:
                return (site["id"], None)

        # Dictionary of site id to utc_offset name (if group by utc_offset is used)
        if "utc_offset" in self.group_by:
            self.sites_utc_offset_lookup = dict(map(get_utc_offset_for_site, sites))

        def get_facility_for_site(site):
            # Will fail if site does not have a facility defined in NetBox
            try:
                return (site["id"], site["facility"])
            except Exception:
                return (site["id"], None)

        # Dictionary of site id to facility (if group by facility is used)
        if "facility" in self.group_by:
            self.sites_facility_lookup = dict(map(get_facility_for_site, sites))

    # Note: depends on the result of refresh_sites_lookup for self.sites_with_prefixes
    def refresh_prefixes(self):
        # Pull all prefixes defined in NetBox
        url = self.api_endpoint + "/api/ipam/prefixes"

        prefixes = self.get_resource_list(url)
        self.prefixes_sites_lookup = defaultdict(list)

        # We are only concerned with Prefixes that have actually been assigned to sites
        for prefix in prefixes:
            # NetBox >=4.2
            if (
                prefix.get("scope_type") == "dcim.site"
                and prefix.get("scope") is not None
            ):
                self.prefixes_sites_lookup[prefix["scope"]["id"]].append(prefix)
            # NetBox <=4.1
            elif prefix.get("site"):
                self.prefixes_sites_lookup[prefix["site"]["id"]].append(prefix)
                # Remove "site" attribute, as it's redundant when prefixes are assigned to site
                del prefix["site"]

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

    def refresh_site_groups_lookup(self):
        if self.api_version < version.parse("2.11"):
            return

        url = self.api_endpoint + "/api/dcim/site-groups/?limit=0"
        site_groups = self.get_resource_list(api_url=url)
        self.site_groups_lookup = dict(
            (site_group["id"], site_group["slug"]) for site_group in site_groups
        )

        def get_site_group_parent(site_group):
            # Will fail if site_group does not have a parent site_group
            try:
                return (site_group["id"], site_group["parent"]["id"])
            except Exception:
                return (site_group["id"], None)

        # Dictionary of site_group id to parent site_group id
        self.site_groups_parent_lookup = dict(
            filter(lambda x: x is not None, map(get_site_group_parent, site_groups))
        )

    def refresh_locations_lookup(self):
        # Locations were added in v2.11. Return empty lookups for previous versions.
        if self.api_version < version.parse("2.11"):
            return

        url = self.api_endpoint + "/api/dcim/locations/?limit=0"
        locations = self.get_resource_list(api_url=url)
        self.locations_lookup = dict(
            (location["id"], location["slug"]) for location in locations
        )

        def get_location_parent(location):
            # Will fail if location does not have a parent location
            try:
                return (location["id"], location["parent"]["id"])
            except Exception:
                return (location["id"], None)

        def get_location_site(location):
            # Locations MUST be assigned to a site
            return (location["id"], location["site"]["id"])

        # Dictionary of location id to parent location id
        self.locations_parent_lookup = dict(
            filter(None, map(get_location_parent, locations))
        )
        # Location to site lookup
        self.locations_site_lookup = dict(map(get_location_site, locations))

    def refresh_tenants_lookup(self):
        url = self.api_endpoint + "/api/tenancy/tenants/?limit=0"
        tenants = self.get_resource_list(api_url=url)
        self.tenants_lookup = dict((tenant["id"], tenant["slug"]) for tenant in tenants)

    def refresh_racks_lookup(self):
        url = self.api_endpoint + "/api/dcim/racks/?limit=0"
        racks = self.get_resource_list(api_url=url)
        self.racks_lookup = dict((rack["id"], rack["name"]) for rack in racks)

        def get_group_for_rack(rack):
            try:
                return (rack["id"], rack["group"]["id"])
            except Exception:
                return (rack["id"], None)

        def get_role_for_rack(rack):
            try:
                return (rack["id"], rack["role"]["slug"])
            except Exception:
                return (rack["id"], None)

        self.racks_group_lookup = dict(map(get_group_for_rack, racks))
        self.racks_role_lookup = dict(map(get_role_for_rack, racks))

    def refresh_rack_groups_lookup(self):
        # Locations were added in v2.11 replacing rack groups. Do nothing for 2.11+
        if self.api_version >= version.parse("2.11"):
            return

        url = self.api_endpoint + "/api/dcim/rack-groups/?limit=0"
        rack_groups = self.get_resource_list(api_url=url)
        self.rack_groups_lookup = dict(
            (rack_group["id"], rack_group["slug"]) for rack_group in rack_groups
        )

        def get_rack_group_parent(rack_group):
            try:
                return (rack_group["id"], rack_group["parent"]["id"])
            except Exception:
                return (rack_group["id"], None)

        # Dictionary of rack group id to parent rack group id
        self.rack_group_parent_lookup = dict(map(get_rack_group_parent, rack_groups))

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

        self.clusters_type_lookup = dict(map(get_cluster_type, clusters))
        self.clusters_group_lookup = dict(map(get_cluster_group, clusters))

    def refresh_services(self):
        url = self.api_endpoint + "/api/ipam/services/?limit=0"
        services = []

        if self.fetch_all:
            services = self.get_resource_list(url)
        elif self.api_version >= version.parse("4.3.0"):
            services = self.get_resource_list_chunked(
                api_url=url,
                query_key="parent_object_id",
                # Query only affected devices and vms and sanitize the list to only contain every ID once
                query_values=set(
                    chain(self.vms_lookup.keys(), self.devices_lookup.keys())
                ),
            )
        else:
            device_services = self.get_resource_list_chunked(
                api_url=url,
                query_key="device_id",
                query_values=self.devices_lookup.keys(),
            )
            vm_services = self.get_resource_list_chunked(
                api_url=url,
                query_key="virtual_machine_id",
                query_values=self.vms_lookup.keys(),
            )
            services = chain(device_services, vm_services)

        # Construct a dictionary of dictionaries, separately for devices and vms.
        # Allows looking up services by device id or vm id
        self.device_services_lookup = defaultdict(dict)
        self.vm_services_lookup = defaultdict(dict)

        for service in services:
            service_id = service["id"]

            if self.api_version >= version.parse("4.3.0"):
                if service.get("parent_object_type") == "dcim.device":
                    self.device_services_lookup[service["parent_object_id"]][
                        service_id
                    ] = service

                if service.get("parent_object_type") == "virtualization.virtualmachine":
                    self.vm_services_lookup[service["parent_object_id"]][
                        service_id
                    ] = service
            else:
                if service.get("device"):
                    self.device_services_lookup[service["device"]["id"]][
                        service_id
                    ] = service

                if service.get("virtual_machine"):
                    self.vm_services_lookup[service["virtual_machine"]["id"]][
                        service_id
                    ] = service

    def refresh_virtual_disks(self):
        url_vm_virtual_disks = (
            self.api_endpoint + "/api/virtualization/virtual-disks/?limit=0"
        )

        vm_virtual_disks = []

        if self.fetch_all:
            vm_virtual_disks = self.get_resource_list(url_vm_virtual_disks)
        else:
            vm_virtual_disks = self.get_resource_list_chunked(
                api_url=url_vm_virtual_disks,
                query_key="virtual_machine_id",
                query_values=self.vms_lookup.keys(),
            )

        self.vm_virtual_disks_lookup = defaultdict(dict)

        for virtual_disk in vm_virtual_disks:
            virtual_disk_id = virtual_disk["id"]
            vm_id = virtual_disk["virtual_machine"]["id"]

            self.vm_virtual_disks_lookup[vm_id][virtual_disk_id] = virtual_disk

    def refresh_interfaces(self):
        url_device_interfaces = self.api_endpoint + "/api/dcim/interfaces/?limit=0"
        url_vm_interfaces = (
            self.api_endpoint + "/api/virtualization/interfaces/?limit=0"
        )

        device_interfaces = []
        vm_interfaces = []

        if self.fetch_all:
            device_interfaces = self.get_resource_list(url_device_interfaces)
            vm_interfaces = self.get_resource_list(url_vm_interfaces)
        else:
            device_interfaces = self.get_resource_list_chunked(
                api_url=url_device_interfaces,
                query_key="device_id",
                query_values=self.devices_lookup.keys(),
            )
            vm_interfaces = self.get_resource_list_chunked(
                api_url=url_vm_interfaces,
                query_key="virtual_machine_id",
                query_values=self.vms_lookup.keys(),
            )

        # Construct a dictionary of dictionaries, separately for devices and vms.
        # For a given device id or vm id, get a lookup of interface id to interface
        # This is because interfaces may be returned multiple times when querying for virtual chassis parent and child in separate queries
        self.device_interfaces_lookup = defaultdict(dict)
        self.vm_interfaces_lookup = defaultdict(dict)

        # /dcim/interfaces gives count_ipaddresses per interface. /virtualization/interfaces does not
        self.devices_with_ips = set()

        for interface in device_interfaces:
            interface_id = interface["id"]
            device_id = interface["device"]["id"]

            # Check if device_id is actually a device we've fetched, and was not filtered out by query_filters
            if device_id not in self.devices_lookup:
                continue

            # Check if device_id is part of a virtual chasis
            # If so, treat its interfaces as actually part of the master
            device = self.devices_lookup[device_id]
            virtual_chassis_master = self._get_host_virtual_chassis_master(device)
            if virtual_chassis_master is not None:
                device_id = virtual_chassis_master

            self.device_interfaces_lookup[device_id][interface_id] = interface

            # Keep track of what devices have interfaces with IPs, so if fetch_all is False we can avoid unnecessary queries
            if interface["count_ipaddresses"] > 0:
                self.devices_with_ips.add(device_id)

        for interface in vm_interfaces:
            interface_id = interface["id"]
            vm_id = interface["virtual_machine"]["id"]

            self.vm_interfaces_lookup[vm_id][interface_id] = interface

    # Note: depends on the result of refresh_interfaces for self.devices_with_ips
    def refresh_ipaddresses(self):
        url = (
            self.api_endpoint
            + "/api/ipam/ip-addresses/?limit=0&assigned_to_interface=true"
        )
        ipaddresses = []

        if self.fetch_all:
            ipaddresses = self.get_resource_list(url)
        else:
            device_ips = self.get_resource_list_chunked(
                api_url=url,
                query_key="device_id",
                query_values=list(self.devices_with_ips),
            )
            vm_ips = self.get_resource_list_chunked(
                api_url=url,
                query_key="virtual_machine_id",
                query_values=self.vms_lookup.keys(),
            )

            ipaddresses = chain(device_ips, vm_ips)

        # Construct a dictionary of lists, to allow looking up ip addresses by interface id
        # Note that interface ids share the same namespace for both devices and vms so this is a single dictionary
        self.ipaddresses_intf_lookup = defaultdict(dict)
        # Construct a dictionary of the IP addresses themselves
        self.ipaddresses_lookup = defaultdict(dict)
        # NetBox v2.9 and onwards
        self.vm_ipaddresses_intf_lookup = defaultdict(dict)
        self.vm_ipaddresses_lookup = defaultdict(dict)
        self.device_ipaddresses_intf_lookup = defaultdict(dict)
        self.device_ipaddresses_lookup = defaultdict(dict)

        for ipaddress in ipaddresses:
            # As of NetBox v2.9 "assigned_object_x" replaces "interface"
            if ipaddress.get("assigned_object_id"):
                interface_id = ipaddress["assigned_object_id"]
                ip_id = ipaddress["id"]
                # We need to copy the ipaddress entry to preserve the original in case caching is used.
                ipaddress_copy = ipaddress.copy()

                if ipaddress["assigned_object_type"] == "virtualization.vminterface":
                    self.vm_ipaddresses_lookup[ip_id] = ipaddress_copy
                    self.vm_ipaddresses_intf_lookup[interface_id][
                        ip_id
                    ] = ipaddress_copy
                else:
                    self.device_ipaddresses_lookup[ip_id] = ipaddress_copy
                    self.device_ipaddresses_intf_lookup[interface_id][
                        ip_id
                    ] = ipaddress_copy  # Remove "assigned_object_X" attributes, as that's redundant when ipaddress is added to an interface

                del ipaddress_copy["assigned_object_id"]
                del ipaddress_copy["assigned_object_type"]
                del ipaddress_copy["assigned_object"]
                continue

            if not ipaddress.get("interface"):
                continue
            interface_id = ipaddress["interface"]["id"]
            ip_id = ipaddress["id"]

            # We need to copy the ipaddress entry to preserve the original in case caching is used.
            ipaddress_copy = ipaddress.copy()

            self.ipaddresses_intf_lookup[interface_id][ip_id] = ipaddress_copy
            self.ipaddresses_lookup[ip_id] = ipaddress_copy
            # Remove "interface" attribute, as that's redundant when ipaddress is added to an interface
            del ipaddress_copy["interface"]

    @property
    def lookup_processes(self):
        lookups = [
            self.refresh_sites_lookup,
            self.refresh_regions_lookup,
            self.refresh_site_groups_lookup,
            self.refresh_locations_lookup,
            self.refresh_tenants_lookup,
            self.refresh_device_roles_lookup,
            self.refresh_platforms_lookup,
            self.refresh_device_types_lookup,
            self.refresh_manufacturers_lookup,
            self.refresh_clusters_lookup,
        ]
        if self.virtual_disks:
            lookups.append(self.refresh_virtual_disks)

        if self.interfaces:
            lookups.append(self.refresh_interfaces)

        if self.services:
            lookups.append(self.refresh_services)

        if self.racks:
            lookups.extend(
                [
                    self.refresh_racks_lookup,
                    self.refresh_rack_groups_lookup,
                ]
            )

        return lookups

    @property
    def lookup_processes_secondary(self):
        lookups = []

        # IP addresses are needed for either interfaces or dns_name options
        if self.interfaces or self.dns_name or self.ansible_host_dns_name:
            lookups.append(self.refresh_ipaddresses)

        if self.prefixes:
            lookups.append(self.refresh_prefixes)

        return lookups

    def refresh_lookups(self, lookups):
        # Exceptions that occur in threads by default are printed to stderr, and ignored by the main thread
        # They need to be caught, and raised in the main thread to prevent further execution of this plugin

        thread_exceptions = []

        def handle_thread_exceptions(lookup):
            def wrapper():
                try:
                    lookup()
                except Exception as e:
                    # Save for the main-thread to re-raise
                    # Also continue to raise on this thread, so the default handler can run to print to stderr
                    thread_exceptions.append(e)
                    raise e

            return wrapper

        thread_list = []

        try:
            for lookup in lookups:
                thread = Thread(target=handle_thread_exceptions(lookup))
                thread_list.append(thread)
                thread.start()

            for thread in thread_list:
                thread.join()

            # Wait till we've joined all threads before raising any exceptions
            for exception in thread_exceptions:
                raise exception

        finally:
            # Avoid retain cycles
            thread_exceptions = None

    def fetch_api_docs(self):
        try:
            tmp_dir = os.path.split(DEFAULT_LOCAL_TMP)[0]
            tmp_file = os.path.join(tmp_dir, "netbox_api_dump.json")
            with open(tmp_file) as file:
                cache = json.load(file)
            cached_api_version = ".".join(cache["info"]["version"].split(".")[:2])
        except Exception:
            cached_api_version = None
            cache = None

        status = self._fetch_information(self.api_endpoint + "/api/status/")
        netbox_api_version = ".".join(status["netbox-version"].split(".")[:2])

        if version.parse(netbox_api_version) >= version.parse("3.5.0"):
            endpoint_url = self.api_endpoint + "/api/schema/?format=json"
        else:
            endpoint_url = self.api_endpoint + "/api/docs/?format=openapi"

        if cache and cached_api_version == netbox_api_version:
            openapi = cache
        else:
            openapi = self._fetch_information(endpoint_url)

            try:
                with open(tmp_file, "w") as file:
                    json.dump(openapi, file)
            except Exception:
                pass

        self.api_version = version.parse(netbox_api_version)
        parsed_endpoint_url = urlparse(self.api_endpoint)
        base_path = parsed_endpoint_url.path

        if self.api_version >= version.parse("3.5.0"):
            self.allowed_device_query_parameters = [
                p["name"]
                for p in openapi["paths"][base_path + "/api/dcim/devices/"]["get"][
                    "parameters"
                ]
            ]
            self.allowed_vm_query_parameters = [
                p["name"]
                for p in openapi["paths"][
                    base_path + "/api/virtualization/virtual-machines/"
                ]["get"]["parameters"]
            ]
        else:
            self.allowed_device_query_parameters = [
                p["name"]
                for p in openapi["paths"][base_path + "/dcim/devices/"]["get"][
                    "parameters"
                ]
            ]
            self.allowed_vm_query_parameters = [
                p["name"]
                for p in openapi["paths"][
                    base_path + "/virtualization/virtual-machines/"
                ]["get"]["parameters"]
            ]

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
                    self.query_filters, self.allowed_device_query_parameters
                )
            )

            vm_query_parameters.extend(
                self.filter_query_parameters(
                    self.query_filters, self.allowed_vm_query_parameters
                )
            )

        if isinstance(self.device_query_filters, Iterable):
            device_query_parameters.extend(
                self.filter_query_parameters(
                    self.device_query_filters, self.allowed_device_query_parameters
                )
            )

        if isinstance(self.vm_query_filters, Iterable):
            vm_query_parameters.extend(
                self.filter_query_parameters(
                    self.vm_query_filters, self.allowed_vm_query_parameters
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

        self.devices_list = []
        self.vms_list = []

        if device_url:
            self.devices_list = self.get_resource_list(device_url)

        if vm_url:
            self.vms_list = self.get_resource_list(vm_url)

        # Allow looking up devices/vms by their ids
        self.devices_lookup = {device["id"]: device for device in self.devices_list}
        self.vms_lookup = {vm["id"]: vm for vm in self.vms_list}

        # There's nothing that explicitly says if a host is virtual or not - add in a new field
        for host in self.devices_list:
            host["is_virtual"] = False

        for host in self.vms_list:
            host["is_virtual"] = True

    def extract_name(self, host):
        # An host in an Ansible inventory requires an hostname.
        # name is an unique but not required attribute for a device in NetBox
        # We default to an UUID for hostname in case the name is not set in NetBox
        # Use virtual chassis name if set by the user.
        if self.virtual_chassis_name and self._get_host_virtual_chassis_master(host):
            return host["virtual_chassis"]["name"] or str(uuid.uuid4())
        elif self.hostname_field:
            return host["custom_fields"][self.hostname_field]
        else:
            return host["name"] or str(uuid.uuid4())

    def generate_group_name(self, grouping, group):
        # Check for special case - if group is a boolean, just return grouping name instead
        # eg. "is_virtual" - returns true for VMs, should put them in a group named "is_virtual", not "is_virtual_True"
        if isinstance(group, bool):
            if group:
                return grouping
            else:
                # Don't create the inverse group
                return None

        # Special case. Extract name from service, which is a hash.
        if grouping == "services":
            group = group["name"]
            grouping = "service"

        if grouping == "status":
            group = group["value"]

        if self.group_names_raw:
            return group
        else:
            return "_".join([grouping, group])

    def add_host_to_groups(self, host, hostname):
        site_group_by = self._pluralize_group_by("site")
        site_group_group_by = self._pluralize_group_by("site_group")

        for grouping in self.group_by:
            # Don't handle regions here since no hosts are ever added to region groups
            # Sites and locations are also specially handled in the main()
            if grouping in ["region", site_group_by, "location", site_group_group_by]:
                continue

            if grouping not in self.group_extractors:
                raise AnsibleError(
                    'group_by option "%s" is not valid. Check group_by documentation or'
                    " check the plurals option, as well as the racks options. It can"
                    " determine what group_by options are valid." % grouping
                )

            groups_for_host = self.group_extractors[grouping](host)

            if not groups_for_host:
                continue

            # Make groups_for_host a list if it isn't already
            if not isinstance(groups_for_host, list):
                groups_for_host = [groups_for_host]

            for group_for_host in groups_for_host:
                group_name = self.generate_group_name(grouping, group_for_host)

                if not group_name:
                    continue

                # Group names may be transformed by the ansible TRANSFORM_INVALID_GROUP_CHARS setting
                # add_group returns the actual group name used
                transformed_group_name = self.inventory.add_group(group=group_name)
                self.inventory.add_host(group=transformed_group_name, host=hostname)

    def _add_site_groups(self):
        # Map site id to transformed group names
        self.site_group_names = dict()

        for (
            site_id,
            site_name,
        ) in self.sites_lookup_slug.items():  # "Slug" only. Data not used for grouping
            site_group_name = self.generate_group_name(
                self._pluralize_group_by("site"), site_name
            )
            # Add the site group to get its transformed name
            site_transformed_group_name = self.inventory.add_group(
                group=site_group_name
            )
            self.site_group_names[site_id] = site_transformed_group_name

    def _add_region_groups(self):
        # Mapping of region id to group name
        region_transformed_group_names = self._setup_nested_groups(
            "region", self.regions_lookup, self.regions_parent_lookup
        )

        # Add site groups as children of region groups
        for site_id in self.sites_lookup:
            region_id = self.sites_region_lookup.get(site_id, None)
            if region_id is None:
                continue

            self.inventory.add_child(
                region_transformed_group_names[region_id],
                self.site_group_names[site_id],
            )

    def _add_site_group_groups(self):
        # Mapping of site_group id to group name
        site_group_transformed_group_names = self._setup_nested_groups(
            "site_group", self.site_groups_lookup, self.site_groups_parent_lookup
        )

        # Add site groups as children of site_group groups
        for site_id in self.sites_lookup:
            site_group_id = self.sites_site_group_lookup.get(site_id, None)
            if site_group_id is None:
                continue

            self.inventory.add_child(
                site_group_transformed_group_names[site_group_id],
                self.site_group_names[site_id],
            )

    def _add_location_groups(self):
        # Mapping of location id to group name
        self.location_group_names = self._setup_nested_groups(
            "location", self.locations_lookup, self.locations_parent_lookup
        )

        # Add location to site groups as children
        for location_id, location_slug in self.locations_lookup.items():
            if self.locations_parent_lookup.get(location_id, None):
                # Only top level locations should be children of sites
                continue

            site_transformed_group_name = self.site_group_names[
                self.locations_site_lookup[location_id]
            ]

            self.inventory.add_child(
                site_transformed_group_name, self.location_group_names[location_id]
            )

    def _setup_nested_groups(self, group, lookup, parent_lookup):
        # Mapping of id to group name
        transformed_group_names = dict()

        # Create groups for each object
        for obj_id in lookup:
            group_name = self.generate_group_name(group, lookup[obj_id])
            transformed_group_names[obj_id] = self.inventory.add_group(group=group_name)

        # Now that all groups exist, add relationships between them
        for obj_id in lookup:
            group_name = transformed_group_names[obj_id]
            parent_id = parent_lookup.get(obj_id, None)
            if parent_id is not None and parent_id in transformed_group_names:
                parent_name = transformed_group_names[parent_id]
                self.inventory.add_child(parent_name, group_name)

        return transformed_group_names

    def _set_variable(self, hostname, key, value):
        for item in self.rename_variables:
            if item["pattern"].match(key):
                key = item["pattern"].sub(item["repl"], key)
                break

        self.inventory.set_variable(hostname, key, value)

    def _fill_host_variables(self, host, hostname):
        extracted_primary_ip = self.extract_primary_ip(host=host)
        if extracted_primary_ip:
            self._set_variable(hostname, "ansible_host", extracted_primary_ip)

        if self.ansible_host_dns_name:
            extracted_dns_name = self.extract_dns_name(host=host)
            if extracted_dns_name:
                self._set_variable(hostname, "ansible_host", extracted_dns_name)

        extracted_primary_ip4 = self.extract_primary_ip4(host=host)
        if extracted_primary_ip4:
            self._set_variable(hostname, "primary_ip4", extracted_primary_ip4)

        extracted_primary_ip6 = self.extract_primary_ip6(host=host)
        if extracted_primary_ip6:
            self._set_variable(hostname, "primary_ip6", extracted_primary_ip6)

        extracted_oob_ip = self.extract_oob_ip(host=host)
        if extracted_oob_ip:
            self._set_variable(hostname, "oob_ip", extracted_oob_ip)
            if self.oob_ip_as_primary_ip:
                self._set_variable(hostname, "ansible_host", extracted_oob_ip)

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

            if attribute == "site_group":
                attribute = "site_groups"

            if attribute == "location":
                attribute = "locations"

            if attribute == "rack_group":
                attribute = "rack_groups"

            # Flatten the dict into separate host vars, if enabled
            if isinstance(extracted_value, dict) and (
                (attribute == "config_context" and self.flatten_config_context)
                or (attribute == "custom_fields" and self.flatten_custom_fields)
                or (
                    attribute == "local_context_data"
                    and self.flatten_local_context_data
                )
            ):
                for key, value in extracted_value.items():
                    self._set_variable(hostname, key, value)
            else:
                self._set_variable(hostname, attribute, extracted_value)

    def _get_host_virtual_chassis_master(self, host):
        virtual_chassis = host.get("virtual_chassis", None)

        if not virtual_chassis:
            return None

        master = virtual_chassis.get("master", None)

        if not master:
            return None

        return master.get("id", None)

    def main(self):
        # Check if pytz lib is install, and give error if not
        if PYTZ_IMPORT_ERROR:
            raise AnsibleError(
                "pytz must be installed to use this plugin"
            ) from PYTZ_IMPORT_ERROR

        # Get info about the API - version, allowed query parameters
        self.fetch_api_docs()

        self.fetch_hosts()

        # Interface, and Service lookup will depend on hosts, if option fetch_all is false
        self.refresh_lookups(self.lookup_processes)

        # Looking up IP Addresses depends on the result of interfaces count_ipaddresses field
        # - can skip any device/vm without any IPs
        self.refresh_lookups(self.lookup_processes_secondary)

        # If we're grouping by regions, hosts are not added to region groups
        # If we're grouping by locations, hosts may be added to the site or location
        # - the site groups are added as sub-groups of regions
        # - the location groups are added as sub-groups of sites
        # So, we need to make sure we're also grouping by sites if regions or locations are enabled
        site_group_by = self._pluralize_group_by("site")
        site_group_group_by = self._pluralize_group_by("site")
        if (
            site_group_by in self.group_by
            or "location" in self.group_by
            or "region" in self.group_by
            or site_group_group_by in self.group_by
        ):
            self._add_site_groups()

        # Create groups for locations. Will be a part of site groups.
        if "location" in self.group_by and self.api_version >= version.parse("2.11"):
            self._add_location_groups()

        # Create groups for regions, containing the site groups
        if "region" in self.group_by:
            self._add_region_groups()

        # Create groups for site_groups, containing the site groups
        if "site_group" in self.group_by and self.api_version >= version.parse("2.11"):
            self._add_site_group_groups()

        for host in chain(self.devices_list, self.vms_list):
            virtual_chassis_master = self._get_host_virtual_chassis_master(host)
            if (
                virtual_chassis_master is not None
                and virtual_chassis_master != host["id"]
            ):
                # Device is part of a virtual chassis, but is not the master
                continue

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

            # Special processing for sites and locations as those groups were already created
            if getattr(self, "location_group_names", None) and host.get("location"):
                # Add host to location group when host is assigned to the location
                self.inventory.add_host(
                    group=self.location_group_names[host["location"]["id"]],
                    host=hostname,
                )
            elif getattr(self, "site_group_names", None) and host.get("site"):
                # Add host to site group when host is NOT assigned to a location
                self.inventory.add_host(
                    group=self.site_group_names[host["site"]["id"]],
                    host=hostname,
                )

    def _set_authorization(self):
        # NetBox access
        if version.parse(ansible_version) < version.parse("2.11"):
            token = self.get_option("token")
        else:
            self.templar.available_variables = self._vars
            token = self.templar.template(
                self.get_option("token"), fail_on_undefined=False
            )
        if token:
            # check if token is new format
            if isinstance(token, dict):
                self.headers.update(
                    {"Authorization": f"{token['type'].capitalize()} {token['value']}"}
                )
            else:
                self.headers.update({"Authorization": "Token %s" % token})
        headers = self.get_option("headers")
        if headers:
            if isinstance(headers, str):
                headers = json.loads(headers)
            if isinstance(headers, dict):
                self.headers.update(headers)

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path=path)
        self.use_cache = cache

        # Handle extra "/" from api_endpoint configuration and trim if necessary, see PR#49943
        self.api_endpoint = self.get_option("api_endpoint").strip("/")
        self.timeout = self.get_option("timeout")
        self.max_uri_length = self.get_option("max_uri_length")
        self.validate_certs = self.get_option("validate_certs")
        self.follow_redirects = self.get_option("follow_redirects")
        self.config_context = self.get_option("config_context")
        self.flatten_config_context = self.get_option("flatten_config_context")
        self.flatten_local_context_data = self.get_option("flatten_local_context_data")
        self.flatten_custom_fields = self.get_option("flatten_custom_fields")
        self.plurals = self.get_option("plurals")
        self.virtual_disks = self.get_option("virtual_disks")
        self.interfaces = self.get_option("interfaces")
        self.services = self.get_option("services")
        self.site_data = self.get_option("site_data")
        self.prefixes = self.get_option("prefixes")
        self.fetch_all = self.get_option("fetch_all")
        self.headers = {
            "User-Agent": "ansible %s Python %s"
            % (ansible_version, python_version.split(" ", maxsplit=1)[0]),
            "Content-type": "application/json",
        }
        self.cert = self.get_option("cert")
        self.key = self.get_option("key")
        self.ca_path = self.get_option("ca_path")
        self.oob_ip_as_primary_ip = self.get_option("oob_ip_as_primary_ip")
        self.hostname_field = self.get_option("hostname_field")

        self._set_authorization()

        # Filter and group_by options
        self.group_by = self.get_option("group_by")
        self.group_names_raw = self.get_option("group_names_raw")
        if version.parse(ansible_version) < version.parse("2.11"):
            self.query_filters = self.get_option("query_filters")
            self.device_query_filters = self.get_option("device_query_filters")
            self.vm_query_filters = self.get_option("vm_query_filters")
        else:
            self.query_filters = self.templar.template(self.get_option("query_filters"))
            self.device_query_filters = self.templar.template(
                self.get_option("device_query_filters")
            )
            self.vm_query_filters = self.templar.template(
                self.get_option("vm_query_filters")
            )
        self.virtual_chassis_name = self.get_option("virtual_chassis_name")
        self.dns_name = self.get_option("dns_name")
        self.ansible_host_dns_name = self.get_option("ansible_host_dns_name")
        self.racks = self.get_option("racks")

        # Compile regular expressions, if any
        self.rename_variables = self.parse_rename_variables(
            self.get_option("rename_variables")
        )

        self.main()

    def parse_rename_variables(self, rename_variables):
        return [
            {"pattern": re.compile(i["pattern"]), "repl": i["repl"]}
            for i in rename_variables or ()
        ]
