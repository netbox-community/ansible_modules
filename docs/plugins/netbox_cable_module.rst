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

.. Anchors

.. _ansible_collections.netbox.netbox.netbox_cable_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netbox.netbox.netbox_cable -- Create, update or delete cables within NetBox
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `netbox.netbox collection <https://galaxy.ansible.com/netbox/netbox>`_ (version 3.5.0).

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
                                            <div>Defines the cable configuration</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/color"></div>
                    <b>color</b>
                    <a class="ansibleOptionLink" href="#parameter-data/color" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The color of the cable</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/label"></div>
                    <b>label</b>
                    <a class="ansibleOptionLink" href="#parameter-data/label" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The label of the cable</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/length"></div>
                    <b>length</b>
                    <a class="ansibleOptionLink" href="#parameter-data/length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The length of the cable</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/length_unit"></div>
                    <b>length_unit</b>
                    <a class="ansibleOptionLink" href="#parameter-data/length_unit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>m</li>
                                                                                                                                                                                                <li>cm</li>
                                                                                                                                                                                                <li>ft</li>
                                                                                                                                                                                                <li>in</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The unit in which the length of the cable is measured</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-data/status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>connected</li>
                                                                                                                                                                                                <li>planned</li>
                                                                                                                                                                                                <li>decommissioning</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The status of the cable</div>
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
                                            <div>Any tags that the cable may need to be associated with</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/termination_a"></div>
                    <b>termination_a</b>
                    <a class="ansibleOptionLink" href="#parameter-data/termination_a" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The termination a</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/termination_a_type"></div>
                    <b>termination_a_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data/termination_a_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>circuits.circuittermination</li>
                                                                                                                                                                                                <li>dcim.consoleport</li>
                                                                                                                                                                                                <li>dcim.consoleserverport</li>
                                                                                                                                                                                                <li>dcim.frontport</li>
                                                                                                                                                                                                <li>dcim.interface</li>
                                                                                                                                                                                                <li>dcim.powerfeed</li>
                                                                                                                                                                                                <li>dcim.poweroutlet</li>
                                                                                                                                                                                                <li>dcim.powerport</li>
                                                                                                                                                                                                <li>dcim.rearport</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the termination a</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/termination_b"></div>
                    <b>termination_b</b>
                    <a class="ansibleOptionLink" href="#parameter-data/termination_b" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The termination b</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/termination_b_type"></div>
                    <b>termination_b_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data/termination_b_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>circuits.circuittermination</li>
                                                                                                                                                                                                <li>dcim.consoleport</li>
                                                                                                                                                                                                <li>dcim.consoleserverport</li>
                                                                                                                                                                                                <li>dcim.frontport</li>
                                                                                                                                                                                                <li>dcim.interface</li>
                                                                                                                                                                                                <li>dcim.powerfeed</li>
                                                                                                                                                                                                <li>dcim.poweroutlet</li>
                                                                                                                                                                                                <li>dcim.powerport</li>
                                                                                                                                                                                                <li>dcim.rearport</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the termination b</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>cat3</li>
                                                                                                                                                                                                <li>cat5</li>
                                                                                                                                                                                                <li>cat5e</li>
                                                                                                                                                                                                <li>cat6</li>
                                                                                                                                                                                                <li>cat6a</li>
                                                                                                                                                                                                <li>cat7</li>
                                                                                                                                                                                                <li>dac-active</li>
                                                                                                                                                                                                <li>dac-passive</li>
                                                                                                                                                                                                <li>mrj21-trunk</li>
                                                                                                                                                                                                <li>coaxial</li>
                                                                                                                                                                                                <li>mmf</li>
                                                                                                                                                                                                <li>mmf-om1</li>
                                                                                                                                                                                                <li>mmf-om2</li>
                                                                                                                                                                                                <li>mmf-om3</li>
                                                                                                                                                                                                <li>mmf-om4</li>
                                                                                                                                                                                                <li>smf</li>
                                                                                                                                                                                                <li>smf-os1</li>
                                                                                                                                                                                                <li>smf-os2</li>
                                                                                                                                                                                                <li>aoc</li>
                                                                                                                                                                                                <li>power</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the cable</div>
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
                                            <div>The NetBox API token.</div>
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
                                            <div>The URL of the NetBox instance.</div>
                                            <div>Must be accessible by the Ansible control host.</div>
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
                                            <div>This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined</div>
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
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The state of the object.</div>
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
                                            <div>If <code>no</code>, SSL certificates will not be validated.</div>
                                            <div>This should only be used on personally controlled sites using a self-signed certificates.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


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

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cable"></div>
                    <b>cable</b>
                    <a class="ansibleOptionLink" href="#return-cable" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>success (when <em>state=present</em>)</td>
                <td>
                                            <div>Serialized object as created or already existent within NetBox</div>
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

- Tobias Groß (@toerb)



.. Parsing errors

