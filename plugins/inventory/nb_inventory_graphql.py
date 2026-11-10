# Copyright (c) 2026 Mikulas Willaschek
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: nb_inventory_graphql
    author:
        - Mikulas Willaschek (@MikuuW)
    short_description: NetBox inventory source using the GraphQL API
    version_added: "3.25.0"
    description:
        - Get inventory hosts from NetBox with user-defined GraphQL queries.
        - Every object returned by a query becomes a host. Every field selected in the query becomes a host variable.
        - The C(name) field is not set as a host variable because the name is reserved in Ansible. It is still available
          in the expressions of this plugin. Use a GraphQL alias to keep it, or to rename other reserved names like C(tags).
        - Groups and additional variables are created with the C(compose), C(groups) and C(keyed_groups) options.
    extends_documentation_fragment:
        - constructed
        - inventory_cache
    options:
        plugin:
            description: token that ensures this is a source file for the 'nb_inventory_graphql' plugin.
            required: true
            choices: ['netbox.netbox.nb_inventory_graphql']
        api_endpoint:
            description: Endpoint of the NetBox API
            required: true
            env:
                - name: NETBOX_API
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
        validate_certs:
            description:
                - Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.
            default: true
            type: boolean
        cert:
            description:
                - Certificate path
            type: path
        key:
            description:
                - Certificate key path
            type: path
        ca_path:
            description:
                - CA path
            type: path
        follow_redirects:
            description:
                - Determine how redirects are followed.
                - By default, I(follow_redirects) is set to uses urllib2 default behavior.
            default: urllib2
            choices: ['urllib2', 'all', 'yes', 'safe', 'none']
        timeout:
            description: Timeout for NetBox requests in seconds
            type: int
            default: 60
        headers:
            description: Dictionary of headers to be passed to the NetBox API.
            default: {}
            env:
                - name: NETBOX_HEADERS
        ansible_host_dns_name:
            description:
                - If True, sets DNS Name (fetched from primary_ip) to be used in ansible_host variable, instead of IP Address.
                - C(ansible_host) is only set if the query selects C(address) (and C(dns_name)) of C(primary_ip4) or C(primary_ip6).
            type: boolean
            default: false
        sources:
            description:
                - List of GraphQL queries to build the inventory from.
                - If several sources return a host with the same name, the variables of the later source win.
            required: true
            type: list
            elements: dict
            suboptions:
                query_file:
                    description:
                        - Path to a file containing the GraphQL query.
                        - Relative paths are resolved against the directory of the inventory source file.
                        - To fetch more than one page, the query has to declare C($pagination) of type C(OffsetPaginationInput)
                          and pass it to the list field. Without it a single request is sent and NetBox decides how many
                          objects it returns.
                    required: true
                    type: path
                list_path:
                    description: Name of the list field in the query response, for example C(device_list).
                    required: true
                    type: str
                hostname:
                    description:
                        - Jinja2 expression evaluated against each object to get the inventory hostname.
                        - By default, the inventory hostname is the C(name) field of the object.
                        - A random UUID is used if the result is empty.
                    type: str
                variables:
                    description: Variables to be passed to the GraphQL query.
                    type: dict
                    default: {}
"""

EXAMPLES = """
# netbox_inventory.yml file in YAML format
# Example command line: ansible-inventory -v --list -i netbox_inventory.yml
#
# devices.graphql, next to the inventory file:
#
#   query ($pagination: OffsetPaginationInput) {
#     device_list(pagination: $pagination) {
#       name
#       status
#       role { slug }
#       primary_ip4 { address dns_name }
#     }
#   }

plugin: netbox.netbox.nb_inventory_graphql
api_endpoint: http://localhost:8000
token: <insert token>
sources:
  - query_file: devices.graphql
    list_path: device_list
keyed_groups:
  - prefix: role
    key: role.slug
  - prefix: status
    key: status

# Devices and virtual machines in one inventory, each with its own query

plugin: netbox.netbox.nb_inventory_graphql
api_endpoint: http://localhost:8000
token:
  type: Bearer
  value: test123456
ansible_host_dns_name: true
sources:
  - query_file: devices.graphql
    list_path: device_list
  - query_file: virtual_machines.graphql
    list_path: virtual_machine_list
    hostname: name ~ '.example.com'
groups:
  virtual: cluster is defined
