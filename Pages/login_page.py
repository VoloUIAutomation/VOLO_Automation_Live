from selenium.webdriver.common.by import By
from Helpers.helpers_lib import GeneralHelpers
from TestData import testdata

email_field = (By.ID, "dwfrm_login_username")
pass_field = (By.ID, "dwfrm_login_password")
btn_sign_in = (By.XPATH, "//button[@id='login']")


class LoginPage(GeneralHelpers):

    def login(self):
        self.find_and_send_keys(email_field, testdata.username)
        self.find_and_send_keys(pass_field, testdata.password)
        self.find_and_click(btn_sign_in)
