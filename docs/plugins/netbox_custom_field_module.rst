
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

.. _ansible_collections.netbox.netbox.netbox_custom_field_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_custom_field module -- Creates, updates or deletes custom fields within NetBox
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.14.0).

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.netbox.netbox.netbox_custom_field_module_requirements>` for details.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_custom_field`.

.. version_added

.. rst-class:: ansible-version-added

New in netbox.netbox 3.6.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates or removes custom fields from NetBox


.. Aliases


.. Requirements

.. _ansible_collections.netbox.netbox.netbox_custom_field_module_requirements:

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

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-cert:

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

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data:

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

      Defines the custom field


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/choices"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/choices:

      .. rst-class:: ansible-option-title

      **choices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/choices" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of available choices (for selection fields)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/content_types"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/content_types:

      .. rst-class:: ansible-option-title

      **content_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/content_types" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The content type(s) to apply this custom field to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/default"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/default:

      .. rst-class:: ansible-option-title

      **default**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/default" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Default value of the custom field


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/description"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/description:

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

      Description of the custom field


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/filter_logic"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/filter_logic:

      .. rst-class:: ansible-option-title

      **filter_logic**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/filter_logic" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`any`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Filter logic of the custom field


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/group_name"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/group_name:

      .. rst-class:: ansible-option-title

      **group_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/group_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in netbox.netbox 3.10.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The group to associate the custom field with


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/label"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/label:

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

      Label of the custom field


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/name"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/name:

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

      Name of the custom field


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/object_type"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/object_type:

      .. rst-class:: ansible-option-title

      **object_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/object_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in netbox.netbox 3.7.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The object type of the custom field (if any)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/required"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/required:

      .. rst-class:: ansible-option-title

      **required**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/required" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Whether the custom field is required


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/search_weight"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/search_weight:

      .. rst-class:: ansible-option-title

      **search_weight**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/search_weight" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      :ansible-option-versionadded:`added in netbox.netbox 3.10.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/type"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/type:

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

      The type of custom field


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"text"`
      - :ansible-option-choices-entry:`"longtext"`
      - :ansible-option-choices-entry:`"integer"`
      - :ansible-option-choices-entry:`"decimal"`
      - :ansible-option-choices-entry:`"boolean"`
      - :ansible-option-choices-entry:`"date"`
      - :ansible-option-choices-entry:`"datetime"`
      - :ansible-option-choices-entry:`"url"`
      - :ansible-option-choices-entry:`"json"`
      - :ansible-option-choices-entry:`"select"`
      - :ansible-option-choices-entry:`"multiselect"`
      - :ansible-option-choices-entry:`"object"`
      - :ansible-option-choices-entry:`"multiobject"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/ui_visibility"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/ui_visibility:

      .. rst-class:: ansible-option-title

      **ui_visibility**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/ui_visibility" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in netbox.netbox 3.10.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The UI visibility of the custom field


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"read-write"`
      - :ansible-option-choices-entry:`"read-only"`
      - :ansible-option-choices-entry:`"hidden"`
      - :ansible-option-choices-entry:`"hidden-ifunset"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/validation_maximum"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/validation_maximum:

      .. rst-class:: ansible-option-title

      **validation_maximum**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/validation_maximum" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The maximum allowed value (for numeric fields)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/validation_minimum"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/validation_minimum:

      .. rst-class:: ansible-option-title

      **validation_minimum**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/validation_minimum" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The minimum allowed value (for numeric fields)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/validation_regex"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/validation_regex:

      .. rst-class:: ansible-option-title

      **validation_regex**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/validation_regex" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The regular expression to enforce on text fields


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-data/weight"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-data/weight:

      .. rst-class:: ansible-option-title

      **weight**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-data/weight" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Fields with higher weights appear lower in a form


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-netbox_token:

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

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-netbox_url:

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

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-query_params:

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

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-state:

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

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__parameter-validate_certs:

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
   - This should be ran with connection \ :literal:`local`\  and hosts \ :literal:`localhost`\ 

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Test NetBox custom_fields module"
      connection: local
      hosts: localhost  
      tasks:
        - name: Create a custom field on device and virtual machine
          netbox.netbox.netbox_custom_field:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              content_types:
                - dcim.device
                - virtualization.virtualmachine
              name: A Custom Field
              type: text

        - name: Update the custom field to make it required
          netbox.netbox.netbox_custom_field:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: A Custom Field
              required: yes    

        - name: Update the custom field to make it read only
          netbox.netbox.netbox_custom_field:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: A Custom Field
              ui_visibility: read-only      

        - name: Delete the custom field
          netbox.netbox.netbox_custom_field:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              name: A Custom Field
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
        <div class="ansibleOptionAnchor" id="return-custom_field"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__return-custom_field:

      .. rst-class:: ansible-option-title

      **custom_field**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-custom_field" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Serialized object as created/existent/updated/deleted within NetBox


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.netbox.netbox.netbox_custom_field_module__return-msg:

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

- Martin Rødvand (@rodvand)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/netbox-community/ansible_modules/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/netbox-community/ansible_modules" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

