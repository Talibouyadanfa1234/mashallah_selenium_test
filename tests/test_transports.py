from seleniumbase import BaseCase

from page_objects.transports_page import TransportsPage

class TestTransports(BaseCase):
    # ...

    def test_transport_options(self):
        self.open("https://recette-front.machallahtravels.com/transports")
        page = TransportsPage()

        page.verify_section_title(self)


        # Tester l'action sur "Location de véhicules"
        page.click_location_de_vehicules(self)
        self.sleep(1)
        self.assert_true("location" in self.get_current_url().lower() and self.get_current_url() != "https://recette-front.machallahtravels.com/transports")
        print(self.get_current_url().lower())
        self.go_back()

        # Tester l'action sur "Réserver un bus"
        page.click_reserver_un_bus(self)
        self.sleep(1)
        print(self.get_current_url().lower())
        self.assert_true("reservation" in self.get_current_url().lower() and self.get_current_url() != "https://recette-front.machallahtravels.com/transports")
