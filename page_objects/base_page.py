from seleniumbase import BaseCase

class BasePage(BaseCase):

    def open_page(self, url):
        self.open(url)

    def click_element(self, selector):
        self.click(selector)

    def type_text(self, selector, text):
        self.type(selector, text)

    def get_text_of(self, selector):
        return self.get_text(selector)

    def is_visible(self, selector):
        try:
            self.assert_element(selector)
            return True
        except Exception:
            return False
