# -*- coding: utf-8 -*-
# Copyright (c) 2026 Mikulas Willaschek
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
from io import BytesIO
from unittest.mock import patch
from urllib.error import HTTPError

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader

try:
    from ansible_collections.netbox.netbox.plugins.inventory import (
        nb_inventory_graphql,
    )
except ImportError:
    import sys

    # Not installed as a collection
    # Try importing relative to root directory of this ansible_modules project
    sys.path.append("plugins/inventory")
    import nb_inventory_graphql

try:
    from ansible.template import trust_as_template
except ImportError:
    # ansible-core < 2.19 has no template trust
    def trust_as_template(value):
        return value


PAGINATED_QUERY = """
query ($pagination: OffsetPaginationInput) {
  device_list(pagination: $pagination) { name }
}
"""

DEVICES = [
    {
        "name": "sw1",
        "status": "ACTIVE",
        "role": {"slug": "switch"},
        "primary_ip4": {"address": "192.0.2.1/24", "dns_name": "sw1.example.com"},
        "primary_ip6": None,
    },
    {
        "name": "sw2",
        "status": "OFFLINE",
        "role": {"slug": "switch"},
        "primary_ip4": None,
        "primary_ip6": {"address": "2001:db8::2/64", "dns_name": ""},
    },
    {
        "name": "pdu1",
        "status": "ACTIVE",
        "role": {"slug": "pdu"},
        "primary_ip4": None,
        "primary_ip6": None,
    },
]


def response(data=None, errors=None):
    return BytesIO(json.dumps({"data": data, "errors": errors}).encode())


def device_pages(*pages):
    return [response({"device_list": page}) for page in pages]


def request_variables(mock_open_url):
    return [
        json.loads(call.kwargs["data"])["variables"]
        for call in mock_open_url.call_args_list
    ]


@pytest.fixture
def mock_open_url():
    with patch.object(nb_inventory_graphql, "open_url") as mock:
        yield mock


@pytest.fixture
def run(tmp_path):
    """Parse an inventory source without going through the plugin loader."""
    (tmp_path / "devices.graphql").write_text(PAGINATED_QUERY)
    path = str(tmp_path / "netbox.yml")
    cache_store = {}

    def _run(use_cache=True, **options):
        plugin = nb_inventory_graphql.InventoryModule()
        plugin._options = {
            "api_endpoint": "https://netbox.example.com/",
            "token": "0123456789",
            "validate_certs": True,
            "cert": None,
            "key": None,
            "ca_path": None,
            "follow_redirects": "urllib2",
            "timeout": 60,
            "headers": {},
            "ansible_host_dns_name": False,
            "sources": [{"query_file": "devices.graphql", "list_path": "device_list"}],
            "strict": False,
            "compose": {},
            "groups": {},
            "keyed_groups": [],
            "use_extra_vars": False,
            "leading_separator": True,
            "cache": False,
        }
        plugin._options.update(options)
        plugin._cache = cache_store
        with patch.object(plugin, "_read_config_data"):
            plugin.parse(InventoryData(), DataLoader(), path, cache=use_cache)
        return plugin

    return _run


def test_hosts_and_variables(run, mock_open_url):
    mock_open_url.side_effect = device_pages(DEVICES, [])
    inventory = run().inventory

    assert sorted(inventory.hosts) == ["pdu1", "sw1", "sw2"]
    host_vars = inventory.get_host("sw1").get_vars()
    assert host_vars["role"] == {"slug": "switch"}
    assert host_vars["status"] == "ACTIVE"
    assert "name" not in host_vars

    request = mock_open_url.call_args.kwargs
    assert mock_open_url.call_args.args == ("https://netbox.example.com/graphql/",)
    assert request["method"] == "POST"
    assert request["headers"]["Authorization"] == "Token 0123456789"


def test_token_type_and_headers(run, mock_open_url):
    mock_open_url.side_effect = device_pages([])
    run(
        token={"type": "bearer", "value": "nbt_abc"},
        headers='{"X-NetBox-Branch": "abc"}',
    )

    headers = mock_open_url.call_args.kwargs["headers"]
    assert headers["Authorization"] == "Bearer nbt_abc"
    assert headers["X-NetBox-Branch"] == "abc"


@pytest.mark.parametrize(
    "dns_name_option, expected",
    [
        (False, {"sw1": "192.0.2.1", "sw2": "2001:db8::2", "pdu1": None}),
        (True, {"sw1": "sw1.example.com", "sw2": "2001:db8::2", "pdu1": None}),
    ],
)
def test_ansible_host(run, mock_open_url, dns_name_option, expected):
    mock_open_url.side_effect = device_pages(DEVICES, [])
    inventory = run(ansible_host_dns_name=dns_name_option).inventory

    for hostname, ansible_host in expected.items():
        assert inventory.get_host(hostname).get_vars().get("ansible_host") == (
            ansible_host
        )


def test_constructed_options(run, mock_open_url):
    mock_open_url.side_effect = device_pages(DEVICES, [])
    inventory = run(
        compose={"device_name": trust_as_template("name | upper")},
        groups={"offline": trust_as_template("status == 'OFFLINE'")},
        keyed_groups=[{"prefix": "role", "key": trust_as_template("role.slug")}],
    ).inventory

    groups = inventory.get_groups_dict()
    assert groups["offline"] == ["sw2"]
    assert sorted(groups["role_switch"]) == ["sw1", "sw2"]
    assert groups["role_pdu"] == ["pdu1"]
    assert inventory.get_host("pdu1").get_vars()["device_name"] == "PDU1"


