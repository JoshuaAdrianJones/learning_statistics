# Run all targets
.PHONY: all
all: black isort pytest mypy flake8

# Run black
.PHONY: black
black:
	black .

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
	flake8