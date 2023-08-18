
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
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_power_outlet_template module -- Create, update or delete power outlet templates within NetBox
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.14.0).

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.netbox.netbox.netbox_power_outlet_template_module_requirements>` for details.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_power_outlet_template`.

.. version_added

.. rst-class:: ansible-version-added

New in netbox.netbox 0.2.3

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates or removes power outlet templates from NetBox


.. Aliases


.. Requirements

.. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module_requirements:

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

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-cert:

      .. rst-class:: ansible-option-title

      **cert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

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

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-data:

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

      Defines the power outlet configuration


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/device_type"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-data/device_type:

      .. rst-class:: ansible-option-title

      **device_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/device_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The device type the power outlet is attached to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/feed_leg"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-data/feed_leg:

      .. rst-class:: ansible-option-title

      **feed_leg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/feed_leg" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The phase, in case of three-phase feed


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"A"`
      - :ansible-option-choices-entry:`"B"`
      - :ansible-option-choices-entry:`"C"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/name"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-data/name:

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

      The name of the power outlet


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/power_port_template"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-data/power_port_template:

      .. rst-class:: ansible-option-title

      **power_port_template**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/power_port_template" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The attached power port template


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/type"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-data/type:

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

      The type of the power outlet


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"iec-60320-c5"`
      - :ansible-option-choices-entry:`"iec-60320-c7"`
      - :ansible-option-choices-entry:`"iec-60320-c13"`
      - :ansible-option-choices-entry:`"iec-60320-c15"`
      - :ansible-option-choices-entry:`"iec-60320-c19"`
      - :ansible-option-choices-entry:`"iec-60309-p-n-e-4h"`
      - :ansible-option-choices-entry:`"iec-60309-p-n-e-6h"`
      - :ansible-option-choices-entry:`"iec-60309-p-n-e-9h"`
      - :ansible-option-choices-entry:`"iec-60309-2p-e-4h"`
      - :ansible-option-choices-entry:`"iec-60309-2p-e-6h"`
      - :ansible-option-choices-entry:`"iec-60309-2p-e-9h"`
      - :ansible-option-choices-entry:`"iec-60309-3p-e-4h"`
      - :ansible-option-choices-entry:`"iec-60309-3p-e-6h"`
      - :ansible-option-choices-entry:`"iec-60309-3p-e-9h"`
      - :ansible-option-choices-entry:`"iec-60309-3p-n-e-4h"`
      - :ansible-option-choices-entry:`"iec-60309-3p-n-e-6h"`
      - :ansible-option-choices-entry:`"iec-60309-3p-n-e-9h"`
      - :ansible-option-choices-entry:`"nema-5-15r"`
      - :ansible-option-choices-entry:`"nema-5-20r"`
      - :ansible-option-choices-entry:`"nema-5-30r"`
      - :ansible-option-choices-entry:`"nema-5-50r"`
      - :ansible-option-choices-entry:`"nema-6-15r"`
      - :ansible-option-choices-entry:`"nema-6-20r"`
      - :ansible-option-choices-entry:`"nema-6-30r"`
      - :ansible-option-choices-entry:`"nema-6-50r"`
      - :ansible-option-choices-entry:`"nema-l5-15r"`
      - :ansible-option-choices-entry:`"nema-l5-20r"`
      - :ansible-option-choices-entry:`"nema-l5-30r"`
      - :ansible-option-choices-entry:`"nema-l5-50r"`
      - :ansible-option-choices-entry:`"nema-l6-20r"`
      - :ansible-option-choices-entry:`"nema-l6-30r"`
      - :ansible-option-choices-entry:`"nema-l6-50r"`
      - :ansible-option-choices-entry:`"nema-l14-20r"`
      - :ansible-option-choices-entry:`"nema-l14-30r"`
      - :ansible-option-choices-entry:`"nema-l21-20r"`
      - :ansible-option-choices-entry:`"nema-l21-30r"`
      - :ansible-option-choices-entry:`"CS6360C"`
      - :ansible-option-choices-entry:`"CS6364C"`
      - :ansible-option-choices-entry:`"CS8164C"`
      - :ansible-option-choices-entry:`"CS8264C"`
      - :ansible-option-choices-entry:`"CS8364C"`
      - :ansible-option-choices-entry:`"CS8464C"`
      - :ansible-option-choices-entry:`"ita-e"`
      - :ansible-option-choices-entry:`"ita-f"`
      - :ansible-option-choices-entry:`"ita-g"`
      - :ansible-option-choices-entry:`"ita-h"`
      - :ansible-option-choices-entry:`"ita-i"`
      - :ansible-option-choices-entry:`"ita-j"`
      - :ansible-option-choices-entry:`"ita-k"`
      - :ansible-option-choices-entry:`"ita-l"`
      - :ansible-option-choices-entry:`"ita-m"`
      - :ansible-option-choices-entry:`"ita-n"`
      - :ansible-option-choices-entry:`"ita-o"`
      - :ansible-option-choices-entry:`"hdot-cx"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-netbox_token:

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

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-netbox_url:

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

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-query_params:

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

      This can be used to override the specified values in ALLOWED\_QUERY\_PARAMS that are defined

      in plugins/module\_utils/netbox\_utils.py and provides control to users on what may make

      an object unique in their environment.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-state:

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

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`no`\ , SSL certificates will not be validated.

      This should only be used on personally controlled sites using a self-signed certificates.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`true`

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

    
    - name: "Test NetBox modules"
      connection: local
      hosts: localhost
      gather_facts: False

      tasks:
        - name: Create power outlet template within NetBox with only required information
          netbox.netbox.netbox_power_outlet_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Outlet Template
              device_type: Test Device Type
            state: present

        - name: Update power outlet template with other fields
          netbox.netbox.netbox_power_outlet_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Outlet Template
              device_type: Test Device Type
              type: iec-60320-c6
              power_port_template: Test Power Port Template
              feed_leg: A
            state: present

        - name: Delete power outlet template within netbox
          netbox.netbox.netbox_power_outlet_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Outlet Template
              device_type: Test Device Type
            state: absent




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
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__return-msg:

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


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-power_outlet_template"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_outlet_template_module__return-power_outlet_template:

      .. rst-class:: ansible-option-title

      **power_outlet_template**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-power_outlet_template" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Serialized object as created or already existent within NetBox


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success (when \ :emphasis:`state=present`\ )


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Tobias Groß (@toerb)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/netbox-community/ansible_modules/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/netbox-community/ansible_modules" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

