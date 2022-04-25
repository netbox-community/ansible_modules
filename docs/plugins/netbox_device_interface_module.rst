.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_device_interface_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_device_interface module -- Creates or removes interfaces on devices from NetBox
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.7.1).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_device_interface`.

.. version_added

.. versionadded:: 0.1.0 of netbox.netbox

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates or removes interfaces from NetBox


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- pynetbox


.. Options

Parameters
----------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cert"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-cert:

      .. rst-class:: ansible-option-title

      **cert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Certificate path


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines the interface configuration


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/bridge"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/bridge:

      .. rst-class:: ansible-option-title

      **bridge**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/bridge" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      :ansible-option-versionadded:`added in 3.6.0 of netbox.netbox`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Bridge the interface will connected to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/custom_fields"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/custom_fields:

      .. rst-class:: ansible-option-title

      **custom_fields**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/custom_fields" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      must exist in NetBox


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/description"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/description:

      .. rst-class:: ansible-option-title

      **description**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/description" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The description of the interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/device"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/device:

      .. rst-class:: ansible-option-title

      **device**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/device" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Name of the device the interface will be associated with (case-sensitive)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/duplex"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/duplex:

      .. rst-class:: ansible-option-title

      **duplex**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/duplex" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in 3.7.0 of netbox.netbox`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The duplex of the interface


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`half`
      - :ansible-option-choices-entry:`full`
      - :ansible-option-choices-entry:`auto`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/enabled"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/enabled:

      .. rst-class:: ansible-option-title

      **enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/enabled" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Sets whether interface shows enabled or disabled


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/form_factor"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/form_factor:

      .. rst-class:: ansible-option-title

      **form_factor**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/form_factor" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Form factor of the interface:
          ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE)
          This has to be specified exactly as what is found within UI
          


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/label"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/label:

      .. rst-class:: ansible-option-title

      **label**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/label" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Physical label of the interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/lag"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/lag:

      .. rst-class:: ansible-option-title

      **lag**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/lag" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Parent LAG interface will be a member of


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/mac_address"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/mac_address:

      .. rst-class:: ansible-option-title

      **mac_address**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/mac_address" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The MAC address of the interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/mark_connected"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/mark_connected:

      .. rst-class:: ansible-option-title

      **mark_connected**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/mark_connected" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Mark an interface as connected without a cable attached (netbox >= 2.11 required)


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/mgmt_only"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/mgmt_only:

      .. rst-class:: ansible-option-title

      **mgmt_only**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/mgmt_only" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      This interface is used only for out-of-band management


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/mode"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode of the interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/mtu"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/mtu:

      .. rst-class:: ansible-option-title

      **mtu**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/mtu" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The MTU of the interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/name"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Name of the interface to be created


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/parent_interface"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/parent_interface:

      .. rst-class:: ansible-option-title

      **parent_interface**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/parent_interface" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      :ansible-option-versionadded:`added in 3.2.0 of netbox.netbox`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The device's parent interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/speed"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/speed:

      .. rst-class:: ansible-option-title

      **speed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/speed" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      :ansible-option-versionadded:`added in 3.7.0 of netbox.netbox`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The speed of the interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/tagged_vlans"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/tagged_vlans:

      .. rst-class:: ansible-option-title

      **tagged_vlans**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/tagged_vlans" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A list of tagged VLANS to be assigned to interface. Mode must be set to either \ :literal:`Tagged`\  or \ :literal:`Tagged All`\ 


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/tags"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/tags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Any tags that the interface may need to be associated with


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/type"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Form factor of the interface:
          ex. 1000Base-T (1GE), Virtual, 10GBASE-T (10GE)
          This has to be specified exactly as what is found within UI
          


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/untagged_vlan"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/untagged_vlan:

      .. rst-class:: ansible-option-title

      **untagged_vlan**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/untagged_vlan" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The untagged VLAN to be assigned to interface


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/vrf"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-data/vrf:

      .. rst-class:: ansible-option-title

      **vrf**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/vrf" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      :ansible-option-versionadded:`added in 3.7.0 of netbox.netbox`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The VRF of the interface


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-netbox_token:

      .. rst-class:: ansible-option-title

      **netbox_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-netbox_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The NetBox API token.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netbox_url"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-netbox_url:

      .. rst-class:: ansible-option-title

      **netbox_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-netbox_url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The URL of the NetBox instance.

      Must be accessible by the Ansible control host.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-query_params"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-query_params:

      .. rst-class:: ansible-option-title

      **query_params**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query_params" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined

      in plugins/module_utils/netbox_utils.py and provides control to users on what may make

      an object unique in their environment.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The state of the object.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`present` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`absent`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-update_vc_child"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-update_vc_child:

      .. rst-class:: ansible-option-title

      **update_vc_child**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-update_vc_child" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use when master device is specified for \ :literal:`device`\  and the specified interface exists on a child device
          and needs updated
          


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`no`\ , SSL certificates will not be validated.

      This should only be used on personally controlled sites using a self-signed certificates.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"yes"`

      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - Tags should be defined as a YAML list
   - This should be ran with connection \ :literal:`local`\  and hosts \ :literal:`localhost`\ 

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Test NetBox interface module"
      connection: local
      hosts: localhost
      gather_facts: False
      tasks:
        - name: Create interface within NetBox with only required information
          netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: GigabitEthernet1
            state: present
        - name: Delete interface within netbox
          netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: GigabitEthernet1
            state: absent
        - name: Create LAG with several specified options
          netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: port-channel1
              type: Link Aggregation Group (LAG)
              mtu: 1600
              mgmt_only: false
              mode: Access
            state: present
        - name: Create interface and assign it to parent LAG
          netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: GigabitEthernet1
              enabled: false
              type: 1000Base-t (1GE)
              lag:
                name: port-channel1
              mtu: 1600
              mgmt_only: false
              mode: Access
            state: present
        - name: Create interface as a trunk port
          netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: GigabitEthernet25
              enabled: false
              type: 1000Base-t (1GE)
              untagged_vlan:
                name: Wireless
                site: Test Site
              tagged_vlans:
                - name: Data
                  site: Test Site
                - name: VoIP
                  site: Test Site
              mtu: 1600
              mgmt_only: true
              mode: Tagged
            state: present
        - name: Update interface on child device on virtual chassis
          netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: GigabitEthernet2/0/1
              enabled: false
            update_vc_child: True
        - name: Mark interface as connected without a cable (netbox >= 2.11 required)
          netbox.netbox.netbox_device_interface:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              device: test100
              name: GigabitEthernet1
              mark_connected: true
            state: present




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-interface"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__return-interface:

      .. rst-class:: ansible-option-title

      **interface**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-interface" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Serialized object as created or already existent within NetBox


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on creation


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.netbox.netbox.netbox_device_interface_module__return-msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Message indicating failure or info about what has been achieved


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Mikhail Yohman (@FragmentedPacket)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/netbox-community/ansible_modules/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/netbox-community/ansible_modules" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

