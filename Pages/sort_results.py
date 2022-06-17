from selenium.webdriver.common.by import By
from helpers import helpers
from testData import test_data
import time
from helpers.test_logger import logger


search_icon = (By.XPATH, "//div[@class='header-bottom']//div[6]/*[@class = 'menu-search ']/button/span") #"//*[@id='header']/div[3]/div[6]/div[1]/button/span"
search_field = (By.XPATH, "//*[@id='searchInput']")
see_all = (By.XPATH, "//*[@id='suggestions']//*[@class='suggestedproducts']/*[@class='suggestedheader']/*[@class='allsuggestedproducts']/a")
sort_dropdown = (By.XPATH, "//*[@id='secondary']//*[@class='label']")
hige_to_low = (By.XPATH, "//li[text()='Price High to Low']")
result_prices = (By.XPATH, "//div[@class='total-price']/span[@class = 'price-regular']")


# function sorting
def search_product(driver):
    logger("Search products run started")
    price_list = []
    helpers.find_and_click(driver,search_icon)
    helpers.find_and_send_keys(driver, search_field, test_data.search_text)
    helpers.find_and_click(driver, see_all)
    helpers.find_and_click(driver, sort_dropdown)
    helpers.find_and_click(driver, hige_to_low)
    time.sleep(6)
    results = helpers.find_elements(driver, result_prices, get_text=True)
    for item in results:
        price = item.strip('$').strip('USD')
        price_list.append(float(price))

    flag = 0
    i = 1
    while i < len(price_list):
        if (price_list[i] > price_list[i - 1]):
            flag = 1
        i += 1

    if flag:
        logger("No,sorting doesn't work!!!!")
    else:
       logger("Higher to Low sorting works correctly")
