from seleniumbase import BaseCase

class HomePage:
    TITLE_TEXT = "Des déplacements sûrs\net confortables"
    TRANSPORT_BTN = "span.mat-mdc-button-touch-target"
    PELERINAGE_BTN = "span.mat-mdc-button-touch-target"

    TITRE_H1 = "p"

    def verify_title_present(self, sb):
        sb.assert_element(self.TITRE_H1)
        texte = sb.get_text(self.TITRE_H1)
        print(texte)
        assert self.TITLE_TEXT in texte


    def click_transport_commencer(self, sb):
        sb.wait_for_element_visible(self.TRANSPORT_BTN, timeout=10)
        sb.click(self.TRANSPORT_BTN)
        sb.sleep(1)  # courte pause pour attendre l'effet du clic

    def click_pelerinage_commencer(self, sb):
        sb.wait_for_element_visible(self.PELERINAGE_BTN , timeout=10)
        buttons = sb.find_elements("css selector", self.PELERINAGE_BTN )
        if len(buttons) >= 2:
            buttons[1].click()  # clic sur le 2e bouton (index 1)
        else:
            raise Exception("Bouton 'Pèlerinage -> Commencer' non trouvé.")
        sb.sleep(1)

