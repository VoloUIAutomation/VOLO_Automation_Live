from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers

lbl_account = (By.XPATH, "//div[@class='topbar-navlinks']/span[@class='ir-greet-customer']")
lnk_login = (By.XPATH, "(//a[contains(text(), 'Login/Sign up')])[1]")


class BasePage(GeneralHelpers):

    def click_login(self):
        self.find_and_click(lbl_account)
        self.find_and_click(lnk_login)
        self.wait_for_page('Account-Show')


