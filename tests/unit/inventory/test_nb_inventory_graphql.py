# -*- coding: utf-8 -*-
# Copyright (c) 2026 Mikulas Willaschek
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""Unit tests for nb_inventory_graphql.

All GraphQL responses are mocked (JSON fixtures under fixtures/nb_inventory_graphql/, or inline
dicts for small variations); no real network calls are made. Jinja templates (source.hostname,
compose, keyed_groups) must come from a trusted-as-template source, exactly like
_read_config_data() loads the real YAML inventory config — see load_trusted_config().
"""

import json
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

try:
    from ansible_collections.netbox.netbox.plugins.inventory import (
        nb_inventory_graphql,
    )
    from ansible_collections.netbox.netbox.plugins.inventory.nb_inventory_graphql import (
        InventoryModule,
    )
    from ansible_collections.netbox.netbox.plugins.test.any_attribute_equals import (
        any_attribute_equals,
    )
except ImportError:
    import sys

    # Not installed as a collection - try importing relative to the root directory
    # of this ansible_modules checkout instead (see CONTRIBUTING.md).
    sys.path.append("plugins/inventory")
    sys.path.append("plugins/test")
    import nb_inventory_graphql
    from nb_inventory_graphql import InventoryModule
    from any_attribute_equals import any_attribute_equals

# Register plugins/test/ with the real Jinja test loader so any_attribute_equals is resolvable
# as `is any_attribute_equals(...)` inside Templar-evaluated compose expressions. Required
# unconditionally (not just in the sys.path fallback above): even when the try block above
# succeeds via the ansible_collections namespace, a bare `pytest` run - unlike `ansible-test
# units` - does not itself initialize collection-based Jinja plugin discovery.
from pathlib import Path as _Path

from ansible.plugins.loader import test_loader

test_loader.add_directory(
    str(_Path(__file__).resolve().parents[3] / "plugins" / "test")
)

from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader

FIXTURES = Path(__file__).parent / "fixtures" / "nb_inventory_graphql"
VMS_QUERY_FILE = str(FIXTURES / "queries" / "vms.graphql")
DEVICES_QUERY_FILE = str(FIXTURES / "queries" / "devices.graphql")

DEFAULT_OPTIONS = {
    "plugin": "nb_inventory_graphql",
    "api_endpoint": "http://netbox.example.com",
    "token": None,
    "validate_certs": True,
    "cert": None,
    "key": None,
    "ca_path": None,
    "follow_redirects": "urllib2",
    "timeout": 60,
    "headers": {},
    "ansible_host_dns_name": False,
    "sources": [],
    "compose": {},
    "groups": {},
    "keyed_groups": [],
    "leading_separator": True,
    "use_extra_vars": False,
    "strict": False,
    "cache": False,
}


def load_fixture(name):
    return json.loads((FIXTURES / name).read_text())


def load_trusted_config(tmp_path, loader, yaml_text):
    """Parse YAML the same way _read_config_data() does, so Jinja templates in
    sources[].hostname / compose / keyed_groups pass ansible-core's template trust check.
    """
    config_path = tmp_path / "netbox_graphql.yml"
    config_path.write_text(yaml_text)
    return loader.load_from_file(str(config_path), trusted_as_template=True)


def make_plugin(tmp_path, yaml_text="", **overrides):
    loader = DataLoader()
    config = load_trusted_config(tmp_path, loader, yaml_text) if yaml_text else {}

    plugin = InventoryModule()
    plugin._options = dict(DEFAULT_OPTIONS, **dict(config, **overrides))
    plugin.inventory = InventoryData()
    plugin.display = Mock()
    plugin.graphql_url = "http://netbox.example.com/graphql/"
    plugin.headers = {"Content-Type": "application/json"}
    plugin.loader = loader
    plugin._inventory_dir = str(tmp_path)
    return plugin


class FakeResponse:
    def __init__(self, payload):
        self._body = json.dumps(payload).encode()

    def read(self):
        return self._body


def run_sources(plugin, sources):
    seen_hosts = {}
    for source in sources:
        for element in plugin._fetch_source_elements(source):
            plugin._populate_host_from_element(source, element, seen_hosts)
    return seen_hosts


def source(
    name="vms",
    query_file=VMS_QUERY_FILE,
    list_path="virtual_machine_list",
    hostname="{{ name }}",
):
    return {
        "name": name,
        "query_file": query_file,
        "list_path": list_path,
        "hostname": hostname,
    }


# --- 1. Standard scenario: reproduces the v0.1 acceptance graph via keyed_groups --------------


def test_standard_scenario_matches_acceptance_graph(tmp_path):
    yaml_text = """
