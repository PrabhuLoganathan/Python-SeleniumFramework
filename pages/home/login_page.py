# from selenium import webdriver
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
import logging


class LoginPage(SeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_input = "user_email"
    _pwd_input = "user_password"
    _login_btn = "commit"

    def click_login_link(self):
        # self.get_login_link().click()
        self.element_click(self._login_link, locator_type="linktext")

    def enter_email(self, email):
        # self.get_email_input().send_keys(email)
        self.element_send_keys(email, self._email_input)

    def enter_pwd(self, pwd):
        # self.get_pwd_input().send_keys(pwd)
        self.element_send_keys(pwd, self._pwd_input)

    def click_login_btn(self):
        # self.get_login_btn().click()
        self.element_click(self._login_btn, locator_type="name")

    def login(self, username='', pwd=''):
        self.click_login_link()
        self.enter_email(username)
        self.enter_pwd(pwd)
        self.click_login_btn()

    def verify_login_success(self):
        result = self.is_element_present(".//div[@id='navbar']//span[text()='Test User']",
                                         by_type="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present("//div[contains(text(),'Invalid email or password')]",
                                         by_type="xpath")
        return result