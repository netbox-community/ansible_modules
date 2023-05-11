from invoke import run, task


@task
def update(context):
    """Update the project dependencies via poetry"""
    run("poetry update", echo=True)


@task
def lint_fix(context):
    """Run linters with auto-fixes"""
    run("pre-commit run --all", echo=True)


@task
def lint_update(context):
    """Update linters"""
    run("pre-commit autoupdate", echo=True)

# TODO: Integration Testing w/ docker

# TODO: Unit Testing w/ docker

# TODO: Build Collection
#@task
#def build(context):
#    """Build the collection"""
#    run("ansible-galaxy collection build .", echo=True)

# TODO: Install Collection
#@task
#def install(context):
#    """Install the collection"""
#    run("ansible-galaxy collection install netbox_ansible-*.tar.gz", echo=True)
