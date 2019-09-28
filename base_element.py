from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base_page import BasePage


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def __set__(self, value):
        """Sets the text to the value supplied"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        self.driver.find_element_by_name(self.locator).clear()
        self.driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj):
        """Gets the text of the specified object"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element = self.driver.find_element(*self.locator)
        return element.get_attribute("value")

    def get_element(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element = self.driver.find_element(*self.locator)
        return element

    def click(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator))
        element = self.driver.find_element(*self.locator)
        element.click()
        return element


class HomePage(BasePage):
    page_elements = {
        'login_link': (By.NAME, 'Cancel'),
        'username_box': (By.NAME, 'username'),
        'password_box': (By.NAME, 'password'),
        'login_btn': (By.NAME, 'Login'),
        'side_menu': (By.CLASS_NAME, 'btn-secondary'),
        'logout': (By.LINK_TEXT, 'Logout')
    }
    url = "http://autothon-nagarro-frontend-b08.azurewebsites.net/"

    def __init__(self, driver):
        super().__init__(driver)
        for key, value in self.page_elements.items():
            setattr(self, key, BasePageElement(self.driver, value))

    def navigate(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def login(self, username, password):
        self.side_menu.click()
        self.login_link.click()
        self.username_box = username
        self.password_box = password
        self.login_btn.click()

    def verify_logout_exists(self):
        try:
            logout = self.logout.get_element()
            return logout.is_displayed()
        except TimeoutException:
            return False
