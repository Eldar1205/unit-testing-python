# Unit Testing - Python
Python code examples for Unit Testing

## How examples are written
The examples are written to reflect how a simple `OrderValidator` class which doesn't follow *Single Responsibility Principle* isn't unit testable can be split to multiple testable classes that following that principle and are unit testable.

1. The not testable examples are under folders "not_testable"
2. The testable examples are under folders "testable"

The test code uses:
1. [pytest](https://docs.pytest.org/en/7.1.x/) as the test framework of choice
2. [freezegun](https://stevepulec.com/freezegun/) in order to control `datetime.now` results in tests

## Running the examples
1. Clone this repo
2. Install Python 3.10 if not already installed
3. Install Python poetry dependency management tool: https://python-poetry.org/docs/
4. Open a terminal (cmd/bash/PowerShell/etc.)
5. Recommended: configure poetry to create virtual environments in project folder: `poetry config virtualenvs.in-project true`
6. Navigate to repo root directory
7. Install dependencies using poetry: `poetry install`
8. Activate the virtual environment: `poetry shell`
9. Run the tests: `poetry run pytest`