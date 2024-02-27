# Pytest Framework

---
Pytest is the framework by which we can test the python module

## Features
1) Fixtures
2) Parallel testing
3) Skip the tests
4) Group tests
5) Batch testing
6) Parameterization
7) Reports

## Rules
* File names should start with `test_` or end with `_test`
* Class name should start with `“Test”`
```python
import pytest

class TestClass:
    def testMethod1(self):
        print("this is test method1")
    def testMethod2(self):
        print("this is test method2")
```
* Test method names should start with `“test”`
* Create module name `conftest.py` for common pytest fixture function
## Commands to Run Pytest
**1. Single module**
```commandline
pytest -v -s day26-pytest\modules\test_Login.py
```
**2.All the modules in a directory/package**
```commandline
pytest -v -s day26-pytest\modules
```
**3.un Specific Test Method from a Module**
```commandline
pytest -v -s day26-pytest\modules\test_Login.py::TestLogin::test_LoginByEmail
```
> ℹ️ [!NOTE]
> 
> 1. If we not specify the scope in fixture function or module will run each time
> 2. If we want to run particular code from fixture after test function then add `yield` Keyword