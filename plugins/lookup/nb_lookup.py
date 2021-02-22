# -*- coding: utf-8 -*-

# Copyright: (c) 2019. Chris Mills <chris@discreet-its.co.uk>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
netbox.py

A lookup function designed to return data from the Netbox application
"""

from __future__ import absolute_import, division, print_function

import os
import functools
from pprint import pformat

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.parsing.splitter import parse_kv, split_args
from ansible.utils.display import Display

import pynetbox
import requests

__metaclass__ = type

DOCUMENTATION = """
    lookup: nb_lookup
    author: Chris Mills (@cpmills1975)
    version_added: "2.9"
    short_description: Queries and returns elements from Netbox
    description:
        - Queries Netbox via its API to return virtually any information
          capable of being held in Netbox.
        - If wanting to obtain the plaintext attribute of a secret, key_file must be provided.
    options:
        _terms:
            description:
                - The Netbox object type to query
            required: True
        api_endpoint:
            description:
                - The URL to the Netbox instance to query
            env:
                # in order of precendence
                - name: NETBOX_API
                - name: NETBOX_URL
            required: True
        api_filter:
            description:
                - The api_filter to use.
            required: False
        plugin:
            description:
                - The Netbox plugin to query
            required: False
        token:
            description:
                - The API token created through Netbox
                - This may not be required depending on the Netbox setup.
            env:
                # in order of precendence
                - name: NETBOX_TOKEN
                - name: NETBOX_API_TOKEN
            required: False
        validate_certs:
            description:
                - Whether or not to validate SSL of the NetBox instance
            required: False
            default: True
        key_file:
            description:
                - The location of the private key tied to user account.
            required: False
        raw_data:
            description:
                - Whether to return raw API data with the lookup/query or whether to return a key/value dict
            required: False
    requirements:
        - pynetbox
"""

EXAMPLES = """
tasks:
  # query a list of devices
  - name: Obtain list of devices from Netbox
    debug:
      msg: >
        "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
         manufactured by {{ item.value.device_type.manufacturer.name }}"
    loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                    api_endpoint='http://localhost/',
                    token='<redacted>') }}"

# This example uses an API Filter

tasks:
  # query a list of devices
  - name: Obtain list of devices from Netbox
    debug:
      msg: >
        "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
         manufactured by {{ item.value.device_type.manufacturer.name }}"
    loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                    api_endpoint='http://localhost/',
                    api_filter='role=management tag=Dell'),
                    token='<redacted>') }}"

# Obtain a secret for R1-device
tasks:
  - name: "Obtain secrets for R1-Device"
    debug:
      msg: "{{ query('netbox.netbox.nb_lookup', 'secrets', api_filter='device=R1-Device', api_endpoint='http://localhost/', token='<redacted>', key_file='~/.ssh/id_rsa') }}"

# Fetch bgp sessions for R1-device
tasks:
  - name: "Obtain bgp sessions for R1-Device"
    debug:
      msg: "{{ query('netbox.netbox.nb_lookup', 'bgp_sessions',
                     api_filter='device=R1-Device',
                     api_endpoint='http://localhost/',
                     token='<redacted>',
                     plugin='mycustomstuff') }}"

      msg: "{{ query('netbox.netbox.nb_lookup', 'secrets', api_filter='device=R1-Device', api_endpoint='http://localhost/', token='<redacted>', key_file='~/.ssh/id_rsa') }}"
"""

RETURN = """
  _list:
    description:
      - list of composed dictionaries with key and value
    type: list
