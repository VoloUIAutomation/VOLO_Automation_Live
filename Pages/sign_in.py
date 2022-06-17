from selenium.webdriver.common.by import By
from helpers import helpers
from testData import test_data
from helpers.test_logger import logger
import time


my_account = (By.XPATH, "//div[@class = 'topbar-navlinks']/span[@class= 'ir-greet-customer']")
select_login = (By.XPATH, "//*[@class='topbar-navlinks']//*[@id = 'greeting-menu']/*[@class = 'user-links']/ul/*[3]/a")
email_field = (By.XPATH, "//input[@id='dwfrm_login_username']")
pass_field = (By.XPATH, "//input[@id='dwfrm_login_password']")
signin_button = (By.XPATH, "//*[@id='login']")

# Sign in
def sing_in_account(driver):
    helpers.find_and_click(driver, my_account)
    time.sleep(3)
    helpers.find_and_click(driver, select_login)
    time.sleep(5)
    helpers.find_and_send_keys(driver, email_field, test_data.email)
    helpers.find_and_send_keys(driver, pass_field, test_data.password)
    helpers.find_and_click(driver, signin_button)
    logger("User Signed in Successfully")
