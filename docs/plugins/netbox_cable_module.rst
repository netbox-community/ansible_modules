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

.. _ansible_collections.netbox.netbox.netbox_cable_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_cable module -- Create, update or delete cables within NetBox
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.7.1).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_cable`.

.. version_added

.. versionadded:: 0.3.0 of netbox.netbox

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates or removes cables from NetBox


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

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-cert:

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

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data:

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

      Defines the cable configuration


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/color"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/color:

      .. rst-class:: ansible-option-title

      **color**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/color" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The color of the cable


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/custom_fields"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/custom_fields:

      .. rst-class:: ansible-option-title

      **custom_fields**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/custom_fields" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      :ansible-option-versionadded:`added in 3.6.0 of netbox.netbox`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Must exist in NetBox


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/label"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/label:

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

      The label of the cable


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/length"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/length:

      .. rst-class:: ansible-option-title

      **length**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/length" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The length of the cable


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/length_unit"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/length_unit:

      .. rst-class:: ansible-option-title

      **length_unit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/length_unit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The unit in which the length of the cable is measured


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`m`
      - :ansible-option-choices-entry:`cm`
      - :ansible-option-choices-entry:`ft`
      - :ansible-option-choices-entry:`in`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/status"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/status:

      .. rst-class:: ansible-option-title

      **status**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/status" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The status of the cable


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`connected`
      - :ansible-option-choices-entry:`planned`
      - :ansible-option-choices-entry:`decommissioning`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/tags"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/tags:

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

      Any tags that the cable may need to be associated with


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/termination_a"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/termination_a:

      .. rst-class:: ansible-option-title

      **termination_a**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/termination_a" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The termination a


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/termination_a_type"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/termination_a_type:

      .. rst-class:: ansible-option-title

      **termination_a_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/termination_a_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The type of the termination a


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`circuits.circuittermination`
      - :ansible-option-choices-entry:`dcim.consoleport`
      - :ansible-option-choices-entry:`dcim.consoleserverport`
      - :ansible-option-choices-entry:`dcim.frontport`
      - :ansible-option-choices-entry:`dcim.interface`
      - :ansible-option-choices-entry:`dcim.powerfeed`
      - :ansible-option-choices-entry:`dcim.poweroutlet`
      - :ansible-option-choices-entry:`dcim.powerport`
      - :ansible-option-choices-entry:`dcim.rearport`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/termination_b"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/termination_b:

      .. rst-class:: ansible-option-title

      **termination_b**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/termination_b" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`raw` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The termination b


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/termination_b_type"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/termination_b_type:

      .. rst-class:: ansible-option-title

      **termination_b_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/termination_b_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The type of the termination b


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`circuits.circuittermination`
      - :ansible-option-choices-entry:`dcim.consoleport`
      - :ansible-option-choices-entry:`dcim.consoleserverport`
      - :ansible-option-choices-entry:`dcim.frontport`
      - :ansible-option-choices-entry:`dcim.interface`
      - :ansible-option-choices-entry:`dcim.powerfeed`
      - :ansible-option-choices-entry:`dcim.poweroutlet`
      - :ansible-option-choices-entry:`dcim.powerport`
      - :ansible-option-choices-entry:`dcim.rearport`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/type"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-data/type:

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

      The type of the cable


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`cat3`
      - :ansible-option-choices-entry:`cat5`
      - :ansible-option-choices-entry:`cat5e`
      - :ansible-option-choices-entry:`cat6`
      - :ansible-option-choices-entry:`cat6a`
      - :ansible-option-choices-entry:`cat7`
      - :ansible-option-choices-entry:`dac-active`
      - :ansible-option-choices-entry:`dac-passive`
      - :ansible-option-choices-entry:`mrj21-trunk`
      - :ansible-option-choices-entry:`coaxial`
      - :ansible-option-choices-entry:`mmf`
      - :ansible-option-choices-entry:`mmf-om1`
      - :ansible-option-choices-entry:`mmf-om2`
      - :ansible-option-choices-entry:`mmf-om3`
      - :ansible-option-choices-entry:`mmf-om4`
      - :ansible-option-choices-entry:`smf`
      - :ansible-option-choices-entry:`smf-os1`
      - :ansible-option-choices-entry:`smf-os2`
      - :ansible-option-choices-entry:`aoc`
      - :ansible-option-choices-entry:`power`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-netbox_token:

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

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-netbox_url:

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

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-query_params:

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

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__parameter-validate_certs:

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

    
    - name: "Test NetBox modules"
      connection: local
      hosts: localhost
      gather_facts: False

      tasks:
        - name: Create cable within NetBox with only required information
          netbox_cable:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              termination_a_type: dcim.interface
              termination_a:
                device: Test Nexus Child One
                name: Ethernet2/2
              termination_b_type: dcim.interface
              termination_b:
                device: Test Nexus Child One
                name: Ethernet2/1
            state: present

        - name: Update cable with other fields
          netbox_cable:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              termination_a_type: dcim.interface
              termination_a:
                device: Test Nexus Child One
                name: Ethernet2/2
              termination_b_type: dcim.interface
              termination_b:
                device: Test Nexus Child One
                name: Ethernet2/1
              type: mmf-om4
              status: planned
              label: label123
              color: abcdef
              length: 30
              length_unit: m
              tags:
                - foo
            state: present

        - name: Delete cable within netbox
          netbox_cable:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              termination_a_type: dcim.interface
              termination_a:
                device: Test Nexus Child One
                name: Ethernet2/2
              termination_b_type: dcim.interface
              termination_b:
                device: Test Nexus Child One
                name: Ethernet2/1
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
        <div class="ansibleOptionAnchor" id="return-cable"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__return-cable:

      .. rst-class:: ansible-option-title

      **cable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-cable" title="Permalink to this return value"></a>

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


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.netbox.netbox.netbox_cable_module__return-msg:

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

