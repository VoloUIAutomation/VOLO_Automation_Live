import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from helpers import helpers
from testData import test_data

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def open_url(driver):
    helpers.go_to_page(driver, test_data.main_url)