sources:
  - name: vms
    query_file: {0}
    list_path: virtual_machine_list
    hostname: "{{{{ name }}}}"
keyed_groups:
  - key: services | map(attribute='name') | list
    prefix: ""
    separator: ""
""".format(
        VMS_QUERY_FILE
    )
    plugin = make_plugin(tmp_path, yaml_text, ansible_host_dns_name=True)
    payload = load_fixture("standard.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        run_sources(plugin, plugin.get_option("sources"))
    plugin.inventory.reconcile_inventory()

    groups = plugin.inventory.get_groups_dict()
    assert groups["web"] == ["app-vm-01"]
    assert groups["api"] == ["app-vm-01"]
    assert sorted(groups["ungrouped"]) == ["dev-vm-01", "prod-vm-01"]

    app_vm_vars = plugin.inventory.get_host("app-vm-01").get_vars()
    assert app_vm_vars["ansible_host"] == "app-vm-01"
    assert app_vm_vars["primary_ip4"] == {
        "address": "192.0.2.73/24",
        "dns_name": "app-vm-01",
    }
    assert [s["name"] for s in app_vm_vars["services"]] == ["web", "api"]

    dev_vm_vars = plugin.inventory.get_host("dev-vm-01").get_vars()
    assert "ansible_host" not in dev_vm_vars


def test_keyed_groups_with_prefix_yields_prefixed_group_names(tmp_path):
    yaml_text = """
sources:
  - name: vms
    query_file: {0}
    list_path: virtual_machine_list
    hostname: "{{{{ name }}}}"
keyed_groups:
  - key: services | map(attribute='name') | list
    prefix: service
""".format(
        VMS_QUERY_FILE
    )
    plugin = make_plugin(tmp_path, yaml_text)
    payload = load_fixture("standard.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        run_sources(plugin, plugin.get_option("sources"))

    groups = plugin.inventory.get_groups_dict()
    assert groups["service_web"] == ["app-vm-01"]
    assert groups["service_api"] == ["app-vm-01"]


# --- 2. ansible_host derivation — direct unit test, no templating involved --------------------


def vm(name, primary_ip4=None, primary_ip6=None):
    return {
        "id": "1",
        "name": name,
        "primary_ip4": primary_ip4,
        "primary_ip6": primary_ip6,
    }


@pytest.mark.parametrize(
    "description, element, dns_name_option, expected_ansible_host",
    [
        (
            "dns_name present + option on -> dns_name wins",
            vm(
                "a", primary_ip4={"address": "10.0.0.1/24", "dns_name": "a.example.com"}
            ),
            True,
            "a.example.com",
        ),
        (
            "empty dns_name + option on -> falls back to IP",
            vm("b", primary_ip4={"address": "10.0.0.2/24", "dns_name": ""}),
            True,
            "10.0.0.2",
        ),
        (
            "dns_name present but option off -> IP is used",
            vm(
                "c", primary_ip4={"address": "10.0.0.3/24", "dns_name": "c.example.com"}
            ),
            False,
            "10.0.0.3",
        ),
        (
            "no primary IP at all -> ansible_host not set",
            vm("d"),
            False,
            None,
        ),
        (
            "only primary_ip6 -> IPv6 address is used",
            vm("e", primary_ip6={"address": "2001:db8::1/64", "dns_name": ""}),
            False,
            "2001:db8::1",
        ),
    ],
)
def test_ansible_host_matrix(
    tmp_path, description, element, dns_name_option, expected_ansible_host
):
    plugin = make_plugin(tmp_path, ansible_host_dns_name=dns_name_option)
    hostname = element["name"]
    plugin.inventory.add_host(host=hostname)

    plugin._derive_ansible_host(element, hostname)

    host_vars = plugin.inventory.get_host(hostname).get_vars()
    if expected_ansible_host is None:
        assert "ansible_host" not in host_vars, description
    else:
        assert host_vars["ansible_host"] == expected_ansible_host, description


# --- 3. Sources engine --------------------------------------------------------------------------


def test_multiple_sources_produce_both_host_types(tmp_path):
    yaml_text = """
sources:
  - name: vms
    query_file: {0}
    list_path: virtual_machine_list
    hostname: "{{{{ name }}}}"
  - name: devices
    query_file: {1}
    list_path: device_list
    hostname: "{{{{ name }}}}"
