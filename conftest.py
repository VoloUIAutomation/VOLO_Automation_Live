import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Helpers.helpers_lib import GeneralHelpers
from Pages.base_page import BasePage
import logging
from TestData import testdata

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    general = GeneralHelpers(driver)
    base = BasePage(driver)
    login = LoginPage(driver)

    general.go_to_page(testdata.home_url)
    base.click_login()
    login.login()