def test_hostname_expression(run, mock_open_url):
    mock_open_url.side_effect = device_pages(DEVICES, [])
    source = {
        "query_file": "devices.graphql",
        "list_path": "device_list",
        "hostname": trust_as_template("name ~ '.' ~ role.slug"),
    }
    inventory = run(sources=[source]).inventory

    assert sorted(inventory.hosts) == ["pdu1.pdu", "sw1.switch", "sw2.switch"]


def test_hostname_expression_error(run, mock_open_url):
    mock_open_url.side_effect = device_pages(DEVICES, [])
    source = {
        "query_file": "devices.graphql",
        "list_path": "device_list",
        "hostname": trust_as_template("missing.field"),
    }

    with pytest.raises(AnsibleError, match="Could not evaluate hostname"):
        run(sources=[source])


def test_hostname_falls_back_to_uuid(run, mock_open_url):
    mock_open_url.side_effect = device_pages([{"name": None}, {"id": "7"}], [])
    inventory = run().inventory

    assert len(inventory.hosts) == 2
    assert all(len(hostname) == 36 for hostname in inventory.hosts)


def test_later_source_wins(run, tmp_path, mock_open_url):
    (tmp_path / "vms.graphql").write_text("{ virtual_machine_list { name } }")
    mock_open_url.side_effect = [
        response({"device_list": [{"name": "host1", "status": "ACTIVE", "vcpus": 1}]}),
        response({"device_list": []}),
        response({"virtual_machine_list": [{"name": "host1", "status": "OFFLINE"}]}),
    ]
    sources = [
        {"query_file": "devices.graphql", "list_path": "device_list"},
        {"query_file": "vms.graphql", "list_path": "virtual_machine_list"},
    ]
    host_vars = run(sources=sources).inventory.get_host("host1").get_vars()

    assert host_vars["status"] == "OFFLINE"
    assert host_vars["vcpus"] == 1


def test_pagination_stops_at_empty_page(run, mock_open_url):
    # The first page is shorter than the requested limit, as it is when
    # MAX_PAGE_SIZE of NetBox is lower than the page size of the plugin.
    mock_open_url.side_effect = device_pages(DEVICES[:2], DEVICES[2:], [])
    inventory = run(
        sources=[
            {
                "query_file": "devices.graphql",
                "list_path": "device_list",
                "variables": {"status": "ACTIVE"},
            }
        ]
    ).inventory

    assert len(inventory.hosts) == 3
    limit = nb_inventory_graphql.PAGE_SIZE
    assert request_variables(mock_open_url) == [
        {"status": "ACTIVE", "pagination": {"offset": 0, "limit": limit}},
        {"status": "ACTIVE", "pagination": {"offset": 2, "limit": limit}},
        {"status": "ACTIVE", "pagination": {"offset": 3, "limit": limit}},
    ]


def test_query_without_pagination_is_sent_once(run, tmp_path, mock_open_url):
    (tmp_path / "devices.graphql").write_text("{ device_list { name } }")
    mock_open_url.side_effect = device_pages(DEVICES)
    inventory = run().inventory

    assert len(inventory.hosts) == 3
    assert request_variables(mock_open_url) == [{}]


def test_query_file_absolute_path(run, tmp_path_factory, mock_open_url):
    query_file = tmp_path_factory.mktemp("queries") / "devices.graphql"
    query_file.write_text("{ device_list { name } }")
    mock_open_url.side_effect = device_pages(DEVICES)
    inventory = run(
        sources=[{"query_file": str(query_file), "list_path": "device_list"}]
    ).inventory

    assert len(inventory.hosts) == 3


def test_cache(run, mock_open_url):
    mock_open_url.side_effect = device_pages(DEVICES, [])
    run(cache=True)
    assert mock_open_url.call_count == 2

    # Served from the cache
    inventory = run(cache=True).inventory
    assert mock_open_url.call_count == 2
    assert len(inventory.hosts) == 3

    # --flush-cache fetches again and updates the cache
    mock_open_url.side_effect = device_pages(DEVICES[:1], [])
    inventory = run(use_cache=False, cache=True).inventory
    assert mock_open_url.call_count == 4
    assert len(inventory.hosts) == 1


def test_cache_disabled(run, mock_open_url):
    mock_open_url.side_effect = device_pages(DEVICES, [], DEVICES, [])
    run()
    run()

    assert mock_open_url.call_count == 4


def test_graphql_errors(run, mock_open_url):
    mock_open_url.side_effect = [
        response(errors=[{"message": "Cannot query field 'foo' on type 'DeviceType'."}])
    ]

    with pytest.raises(AnsibleError, match="Cannot query field 'foo'"):
        run()


def test_http_error(run, mock_open_url):
    mock_open_url.side_effect = HTTPError(
        "https://netbox.example.com/graphql/",
        403,
        "Forbidden",
        {},
        BytesIO(b'{"detail": "Invalid token"}'),
    )

    with pytest.raises(AnsibleError, match="HTTP 403.*Invalid token"):
        run()


def test_response_is_not_json(run, mock_open_url):
    mock_open_url.side_effect = [BytesIO(b"<html>Login</html>")]

    with pytest.raises(AnsibleError, match="did not return JSON"):
        run()


def test_list_path_not_in_response(run, mock_open_url):
    mock_open_url.side_effect = [response({"devices": []})]

    with pytest.raises(AnsibleError, match="list_path 'device_list' is not a list"):
        run()


def test_query_file_missing(run, mock_open_url):
    source = {"query_file": "missing.graphql", "list_path": "device_list"}

    with pytest.raises(AnsibleError, match="Could not read query_file"):
        run(sources=[source])
    mock_open_url.assert_not_called()
