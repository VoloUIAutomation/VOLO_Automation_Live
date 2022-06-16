from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Helpers.test_logger import logger
from selenium.webdriver.common.action_chains import ActionChains


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
        elem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located(loc),
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
        elements = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located(loc),
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


def select_option_drpdwn(driver, loc, value="", index=int, text=""):
    select = Select(find(driver, loc))
    if value:
        return select.select_by_value(value)
    elif index:
        return select.select_by_index(index)
    elif text:
        return select.select_by_visible_text(text)


def hover_element(driver, loc, timeout=10):
    elem = find(driver, loc, timeout)
    actions = ActionChains(driver)
    actions.move_to_element(elem).perform()


def hover_and_click(driver, loc, timeout=10):
    elem = find(driver, loc, timeout)
    actions = ActionChains(driver)
    actions.move_to_element(elem).click()


def clickable_elem(driver, loc, timeout=20):
    elem = WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(loc))
    return elem


def visible_elem(driver, loc, timeout=20):
    elem = WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(loc))
    return elem
