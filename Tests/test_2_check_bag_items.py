
from pytest import console_main
from Pages.item_list_page import ItemListPage
from Pages.search_bar import SearchBar
from Helpers.helpers_lib import GeneralHelpers
from Pages.item_details_page import ItemDetailsPage
from Pages.cart_page import CartPage
from TestData import testdata
import time

"""
1. Login to the app
2. Search any product
3. Open first item
4. Add some number of the same item  to the bag
5. Check Total price in bag is correct
"""


def test(driver, login, item_count=3):
    item_page = ItemListPage(driver)
    search = SearchBar(driver)
    item_details = ItemDetailsPage(driver)
    cart = CartPage(driver)
    gen_helpers = GeneralHelpers(driver)
    search.search_item(testdata.search_item_keyword)
    gen_helpers.wait_for_page_load()
    item_page.open_first_item()
    item_details.choose_size()
    item_details.increase_quantity(item_count)
    item_details.click_add_to_bag()
    expected_total = item_details.get_item_price()*item_count
    actual_total = cart.get_cart_total_price()
    cart.remove_items()
    assert expected_total == actual_total, "Total Price of cart is incorrect"
