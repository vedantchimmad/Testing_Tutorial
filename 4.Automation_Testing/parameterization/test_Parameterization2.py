import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin","admin123"),
                              ("adm","admin123"),
                              ("Admin","adm"),
                              ("adm","adm")
                              ]
                             )
    def test_Login(self,user,pwd):
        self.serv_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "txtUsername").send_keys(user)
        self.driver.find_element(By.ID, "txtPassword").send_keys(pwd)
        self.driver.find_element(By.ID, "btnLogin").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False


