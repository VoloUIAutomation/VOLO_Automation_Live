from selenium.webdriver.common.by import By
from Helpers import helpers
from TestData import test_data


search_icon = (By.XPATH, "//*[@id='header']/div[3]/div[6]/div[1]/button/span")
shearch_field = (By.XPATH, "//*[@id='searchInput']")
see_all = (By.XPATH, "//*[@id='suggestions']/div[2]/div[1]/span[2]/a")
sort_dropdown = (By.XPATH, "//*[@id='secondary']/div/div[2]/form/fieldset/div/div/div[2]/span")
hige_to_low = (By.XPATH, "//*[@id='secondary']/div/div[2]/form/fieldset/div/div/div[3]/div/ul/li[5]")
result_prices = (By.XPATH, "//div[@class='total-price']/span[@class = 'price-regular']")

# function sorting
def search_product(driver):
    price_list = []
    helpers.find_and_click(driver,search_icon)
    helpers.find_and_click(driver, see_all)
    helpers.find_and_select_element(driver, sort_dropdown, value= 'Price High to Low')
    results = helpers.find_all(driver, result_prices, gettext = True)
    price_list.append(results)


