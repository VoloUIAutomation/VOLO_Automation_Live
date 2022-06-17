from Helpers.helpers_lib import GeneralHelpers
from Pages.item_list_page import ItemListPage
from Pages.search_bar import SearchBar
from TestData import testdata
"""
1. Login to the app
2. Search any product
3. Sort by price higher to low
4. Check that sorting work correctly
"""


def test_price_ordering(driver, login):
    item_page = ItemListPage(driver)
    search = SearchBar(driver)
    gen_helpers = GeneralHelpers(driver)
    search.search_item(testdata.search_item_keyword)

    item_page.choose_categories()
    item_page.choose_price_high_to_low()
    gen_helpers.wait_for_page_load()
    actual_list = item_page.get_price_list()
    expected_list = sorted(actual_list)
    assert actual_list == expected_list, "Price is not ordered from high to low"

