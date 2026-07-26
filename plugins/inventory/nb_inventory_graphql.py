# Copyright (c) 2026 Mikulas Willaschek
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
    name: nb_inventory_graphql
    author:
      - Mikulas Willaschek
    short_description: Generic NetBox inventory source using the GraphQL API
    description:
      - Builds an Ansible inventory from one or more user-defined GraphQL queries against a
        NetBox instance ("sources"). The plugin has no built-in knowledge of the NetBox schema;
        it sends whatever query a source points to, walks the response to a list of objects, and
        turns each object into a host. All fields of an object become host variables verbatim.
      - Grouping and derived host variables are handled entirely through the standard Ansible
        C(constructed) fragment (C(compose), C(groups), C(keyed_groups)) rather than
        plugin-specific options — this is what makes the plugin generic across VMs, devices, or
        any other NetBox object type without requiring new Python code or options per type.
      - Nested data (services, interfaces, IP addresses, ...) is resolved server-side by
        GraphQL, so no client-side joining of separately fetched endpoints takes place.
      - C(sources[].query_file) is required — this plugin does not ship a default query. Minimal
        starter queries for virtual machines and devices (C(id), C(name), C(primary_ip4),
        C(primary_ip6)) are shipped under C(examples/nb_inventory_graphql/) in this collection;
        copy and extend them for anything more.
      - Targets NetBox 4.6.5. No version branching is performed.
    extends_documentation_fragment:
      - ansible.builtin.constructed
      - ansible.builtin.inventory_cache
    options:
      plugin:
        description: Token that ensures this is a source file for the C(nb_inventory_graphql) plugin.
        required: true
        choices: ["netbox.netbox.nb_inventory_graphql"]
        type: str
      api_endpoint:
        description: Root URL of the NetBox instance. The GraphQL endpoint is derived as C(<api_endpoint>/graphql/).
        required: true
        type: str
        env:
          - name: NETBOX_API
      token:
        description:
          - NetBox API token.
          - May be a plain string, which is sent as header C(Authorization) with value C(Token <value>).
          - May also be a dictionary with the keys C(type) and C(value), which is sent as
            header C(Authorization) with value C(<Type> <value>) to support Bearer or OAuth tokens.
        required: false
        type: raw
        env:
          - name: NETBOX_TOKEN
          - name: NETBOX_API_KEY
      validate_certs:
        description: Whether to validate the TLS certificate of the NetBox instance.
        default: true
        type: boolean
      cert:
        description: Path to a client certificate used for mutual TLS.
        type: path
      key:
        description: Path to the private key belonging to I(cert).
        type: path
      ca_path:
        description: Path to a CA bundle used to validate the NetBox certificate.
        type: path
      follow_redirects:
        description: How to handle HTTP redirects returned by NetBox.
        default: urllib2
        choices: ["urllib2", "all", "yes", "safe", "none"]
        type: str
      timeout:
        description: Timeout in seconds for the GraphQL request.
        default: 60
        type: int
      headers:
        description:
          - Additional HTTP headers merged into the request after the authorization header.
          - Useful for example to select a branch with C(X-NetBox-Branch).
        default: {}
        type: dict
        env:
          - name: NETBOX_HEADERS
      ansible_host_dns_name:
        description:
          - Use the DNS name of the primary IP as C(ansible_host) instead of the IP itself.
          - Falls back to the IP address when the primary IP has no DNS name.
          - Kept as an explicit, dedicated option rather than expressed through C(compose)
            because C(ansible_host) is security-relevant (it is the SSH connection target) and
            the fallback chain (DNS name, then IPv4, then IPv6, then unset) is intricate enough
            to warrant a small, directly testable Python function over a Jinja expression. It can
            still be overridden per-host via C(compose).
          - Only takes effect for objects whose GraphQL selection includes a C(primary_ip4) and/or
            C(primary_ip6) field shaped as C({address, dns_name}), matching NetBox's own schema.
        default: false
        type: boolean
      sources:
        description:
          - One or more independent GraphQL queries. Every source is fetched with its own HTTP
            request(s) (paginated, see O(sources[].list_path)) and every element found in it
            becomes one inventory host.
          - If two sources produce the same hostname, the source that runs later in the list wins
            (its fields overwrite same-named fields from the earlier source) and a warning is
            emitted — sources are not merged silently.
        required: true
        type: list
        elements: dict
        version_added: "3.24.0"
        options:
          name:
            description: Unique label for this source, used in error messages and warnings only.
            required: true
            type: str
          query_file:
            description:
              - Path to a C(.graphql) file containing the query to run.
              - Relative paths are resolved against the directory of the inventory configuration
                file (not the current working directory).
              - The query SHOULD declare and use a C($pagination) variable of type
                C(OffsetPaginationInput) on its top-level list field so the plugin can paginate
                large result sets; if it does not, NetBox silently ignores the extra variable and
                only the server's default page is returned.
            required: true
            type: path
          list_path:
            description:
              - Dotted path to the list of objects inside the GraphQL response's C(data) object,
                for example C(virtual_machine_list) or C(nested.list_field).
              - This is a plain, recursive dictionary lookup — not a query language of its own.
            required: true
            type: str
          hostname:
            description:
              - Jinja2 template evaluated against each raw object from O(sources[].list_path) to
                produce the inventory hostname.
              - Falls back to a random UUID if the template renders empty, matching how NetBox
                itself allows unnamed devices.
            required: true
            type: str
          variables:
            description:
              - GraphQL query variables, passed through to the request unmodified (in addition to
                the pagination variable the plugin injects itself).
            default: {}
            type: dict
