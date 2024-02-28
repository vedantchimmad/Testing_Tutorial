# Pytest fixture

---
Pytest fixture is the feature of pytest to run the function before executing the test function 
>[!NOTE]
> 
> Create common module name conftest.py for common pytest fixture function
```python
# conftest.py
import pytest

@pytest.fixture()  # decorator
def setup():
    print("Launching browser...")  # Executes once before every test method
    yield
    print("closing browser..") 
```
To run the common function one time 
```python
import pytest

@pytest.fixture(scope="module")  # decorator
def setup():
    print("Launching browser...")  # Executes once before every test method
    yield
    print("closing browser..") 
```
```python
# test_Login.py
import pytest

class TestLogin:
    def test_LoginByEmail(self,setup):
        print("This is login by email..")
        assert True == True

    def test_LoginByFacebook(self,setup):
        print("This is login by facebook..")
        assert True == True

    def test_LoginByTwitter(self,setup):
        print("This is login by twitte..")
        assert True == True
```