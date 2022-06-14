from selenium.webdriver.common.by import By
from Helpers import helpers
from TestData import test_data

myaccoutn_btn = (By.XPATH, "//span[@class='profile-name']//span[@class='greet-customer']")
login_signup_btn = (By.XPATH, "//div[@class='header-top']//li[3]//a[1]")

mail_fld = (By.ID, "dwfrm_login_username")
password_fld = (By.ID, "dwfrm_login_password")
login_btn = (By.ID, "login")

man_btn = (By.ID, "nav_Mens")
any_dress = (By.XPATH, "//div[normalize-space()='Graphic T-Shirts']")
add_to_bag_btn = (By.XPATH, "(//span[@class='add-to-bag-text'][normalize-space()='Add to Bag'])[1]")
choose_size = (By.XPATH, "//span[contains(text(),'XS')])[1]")
bag_icon_btn = (By.ID, "cartTotal")
price = (By.XPATH, "//span[@class='value']")


def get_login(driver):
    helpers.find_and_click(driver, myaccoutn_btn)


def login(driver):
    helpers.find_and_send_keys(driver, mail_fld, test_data.email)
    helpers.find_and_send_keys(driver, password_fld, test_data.password)
    helpers.find_and_click(driver, login_btn)


def search(driver):
    helpers.find_and_send_keys(driver, )