"""

EXAMPLES = r"""
# --- (a) Minimal example: one source, no grouping -------------------------------------------
# See examples/nb_inventory_graphql/ in this collection for ready-to-copy starter files
# (netbox_graphql.yml + queries/virtual_machines.graphql + queries/devices.graphql).
plugin: netbox.netbox.nb_inventory_graphql
api_endpoint: "{{ lookup('env', 'NETBOX_API') }}"
token: "{{ lookup('env', 'NETBOX_TOKEN') }}"
sources:
  - name: vms
    query_file: queries/virtual_machines.graphql
    list_path: virtual_machine_list
    hostname: "{{ name }}"

# --- (b) group by service name and by status --------------------------------------------------
plugin: netbox.netbox.nb_inventory_graphql
api_endpoint: "{{ lookup('env', 'NETBOX_API') }}"
token: "{{ lookup('env', 'NETBOX_TOKEN') }}"
ansible_host_dns_name: true
sources:
  - name: vms
    query_file: queries/virtual_machines.graphql
    list_path: virtual_machine_list
    hostname: "{{ name }}"
keyed_groups:
  - key: services | map(attribute='name') | list
    prefix: service
  - key: status
    prefix: status

# --- (c) compose reference cases -------------------------------------------------------------
plugin: netbox.netbox.nb_inventory_graphql
api_endpoint: "{{ lookup('env', 'NETBOX_API') }}"
token: "{{ lookup('env', 'NETBOX_TOKEN') }}"
sources:
  - name: vms
    query_file: queries/virtual_machines.graphql
    list_path: virtual_machine_list
    hostname: "{{ name }}"
compose:
  # Use case 1: "first element matching a condition" — pure standard Jinja, no plugin support needed.
  n8n_service: >-
    services | selectattr('name', 'equalto', 'n8n') | list | first | default(omit)
  # Use case 2: cross-referencing two independent nested structures against each other (which
  # interface owns the primary IP?) — selectattr can only compare against a fixed value, not
  # recurse into another variable's nested list, so this needs the any_attribute_equals test
  # shipped alongside this plugin.
  primary_interface: >-
    interfaces
    | selectattr('ip_addresses', 'any_attribute_equals', 'address', primary_ip4.address)
    | first | default(omit)

# --- (d) two sources: VMs and devices in one inventory ---------------------------------------
plugin: netbox.netbox.nb_inventory_graphql
api_endpoint: "{{ lookup('env', 'NETBOX_API') }}"
token: "{{ lookup('env', 'NETBOX_TOKEN') }}"
sources:
  - name: vms
    query_file: queries/virtual_machines.graphql
    list_path: virtual_machine_list
    hostname: "{{ name }}"
  - name: devices
    query_file: queries/devices.graphql
    list_path: device_list
    hostname: "{{ name }}"
