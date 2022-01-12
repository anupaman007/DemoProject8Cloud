from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "Firefox":
        driver = webdriver.Firefox(executable_path=r"C:\Users\user\Desktop\Automation Test\geckodriver.exe")
        print("Launching Firefox Browser..................")
    else:
        driver = webdriver.Chrome(executable_path=r"C:\Users\user\Desktop\Automation Test\chromedriver.exe")
        print("Launching Chrome Browser..................")
    return driver


def pytest_addoption(parser):   # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")


# *****************PyTest HTML Report**************************
# It is hook for adding environment  info to HTML Report


def pytest_configure(config):
    config._metadata['Project Name'] = '8Cloud'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester Name'] = 'Anupama'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


