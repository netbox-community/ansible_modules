# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Bruno Inec (@sweenu) <bruno@inec.fr>
# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
import os
from functools import partial
from unittest.mock import patch, MagicMock, Mock
from ansible.module_utils.basic import AnsibleModule

try:
    from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
        NetboxModule,
    )
    from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
        NB_DEVICES,
    )
    from ansible_collections.netbox.netbox.tests.test_data import load_test_data

    MOCKER_PATCH_PATH = "ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils.NetboxModule"
except ImportError:
    import sys

    # Not installed as a collection
    # Try importing relative to root directory of this ansible_modules project

    sys.path.append("plugins/module_utils")
    sys.path.append("tests")
    from netbox_utils import NetboxModule
    from netbox_dcim import NB_DEVICES
    from test_data import load_test_data

    MOCKER_PATCH_PATH = "netbox_utils.NetboxModule"

load_relative_test_data = partial(
    load_test_data, os.path.dirname(os.path.abspath(__file__))
)


@pytest.fixture
def fixture_arg_spec():
    return {
        "netbox_url": "http://netbox.local/",
        "netbox_token": "0123456789",
        "data": {
            "name": "Test Device1",
            "device_role": "Core Switch",
            "device_type": "Cisco Switch",
            "manufacturer": "Cisco",
            "site": "Test Site",
            "asset_tag": "1001",
        },
        "state": "present",
        "validate_certs": False,
        "cert": None,
    }


@pytest.fixture
def normalized_data():
    return {
        "name": "Test Device1",
        "device_role": "core-switch",
        "device_type": "cisco-switch",
        "manufacturer": "cisco",
        "site": "test-site",
        "asset_tag": "1001",
    }


@pytest.fixture
def mock_ansible_module(fixture_arg_spec):
    module = MagicMock(name="AnsibleModule")
    module.check_mode = False
    module.params = fixture_arg_spec

    return module


@pytest.fixture
def find_ids_return():
    return {
        "name": "Test Device1",
        "device_role": 1,
        "device_type": 1,
        "manufacturer": 1,
        "site": 1,
        "asset_tag": "1001",
    }


@pytest.fixture
def nb_obj_mock(mocker, normalized_data):
    nb_obj = mocker.Mock(name="nb_obj_mock")
    nb_obj.delete.return_value = True
    nb_obj.update.return_value = True
    nb_obj.update.side_effect = normalized_data.update
    nb_obj.serialize.return_value = normalized_data

    return nb_obj


@pytest.fixture
def endpoint_mock(mocker, nb_obj_mock):
    endpoint = mocker.Mock(name="endpoint_mock")
    endpoint.create.return_value = nb_obj_mock

    return endpoint


@pytest.fixture
def on_creation_diff(mock_netbox_module):
    return mock_netbox_module._build_diff(
        before={"state": "absent"}, after={"state": "present"}
    )


@pytest.fixture
def on_deletion_diff(mock_netbox_module):
    return mock_netbox_module._build_diff(
        before={"state": "present"}, after={"state": "absent"}
    )


@pytest.fixture
def mock_netbox_module(mocker, mock_ansible_module, find_ids_return):
    find_ids = mocker.patch("%s%s" % (MOCKER_PATCH_PATH, "._find_ids"))
    find_ids.return_value = find_ids_return
    nb_client = mocker.Mock(name="pynetbox.api")
    nb_client.version = "2.10"
    netbox = NetboxModule(mock_ansible_module, NB_DEVICES, nb_client=nb_client)

    return netbox


@pytest.fixture
def changed_serialized_obj(nb_obj_mock):
    changed_serialized_obj = nb_obj_mock.serialize().copy()
    changed_serialized_obj["name"] += " (modified)"

    return changed_serialized_obj


@pytest.fixture
def on_update_diff(mock_netbox_module, nb_obj_mock, changed_serialized_obj):
    return mock_netbox_module._build_diff(
        before={"name": "Test Device1"}, after={"name": "Test Device1 (modified)"}
    )


def test_init(mock_netbox_module, find_ids_return):
    """Test that we can get a real mock NetboxModule."""
    assert mock_netbox_module.data == find_ids_return