"""

import json
import os
import uuid
from ipaddress import ip_interface
from urllib.error import HTTPError, URLError

from ansible.errors import AnsibleError
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.urls import open_url
from ansible.plugins.inventory import BaseInventoryPlugin, Cacheable, Constructable

PAGE_SIZE = 1000


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "netbox.netbox.nb_inventory_graphql"

    def _query(self, query, variables):
        try:
            response = open_url(
                self.api_endpoint + "/graphql/",
                data=json.dumps({"query": query, "variables": variables}),
                method="POST",
                headers=self.headers,
                timeout=self.get_option("timeout"),
                validate_certs=self.get_option("validate_certs"),
                follow_redirects=self.get_option("follow_redirects"),
                client_cert=self.get_option("cert"),
                client_key=self.get_option("key"),
                ca_path=self.get_option("ca_path"),
            )
            result = json.loads(response.read())
        except HTTPError as e:
            raise AnsibleError(
                "NetBox returned HTTP %s: %s" % (e.code, to_native(e.read()))
            )
        except URLError as e:
            raise AnsibleError(
                "Failed to connect to %s: %s" % (self.api_endpoint, to_native(e.reason))
            )
        except ValueError:
            raise AnsibleError("NetBox did not return JSON. Check api_endpoint.")

        if result.get("errors"):
            raise AnsibleError(
                "GraphQL query failed: %s"
                % "; ".join(to_native(e.get("message")) for e in result["errors"])
            )
        return result["data"]

    def _fetch_source(self, source, path):
        query_file = os.path.join(os.path.dirname(path), source["query_file"])
        try:
            with open(query_file, encoding="utf-8") as f:
                query = f.read()
        except OSError as e:
            raise AnsibleError("Could not read query_file: %s" % to_native(e))

        variables = dict(source.get("variables") or {})
        list_path = source["list_path"]

        cache_key = self.get_cache_key(
            json.dumps([self.api_endpoint, query, variables, list_path], sort_keys=True)
        )
        user_cache_setting = self.get_option("cache")
        if user_cache_setting and self.use_cache:
            try:
                return self._cache[cache_key]
            except KeyError:
                pass

        # A query that does not take $pagination returns the same objects for
        # every offset, so it is only sent once.
        paginate = "$pagination" in query
        objects = []
        while True:
            if paginate:
                variables["pagination"] = {"offset": len(objects), "limit": PAGE_SIZE}
            data = self._query(query, variables)
            if not isinstance(data.get(list_path), list):
                raise AnsibleError(
                    "list_path '%s' is not a list in the response of %s. Returned fields: %s"
                    % (list_path, source["query_file"], ", ".join(data))
                )
            # NetBox may return fewer objects than requested (MAX_PAGE_SIZE),
            # so only an empty page marks the end.
            objects.extend(data[list_path])
            if not paginate or not data[list_path]:
                break

        if user_cache_setting:
            self._cache[cache_key] = objects
        return objects

    def _ansible_host(self, obj):
        primary_ip = obj.get("primary_ip4") or obj.get("primary_ip6")
        if not isinstance(primary_ip, dict):
            return None
        if self.get_option("ansible_host_dns_name") and primary_ip.get("dns_name"):
            return primary_ip["dns_name"]
        if primary_ip.get("address"):
            return str(ip_interface(primary_ip["address"]).ip)
        return None

    def _add_host(self, obj, hostname_expression):
        strict = self.get_option("strict")
        if hostname_expression:
            try:
                hostname = self._compose(hostname_expression, obj)
            except Exception as e:
                raise AnsibleError(
                    "Could not evaluate hostname '%s': %s"
                    % (hostname_expression, to_native(e))
                )
        else:
            hostname = obj.get("name")
        hostname = self.inventory.add_host(
            to_native(hostname) if hostname else str(uuid.uuid4())
        )

        for key, value in obj.items():
            # "name" is a reserved variable name in Ansible
            if key != "name":
                self.inventory.set_variable(hostname, key, value)
        ansible_host = self._ansible_host(obj)
        if ansible_host:
            self.inventory.set_variable(hostname, "ansible_host", ansible_host)

        host_vars = dict(self.inventory.get_host(hostname).get_vars(), **obj)
        self._set_composite_vars(
            self.get_option("compose"), host_vars, hostname, strict=strict
        )
        self._add_host_to_composed_groups(
            self.get_option("groups"), host_vars, hostname, strict=strict
        )
        self._add_host_to_keyed_groups(
            self.get_option("keyed_groups"), host_vars, hostname, strict=strict
        )

    def _set_authorization(self):
        self.templar.available_variables = self._vars
        token = self.templar.template(self.get_option("token"), fail_on_undefined=False)
        if token:
            if isinstance(token, dict):
                self.headers["Authorization"] = "%s %s" % (
                    token["type"].capitalize(),
                    token["value"],
                )
            else:
                self.headers["Authorization"] = "Token %s" % token
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

        self.api_endpoint = self.get_option("api_endpoint").strip("/")
        self.headers = {"Content-type": "application/json"}
        self._set_authorization()

        for source in self.get_option("sources"):
            for obj in self._fetch_source(source, path):
                self._add_host(obj, source.get("hostname"))
