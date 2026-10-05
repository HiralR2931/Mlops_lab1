# MLOps Lab 1 – GitHub Actions Basics

A small calculator module tested automatically with **pytest** and **unittest** on every push to `main` using GitHub Actions.

## Project structure

```
Mlops_Lab1/
├── .github/workflows/
│   ├── github_lab1_pytest_action.yml   # CI: runs pytest, uploads XML report
│   └── unittest_action.yml             # CI: runs unittest
├── src/
│   ├── __init__.py
│   └── calculator.py                   # add, subtract, multiply, power, modulo, compound_operation
├── tests/
│   ├── test_calculator_pytest.py
│   └── test_calculator_unittest.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Functions

| Function | What it does |
|---|---|
| `add(x, y)` | x + y |
| `subtract(x, y)` | x - y |
| `multiply(x, y)` | x * y |
| `power(x, y)` | x ** y (custom) |
| `modulo(x, y)` | x % y, raises `ValueError` if y is 0 (custom) |
| `compound_operation(x, y, z)` | (x + y) * z (custom) |

All functions raise `ValueError` if inputs are not numbers.

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python -m pytest tests/ -v
python -m unittest discover -s tests -p "test_calculator_unittest.py" -v
```

## CI

On every push or pull request to `main`, both workflows run on an Ubuntu runner. Results appear in the repo's **Actions** tab; the pytest workflow also uploads `pytest-report.xml` as an artifact.
