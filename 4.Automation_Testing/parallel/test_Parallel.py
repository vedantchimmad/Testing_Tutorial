import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()


    def test_login_edge(self):
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_firefox(self):
        from selenium.webdriver.firefox.service import Service
        self.serv_obj = Service("C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
        self.driver = webdriver.Firefox(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

