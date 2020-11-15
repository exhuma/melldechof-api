import invoke


@invoke.task
def run(context):
    context.run("poetry run uvicorn melldechof.api:app", replace_env=False, pty=True)


@invoke.task
def develop(context):
    context.run("poetry install", replace_env=False, pty=True)
