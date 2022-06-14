from selenium.webdriver.common.by import By
from Helpers import helpers
from TestData import test_data


my_account = (By.XPATH, "//*[@id='header']/div[2]/div/span[1]/span/span[1]")
login_button = (By.XPATH, "//*[@id='greeting-menu']/div[1]/ul/li[3]/a")
email_field = (By.XPATH, "//*[@id='dwfrm_login_username']")
pass_field = (By.XPATH, "//*[@id='dwfrm_login_password']")
signin_button = (By.XPATH, "//*[@id='login']")

# Sign in
def sing_in(driver):
    helpers.find_and_click(driver, my_account)
    helpers.find_and_click(driver, login_button)
    helpers.find_and_send_keys(driver, email_field, test_data.email)
    helpers.find_and_send_keys(driver, pass_field, test_data.password)
    helpers.find_and_click(driver, signin_button)
