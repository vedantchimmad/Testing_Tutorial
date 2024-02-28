# Grouping

---
This decorator will help to group the set of function based on name

>[!NOTE]
> 
> 1. Add the markers in pytest.ini file if not added
> 2. And we can control this in run time
```commandline
pytest -v -s -m "sanity" day27\test_Grouping.py
pytest -v -s -m "not sanity" day27\test_Grouping.py
```
```python
import pytest

class TestClass:

    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is login by email........")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is login by facebook........")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login by twitter........")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signupByEmail(self):
        print("This is signup by email test")
        assert True == True

    @pytest.mark.regression
    def test_signupByFacebook(self):
        print("This is signup by facebook test")
        assert True == True

    @pytest.mark.regression
    def test_signupbytwitter(self):
        print("This is signup by twitter test")
        assert True == True

```