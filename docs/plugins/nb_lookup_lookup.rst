.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.13.1

.. Anchors

.. _ansible_collections.netbox.netbox.nb_lookup_lookup:

.. Anchors: short name for ansible.builtin

.. Title

netbox.netbox.nb_lookup lookup -- Queries and returns elements from NetBox
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This lookup plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/ui/repo/published/netbox/netbox/>`_ (version 3.21.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install netbox.netbox`.
    You need further requirements to be able to use this lookup plugin,
    see :ref:`Requirements <ansible_collections.netbox.netbox.nb_lookup_lookup_requirements>` for details.

    To use it in a playbook, specify: :code:`netbox.netbox.nb_lookup`.

.. version_added

.. rst-class:: ansible-version-added

New in netbox.netbox 0.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Queries NetBox via its API to return virtually any information capable of being held in NetBox.


.. Aliases


.. Requirements

.. _ansible_collections.netbox.netbox.nb_lookup_lookup_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this lookup.

- pynetbox




.. Terms

Terms
-----

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
        <div class="ansibleOptionAnchor" id="parameter-_terms"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-_terms:

      .. rst-class:: ansible-option-title

      **Terms**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-_terms" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The NetBox object type to query


      .. raw:: html

        </div>





.. Options

Keyword parameters
------------------

This describes keyword parameters of the lookup. These are the values ``key1=value1``, ``key2=value2`` and so on in the following
examples: ``lookup('netbox.netbox.nb_lookup', key1=value1, key2=value2, ...)`` and ``query('netbox.netbox.nb_lookup', key1=value1, key2=value2, ...)``

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
        <div class="ansibleOptionAnchor" id="parameter-api_endpoint"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-api_endpoint:

      .. rst-class:: ansible-option-title

      **api_endpoint**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_endpoint" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The URL to the NetBox instance to query


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NETBOX\_API`

      - Environment variable: :envvar:`NETBOX\_URL`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_filter"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-api_filter:

      .. rst-class:: ansible-option-title

      **api_filter**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_filter" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The api\_filter to use. Filters should be key value pairs separated by a space.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-headers"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-headers:

      .. rst-class:: ansible-option-title

      **headers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-headers" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary of headers to be passed to the NetBox API.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`{}`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NETBOX\_HEADERS`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-key_file"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-key_file:

      .. rst-class:: ansible-option-title

      **key_file**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-key_file" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      (DEPRECATED) - NetBox 2.11 and earlier only

      The location of the private key tied to user account. Mutually exclusive with :emphasis:`private\_key`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-plugin"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-plugin:

      .. rst-class:: ansible-option-title

      **plugin**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The NetBox plugin to query


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-private_key"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-private_key:

      .. rst-class:: ansible-option-title

      **private_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-private_key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      (DEPRECATED) - NetBox 2.11 and earlier only

      The private key as a string. Mutually exclusive with :emphasis:`key\_file`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-raw_data"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-raw_data:

      .. rst-class:: ansible-option-title

      **raw_data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-raw_data" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to return raw API data with the lookup/query or whether to return a key/value dict


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-token"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-token:

      .. rst-class:: ansible-option-title

      **token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The API token created through NetBox

      This may not be required depending on the NetBox setup.


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`NETBOX\_TOKEN`

      - Environment variable: :envvar:`NETBOX\_API\_TOKEN`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether or not to validate SSL of the NetBox instance


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`true`

      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
     ``lookup('netbox.netbox.nb_lookup', term1, term2, key1=value1, key2=value2)`` and ``query('netbox.netbox.nb_lookup', term1, term2, key1=value1, key2=value2)``

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    tasks:
      # query a list of devices
      - name: Obtain list of devices from NetBox
        debug:
          msg: >
            "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
             manufactured by {{ item.value.device_type.manufacturer.name }}"
        loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                        api_endpoint='http://localhost/',
                        token='<redacted>') }}"

        # This example uses an API Filter
      - name: Obtain list of devices from NetBox
        debug:
          msg: >
            "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
             manufactured by {{ item.value.device_type.manufacturer.name }}"
        loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                        api_endpoint='http://localhost/',
                        api_filter='role=management tag=Dell'),
                        token='<redacted>') }}"
        # This example uses an API Filter with a variable and jinja concatenation
      - name: Set hostname fact
        set_fact:
          hostname: "my-server"
      - name: Obtain details of a single device from NetBox
        debug:
          msg: >
            "Device {{item.0.value.display}} (ID: {{item.0.key}}) was
             manufactured by {{ item.0.value.device_type.manufacturer.name }}"
        loop:
          - '{{ query("netbox.netbox.nb_lookup", "devices",
            api_endpoint="http://localhost/",
            api_filter="name=" ~hostname,
            token="<redacted>") }}'



.. Facts


.. Return values

Return Value
------------

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
        <div class="ansibleOptionAnchor" id="return-_list"></div>

      .. _ansible_collections.netbox.netbox.nb_lookup_lookup__return-_list:

      .. rst-class:: ansible-option-title

      **Return value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-_list" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      list of composed dictionaries with key and value


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Chris Mills (@cpmills1975)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

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
