from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers
from TestData import testdata
import time


class CartPage(GeneralHelpers):
    total_price = (
        By.XPATH, "//tr[@class='ordertot']//td[@class='price']//span")
    item_count = (
        By.XPATH, "//div[@class='minicartTotal']//span[@id='itemcount']")
    btn_view_bag = (By.XPATH, "//a[text()='VIEW BAG']")
    btn_remove = (By.XPATH, "//button[@value='Remove']/span")
    empty_bag_message = (By.XPATH, "//div[@id='primary']//span")

    def get_cart_items(self):
        item_count = self.find(self.item_count, get_text=True)
        return item_count

    def click_view_cart(self):
        self.wait_element_appear(self.btn_view_bag)
        self.find_and_click(self.btn_view_bag)

    def get_cart_total_price(self):
        self.wait_element_appear(self.btn_view_bag)
        self.find_and_click(self.btn_view_bag)
        self.wait_for_page('Cart-Show')
        total_price = self.find(self.total_price, get_text=True)
        total_price_amount = total_price.split('$')[1].strip()
        return float(total_price_amount)

    def remove_items(self):
        self.find_and_click(self.btn_remove)
        self.wait_element_appear(self.empty_bag_message)

    def get_empty_bag_message(self):
        message = self.find(self.empty_bag_message, get_text=True)
        return message
