import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from Helpers import helpers
from TestData import test_data


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()


@pytest.fixture()
def open_url(driver):
    helpers.go_to_page(driver, test_data.url)

