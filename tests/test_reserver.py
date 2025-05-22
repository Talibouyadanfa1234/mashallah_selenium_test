from seleniumbase import BaseCase

from page_objects.reserver_bus import ReservationFormPage


class TestReserver(BaseCase):
    def test_title_content(self):
        self.open("https://recette-front.machallahtravels.com"+ "/transports/locations")  # Ou redirige après "commencer"
        page = ReservationFormPage()
        page.verify_title_h2_present(self)

    def test_remplir_formulaire(self):
        self.open("https://recette-front.machallahtravels.com"+ "/transports/locations")  # Ou redirige après "commencer"
        form = ReservationFormPage()
        form.fill_form(self)
