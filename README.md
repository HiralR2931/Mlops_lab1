# MLOps Lab 1 – GitHub Actions Basics

A small calculator module tested automatically with **pytest** and **unittest** using GitHub Actions.

## Project structure

```
Mlops_lab1/
├── .github/workflows/
│   ├── pytest_action.yml        # CI: runs pytest on every push
│   └── unittest_action.yml      # CI: runs unittest on push / PR to main
├── src/
│   ├── __init__.py
│   └── calculator.py            # add, subtract, multiply, power, modulo, compound_operation
├── tests/
│   ├── test_calculator_pytest.py
│   └── test_calculator_unittest.py
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

## CI workflows

| Workflow | Trigger | Python | Command |
|---|---|---|---|
| Testing with Pytest (`pytest_action.yml`) | every push | 3.8 | `pytest tests/ -v` |
| Testing with Unittest (`unittest_action.yml`) | push / PR to `main` | 3.9 | `python -m unittest tests.test_calculator_unittest -v` |

Both run on an Ubuntu runner. Results appear in the repo's **Actions** tab, and the unittest workflow prints a pass/fail message at the end.
