from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers


txt_selected_filters = (By.XPATH, "//ul[@id='searchSelectedFilters']//a")
txt_search_result = (By.XPATH, "//span[contains(text(),'items found')]")
txt_products = (By.XPATH, "//div[@id='products']/article")

btn_add_to_bag = (By.XPATH, "//form[@id='buyBoxForm']//button[@type='submit']")
txt_add_to_bag_modal_desc = (By.XPATH, "//p[@id='modalDescription']")
btn_close_modal_window = (By.XPATH, "//button[@aria-label='Close']")
btn_view_bag = (By.XPATH, "//form/a[@href='/cart']")

chb_shop_by_brand = (By.XPATH, "//span[contains(text(),'Calvin Klein')]")
txt_shop_by_brand_available = (By.XPATH, "//span[contains(text(),'Calvin Klein')]/../span[@aria-label]")

chb_shop_by_price_50 = (By.XPATH, "//span[contains(text(),'$50.00 and Under')]")


class SearchPage(BasePage):

    def get_selected_filters(self):
        filters = self.find_all(txt_selected_filters)
        s_filters = [i.text for i in filters]
        return s_filters

    def get_result_count(self):
        return self.find(txt_search_result, get_text=True).split(" ")[0]

    def click_shop_by__filter(self, name, get_available_count=False):
        count = None
        c_page = self.driver.current_url
        filter_loc = (By.XPATH, f"//span[contains(text(),'{name}')]")
        if get_available_count:
            count = self.find(remake_locator(filter_loc, "/../span[@aria-label]"), get_text=True)
            count = count.replace('(', '').replace(')', '')
        self.find_and_click(filter_loc)
        self.wait_for_page(not_page=c_page)
        self.wait_for_page_load()
        s_filters = self.get_selected_filters()
        assert name in s_filters, f"Filter '{name}' isn't selected. Selected filters: {s_filters}"
        return count

    def click_on_product(self, ind=1):
        item_loc = remake_locator(txt_products, f"[{ind}]")
        item_price_loc = remake_locator(txt_products, f"[{ind}]//span[@itemprop='price']")
        item_price = self.find(item_price_loc, get_attribute="content")
        self.find_and_click(item_loc)
        return float(item_price)

    def add_product_to_favorite(self, ind=1):
        self.find_and_click(remake_locator(txt_products, f"[{ind}]//button[contains(@aria-label,'Favorite')]/span"))

    def click_add_to_bag_button(self):
        self.find_and_click(btn_add_to_bag)
        self.find(txt_add_to_bag_modal_desc)

    def click_view_bag_button(self):
        self.find_and_click(btn_view_bag)
        self.wait_for_page("/cart")

    def click_close_button(self):
        self.find_and_click(btn_close_modal_window)

    # def click_shop_by_price_50(self):
    #     c_page = self.driver.current_url
    #     self.find_and_click(chb_shop_by_price_50)
    #     self.wait_for_page(not_page=c_page)
    #     self.wait_for_page_load()
    #     s_filters = self.selected_filters()
    #     assert '$50.00 and Under' in s_filters
