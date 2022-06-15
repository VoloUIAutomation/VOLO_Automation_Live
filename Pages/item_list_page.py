from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers
from TestData import testdata


class ItemListPage(GeneralHelpers):
    categories = (
        By.XPATH, "//div[contains(@class,'desktopRefinements')]//div[contains(@class,'categoryrefinement')]/h3/span")
    categories_by_type = (
        By.XPATH, f"//li[@class='expandable']/a[text()='{testdata.category}']")
    personalized = (By.XPATH, "//span[text()='Personalized']")
    price_high_to_low = (
        By.XPATH, "//div[@class='selectric-scroll']//li[text()='Price High to Low']")
    first_item = (
        By.XPATH, "//a[@class='name-link']//h2[text()='Snowy Fox Open Collar Cardigan']")
    
    item_price = (By.XPATH, '//input[@class="salesPriceValue"]')
    item_list = (By.XPATH, "//div[@class='product-name']/a")
    first_item =(By.XPATH, "(//div[@class='product-name']/a)[1]")

    def choose_categories(self):
    
        self.find_and_click(self.categories)
        self.find_and_click(self.categories_by_type)
        
    def choose_price_high_to_low(self):
        self.find_and_click(self.personalized)
        self.find_and_click(self.price_high_to_low)
    
    def choose_item(self):
        self.find_and_click(self.first_item)
    
    def get_price_list(self):
        els = self.find_all(self.item_price)
        prices = [el.text for el in els]
        return prices

    def open_first_item(self):
      self.find_and_click(self.first_item)
