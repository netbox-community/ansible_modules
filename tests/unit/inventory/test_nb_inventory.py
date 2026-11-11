# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Hillsong, Douglas Heriot (@DouglasHeriot) <douglas.heriot@hillsong.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from functools import partial
from pathlib import Path
from unittest.mock import Mock, call, mock_open, patch

import pytest
from packaging import version

try:
    from ansible_collections.netbox.netbox.plugins.inventory.nb_inventory import (
        InventoryModule,
    )
    from ansible_collections.netbox.netbox.tests.unit.helpers.load_data import (
        load_test_data,
    )

except ImportError:
    import sys

    # Not installed as a collection
    # Try importing relative to root directory of this ansible_modules project

    sys.path.append("plugins/inventory")
    sys.path.append("tests")
    from tests.unit.helpers.load_data import load_test_data

load_relative_test_data = partial(load_test_data, Path(__file__).resolve().parent)


class MockInventory:
    def __init__(self):
        self.variables = {}

    def set_variable(self, hostname, key, value):
        if hostname not in self.variables:
            self.variables[hostname] = {}

        self.variables[hostname][key] = value


@pytest.fixture
def inventory_fixture(
    allowed_device_query_parameters_fixture, allowed_vm_query_parameters_fixture
):
    inventory = InventoryModule()
    inventory.api_endpoint = "https://netbox.test.endpoint:1234"

    # Fill in data that is fetched dynamically
    inventory.api_version = version.Version("2.0")
    inventory.allowed_device_query_parameters = allowed_device_query_parameters_fixture
    inventory.allowed_vm_query_parameters = allowed_vm_query_parameters_fixture

    # Inventory mock, to validate what has been set via inventory.inventory.set_variable
    inventory.inventory = MockInventory()

    return inventory


@pytest.fixture
def templar_fixture():
    templar = Mock()

    return templar


@pytest.fixture
def allowed_device_query_parameters_fixture():
    # Subset of parameters - real list is fetched dynamically from NetBox openapi endpoint
    return [
        "id",
        "interfaces",
        "has_primary_ip",
        "mac_address",
        "name",
        "platform",
        "rack_id",
        "region",
        "role",
        "tag",
    ]


@pytest.fixture
def allowed_vm_query_parameters_fixture():
    # Subset of parameters - real list is fetched dynamically from NetBox openapi endpoint
    return [
        "id",
        "virtual_disks",
        "interfaces",
        "disk",
        "mac_address",
        "name",
        "platform",
        "region",
        "role",
        "tag",
    ]


@pytest.mark.parametrize(
    "parameter, expected", load_relative_test_data("validate_query_parameter")
)
def test_validate_query_parameter(inventory_fixture, parameter, expected):
    value = "some value, doesn't matter"
    result = inventory_fixture.validate_query_parameter(
        {parameter: value}, inventory_fixture.allowed_device_query_parameters
    )
    assert (result == (parameter, value)) == expected


@pytest.mark.parametrize(
    "parameters, expected", load_relative_test_data("filter_query_parameters")
)
def test_filter_query_parameters(inventory_fixture, parameters, expected):
    result = inventory_fixture.filter_query_parameters(
        parameters, inventory_fixture.allowed_device_query_parameters
    )

    # Result is iterators of tuples
    # expected from json file is an array of dicts

    # Convert result iterator to list so we can get the length, and iterate over with an index
    result_list = list(result)

    assert len(result_list) == len(expected)

    for i, parameter in enumerate(result_list):
        assert parameter[0] == list(expected[i].keys())[0]
        assert parameter[1] == list(expected[i].values())[0]


@pytest.mark.parametrize("options, expected", load_relative_test_data("refresh_url"))
def test_refresh_url(inventory_fixture, options, expected):
    inventory_fixture.query_filters = options["query_filters"]
    inventory_fixture.device_query_filters = options["device_query_filters"]
    inventory_fixture.vm_query_filters = options["vm_query_filters"]
    inventory_fixture.config_context = options["config_context"]

    result = inventory_fixture.refresh_url()

    assert result == tuple(expected)


def test_refresh_lookups(inventory_fixture):
    def raises_exception():
        raise Exception("Error from within a thread")

    def does_not_raise():
        pass

    with pytest.raises(Exception) as e:
        inventory_fixture.refresh_lookups([does_not_raise, raises_exception])
    assert "Error from within a thread" in str(e)

    inventory_fixture.refresh_lookups([does_not_raise, does_not_raise])


