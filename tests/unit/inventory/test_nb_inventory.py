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
    inventory.timeout = 60

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


@pytest.mark.parametrize(
    "description,options,expected", load_relative_test_data("get_filters")
)
def test_get_filters(inventory_fixture, description, options, expected):
    inventory_fixture.query_filters = options["query_filters"]
    inventory_fixture.device_query_filters = options["device_query_filters"]
    inventory_fixture.vm_query_filters = options["vm_query_filters"]
    inventory_fixture.config_context = options["config_context"]

    result = inventory_fixture.get_filters()

    assert isinstance(result, tuple), "get_filters() should return a tuple"
    assert (
        len(result) == 2
    ), "get_filters() should return a 2-tuple (device_filters, vm_filters)"

    device_filters, vm_filters = result
    expected_device_filters, expected_vm_filters = expected

    assert isinstance(device_filters, list), "Device filters should be a list"
    assert isinstance(vm_filters, list), "VM filters should be a list"

    assert len(device_filters) == len(
        expected_device_filters
    ), f"Device filters count mismatch: expected {len(expected_device_filters)}, got {len(device_filters)}"
    assert len(vm_filters) == len(
        expected_vm_filters
    ), f"VM filters count mismatch: expected {len(expected_vm_filters)}, got {len(vm_filters)}"

    for i, filter_tuple in enumerate(device_filters):
        assert (
            list(filter_tuple) in expected_device_filters
        ), f"Device filter {filter_tuple} not in expected filters: {expected_device_filters}"

    for i, filter_tuple in enumerate(vm_filters):
        assert (
            list(filter_tuple) in expected_vm_filters
        ), f"VM filter {filter_tuple} not in expected filters: {expected_vm_filters}"


def test_fetch_hosts_without_filters(inventory_fixture):
    inventory_fixture.query_filters = []
    inventory_fixture.device_query_filters = []
    inventory_fixture.vm_query_filters = []
    inventory_fixture.nb = Mock()
    inventory_fixture.nb.dcim.devices.filter.return_value = [{"id": 1}]
    inventory_fixture.nb.virtualization.virtual_machines.filter.return_value = [
        {"id": 2}
    ]

    def fetch(key, pynetbox_fn, filters=None):
        return list(pynetbox_fn())

    inventory_fixture._fetch_information_pynetbox = fetch

    inventory_fixture.fetch_hosts()

    inventory_fixture.nb.dcim.devices.filter.assert_called_once_with()
    inventory_fixture.nb.virtualization.virtual_machines.filter.assert_called_once_with()
    assert inventory_fixture.devices_lookup == {1: {"id": 1, "is_virtual": False}}
    assert inventory_fixture.vms_lookup == {2: {"id": 2, "is_virtual": True}}


def test_fetch_hosts_with_invalid_query_filters(inventory_fixture):
    inventory_fixture.query_filters = [{"invalid_param": "value"}]
    inventory_fixture.device_query_filters = []
    inventory_fixture.vm_query_filters = []
    inventory_fixture.nb = Mock()
    inventory_fixture._fetch_information_pynetbox = Mock()

    inventory_fixture.fetch_hosts()

    inventory_fixture._fetch_information_pynetbox.assert_not_called()
    inventory_fixture.nb.dcim.devices.filter.assert_not_called()
    inventory_fixture.nb.virtualization.virtual_machines.filter.assert_not_called()


def test_fetch_information_pynetbox_cache_key_includes_filters(inventory_fixture):
    inventory_fixture.use_cache = True
    inventory_fixture._cache = {}
    inventory_fixture.get_option = Mock(return_value=True)

    first_fetch = Mock(return_value=[{"id": 1}])
    second_fetch = Mock(return_value=[{"id": 2}])

    inventory_fixture._fetch_information_pynetbox(
        "devices", first_fetch, filters=[("name", "router1")]
    )
    inventory_fixture._fetch_information_pynetbox(
        "devices", second_fetch, filters=[("name", "router2")]
    )
    inventory_fixture._fetch_information_pynetbox(
        "devices", second_fetch, filters=[("name", "router1")]
    )

    first_fetch.assert_called_once()
    second_fetch.assert_called_once()
    assert len(inventory_fixture._cache) == 2


def test_refresh_services_without_hosts(inventory_fixture):
    inventory_fixture.fetch_all = False
    inventory_fixture.devices_lookup = {}
    inventory_fixture.vms_lookup = {}
    inventory_fixture.nb = Mock()
    inventory_fixture._fetch_information_pynetbox = Mock()

    inventory_fixture.refresh_services()

    inventory_fixture._fetch_information_pynetbox.assert_not_called()
    assert inventory_fixture.device_services_lookup == {}
    assert inventory_fixture.vm_services_lookup == {}


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
    "plurals, services, virtual_disks, interfaces, dns_name, ansible_host_dns_name, racks, expected, not_expected",
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
    inventory_fixture.racks = racks
    extractors = inventory_fixture.group_extractors

    for key in expected:
        assert key in extractors

    for key in not_expected:
        assert key not in expected


@patch(
    "ansible_collections.netbox.netbox.plugins.inventory.nb_inventory.DEFAULT_LOCAL_TMP",
    "/fake/path/asdasd3456",
)
@pytest.mark.parametrize("netbox_ver", ["2.0.2", "3.0.0"])
def test_fetch_api_docs(inventory_fixture, netbox_ver):
    inventory_fixture.nb = Mock()
    inventory_fixture.nb.status.return_value = {"netbox-version": netbox_ver}
    get_mock = inventory_fixture.nb.http_session.get
    get_mock.return_value.content = b"{}"

    with pytest.raises(KeyError, match="paths"):
        with patch("builtins.open", mock_open()) as filemock:
            with patch(
                "ansible_collections.netbox.netbox.plugins.inventory.nb_inventory.json"
            ) as json_mock:
                json_mock.load.return_value = {"info": {"version": "2.0"}}
                json_mock.loads.return_value = {"info": {"version": "3.0"}}
                inventory_fixture.fetch_api_docs()

    if netbox_ver == "3.0.0":
        get_mock.assert_called_once()
    else:
        get_mock.assert_not_called()

    ref_args_list = [call("/fake/path/netbox_api_dump.json")]
    if netbox_ver == "3.0.0":
        ref_args_list.append(call("/fake/path/netbox_api_dump.json", "w"))

    assert filemock.call_args_list == ref_args_list
    assert str(inventory_fixture.api_version) == netbox_ver[:-2]


@pytest.mark.parametrize(
    "ca_path, validate_certs, expected_verify",
    [(False, True, True), (False, False, False), ("/tmp/ca.pem", True, "/tmp/ca.pem")],
)
def test_build_session(inventory_fixture, ca_path, validate_certs, expected_verify):
    inventory_fixture.ca_path = ca_path
    inventory_fixture.validate_certs = validate_certs
    inventory_fixture.cert = "/tmp/client.pem"
    inventory_fixture.key = "/tmp/client.key"
    inventory_fixture.get_option = Mock(return_value={"X-Test-Header": "present"})

    session = inventory_fixture._build_session()

    assert session.timeout == inventory_fixture.timeout
    assert session.verify == expected_verify
    assert session.cert == ("/tmp/client.pem", "/tmp/client.key")
    assert session.headers["X-Test-Header"] == "present"


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
