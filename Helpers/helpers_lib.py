import random
import string
import logging
from time import sleep
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class GeneralHelpers:
    def __init__(self, driver):
        self.driver = driver
        # self.actions = ActionChains(driver)

    def go_to_page(self, url):
        logging.info(f"Navigate to {url}")
        self.driver.get(url)
        self.driver.maximize_window()

    def find_and_click(self, loc, timeout=60):
        elem = self.find(loc, timeout)
        logging.info(f"Click on {loc[1]}")
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=60):
        elem = self.find(loc, timeout)
        logging.info(f"Send '{inp_text}' to {loc[1]}")
        elem.send_keys(inp_text)

    def find(self, loc, timeout=20, should_exist=True, get_text="", get_attribute=""):
        logging.info(f"Search element '{loc[1]}'")
        try:
            elem = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(loc),
                                                             message=f"Element '{loc}' not found!")
        except Exception as e:
            logging.error(e)
            if should_exist:
                raise Exception(e)
            return False
        if get_text:
            logging.info(f"Element text: {elem.text}")
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_all(self, loc, timeout=10):
        logging.info(f"Search elements '{loc[1]}'")
        try:
            elements = WebDriverWait(self.driver, timeout).\
                until(expected_conditions.presence_of_all_elements_located(loc), message=f"Elements '{loc}' not found!")
        except Exception as e:
            logging.error(e)
            return False
        logging.info(f"Found: {len(elements)}")
        return elements

    def wait_element_disappear(self, loc, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(expected_conditions.presence_of_element_located(loc))

    def wait_for_page(self, page="", not_page="", timeout=10):
        if page:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(page))
        elif not_page:
            WebDriverWait(self.driver, timeout).until_not(expected_conditions.url_contains(not_page))

    def hover_element(self, loc):
        logging.info(f"Hover element '{loc[1]}'")
        hover = self.actions.move_to_element(self.find(loc)).pause(0.5)
        hover.perform()

    def wait_for_page_load(self, timeout=30):
        max_time = int(datetime.now().timestamp()) + timeout
        logging.info(". . . Wait for page loading . . .")
        while max_time > int(datetime.now().timestamp()):
            page_state = self.driver.execute_script('return document.readyState;')
            if page_state == 'complete':
                return
            else:
                sleep(1)

    def remake_locator(locator, suffix=""):
        by, loc = locator
        return by, f"{loc}{suffix}"

    def random_string(symbols_count):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=symbols_count))