@pytest.mark.parametrize("before, after", load_relative_test_data("normalize_data"))
def test_normalize_data_returns_correct_data(mock_netbox_module, before, after):
    norm_data = mock_netbox_module._normalize_data(before)

    assert norm_data == after


@pytest.mark.parametrize("data, expected", load_relative_test_data("arg_spec_default"))
def test_remove_arg_spec_defaults(mock_netbox_module, data, expected):
    new_data = mock_netbox_module._remove_arg_spec_default(data)

    assert new_data == expected


@pytest.mark.parametrize("non_slug, expected", load_relative_test_data("slug"))
def test_to_slug_returns_valid_slug(mock_netbox_module, non_slug, expected):
    got_slug = mock_netbox_module._to_slug(non_slug)

    assert got_slug == expected


@pytest.mark.parametrize("endpoint, app", load_relative_test_data("find_app"))
def test_find_app_returns_valid_app(mock_netbox_module, endpoint, app):
    assert app == mock_netbox_module._find_app(endpoint), "app: %s, endpoint: %s" % (
        app,
        endpoint,
    )


@pytest.mark.parametrize(
    "endpoint, data, expected", load_relative_test_data("choices_id")
)
def test_change_choices_id(mocker, mock_netbox_module, endpoint, data, expected):
    fetch_choice_value = mocker.patch(
        "%s%s" % (MOCKER_PATCH_PATH, "._fetch_choice_value")
    )
    fetch_choice_value.return_value = "temp"
    new_data = mock_netbox_module._change_choices_id(endpoint, data)
    assert new_data == expected


@pytest.mark.parametrize(
    "parent, module_data, expected",
    load_relative_test_data("build_query_params_no_child"),
)
def test_build_query_params_no_child(
    mock_netbox_module, mocker, parent, module_data, expected
):
    get_query_param_id = mocker.patch(
        "%s%s" % (MOCKER_PATCH_PATH, "._get_query_param_id")
    )
    get_query_param_id.return_value = 1
    query_params = mock_netbox_module._build_query_params(parent, module_data)
    assert query_params == expected


@pytest.mark.parametrize(
    "parent, module_data, child, expected",
    load_relative_test_data("build_query_params_child"),
)
def test_build_query_params_child(
    mock_netbox_module, mocker, parent, module_data, child, expected
):
    get_query_param_id = mocker.patch(
        "%s%s" % (MOCKER_PATCH_PATH, "._get_query_param_id")
    )
    get_query_param_id.return_value = 1
    # This will need to be updated, but attempting to fix issue quickly
    fetch_choice_value = mocker.patch(
        "%s%s" % (MOCKER_PATCH_PATH, "._fetch_choice_value")
    )
    fetch_choice_value.return_value = 200

    query_params = mock_netbox_module._build_query_params(
        parent, module_data, child=child
    )
    print(query_params)
    assert query_params == expected


@pytest.mark.parametrize(
    "parent, module_data, user_query_params, expected",
    load_relative_test_data("build_query_params_user_query_params"),
)
def test_build_query_params_user_query_params(
    mock_netbox_module, mocker, parent, module_data, user_query_params, expected
):
    get_query_param_id = mocker.patch(
        "%s%s" % (MOCKER_PATCH_PATH, "._get_query_param_id")
    )
    get_query_param_id.return_value = 1
    # This will need to be updated, but attempting to fix issue quickly
    fetch_choice_value = mocker.patch(
        "%s%s" % (MOCKER_PATCH_PATH, "._fetch_choice_value")
    )
    fetch_choice_value.return_value = 200

    query_params = mock_netbox_module._build_query_params(
        parent, module_data, user_query_params
    )
    assert query_params == expected


def test_build_diff_returns_valid_diff(mock_netbox_module):
    before = "The state before"
    after = {"A": "more", "complicated": "state"}
    diff = mock_netbox_module._build_diff(before=before, after=after)

    assert diff == {"before": before, "after": after}


def test_create_netbox_object_check_mode_false(
    mock_netbox_module, endpoint_mock, normalized_data, on_creation_diff
):
    return_value = endpoint_mock.create().serialize()
    serialized_obj, diff = mock_netbox_module._create_netbox_object(
        endpoint_mock, normalized_data
    )
    assert endpoint_mock.create.called_once_with(normalized_data)
    assert serialized_obj.serialize() == return_value
    assert diff == on_creation_diff


