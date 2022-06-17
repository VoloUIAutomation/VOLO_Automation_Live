from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.test_logger import logger
from selenium.webdriver.support import expected_conditions as ec


def go_to_page(driver, url, new_window=False):
    logger(f"{url} page is opened")
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


def wait_element_disappear(driver, loc, timeout=10):
    WebDriverWait(driver, timeout).until_not(ec.presence_of_element_located(loc))


def find_elements(driver, loc, timeout=20, get_text=False, get_attribute=False):
    try:
        elems = WebDriverWait(driver, timeout).until(
            ec.presence_of_all_elements_located(loc),
            message=f"Elements '{loc}' not found!")
    except Exception as e:
        logger(e, error=True)
        return False
    if get_text:
        all_text = [i.text for i in elems if i.is_displayed()]
        return all_text
    elif get_attribute:
        all_attr = [i.get_attribute(get_attribute) for i in elems]
        return all_attr
    return elems
