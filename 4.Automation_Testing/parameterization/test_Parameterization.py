import pytest

class TestClass:
    @pytest.mark.parametrize('num1,num2',[(1,1),(3,5),(10,10),(5,20)])
    def test_calculation(self,num1,num2):
        assert num1==num2
