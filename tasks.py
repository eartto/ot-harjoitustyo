from invoke import task



@task
def build(ctx):
    ctx.run("pip install Pillow", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m")
    ctx.run("coverage html")


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True )
