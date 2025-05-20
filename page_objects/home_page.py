from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class HomePage(BasePage):
    TITLE_TEXT = "Des déplacements sûrs et confortables"

    TRANSPORT_CARD = (By.XPATH, "//div[contains(text(),'TRANSPORT')]/../..")
    PELERINAGE_CARD = (By.XPATH, "//div[contains(text(),'PÈLERINAGE')]/../..")

    TRANSPORT_BUTTON = (By.XPATH, "//div[contains(text(),'TRANSPORT')]/../..//button")
    PELERINAGE_BUTTON = (By.XPATH, "//div[contains(text(),'PÈLERINAGE')]/../..//button")

    def verify_homepage_loaded(self):
        assert self.TITLE_TEXT in self.driver.page_source

    def is_transport_section_visible(self):
        return self.is_element_visible(*self.TRANSPORT_CARD)

    def is_pelerinage_section_visible(self):
        return self.is_element_visible(*self.PELERINAGE_CARD)

    def click_transport_commencer(self):
        self.click(*self.TRANSPORT_BUTTON)

    def click_pelerinage_commencer(self):
        self.click(*self.PELERINAGE_BUTTON)
