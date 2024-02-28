# Order test 

---
This will help to order the function 

Free requisite
>[!NOTE]
> 
> 1. Install package `pytest-ordering` 
> 2. Add customize markers if not added in `pytest.ini` file
```python
import pytest

class TestClass:
    @pytest.mark.third
    def test_methodC(self):
        print("Running method C.. ")

    @pytest.mark.fourth
    def test_methodD(self):
        print("Running method D.. ")

    @pytest.mark.fifth
    def test_methodE(self):
        print("Running method E.. ")

    @pytest.mark.first
    def test_methodA(self):
        print("Running method A.. ")

    @pytest.mark.second
    def test_methodB(self):
        print("Running method B.. ")
```
