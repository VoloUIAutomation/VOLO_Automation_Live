from selenium.webdriver.common.by import By
from Helpers import helpers
from Helpers.test_logger import logger

my_acc_button = (By.XPATH, "//span[@class='profile-name']//span[@class='greet-customer']")
log_in_button = (By.XPATH, "//a[contains(text(), 'Login/Sign up')]")


def go_to_login(driver):
    helpers.find_and_click(driver, my_acc_button)
    helpers.find_and_click(driver, log_in_button)


def get_category(driver, link: str, category: str):
    helpers.hover_element(driver, (By.ID, f"{link}"))
    helpers.find_and_click(driver, (By.XPATH, f"//li[@id='{category}']/a"))
    logger("Category has been chosen", error=False)

