from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers
from TestData import testdata


class CartPage(GeneralHelpers):
    total_price = (By.XPATH, "//div[@id='mini-cart']//span[@class='price-total']")
    item_count = (By.ID, "itemcount")

    def get_cart_items(self):
        item_count = self.find(self.item_count, get_text=True)
        return int(item_count)

    def get_cart_total_price(self):
        total_price = self.find(self.total_price, get_text=True)
        total_price_amount = total_price.split('$')[1].strip()
        return total_price_amount
