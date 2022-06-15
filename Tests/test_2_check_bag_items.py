
from Pages.item_list_page import ItemListPage
from Pages.search_bar import SearchBar
from Pages.item_details_page import ItemDetailsPage
from Pages.cart_page import CartPage
from TestData import testdata
import time

def test(driver, login, logger, item_count=3):
    item_page = ItemListPage(driver)
    search = SearchBar(driver)
    item_details = ItemDetailsPage(driver)
    cart = CartPage(driver)

    search.search_item(testdata.search_item_keyword)
    time.sleep(3)
    item_page.open_first_item()
    item_details.choose_color()
    item_details.choose_size()
    item_details.add_quantity(item_count)
    expected_total = item_details.get_item_price()*item_count
    actual_total = cart.get_cart_total_price()
    actual_items = cart.get_cart_items()

    assert expected_total == actual_total, "Total Price of cart is incorrect"
    assert actual_items == item_count, "Cart Items is incorrect"
