from Helpers.test_logger import logger

from selenium.webdriver.common.by import By
from Helpers import helpers

add_to_bag_btn = (By.ID, "add-to-cart")


def order_item(driver, cloth_id: str, color_code: str, size: str):
    helpers.find_and_click(driver, (By.XPATH, f"//div[@data-itemid='{cloth_id}']"))
    helpers.find_and_click(driver, (By.XPATH, f"//a[@data-color='{color_code}']"))
    helpers.find_and_click(driver, (By.CSS_SELECTOR, f".selectable>a[title='{size}']"))
    helpers.find_and_click(driver, add_to_bag_btn)
    logger("New item has been added", error=False)