@pytest.mark.parametrize(
    "plurals, services, virtual_disks, interfaces, dns_name, ansible_host_dns_name, primary_ip_interface, racks, expected, not_expected",
    load_relative_test_data("group_extractors"),
)
def test_group_extractors(
    inventory_fixture,
    plurals,
    services,
    virtual_disks,
    interfaces,
    dns_name,
    ansible_host_dns_name,
    primary_ip_interface,
    racks,
    expected,
    not_expected,
):
    inventory_fixture.plurals = plurals
    inventory_fixture.services = services
    inventory_fixture.virtual_disks = virtual_disks
    inventory_fixture.interfaces = interfaces
    inventory_fixture.dns_name = dns_name
    inventory_fixture.ansible_host_dns_name = ansible_host_dns_name
    inventory_fixture.primary_ip_interface = primary_ip_interface
    inventory_fixture.racks = racks
    extractors = inventory_fixture.group_extractors

    for key in expected:
        assert key in extractors

    for key in not_expected:
        assert key not in expected


@pytest.mark.parametrize(
    "api_url, max_uri_length, query_key, query_values, expected",
    load_relative_test_data("get_resource_list_chunked"),
)
def test_get_resource_list_chunked(
    inventory_fixture, api_url, max_uri_length, query_key, query_values, expected
):
    mock_get_resource_list = Mock()
    mock_get_resource_list.return_value = ["resource"]

    inventory_fixture.get_resource_list = mock_get_resource_list
    inventory_fixture.max_uri_length = max_uri_length

    resources = inventory_fixture.get_resource_list_chunked(
        api_url, query_key, query_values
    )

    mock_get_resource_list.assert_has_calls(map(call, expected))
    assert mock_get_resource_list.call_count == len(expected)
    assert resources == mock_get_resource_list.return_value * len(expected)


@patch(
    "ansible_collections.netbox.netbox.plugins.inventory.nb_inventory.DEFAULT_LOCAL_TMP",
    "/fake/path/asdasd3456",
)
@pytest.mark.parametrize("netbox_ver", ["2.0.2", "3.0.0"])
def test_fetch_api_docs(inventory_fixture, netbox_ver):
    mock_fetch_information = Mock()
    mock_fetch_information.side_effect = [
        {"netbox-version": netbox_ver},
        {"info": {"version": "3.0"}},
    ]

    inventory_fixture._fetch_information = mock_fetch_information

    with pytest.raises(KeyError, match="paths"):
        with patch("builtins.open", mock_open()) as filemock:
            with patch(
                "ansible_collections.netbox.netbox.plugins.inventory.nb_inventory.json"
            ) as json_mock:
                json_mock.load.return_value = {"info": {"version": "2.0"}}
                inventory_fixture.fetch_api_docs()

    ref_args_list = [call("/fake/path/netbox_api_dump.json")]
    if netbox_ver == "3.0.0":
        ref_args_list.append(call("/fake/path/netbox_api_dump.json", "w"))

    assert filemock.call_args_list == ref_args_list
    assert str(inventory_fixture.api_version) == netbox_ver[:-2]


def test_new_token(inventory_fixture, templar_fixture):
    mock_get_option = Mock()

    mock_templar_template_token = Mock()
    mock_templar_template_token.return_value = {"type": "foo", "value": "bar"}

    inventory_fixture.templar = templar_fixture
    inventory_fixture.templar.template = mock_templar_template_token

    inventory_fixture.get_option = mock_get_option

    inventory_fixture.headers = {}

    inventory_fixture._set_authorization()

    assert "Authorization" in inventory_fixture.headers
    assert inventory_fixture.headers["Authorization"] == "Foo bar"


@pytest.mark.parametrize(
    "custom_fields, expected", load_relative_test_data("extract_custom_fields")
)
def test_extract_custom_fields(inventory_fixture, custom_fields, expected):
    extracted_custom_fields = inventory_fixture.extract_custom_fields(
        {"custom_fields": custom_fields}
    )

    assert extracted_custom_fields == expected


def test_rename_variables(inventory_fixture):
    inventory_fixture.rename_variables = inventory_fixture.parse_rename_variables(
        (
            {"pattern": r"cluster(.*)", "repl": r"netbox_cluster\1"},
            {"pattern": r"ansible_host", "repl": r"host"},
        )
    )

    inventory_fixture._set_variable("host", "ansible_fqdn", "host.example.org")
    inventory_fixture._set_variable("host", "ansible_host", "host")
    inventory_fixture._set_variable("host", "cluster", "staging")
    inventory_fixture._set_variable("host", "cluster_id", "0xdeadbeef")

    assert inventory_fixture.inventory.variables["host"] == {
        "ansible_fqdn": "host.example.org",
        "host": "host",
        "netbox_cluster": "staging",
        "netbox_cluster_id": "0xdeadbeef",
    }


