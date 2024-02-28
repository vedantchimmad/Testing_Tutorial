import pytest

class TestClass:
    def test_LoginByEmail(self):
        print("This is login by email..")
        assert 1 == 1

    def test_LoginByFacebook(self):
        print("This is login by facebook........")
        assert 1 == 1

    def test_LoginByTwitter(self):
        print("This is login by twitter........")
        assert 1 == 1

    @pytest.mark.skip
    def test_signupByEmail(self):
        print("This is signup by email test")
        assert True == True

    @pytest.mark.skip
    def test_signupByFacebook(self):
        print("This is signup by facebook test")
        assert True == True

    @pytest.mark.skip
    def test_signupbytwitter(self):
         print("This is signup by twitter test")
         assert True == True
