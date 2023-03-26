# Run all targets
.PHONY: all
all: black isort pytest flake8 pylint

# Run black
.PHONY: black
black:
	black --line-length 90 .

# Run isort with the black profile
.PHONY: isort
isort:
	isort . --profile black

# Run pytest
.PHONY: pytest
pytest:
	pytest

# Run mypy
.PHONY: mypy
mypy:
	mypy .

# Run flake8
.PHONY: flake8
flake8:
	flake8 *.py

# run pylint
.PHONY: pylint
pylint:
	pylint --rcfile=.pylintrc *.py
