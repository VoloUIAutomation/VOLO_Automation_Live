from selenium.webdriver.common.by import By
from Helpers import helpers
from Helpers.test_logger import logger

view_bag_btn = (By.XPATH, "//a[@title='VIEW BAG']")
quantity_plus = (By.XPATH, "//span[@class='qty-icon plus']")
quantity_minus = (By.XPATH, "//span[@class='qty-icon minus']")
total_price = (By.XPATH, "//li[@class='item-total cart-items']/span")
subtotal_price = (By.XPATH, "//tr[@class='subtotal']//child::td[@class='price']")


def view_bag(driver):
    helpers.clickable_elem(driver, view_bag_btn)
    helpers.find_and_click(driver, view_bag_btn)
    logger("Bag is opened", error=False)


def plus_quantity(driver):
    helpers.find_and_click(driver, quantity_plus)
    helpers.visible_elem(driver, quantity_minus)
    logger("Additional item has been added", error=False)


def get_prices(driver):
    final_total_price = helpers.find(driver, total_price, get_text=True)
    final_subtotal_total = helpers.find(driver, subtotal_price, get_text=True)
    logger(f"Prices are {final_total_price} = {final_subtotal_total}", error=False)
    return final_total_price, final_subtotal_total
