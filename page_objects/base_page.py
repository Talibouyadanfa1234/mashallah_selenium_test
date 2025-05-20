from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            self.driver.find_element(by, value).click()
        except TimeoutException:
            raise Exception(f"Element not clickable: {by} = {value}")

    def wait_for_element(self, by, value):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            raise Exception(f"Element not found: {by} = {value}")

    def is_element_visible(self, by, value):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            return False

    def get_text(self, by, value):
        try:
            return self.find(by, value).text
        except NoSuchElementException:
            return None

    def type(self, by, value, text):
        try:
            field = self.find(by, value)
            field.clear()
            field.send_keys(text)
        except NoSuchElementException:
            raise Exception(f"Unable to type in element: {by} = {value}")