"""


def get_endpoint(netbox, term):
    """
    get_endpoint(netbox, term)
        netbox: a predefined pynetbox.api() pointing to a valid instance
                of Netbox
        term: the term passed to the lookup function upon which the api
              call will be identified
    """

    netbox_endpoint_map = {
        "aggregates": {"endpoint": netbox.ipam.aggregates},
        "circuit-terminations": {"endpoint": netbox.circuits.circuit_terminations},
        "circuit-types": {"endpoint": netbox.circuits.circuit_types},
        "circuits": {"endpoint": netbox.circuits.circuits},
        "circuit-providers": {"endpoint": netbox.circuits.providers},
        "cables": {"endpoint": netbox.dcim.cables},
        "cluster-groups": {"endpoint": netbox.virtualization.cluster_groups},
        "cluster-types": {"endpoint": netbox.virtualization.cluster_types},
        "clusters": {"endpoint": netbox.virtualization.clusters},
        "config-contexts": {"endpoint": netbox.extras.config_contexts},
        "console-connections": {"endpoint": netbox.dcim.console_connections},
        "console-ports": {"endpoint": netbox.dcim.console_ports},
        "console-server-port-templates": {
            "endpoint": netbox.dcim.console_server_port_templates
        },
        "console-server-ports": {"endpoint": netbox.dcim.console_server_ports},
        "device-bay-templates": {"endpoint": netbox.dcim.device_bay_templates},
        "device-bays": {"endpoint": netbox.dcim.device_bays},
        "device-roles": {"endpoint": netbox.dcim.device_roles},
        "device-types": {"endpoint": netbox.dcim.device_types},
        "devices": {"endpoint": netbox.dcim.devices},
        "export-templates": {"endpoint": netbox.dcim.export_templates},
        "front-port-templates": {"endpoint": netbox.dcim.front_port_templates},
        "front-ports": {"endpoint": netbox.dcim.front_ports},
        "graphs": {"endpoint": netbox.extras.graphs},
        "image-attachments": {"endpoint": netbox.extras.image_attachments},
        "interface-connections": {"endpoint": netbox.dcim.interface_connections},
        "interface-templates": {"endpoint": netbox.dcim.interface_templates},
        "interfaces": {"endpoint": netbox.dcim.interfaces},
        "inventory-items": {"endpoint": netbox.dcim.inventory_items},
        "ip-addresses": {"endpoint": netbox.ipam.ip_addresses},
        "manufacturers": {"endpoint": netbox.dcim.manufacturers},
        "object-changes": {"endpoint": netbox.extras.object_changes},
        "platforms": {"endpoint": netbox.dcim.platforms},
        "power-connections": {"endpoint": netbox.dcim.power_connections},
        "power-outlet-templates": {"endpoint": netbox.dcim.power_outlet_templates},
        "power-outlets": {"endpoint": netbox.dcim.power_outlets},
        "power-port-templates": {"endpoint": netbox.dcim.power_port_templates},
        "power-ports": {"endpoint": netbox.dcim.power_ports},
        "prefixes": {"endpoint": netbox.ipam.prefixes},
        "rack-groups": {"endpoint": netbox.dcim.rack_groups},
        "rack-reservations": {"endpoint": netbox.dcim.rack_reservations},
        "rack-roles": {"endpoint": netbox.dcim.rack_roles},
        "racks": {"endpoint": netbox.dcim.racks},
        "rear-port-templates": {"endpoint": netbox.dcim.rear_port_templates},
        "rear-ports": {"endpoint": netbox.dcim.rear_ports},
        "regions": {"endpoint": netbox.dcim.regions},
        "reports": {"endpoint": netbox.extras.reports},
        "rirs": {"endpoint": netbox.ipam.rirs},
        "roles": {"endpoint": netbox.ipam.roles},
        "secret-roles": {"endpoint": netbox.secrets.secret_roles},
        "secrets": {"endpoint": netbox.secrets.secrets},
        "services": {"endpoint": netbox.ipam.services},
        "sites": {"endpoint": netbox.dcim.sites},
        "tags": {"endpoint": netbox.extras.tags},
        "tenant-groups": {"endpoint": netbox.tenancy.tenant_groups},
        "tenants": {"endpoint": netbox.tenancy.tenants},
        "topology-maps": {"endpoint": netbox.extras.topology_maps},
        "virtual-chassis": {"endpoint": netbox.dcim.virtual_chassis},
        "virtual-machines": {"endpoint": netbox.virtualization.virtual_machines},
        "virtualization-interfaces": {"endpoint": netbox.virtualization.interfaces},
        "vlan-groups": {"endpoint": netbox.ipam.vlan_groups},
        "vlans": {"endpoint": netbox.ipam.vlans},
        "vrfs": {"endpoint": netbox.ipam.vrfs},
    }

    return netbox_endpoint_map[term]["endpoint"]


def build_filters(filters):
    """
    This will build the filters to be handed to NetBox endpoint call if they exist.

    Args:
        filters (str): String of filters to parse.

    Returns:
        result (list): List of dictionaries to filter by.
    """
    filter = {}
    args_split = split_args(filters)
    args = [parse_kv(x) for x in args_split]
    for arg in args:
        for k, v in arg.items():
            if k not in filter:
                filter[k] = list()
                filter[k].append(v)
            else:
                filter[k].append(v)

    return filter


def get_plugin_endpoint(netbox, plugin, term):
    """
    get_plugin_endpoint(netbox, plugin, term)
        netbox: a predefined pynetbox.api() pointing to a valid instance
                of Netbox
        plugin: a string referencing the plugin name
        term: the term passed to the lookup function upon which the api
              call will be identified
    """
    attr = "plugins.%s.%s" % (plugin, term)

    def _getattr(netbox, attr):
        return getattr(netbox, attr)

    return functools.reduce(_getattr, [netbox] + attr.split("."))


def make_netbox_call(nb_endpoint, filters=None):
    """
    Wrapper for calls to NetBox and handle any possible errors.

    Args:
        nb_endpoint (object): The NetBox endpoint object to make calls.

    Returns:
        results (object): Pynetbox result.

    Raises:
        AnsibleError: Ansible Error containing an error message.
    """
    try:
        if filters:
            results = nb_endpoint.filter(**filters)
        else:
            results = nb_endpoint.all()
    except pynetbox.RequestError as e:
        if e.req.status_code == 404 and "plugins" in e:
            raise AnsibleError(
                "{0} - Not a valid plugin endpoint, please make sure to provide valid plugin endpoint.".format(
                    e.error
                )
            )
        else:
            raise AnsibleError(e.error)

    return results


class LookupModule(LookupBase):
    """
    LookupModule(LookupBase) is defined by Ansible
    """

    def run(self, terms, variables=None, **kwargs):

        netbox_api_token = (
            kwargs.get("token")
            or os.getenv("NETBOX_TOKEN")
            or os.getenv("NETBOX_API_TOKEN")
        )
        netbox_api_endpoint = (
            kwargs.get("api_endpoint")
            or os.getenv("NETBOX_API")
            or os.getenv("NETBOX_URL")
        )
        netbox_ssl_verify = kwargs.get("validate_certs", True)
        netbox_private_key_file = kwargs.get("key_file")
        netbox_api_filter = kwargs.get("api_filter")
        netbox_raw_return = kwargs.get("raw_data")
        netbox_plugin = kwargs.get("plugin")

        if not isinstance(terms, list):
            terms = [terms]

        try:
            session = requests.Session()
            session.verify = netbox_ssl_verify

            netbox = pynetbox.api(
                netbox_api_endpoint,
                token=netbox_api_token if netbox_api_token else None,
                private_key_file=netbox_private_key_file,
            )
            netbox.http_session = session
        except FileNotFoundError:
            raise AnsibleError(
                "%s cannot be found. Please make sure file exists."
                % netbox_private_key_file
            )

        results = []
        for term in terms:
            if netbox_plugin:
                endpoint = get_plugin_endpoint(netbox, netbox_plugin, term)
            else:
                try:
                    endpoint = get_endpoint(netbox, term)
                except KeyError:
                    raise AnsibleError(
                        "Unrecognised term %s. Check documentation" % term
                    )

            Display().vvvv(
                u"Netbox lookup for %s to %s using token %s filter %s"
                % (term, netbox_api_endpoint, netbox_api_token, netbox_api_filter)
            )

            if netbox_api_filter:
                filter = build_filters(netbox_api_filter)

                if "id" in filter:
                    Display().vvvv(
                        u"Filter is: %s and includes id, will use .get instead of .filter"
                        % (filter)
                    )
                    try:
                        id = int(filter["id"][0])
                        nb_data = endpoint.get(id)
                        data = dict(nb_data)
                        Display().vvvvv(pformat(data))
                        return [data]
                    except pynetbox.RequestError as e:
                        raise AnsibleError(e.error)

                Display().vvvv("filter is %s" % filter)

            # Make call to NetBox API and capture any failures
            nb_data = make_netbox_call(
                endpoint, filters=filter if netbox_api_filter else None
            )

            for data in nb_data:
                data = dict(data)
                Display().vvvvv(pformat(data))

                if netbox_raw_return:
                    results.append(data)
                else:
                    key = data["id"]
                    result = {key: data}
                    results.extend(self._flatten_hash_to_list(result))

        return results
