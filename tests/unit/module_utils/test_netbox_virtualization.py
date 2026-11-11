# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import MagicMock
import pytest

try:
    from ansible_collections.netbox.netbox.plugins.module_utils.netbox_virtualization import (
        NetboxVirtualizationModule,
        NB_VM_INTERFACES,
    )
except ImportError:
    import sys

    # Not installed as a collection
    # Try importing relative to root directory of this ansible_modules project

    sys.path.append("plugins/module_utils")
    from netbox_virtualization import NetboxVirtualizationModule, NB_VM_INTERFACES


def _vm_interface_module(api_version, data):
    """Build a NetboxVirtualizationModule for VM interfaces without connecting to
    NetBox; only the methods that talk to the API are mocked."""
    module = NetboxVirtualizationModule.__new__(NetboxVirtualizationModule)
    module.endpoint = NB_VM_INTERFACES
    module.api_version = api_version
    module.state = "present"
    module.data = data
    module.nb = MagicMock()
    module.module = MagicMock()
    module.module.params = {"query_params": None}
    module._build_query_params = MagicMock(return_value={})
    module._nb_endpoint_get = MagicMock(return_value=None)
    module._set_primary_mac_address = MagicMock()

    def ensure_object_exists(nb_endpoint, endpoint_name, name, data):
        module.nb_object = dict(data, id=5)

    module._ensure_object_exists = MagicMock(side_effect=ensure_object_exists)
    return module


@pytest.mark.parametrize("api_version", ["4.2", "4.5"])
def test_legacy_mac_address_becomes_primary_on_netbox_4_2_plus(api_version):
    """On NetBox v4.2+ the read-only mac_address is not sent and is stored as the VM
    interface's primary MAC instead (#1586)."""
    module = _vm_interface_module(
        api_version,
        {"virtual_machine": 1, "name": "Eth0", "mac_address": "00:00:00:AA:AA:01"},
    )

    module.run()

    sent_data = module._ensure_object_exists.call_args[0][3]
    assert "mac_address" not in sent_data
    module._set_primary_mac_address.assert_called_once_with(
        "interface", "Eth0", "00:00:00:AA:AA:01", "virtualization.vminterface"
    )


def test_explicit_primary_mac_address_wins_over_legacy_mac_address():
    """An explicit primary_mac_address is kept and the legacy mac_address is dropped."""
    module = _vm_interface_module(
        "4.2",
        {
            "virtual_machine": 1,
            "name": "Eth0",
            "mac_address": "00:00:00:AA:AA:01",
            "primary_mac_address": 7,
        },
    )

    module.run()

    sent_data = module._ensure_object_exists.call_args[0][3]
    assert "mac_address" not in sent_data
    assert sent_data["primary_mac_address"] == 7
    module._set_primary_mac_address.assert_not_called()


def test_mac_address_sent_unchanged_before_netbox_4_2():
    """NetBox < 4.2 still accepts mac_address on the VM interface itself."""
    module = _vm_interface_module(
        "4.1",
        {"virtual_machine": 1, "name": "Eth0", "mac_address": "00:00:00:AA:AA:01"},
    )

    module.run()

    sent_data = module._ensure_object_exists.call_args[0][3]
    assert sent_data["mac_address"] == "00:00:00:AA:AA:01"
    module._set_primary_mac_address.assert_not_called()
