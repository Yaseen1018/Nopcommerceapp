from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver= webdriver.Chrome()
    elif browser == 'Ie':
        driver= webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")


#pytest html Report

def pytest_configure(config):
    config._metadata['project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['QA'] = 'Yaseen'

#it is hook for delete/modify in to Html reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)
