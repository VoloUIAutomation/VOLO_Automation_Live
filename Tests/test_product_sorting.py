from pages import sign_in, sort_results
from helpers import helpers
from testData import test_data


def test_sorting(driver):
    helpers.go_to_page(driver, test_data.url)
    sign_in.sing_in_account(driver)
    sort_results.search_product(driver)
