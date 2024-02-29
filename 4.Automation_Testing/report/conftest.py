import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        serv_obj = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("C:\\Drivers\\geckodriver-v0.29.1-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    return driver

def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)