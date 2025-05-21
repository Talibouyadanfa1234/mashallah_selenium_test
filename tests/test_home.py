from seleniumbase import BaseCase
from page_objects.home_page import HomePage

BASE_URL = "https://recette-front.machallahtravels.com/accueil"

class TestHome(BaseCase):
    def test_homepage_content(self):
        self.open(BASE_URL)
        page = HomePage()
        page.verify_title_present(self)

    def test_transport_button(self):
        self.open(BASE_URL)
        page = HomePage()

        old_url = self.get_current_url()
        page.click_transport_commencer(self)

        # Option 1 – Attendre que l'URL change
        for _ in range(20):  # max 10 secondes
            self.sleep(0.5)
            new_url = self.get_current_url()
            if new_url != old_url:
                break

        print("Nouvelle URL:", new_url.lower())
        assert "transports" in new_url.lower()


    def test_pelerinage_button(self):
        self.open(BASE_URL)
        page = HomePage()

        old_url = self.get_current_url()
        page.click_pelerinage_commencer(self)

        # Option 1 – Attendre que l'URL change
        for _ in range(20):  # max 10 secondes
            self.sleep(0.5)
            new_url = self.get_current_url()
            if new_url != old_url:
                break

        print("Nouvelle URL:", new_url.lower())
        assert "pelerinage" in new_url.lower()
