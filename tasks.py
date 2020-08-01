import os
from invoke import task


# Name of the docker image/container
NAME = "ansible-modules"
# Gather current working directory for Docker commands
PWD = os.getcwd()


@task
def build_container(context, name=NAME, ansible_ver="latest"):
    """This will build a container with the provided name and ansible version.
    Args:
        context (obj): Used to run specific commands
        name (str): Used to name the docker image
        ansible_ver (str): Allows user to change Ansible version installed within the container
    """
    print(f"Building container {name}")
    result = context.run(
        f"docker build --tag {name} --build-arg ANSIBLE={ansible_ver} -f Dockerfile .",
        hide=True,
    )
    if result.exited != 0:
        print(f"Failed to build container {name}\nError: {result.stderr}")
