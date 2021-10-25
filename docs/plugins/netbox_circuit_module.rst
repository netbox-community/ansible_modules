.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_circuit_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_circuit -- Create, update or delete circuits within Netbox
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.3.0).

    To install it use: :code:`ansible-galaxy collection install netbox.netbox`.

    To use it in a playbook, specify: :code:`netbox.netbox.netbox_circuit`.

.. version_added

.. versionadded:: 0.1.0 of netbox.netbox

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates or removes circuits from Netbox


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- pynetbox


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cert"></div>
                    <b>cert</b>
                    <a class="ansibleOptionLink" href="#parameter-cert" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Certificate path</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data"></div>
                    <b>data</b>
                    <a class="ansibleOptionLink" href="#parameter-data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines the circuit configuration</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/cid"></div>
                    <b>cid</b>
                    <a class="ansibleOptionLink" href="#parameter-data/cid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The circuit id of the circuit</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/circuit_type"></div>
                    <b>circuit_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data/circuit_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The circuit type of the circuit</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/comments"></div>
                    <b>comments</b>
                    <a class="ansibleOptionLink" href="#parameter-data/comments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Comments related to circuit</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/commit_rate"></div>
                    <b>commit_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-data/commit_rate" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Commit rate of the circuit (Kbps)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/custom_fields"></div>
                    <b>custom_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-data/custom_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>must exist in Netbox</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-data/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Description of the circuit</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/install_date"></div>
                    <b>install_date</b>
                    <a class="ansibleOptionLink" href="#parameter-data/install_date" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The date the circuit was installed. e.g. YYYY-MM-DD</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/provider"></div>
                    <b>provider</b>
                    <a class="ansibleOptionLink" href="#parameter-data/provider" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The provider of the circuit</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-data/status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of the circuit</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/tags"></div>
                    <b>tags</b>
                    <a class="ansibleOptionLink" href="#parameter-data/tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=raw</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Any tags that the device may need to be associated with</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/tenant"></div>
                    <b>tenant</b>
                    <a class="ansibleOptionLink" href="#parameter-data/tenant" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The tenant assigned to the circuit</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-netbox_token"></div>
                    <b>netbox_token</b>
                    <a class="ansibleOptionLink" href="#parameter-netbox_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The token created within Netbox to authorize API access</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-netbox_url"></div>
                    <b>netbox_url</b>
                    <a class="ansibleOptionLink" href="#parameter-netbox_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>URL of the Netbox instance resolvable by Ansible control host</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-query_params"></div>
                    <b>query_params</b>
                    <a class="ansibleOptionLink" href="#parameter-query_params" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined</div>
                                            <div>in plugins/module_utils/netbox_utils.py and provides control to users on what may make</div>
                                            <div>an object unique in their environment.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>absent</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Use <code>present</code> or <code>absent</code> for adding or removing.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                                <td>
                                            <div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - Tags should be defined as a YAML list
   - This should be ran with connection ``local`` and hosts ``localhost``

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Test Netbox modules"
      connection: local
      hosts: localhost
      gather_facts: False

      tasks:
        - name: Create circuit within Netbox with only required information
          netbox_circuit:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              cid: Test Circuit
              provider: Test Provider
              circuit_type: Test Circuit Type
            state: present

        - name: Update circuit with other fields
          netbox_circuit:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              cid: Test-Circuit-1000
              provider: Test Provider
              circuit_type: Test Circuit Type
              status: Active
              tenant: Test Tenant
              install_date: "2018-12-25"
              commit_rate: 10000
              description: Test circuit
              comments: "FAST CIRCUIT"
            state: present

        - name: Delete circuit within netbox
          netbox_circuit:
            netbox_url: http://netbox.local
            netbox_token: thisIsMyToken
            data:
              cid: Test-Circuit-1000
            state: absent




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-circuit"></div>
                    <b>circuit</b>
                    <a class="ansibleOptionLink" href="#return-circuit" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success (when <em>state=present</em>)</td>
                <td>
                                            <div>Serialized object as created or already existent within Netbox</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-msg"></div>
                    <b>msg</b>
                    <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Message indicating failure or info about what has been achieved</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Mikhail Yohman (@FragmentedPacket)



.. Parsing errors

