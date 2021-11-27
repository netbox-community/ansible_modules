.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.netbox.netbox.nb_lookup_lookup:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.nb_lookup -- Queries and returns elements from NetBox
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.4.0).

    To install it use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.nb_lookup`.

.. version_added

.. versionadded:: 2.9 of netbox.netbox

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Queries NetBox via its API to return virtually any information capable of being held in NetBox.
- If wanting to obtain the plaintext attribute of a secret, *private_key* or *key_file* must be provided.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the local controller node that executes this lookup.

- pynetbox


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-_terms"></div>
                    <b>_terms</b>
                    <a class="ansibleOptionLink" href="#parameter-_terms" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>The NetBox object type to query</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_endpoint"></div>
                    <b>api_endpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-api_endpoint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:NETBOX_API
                                                                                            </div>
                                                    <div>
                                env:NETBOX_URL
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>The URL to the NetBox instance to query</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_filter"></div>
                    <b>api_filter</b>
                    <a class="ansibleOptionLink" href="#parameter-api_filter" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>The api_filter to use. Filters should be key value pairs separated by a space.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-key_file"></div>
                    <b>key_file</b>
                    <a class="ansibleOptionLink" href="#parameter-key_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>The location of the private key tied to user account. Mutually exclusive with <em>private_key</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-plugin"></div>
                    <b>plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>The NetBox plugin to query</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-private_key"></div>
                    <b>private_key</b>
                    <a class="ansibleOptionLink" href="#parameter-private_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>The private key as a string. Mutually exclusive with <em>key_file</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-raw_data"></div>
                    <b>raw_data</b>
                    <a class="ansibleOptionLink" href="#parameter-raw_data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Whether to return raw API data with the lookup/query or whether to return a key/value dict</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-token"></div>
                    <b>token</b>
                    <a class="ansibleOptionLink" href="#parameter-token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:NETBOX_TOKEN
                                                                                            </div>
                                                    <div>
                                env:NETBOX_API_TOKEN
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>The API token created through NetBox</div>
                                            <div>This may not be required depending on the NetBox setup.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Whether or not to validate SSL of the NetBox instance</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


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

    tasks:
      # query a list of devices
      - name: Obtain list of devices from NetBox
        debug:
          msg: >
            "Device {{ item.value.display_name }} (ID: {{ item.key }}) was
             manufactured by {{ item.value.device_type.manufacturer.name }}"
        loop: "{{ query('netbox.netbox.nb_lookup', 'devices',
                        api_endpoint='http://localhost/',
                        api_filter='role=management tag=Dell'),
                        token='<redacted>') }}"

    # Obtain a secret for R1-device
    tasks:
      - name: "Obtain secrets for R1-Device"
        debug:
          msg: "{{ query('netbox.netbox.nb_lookup', 'secrets', api_filter='device=R1-Device', api_endpoint='http://localhost/', token='<redacted>', key_file='~/.ssh/id_rsa') }}"

    # Fetch bgp sessions for R1-device
    tasks:
      - name: "Obtain bgp sessions for R1-Device"
        debug:
          msg: "{{ query('netbox.netbox.nb_lookup', 'bgp_sessions',
                         api_filter='device=R1-Device',
                         api_endpoint='http://localhost/',
                         token='<redacted>',
                         plugin='mycustomstuff') }}"

          msg: "{{ query('netbox.netbox.nb_lookup', 'secrets', api_filter='device=R1-Device', api_endpoint='http://localhost/', token='<redacted>', key_file='~/.ssh/id_rsa') }}"




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this lookup:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-_list"></div>
                    <b>_list</b>
                    <a class="ansibleOptionLink" href="#return-_list" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>list of composed dictionaries with key and value</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Chris Mills (@cpmills1975)



.. Parsing errors