groups:
  netbox_devices: "device_type is defined"
"""

import json
import os
import uuid
from ipaddress import ip_interface
from urllib.error import HTTPError, URLError

from ansible.errors import AnsibleError
from ansible.module_utils.common.text.converters import to_native, to_text
from ansible.module_utils.urls import open_url
from ansible.plugins.inventory import BaseInventoryPlugin, Cacheable, Constructable

# NetBox's MAX_PAGE_SIZE for this deployment. Sent as an explicit pagination argument on every
# request; a server-side default limit could not be determined empirically (see the PR description
# for the verification performed against a live NetBox 4.6.5 instance).
PAGE_SIZE = 1000


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "nb_inventory_graphql"

    def verify_file(self, path):
        if not super(InventoryModule, self).verify_file(path):
            return False
        return path.endswith((".yml", ".yaml"))

    def _set_authorization(self):
        """Build the request headers. Never log their content — they carry the token."""
        self.headers = {"Content-Type": "application/json"}

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
        if isinstance(headers, str):
            headers = json.loads(headers)
        if headers:
            self.headers.update(headers)

    def _post_graphql(self, query, variables):
        """Issue one POST request and return the GraphQL 'data' object."""
        body = json.dumps({"query": query, "variables": variables})
        try:
            response = open_url(
                self.graphql_url,
                data=body,
                method="POST",
                headers=self.headers,
                timeout=self.get_option("timeout"),
                validate_certs=self.get_option("validate_certs"),
                follow_redirects=self.get_option("follow_redirects"),
                client_cert=self.get_option("cert"),
                client_key=self.get_option("key"),
                ca_path=self.get_option("ca_path"),
            )
        except HTTPError as e:
            if e.code == 401:
                raise AnsibleError(
                    "nb_inventory_graphql: HTTP 401 Unauthorized. "
                    "The 'token' option is missing or invalid."
                )
            if e.code == 403:
                raise AnsibleError(
                    "nb_inventory_graphql: HTTP 403 Forbidden. "
                    "The token does not have permission to read the GraphQL API."
                )
            raise AnsibleError(
                "nb_inventory_graphql: HTTP %s from %s: %s"
                % (e.code, self.graphql_url, to_native(e.read()))
            )
        except URLError as e:
            raise AnsibleError(
                "nb_inventory_graphql: could not reach %s: %s. Consider raising the 'timeout' option."
                % (self.graphql_url, to_native(e.reason))
            )

        try:
            raw = to_text(response.read(), errors="surrogate_or_strict")
        except UnicodeError:
            raise AnsibleError(
                "nb_inventory_graphql: incorrect encoding of the response from NetBox."
            )

        try:
            payload = json.loads(raw)
        except ValueError:
            raise AnsibleError(
                "nb_inventory_graphql: NetBox did not return JSON from %s. This usually means no "
                "valid token was supplied and NetBox redirected to its login page."
                % self.graphql_url
            )

        errors = payload.get("errors")
        data = payload.get("data")
        if errors:
            messages = "; ".join(err.get("message", str(err)) for err in errors)
            if not data:
                raise AnsibleError(
                    "nb_inventory_graphql: GraphQL errors: %s" % messages
                )
            self.display.warning(
                "nb_inventory_graphql: partial GraphQL errors: %s" % messages
            )

        return data or {}

    def _resolve_query_path(self, query_file):
        if os.path.isabs(query_file):
            return query_file
        return os.path.join(self._inventory_dir, query_file)

    def _read_query_file(self, query_file):
        path = self._resolve_query_path(query_file)
        try:
            return self.loader.get_text_file_contents(path)
        except AnsibleError as e:
            raise AnsibleError(
                "nb_inventory_graphql: could not read query_file '%s' ('%s'): %s"
                % (query_file, path, to_native(e))
            )

    @staticmethod
    def _resolve_list_path(data, list_path, source_name):
        """Walk a dotted path into the GraphQL 'data' object."""
        node = data
        for segment in list_path.split("."):
            if not isinstance(node, dict) or segment not in node:
                raise AnsibleError(
                    "nb_inventory_graphql: source '%s': list_path '%s' not found in the response. "
                    "Available top-level keys: %s."
                    % (source_name, list_path, sorted(data.keys()))
                )
            node = node[segment]
        if not isinstance(node, list):
            raise AnsibleError(
                "nb_inventory_graphql: source '%s': list_path '%s' does not resolve to a list (got %s)."
                % (source_name, list_path, type(node).__name__)
            )
        return node

    def _fetch_source_elements(self, source):
        """Fetch all objects of one source, paginating defensively until a short page is seen."""
        query = self._read_query_file(source["query_file"])
        base_variables = source.get("variables") or {}
        elements = []
        offset = 0
        while True:
            variables = dict(
                base_variables, pagination={"offset": offset, "limit": PAGE_SIZE}
            )
            data = self._post_graphql(query, variables)
            page = self._resolve_list_path(data, source["list_path"], source["name"])
            elements.extend(page)
            if len(page) < PAGE_SIZE:
                break
            offset += PAGE_SIZE
        return elements

    @staticmethod
    def _extract_ip(ip_object):
        """Strip the prefix length off a NetBox address field, e.g. '10.0.0.1/24' -> '10.0.0.1'."""
        if not ip_object or not ip_object.get("address"):
            return None
        return str(ip_interface(ip_object["address"]).ip)

    def _derive_ansible_host(self, element, hostname):
        """ansible_host stays explicit Python, not Jinja — see the option's docstring for why."""
        primary_ip = element.get("primary_ip4") or element.get("primary_ip6")
        if not primary_ip:
            return

        address = self._extract_ip(primary_ip)
        if address:
            self.inventory.set_variable(hostname, "ansible_host", address)

        if self.get_option("ansible_host_dns_name"):
            dns_name = primary_ip.get("dns_name")
            if dns_name:
                self.inventory.set_variable(hostname, "ansible_host", dns_name)

    def _render_hostname(self, template, element):
        self.templar.available_variables = element
        hostname = self.templar.template(template, fail_on_undefined=False)
        return hostname or str(uuid.uuid4())

    def _populate_host_from_element(self, source, element, seen_hosts):
        """Turn one raw GraphQL object into a host: dump fields, derive ansible_host, then run the
        standard Constructable hooks against the resulting host variables."""
        hostname = self._render_hostname(source["hostname"], element)

        previous_source = seen_hosts.get(hostname)
        if previous_source is not None and previous_source != source["name"]:
            self.display.warning(
                "nb_inventory_graphql: host '%s' from source '%s' overwrites data previously set "
                "by source '%s'." % (hostname, source["name"], previous_source)
            )
        seen_hosts[hostname] = source["name"]

        self.inventory.add_host(host=hostname)
        for key, value in element.items():
            self.inventory.set_variable(hostname, key, value)
        self._derive_ansible_host(element, hostname)

        host_vars = self.inventory.get_host(hostname).get_vars()
        strict = self.get_option("strict")
        self._set_composite_vars(
            self.get_option("compose"), host_vars, hostname, strict=strict
        )
        self._add_host_to_composed_groups(
            self.get_option("groups"), host_vars, hostname, strict=strict
        )
        self._add_host_to_keyed_groups(
            self.get_option("keyed_groups"), host_vars, hostname, strict=strict
        )

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)
        self._inventory_dir = os.path.dirname(os.path.abspath(path))

        # TODO: cache each source's GraphQL result under get_cache_key(endpoint + query + variables).
        self.use_cache = cache
        if self.get_option("cache"):
            self.display.warning(
                "nb_inventory_graphql: the 'cache' option has no effect yet, caching is not implemented."
            )

        api_endpoint = self.templar.template(
            self.get_option("api_endpoint"), fail_on_undefined=False
        )
        if not api_endpoint:
            raise AnsibleError("nb_inventory_graphql: 'api_endpoint' is required.")
        self.graphql_url = "%s/graphql/" % api_endpoint.rstrip("/")

        self._set_authorization()

        seen_hosts = {}
        for source in self.get_option("sources"):
            for element in self._fetch_source_elements(source):
                self._populate_host_from_element(source, element, seen_hosts)
