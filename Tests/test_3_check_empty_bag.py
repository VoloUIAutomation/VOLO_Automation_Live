
import imp
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
4. Add item  to the bag
5. Remove item from the bag
5. Check "No Items in Your Bag" message is visible
"""


def test(driver, login, item_count=1):
    item_page = ItemListPage(driver)
    search = SearchBar(driver)
    item_details = ItemDetailsPage(driver)
    cart = CartPage(driver)
    gen_helpers = GeneralHelpers(driver)
    search.search_item(testdata.search_item_keyword)
    item_page.open_first_item()
    item_details.choose_color()
    item_details.choose_size()
    item_details.increase_quantity(item_count)
    item_details.click_add_to_bag()
    cart.click_view_cart()
    cart.remove_items()
    gen_helpers.wait_element_appear()
    assert cart.get_empty_bag_message() == "No Items in Your Bag", "Message is incorrect"
