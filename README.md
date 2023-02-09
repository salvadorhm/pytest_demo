# Testing with Pytest and Coverage


## Run app

```bash
python3 mayor.py
```

## Pytest

```bash
python3 -m pytest -v test
```

## Coverage

```bash
python3 -m coverage run -m pytest -v
```

## Coverage report

```bash
python3 -m coverage report
```

## Test cases

|No.|numero1|numero2|result|
|--|--|--|--|
|1.|2|1|2|
|2.|1|2|2|
|3.|2|2|None|
|4.|2|-1|2|
|5.|-1|2|2|
|6.|-1|-1|None|
|7.|-1|-2|-1|
|8.|-2|-1|-1|