@pytest.mark.parametrize(
    "host, lookup, expected",
    [
        # Device with primary IP assigned to an interface
        (
            {"primary_ip": {"id": 1}, "is_virtual": False},
            {1: "Management1"},
            "Management1",
        ),
        # Virtual machine with primary IP assigned to an interface
        ({"primary_ip": {"id": 2}, "is_virtual": True}, {2: "eth0"}, "eth0"),
        # No primary IP
        ({"primary_ip": None, "is_virtual": False}, {1: "Management1"}, None),
        # Primary IP not assigned to an interface
        ({"primary_ip": {"id": 3}, "is_virtual": False}, {1: "Management1"}, None),
    ],
)
def test_extract_primary_ip_interface(inventory_fixture, host, lookup, expected):
    inventory_fixture.ip_interface_name_lookup = lookup

    assert inventory_fixture.extract_primary_ip_interface(host) == expected


def test_refresh_primary_ip_addresses(inventory_fixture):
    inventory_fixture.api_endpoint = "https://netbox.example.com"
    inventory_fixture.devices_list = [
        {"id": 10, "primary_ip": {"id": 1}},
        {"id": 11, "primary_ip": None},
        # Two hosts sharing a primary IP must only request it once
        {"id": 12, "primary_ip": {"id": 1}},
        {"id": 13, "primary_ip": {"id": 4}},
    ]
    inventory_fixture.vms_list = [{"id": 20, "primary_ip": {"id": 2}}]
    ipaddresses = [
        {"id": 1, "assigned_object": {"name": "Management1"}},
        {"id": 2, "assigned_object": {"name": "eth0"}},
        # NetBox returns null for an IP address which is not assigned to an interface
        {"id": 4, "assigned_object": None},
    ]
    inventory_fixture.get_resource_list_chunked = Mock(return_value=ipaddresses)

    inventory_fixture.refresh_primary_ip_addresses()

    inventory_fixture.get_resource_list_chunked.assert_called_once_with(
        api_url="https://netbox.example.com/api/ipam/ip-addresses/?limit=0",
        query_key="id",
        query_values=[1, 2, 4],
    )
    assert inventory_fixture.ip_interface_name_lookup == {1: "Management1", 2: "eth0"}


def test_refresh_primary_ip_addresses_no_primary_ips(inventory_fixture):
    inventory_fixture.devices_list = [{"id": 10, "primary_ip": None}]
    inventory_fixture.vms_list = []
    inventory_fixture.get_resource_list_chunked = Mock()

    inventory_fixture.refresh_primary_ip_addresses()

    # No request should be made when there is nothing to look up
    inventory_fixture.get_resource_list_chunked.assert_not_called()
    assert inventory_fixture.ip_interface_name_lookup == {}


def test_refresh_ipaddresses_interface_name_lookup(inventory_fixture):
    inventory_fixture.api_endpoint = "https://netbox.example.com"
    inventory_fixture.fetch_all = True
    ipaddresses = [
        {
            "id": 1,
            "address": "192.0.2.10/24",
            "assigned_object_id": 100,
            "assigned_object_type": "dcim.interface",
            "assigned_object": {"id": 100, "name": "Management1"},
        },
        {
            "id": 2,
            "address": "192.0.2.20/24",
            "assigned_object_id": 200,
            "assigned_object_type": "virtualization.vminterface",
            "assigned_object": {"id": 200, "name": "eth0"},
        },
    ]
    inventory_fixture.get_resource_list = Mock(return_value=ipaddresses)

    inventory_fixture.refresh_ipaddresses()

    assert inventory_fixture.ip_interface_name_lookup == {1: "Management1", 2: "eth0"}
    # The IP address records exposed in the interfaces host var must not gain new keys
    assert inventory_fixture.device_ipaddresses_lookup[1] == {
        "id": 1,
        "address": "192.0.2.10/24",
    }
    assert inventory_fixture.vm_ipaddresses_lookup[2] == {
        "id": 2,
        "address": "192.0.2.20/24",
    }


@pytest.mark.parametrize(
    "interfaces, dns_name, ansible_host_dns_name, primary_ip_interface, expected",
    [
        (False, False, False, False, []),
        (False, False, False, True, ["refresh_primary_ip_addresses"]),
        # The full IP address fetch is reused instead of making a second request
        (True, False, False, True, ["refresh_ipaddresses"]),
        (False, True, False, True, ["refresh_ipaddresses"]),
        (False, False, True, True, ["refresh_ipaddresses"]),
    ],
)
def test_lookup_processes_secondary_ip_addresses(
    inventory_fixture,
    interfaces,
    dns_name,
    ansible_host_dns_name,
    primary_ip_interface,
    expected,
):
    inventory_fixture.interfaces = interfaces
    inventory_fixture.dns_name = dns_name
    inventory_fixture.ansible_host_dns_name = ansible_host_dns_name
    inventory_fixture.primary_ip_interface = primary_ip_interface
    inventory_fixture.prefixes = False

    names = [lookup.__name__ for lookup in inventory_fixture.lookup_processes_secondary]

    assert names == expected
