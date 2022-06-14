import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lib.test_logger import logger

# helpers
def go_to_page(driver, url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}');")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(driver, loc, timeout=10):
    elem = find(driver, loc, timeout)
    elem.click()


def find_and_send_keys(driver, loc, inp_text, timeout=10):
    elem = find(driver, loc, timeout)
    elem.send_keys(inp_text)


def find(driver, loc, timeout=20, should_exist=True, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located(loc),
            message=f"Element '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        if should_exist:
            raise Exception(e)
        return False
    if get_text:
        return elem.text
    elif get_attribute:
        return elem.get_attribute(get_attribute)
    return elem


def find_all(driver, loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_all_elements_located(loc),
            message=f"Elements '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        return False
    return elements


def wait_element_disappear(driver, loc, timeout=10):
    WebDriverWait(driver, timeout).until_not(expected_conditions.presence_of_element_located(loc))


def wait_for_page(driver, page="", not_page="", timeout=10):
    if page:
        WebDriverWait(driver, timeout).until(expected_conditions.url_contains(page))
    elif not_page:
        WebDriverWait(driver, timeout).until_not(expected_conditions.url_contains(not_page))


def switch_window(driver, window_id=0):
    driver.switch_to.window(driver.window_handles[window_id])


def switch_to_alert(driver):
    return driver.switch_to.alert


def random_string(symbols_count):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=symbols_count))


def find_and_select_element(loc, value='', timeout=20):
    elem = find(loc, timeout)
    select = Select(elem)
    if value:
        select.select_by_value(value)
    else:
        selected_options_list = []
        for elem in select.options:
            selected_options_list.append(elem.get_attribute('value'))
        selected_options_list.pop(0)
        elem = random.choice(selected_options_list)
        select.select_by_value(elem)


def scroll_to_element(loc, timeout=20):
    elem = find(loc, timeout)
    actions = ActionChains(driver)
    actions.move_to_element(elem).perform()