""".format(
        VMS_QUERY_FILE, DEVICES_QUERY_FILE
    )
    plugin = make_plugin(tmp_path, yaml_text)
    vm_payload = load_fixture("standard.json")
    device_payload = load_fixture("devices.json")

    with patch.object(
        nb_inventory_graphql,
        "open_url",
        side_effect=[FakeResponse(vm_payload), FakeResponse(device_payload)],
    ):
        run_sources(plugin, plugin.get_option("sources"))

    assert set(plugin.inventory.hosts) == {"app-vm-01", "dev-vm-01", "host-01", "prod-vm-01"}
    host_vars = plugin.inventory.get_host("host-01").get_vars()
    assert host_vars["device_type"]["model"] == "Server Model 1"
    assert (
        "services" not in host_vars
    )  # VM-only field, never touched by the devices source


def test_list_path_missing_raises_ansible_error(tmp_path):
    plugin = make_plugin(tmp_path)
    payload = {"data": {"virtual_machine_list": []}}

    with pytest.raises(AnsibleError, match="list_path 'device_list' not found"):
        plugin._resolve_list_path(payload["data"], "device_list", "vms")


def test_list_path_wrong_type_raises_ansible_error(tmp_path):
    plugin = make_plugin(tmp_path)
    data = {"virtual_machine_list": {"not": "a list"}}

    with pytest.raises(AnsibleError, match="does not resolve to a list"):
        plugin._resolve_list_path(data, "virtual_machine_list", "vms")


def test_list_path_supports_dotted_nesting(tmp_path):
    plugin = make_plugin(tmp_path)
    data = {"wrapper": {"nested_list": [{"id": "1"}]}}

    result = plugin._resolve_list_path(data, "wrapper.nested_list", "vms")

    assert result == [{"id": "1"}]


def test_name_collision_between_sources_warns_and_last_writer_wins(tmp_path):
    yaml_text = """
sources:
  - name: vms
    query_file: {0}
    list_path: virtual_machine_list
    hostname: "{{{{ name }}}}"
  - name: devices
    query_file: {1}
    list_path: device_list
    hostname: "{{{{ name }}}}"
""".format(
        VMS_QUERY_FILE, DEVICES_QUERY_FILE
    )
    plugin = make_plugin(tmp_path, yaml_text)
    vm_payload = {"data": {"virtual_machine_list": [{"id": "1", "name": "shared"}]}}
    device_payload = {
        "data": {
            "device_list": [{"id": "2", "name": "shared", "role": {"name": "core"}}]
        }
    }

    with patch.object(
        nb_inventory_graphql,
        "open_url",
        side_effect=[FakeResponse(vm_payload), FakeResponse(device_payload)],
    ):
        run_sources(plugin, plugin.get_option("sources"))

    host_vars = plugin.inventory.get_host("shared").get_vars()
    assert host_vars["role"]["name"] == "core"  # the later source (devices) won
    plugin.display.warning.assert_called()


def test_query_file_not_found_raises_clear_error(tmp_path):
    plugin = make_plugin(tmp_path)
    missing = source(query_file=str(tmp_path / "does_not_exist.graphql"))

    with pytest.raises(AnsibleError, match="could not read query_file"):
        plugin._fetch_source_elements(missing)


def test_query_file_relative_path_resolves_against_inventory_dir(tmp_path):
    (tmp_path / "queries").mkdir()
    (tmp_path / "queries" / "vms.graphql").write_text(
        "query { virtual_machine_list { id name } }"
    )
    plugin = make_plugin(tmp_path)
    rel_source = source(query_file="queries/vms.graphql")
    payload = {"data": {"virtual_machine_list": []}}

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        elements = plugin._fetch_source_elements(rel_source)

    assert elements == []


# --- 4. compose reference cases -----------------------------------------------------------------


def test_compose_use_case_1_selectattr_first(tmp_path):
    yaml_text = """
sources:
  - name: vms
    query_file: {0}
    list_path: virtual_machine_list
    hostname: "{{{{ name }}}}"
compose:
  web_service: >-
    services | selectattr('name', 'equalto', 'web') | list | first | default(omit)
""".format(
        VMS_QUERY_FILE
    )
    plugin = make_plugin(tmp_path, yaml_text)
    payload = load_fixture("standard.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        run_sources(plugin, plugin.get_option("sources"))

    assert (
        plugin.inventory.get_host("app-vm-01").get_vars()["web_service"]["name"]
        == "web"
    )
    assert "web_service" not in plugin.inventory.get_host("prod-vm-01").get_vars()


def test_compose_use_case_2_cross_reference_test(tmp_path):
    yaml_text = """
sources:
  - name: vms
    query_file: {0}
    list_path: virtual_machine_list
    hostname: "{{{{ name }}}}"
compose:
  primary_interface: >-
    interfaces
    | selectattr('ip_addresses', 'any_attribute_equals', 'address', primary_ip4.address)
    | first | default(omit)
