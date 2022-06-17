from selenium.webdriver.common.by import By
from Helpers import helpers
from TestData import test_data
from Helpers.test_logger import logger

mail_fld = (By.ID, "dwfrm_login_username")
password_fld = (By.ID, "dwfrm_login_password")
login_btn = (By.ID, "login")


def login(driver):
    try:
        helpers.find_and_send_keys(driver, mail_fld, test_data.email)
        helpers.find_and_send_keys(driver, password_fld, test_data.password)
        helpers.find_and_click(driver, login_btn)
        logger("User logged in", error=False)
    except Exception as err:
        logger(f"Login failed {err}", error=True)
