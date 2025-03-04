.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.13.1

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_power_port_template_module:

.. Anchors: short name for ansible.builtin

.. Title

netbox.netbox.netbox_power_port_template module -- Create, update or delete power port templates within NetBox
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netbox.netbox collection <https://galaxy.ansible.com/ui/repo/published/netbox/netbox/>`_ (version 3.21.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.netbox.netbox.netbox_power_port_template_module_requirements>` for details.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_power_port_template`.

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

- Creates, updates or removes power port templates from NetBox


.. Aliases


.. Requirements

.. _ansible_collections.netbox.netbox.netbox_power_port_template_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- pynetbox






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cert"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-cert:

      .. rst-class:: ansible-option-title

      **cert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines the power port configuration


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/allocated_draw"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data/allocated_draw:

      .. rst-class:: ansible-option-title

      **allocated_draw**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/allocated_draw" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The allocated draw of the power port in watt


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/device_type"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data/device_type:

      .. rst-class:: ansible-option-title

      **device_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/device_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`any`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The device type the power port is attached to

      Either :emphasis:`device\_type` or :emphasis:`module\_type` are required


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/maximum_draw"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data/maximum_draw:

      .. rst-class:: ansible-option-title

      **maximum_draw**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/maximum_draw" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The maximum permissible draw of the power port in watt


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/module_type"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data/module_type:

      .. rst-class:: ansible-option-title

      **module_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/module_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`any`

      :ansible-option-versionadded:`added in netbox.netbox 3.16.0`


      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The module type the power port is attached to

      Either :emphasis:`device\_type` or :emphasis:`module\_type` are required


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/name"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the power port


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/type"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-data/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The type of the power port


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"iec-60320-c6"`
      - :ansible-option-choices-entry:`"iec-60320-c8"`
      - :ansible-option-choices-entry:`"iec-60320-c14"`
      - :ansible-option-choices-entry:`"iec-60320-c16"`
      - :ansible-option-choices-entry:`"iec-60320-c20"`
      - :ansible-option-choices-entry:`"iec-60320-c22"`
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
      - :ansible-option-choices-entry:`"iec-60906-1"`
      - :ansible-option-choices-entry:`"nbr-14136-10a"`
      - :ansible-option-choices-entry:`"nbr-14136-20a"`
      - :ansible-option-choices-entry:`"nema-1-15p"`
      - :ansible-option-choices-entry:`"nema-5-15p"`
      - :ansible-option-choices-entry:`"nema-5-20p"`
      - :ansible-option-choices-entry:`"nema-5-30p"`
      - :ansible-option-choices-entry:`"nema-5-50p"`
      - :ansible-option-choices-entry:`"nema-6-15p"`
      - :ansible-option-choices-entry:`"nema-6-20p"`
      - :ansible-option-choices-entry:`"nema-6-30p"`
      - :ansible-option-choices-entry:`"nema-6-50p"`
      - :ansible-option-choices-entry:`"nema-10-30p"`
      - :ansible-option-choices-entry:`"nema-10-50p"`
      - :ansible-option-choices-entry:`"nema-14-20p"`
      - :ansible-option-choices-entry:`"nema-14-30p"`
      - :ansible-option-choices-entry:`"nema-14-50p"`
      - :ansible-option-choices-entry:`"nema-14-60p"`
      - :ansible-option-choices-entry:`"nema-15-15p"`
      - :ansible-option-choices-entry:`"nema-15-20p"`
      - :ansible-option-choices-entry:`"nema-15-30p"`
      - :ansible-option-choices-entry:`"nema-15-50p"`
      - :ansible-option-choices-entry:`"nema-15-60p"`
      - :ansible-option-choices-entry:`"nema-l1-15p"`
      - :ansible-option-choices-entry:`"nema-l5-15p"`
      - :ansible-option-choices-entry:`"nema-l5-20p"`
      - :ansible-option-choices-entry:`"nema-l5-30p"`
      - :ansible-option-choices-entry:`"nema-l5-50p"`
      - :ansible-option-choices-entry:`"nema-l6-15p"`
      - :ansible-option-choices-entry:`"nema-l6-20p"`
      - :ansible-option-choices-entry:`"nema-l6-30p"`
      - :ansible-option-choices-entry:`"nema-l6-50p"`
      - :ansible-option-choices-entry:`"nema-l10-30p"`
      - :ansible-option-choices-entry:`"nema-l14-20p"`
      - :ansible-option-choices-entry:`"nema-l14-30p"`
      - :ansible-option-choices-entry:`"nema-l14-50p"`
      - :ansible-option-choices-entry:`"nema-l14-60p"`
      - :ansible-option-choices-entry:`"nema-l15-20p"`
      - :ansible-option-choices-entry:`"nema-l15-30p"`
      - :ansible-option-choices-entry:`"nema-l15-50p"`
      - :ansible-option-choices-entry:`"nema-l15-60p"`
      - :ansible-option-choices-entry:`"nema-l21-20p"`
      - :ansible-option-choices-entry:`"nema-l21-30p"`
      - :ansible-option-choices-entry:`"nema-l22-30p"`
      - :ansible-option-choices-entry:`"cs6361c"`
      - :ansible-option-choices-entry:`"cs6365c"`
      - :ansible-option-choices-entry:`"cs8165c"`
      - :ansible-option-choices-entry:`"cs8265c"`
      - :ansible-option-choices-entry:`"cs8365c"`
      - :ansible-option-choices-entry:`"cs8465c"`
      - :ansible-option-choices-entry:`"ita-c"`
      - :ansible-option-choices-entry:`"ita-e"`
      - :ansible-option-choices-entry:`"ita-f"`
      - :ansible-option-choices-entry:`"ita-ef"`
      - :ansible-option-choices-entry:`"ita-g"`
      - :ansible-option-choices-entry:`"ita-h"`
      - :ansible-option-choices-entry:`"ita-i"`
      - :ansible-option-choices-entry:`"ita-j"`
      - :ansible-option-choices-entry:`"ita-k"`
      - :ansible-option-choices-entry:`"ita-l"`
      - :ansible-option-choices-entry:`"ita-m"`
      - :ansible-option-choices-entry:`"ita-n"`
      - :ansible-option-choices-entry:`"ita-o"`
      - :ansible-option-choices-entry:`"usb-a"`
      - :ansible-option-choices-entry:`"usb-b"`
      - :ansible-option-choices-entry:`"usb-c"`
      - :ansible-option-choices-entry:`"usb-mini-a"`
      - :ansible-option-choices-entry:`"usb-mini-b"`
      - :ansible-option-choices-entry:`"usb-micro-a"`
      - :ansible-option-choices-entry:`"usb-micro-b"`
      - :ansible-option-choices-entry:`"usb-micro-ab"`
      - :ansible-option-choices-entry:`"usb-3-b"`
      - :ansible-option-choices-entry:`"usb-3-micro-b"`
      - :ansible-option-choices-entry:`"dc-terminal"`
      - :ansible-option-choices-entry:`"saf-d-grid"`
      - :ansible-option-choices-entry:`"neutrik-powercon-20"`
      - :ansible-option-choices-entry:`"neutrik-powercon-32"`
      - :ansible-option-choices-entry:`"neutrik-powercon-true1"`
      - :ansible-option-choices-entry:`"neutrik-powercon-true1-top"`
      - :ansible-option-choices-entry:`"ubiquiti-smartpower"`
      - :ansible-option-choices-entry:`"hardwired"`
      - :ansible-option-choices-entry:`"other"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-netbox_token:

      .. rst-class:: ansible-option-title

      **netbox_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-netbox_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-netbox_url:

      .. rst-class:: ansible-option-title

      **netbox_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-netbox_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-query_params:

      .. rst-class:: ansible-option-title

      **query_params**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query_params" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

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

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If :literal:`no`\ , SSL certificates will not be validated.

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
   - This should be ran with connection :literal:`local` and hosts :literal:`localhost`

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: "Test NetBox modules"
      connection: local
      hosts: localhost
      gather_facts: false

      tasks:
        - name: Create power port within NetBox with only required information
          netbox.netbox.netbox_power_port_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Port Template
              device_type: Test Device Type
            state: present

        - name: Create power port for a module type within NetBox
          netbox.netbox.netbox_power_port_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Port Template
              module_type: Test Module Type
              type: iec-60320-c6
              maximum_draw: 750
            state: present

        - name: Update power port with other fields
          netbox.netbox.netbox_power_port_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Port Template
              device_type: Test Device Type
              type: iec-60320-c6
              allocated_draw: 16
              maximum_draw: 80
            state: present

        - name: Delete power port within netbox
          netbox.netbox.netbox_power_port_template:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: Test Power Port Template
              device_type: Test Device Type
            state: absent



.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__return-msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

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
        <div class="ansibleOptionAnchor" id="return-power_port_template"></div>

      .. _ansible_collections.netbox.netbox.netbox_power_port_template_module__return-power_port_template:

      .. rst-class:: ansible-option-title

      **power_port_template**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-power_port_template" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Serialized object as created or already existent within NetBox


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success (when :emphasis:`state=present`\ )


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

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/netbox-community/ansible_modules/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/netbox-community/ansible_modules"
    external: true


.. Parsing errors
