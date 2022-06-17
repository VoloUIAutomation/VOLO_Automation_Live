from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers
from TestData import testdata


class ItemDetailsPage(GeneralHelpers):
    item_color = (By.XPATH, f"//a[contains(text(),'{testdata.item_color}')]")
    item_size = (By.XPATH, f"//a[@title='{testdata.size[0]}']/\
        span[text()='{testdata.size[1]}']")
    add_quantity = (By.XPATH, "//div[@class='qty-block-increase']/\
        span[@class='increase-qty unselectable']")
    add_to_bag = (By.XPATH, "//button[@id='add-to-cart']")
    product_price = (By.XPATH, "//div[@id='product-content']\
        //span[@class='price-regular']")

    def choose_color(self):
        self.find_and_click(self.item_color)

    def choose_size(self):
        self.find_and_click(self.item_size)

    def increase_quantity(self, total):
        number = 1
        while number < total:
            self.find_and_click(self.add_quantity)
            number += 1

    def get_item_price(self):
        price = self.find(self.product_price, get_text=True)
        price_amount = price.split('$')[1].strip()
        return float(price_amount)

    def click_add_to_bag(self):
        self.find_and_click(self.add_to_bag)
