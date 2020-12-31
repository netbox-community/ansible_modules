=============
Installation
=============

Ansible Galaxy
---------------

Run the following command to install the netbox.netbox collection:
``ansible-galaxy collection install netbox.netbox``

.. _docs: https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections

.. note::
  Installing Ansible Collections using Git within a ``requirements.yml`` is not supported until Ansible 2.10.

  Follow the official docs_ to learn more about other installation methods.

Build From Source
------------------

Follow these steps to install from source:

1. ``git clone git@github.com:netbox-community/ansible_modules.git``
2. ``cd ansible_modules``
3. ``ansible-galaxy collection build .``
4. ``ansible-galaxy collection install netbox-netbox*.tar.gz``

Build From Source (Pull Request)
-----------------------------------

This is useful to test code within PRs.

1. ``git clone git@github.com:netbox-community/ansible_modules.git``
2. ``cd ansible_modules``
3. ``git fetch origin pull/<pr #>/head:<whatever-name-you-want>``
4. ``git checkout <whatever-name-you-want>``
5. ``ansible-galaxy collection build .``
6. ``ansible-galaxy collection install netbox-netbox*.tar.gz``

.. _GitHub: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/checking-out-pull-requests-locally
.. note:: The following link provides detailed information on checking out pull requests locally: GitHub_