def test_create_netbox_object_check_mode_true(
    mock_netbox_module, endpoint_mock, normalized_data, on_creation_diff
):
    mock_netbox_module.check_mode = True
    serialized_obj, diff = mock_netbox_module._create_netbox_object(
        endpoint_mock, normalized_data
    )
    assert endpoint_mock.create.not_called()
    assert serialized_obj == normalized_data
    assert diff == on_creation_diff


def test_delete_netbox_object_check_mode_false(
    mock_netbox_module, nb_obj_mock, on_deletion_diff
):
    mock_netbox_module.nb_object = nb_obj_mock
    diff = mock_netbox_module._delete_netbox_object()
    assert nb_obj_mock.delete.called_once()
    assert diff == on_deletion_diff


def test_delete_netbox_object_check_mode_true(
    mock_netbox_module, nb_obj_mock, on_deletion_diff
):
    mock_netbox_module.check_mode = True
    mock_netbox_module.nb_object = nb_obj_mock
    diff = mock_netbox_module._delete_netbox_object()
    assert nb_obj_mock.delete.not_called()
    assert diff == on_deletion_diff


def test_update_netbox_object_no_changes(mock_netbox_module, nb_obj_mock):
    mock_netbox_module.nb_object = nb_obj_mock
    unchanged_data = nb_obj_mock.serialize()
    serialized_object, diff = mock_netbox_module._update_netbox_object(unchanged_data)
    assert nb_obj_mock.update.not_called()
    assert serialized_object == unchanged_data
    assert diff is None


def test_update_netbox_object_with_changes_check_mode_false(
    mock_netbox_module, nb_obj_mock, changed_serialized_obj, on_update_diff
):
    mock_netbox_module.nb_object = nb_obj_mock
    serialized_obj, diff = mock_netbox_module._update_netbox_object(
        changed_serialized_obj
    )
    assert nb_obj_mock.update.called_once_with(changed_serialized_obj)
    assert serialized_obj == nb_obj_mock.serialize()
    assert diff == on_update_diff


def test_update_netbox_object_with_changes_check_mode_true(
    mock_netbox_module, nb_obj_mock, changed_serialized_obj, on_update_diff
):
    mock_netbox_module.nb_object = nb_obj_mock
    mock_netbox_module.check_mode = True
    updated_serialized_obj = nb_obj_mock.serialize().copy()
    updated_serialized_obj.update(changed_serialized_obj)

    serialized_obj, diff = mock_netbox_module._update_netbox_object(
        changed_serialized_obj
    )
    assert nb_obj_mock.update.not_called()
    assert serialized_obj == updated_serialized_obj
    assert diff == on_update_diff


@pytest.mark.parametrize("version", ["2.9", "2.8", "2.7"])
def test_version_check_greater_true(mock_netbox_module, nb_obj_mock, version):
    mock_netbox_module.nb_object = nb_obj_mock
    assert mock_netbox_module._version_check_greater("2.10", version)


@pytest.mark.parametrize("version", ["2.13", "2.12", "2.11", "2.10"])
def test_version_check_greater_false(mock_netbox_module, nb_obj_mock, version):
    mock_netbox_module.nb_object = nb_obj_mock
    assert not mock_netbox_module._version_check_greater("2.10", version)


@pytest.mark.parametrize("version", ["2.9", "2.8", "2.7"])
def test_version_check_greater_equal_to_true(mock_netbox_module, nb_obj_mock, version):
    mock_netbox_module.nb_object = nb_obj_mock
    assert mock_netbox_module._version_check_greater(
        version, "2.7", greater_or_equal=True
    )


@pytest.mark.parametrize("version", ["2.6", "2.5", "2.4"])
def test_version_check_greater_equal_to_false(mock_netbox_module, nb_obj_mock, version):
    mock_netbox_module.nb_object = nb_obj_mock
    assert not mock_netbox_module._version_check_greater(
        version, "2.7", greater_or_equal=True
    )