""".format(
        VMS_QUERY_FILE
    )
    plugin = make_plugin(tmp_path, yaml_text)
    payload = load_fixture("standard.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        run_sources(plugin, plugin.get_option("sources"))

    assert (
        plugin.inventory.get_host("app-vm-01").get_vars()["primary_interface"]["name"]
        == "ens18"
    )
    # dev-vm-01 has no primary_ip4 -> "primary_ip4.address" fails to resolve, no traceback, key just absent
    assert "primary_interface" not in plugin.inventory.get_host("dev-vm-01").get_vars()


# --- 5. any_attribute_equals: full coverage -----------------------------------------------------


class TestAnyAttributeEquals:
    def setup_method(self):
        self.test = any_attribute_equals

    def test_match_found(self):
        items = [{"address": "10.0.0.1"}, {"address": "10.0.0.2"}]
        assert self.test(items, "address", "10.0.0.2") is True

    def test_no_match(self):
        items = [{"address": "10.0.0.1"}]
        assert self.test(items, "address", "10.0.0.99") is False

    def test_multiple_matches_still_true(self):
        items = [{"address": "10.0.0.1"}, {"address": "10.0.0.1"}]
        assert self.test(items, "address", "10.0.0.1") is True

    def test_empty_list(self):
        assert self.test([], "address", "10.0.0.1") is False

    def test_none_list(self):
        assert self.test(None, "address", "10.0.0.1") is False

    def test_missing_attribute_no_traceback(self):
        items = [{"other": "field"}]
        assert self.test(items, "address", "10.0.0.1") is False

    def test_dotted_attribute_path(self):
        items = [{"nested": {"address": "10.0.0.1"}}]
        assert self.test(items, "nested.address", "10.0.0.1") is True

    def test_dotted_path_partially_missing_no_traceback(self):
        items = [{"nested": {}}]
        assert self.test(items, "nested.address", "10.0.0.1") is False


# --- 6. GraphQL errors ----------------------------------------------------------------------------


def test_graphql_errors_without_data_raise_ansible_error(tmp_path):
    plugin = make_plugin(tmp_path)
    payload = load_fixture("errors_fatal.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        with pytest.raises(AnsibleError, match="Cannot query field 'bogus_field'"):
            plugin._fetch_source_elements(source())


def test_graphql_errors_with_partial_data_warns_and_builds_inventory(tmp_path):
    plugin = make_plugin(tmp_path)
    payload = load_fixture("errors_partial.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        elements = plugin._fetch_source_elements(source())

    assert [e["name"] for e in elements] == ["prod-vm-01"]
    plugin.display.warning.assert_called()


# --- 7. Empty list -> empty inventory -------------------------------------------------------------


def test_empty_list_yields_empty_inventory(tmp_path):
    plugin = make_plugin(tmp_path)
    payload = load_fixture("empty.json")

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ):
        elements = plugin._fetch_source_elements(source())

    assert elements == []
    run_sources(plugin, [])
    assert plugin.inventory.hosts == {}


# --- 8. Pagination: two pages -> all elements fetched ----------------------------------------------


def test_pagination_fetches_all_pages(tmp_path, monkeypatch):
    monkeypatch.setattr(nb_inventory_graphql, "PAGE_SIZE", 2)
    plugin = make_plugin(tmp_path)

    page1 = {
        "data": {
            "virtual_machine_list": [{"id": "1", "name": "a"}, {"id": "2", "name": "b"}]
        }
    }
    page2 = {"data": {"virtual_machine_list": [{"id": "3", "name": "c"}]}}
    responses = [FakeResponse(page1), FakeResponse(page2)]

    with patch.object(
        nb_inventory_graphql, "open_url", side_effect=responses
    ) as mocked:
        elements = plugin._fetch_source_elements(source())

    assert [e["name"] for e in elements] == ["a", "b", "c"]
    assert mocked.call_count == 2

    first_body = json.loads(mocked.call_args_list[0].kwargs["data"])
    second_body = json.loads(mocked.call_args_list[1].kwargs["data"])
    assert first_body["variables"]["pagination"] == {"offset": 0, "limit": 2}
    assert second_body["variables"]["pagination"] == {"offset": 2, "limit": 2}


def test_source_variables_are_merged_with_pagination(tmp_path):
    plugin = make_plugin(tmp_path)
    payload = {"data": {"virtual_machine_list": []}}
    src = source()
    src["variables"] = {"status": "active"}

    with patch.object(
        nb_inventory_graphql, "open_url", return_value=FakeResponse(payload)
    ) as mocked:
        plugin._fetch_source_elements(src)

    body = json.loads(mocked.call_args.kwargs["data"])
    assert body["variables"]["status"] == "active"
    assert body["variables"]["pagination"] == {
        "offset": 0,
        "limit": nb_inventory_graphql.PAGE_SIZE,
    }
