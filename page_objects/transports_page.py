from seleniumbase import BaseCase

class TransportsPage:
    LOCATION_VEHICULES_CARD = '(//button[.//span[contains(text(), "Continuer")]])[1]' # ou ajuster si besoin
    RESERVER_BUS_CARD = '(//button[.//span[contains(text(), "Continuer")]])[2]'
    TITLE_SECTION = "h2.text-2xl.font-semibold"  # "Choisissez votre formule"
    SUBTITLE = "p.text-lg"

    def verify_section_title(self, sb):
        sb.assert_element(self.TITLE_SECTION)
        title = sb.get_text(self.TITLE_SECTION)
        print(title)
        assert "Machallah Transport" in title


    def click_location_de_vehicules(self, sb):
        sb.assert_element(self.LOCATION_VEHICULES_CARD)
        sb.click(self.LOCATION_VEHICULES_CARD)

    def click_reserver_un_bus(self, sb):
        sb.assert_element(self.RESERVER_BUS_CARD)
        sb.click(self.RESERVER_BUS_CARD)
