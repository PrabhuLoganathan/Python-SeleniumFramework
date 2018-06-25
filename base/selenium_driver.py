from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type + " not supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element found")
        except:
            print("Element not found")
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print("Clicked on element with locator " + locator + " locator type" + locator_type)
        except:
            print("Cannot click on the element with locator " + locator + " locator type" + locator_type")
            print_stack()

    def is_element_present(self, locator, by_type):
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            elements_list = self.driver.find_elements(by_type, locator)
            if len(elements_list) > 0:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, "stopFilter_stops-0")))
            print("Element appeared on the page")
        except:
            print("Element not appeared on the page")
            print_stack()
        return False