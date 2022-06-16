from Pages import login_page, home_page, category_items, shopping_bag_page
from TestData.test_data import header_menu_lnks, mens_clothing, graphic_t_shirts, t_shirt_color, sizes


def test_order_two_items(driver, open_url):
    home_page.go_to_login(driver)
    login_page.login(driver)

    home_page.get_category(driver, header_menu_lnks[1], mens_clothing[4])
    category_items.order_item(driver, graphic_t_shirts["Canadian Summer"],
                              t_shirt_color["Canadian Summer"][1], sizes["XL"])

    shopping_bag_page.view_bag(driver)
    shopping_bag_page.plus_quantity(driver)
    total_calc = shopping_bag_page.get_prices(driver)
    assert total_calc[0] == total_calc[1], "Prices are different"



