from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers
from TestData import testdata
from selenium.webdriver.common.keys import Keys


class SearchBar(GeneralHelpers):
    search_icon = (
        By.XPATH, "(//button[@aria-label='Search']/span[@class='header-icon-search'])[2]")
    search_input = (
        By.ID, "searchInput")
    bag_icon = (
        By.XPATH, "//button[@aria-label='Minicart Icon']/img[@alt='minicart-icon']")
    view_bag = (
        By.XPATH, "//a[contains(@class,'mini-cart-link-cart')]")
    lnk_see_all = (By.XPATH, "//a[text()='See All']")


    def search_item(self, search_content):
        self.find_and_click(self.search_icon)
        self.find_and_send_keys(self.search_input, search_content)
        self.find_and_click(self.lnk_see_all, 120)
