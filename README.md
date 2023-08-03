# Trade Machine
It's a machine that trades.

## Development
First, if you don't have it already, install the latest version of python3 which can be found [here](https://www.python.org/downloads/).

Next, you'll need to install poetry. Poetry is a python package manager that will handle all of the dependencies for you. You can find instructions on how to install poetry [here](https://python-poetry.org/docs/#installation).

After this, you'll need to install uvicorn. Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. You can find instructions on how to install uvicorn [here](https://www.uvicorn.org/#installation).

Once poetry is installed, you can install all of the dependencies by running `poetry install` in the root directory of the project.

Finally, you can run the server by running `poetry run uvicorn trade_machine.main:app --reload` in the root directory of the project.
