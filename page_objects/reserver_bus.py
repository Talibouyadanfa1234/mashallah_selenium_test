from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumbase import BaseCase


class ReservationFormPage:
    TITRE_H2 = "h2.text-xl.font-bold"
    TITLE_TEXT = "Informations du véhicule"
    TITRE_P_SUIVANT = "p"
    TITLE_TEXT_SUIVANTE = "Inscrivez-vous dès aujourd'hui"


    def verify_title_h2_present(self, sb):
        sb.assert_element(self.TITRE_H2)
        sb.highlight(self.TITRE_H2)
        texte = sb.get_text(self.TITRE_H2)
        print(texte)
        assert self.TITLE_TEXT in texte



    def fill_form(self, sb):
        # Catégorie
        sb.wait_for_element_visible("div.mat-mdc-form-field-infix", timeout=10)
        fields = sb.find_elements("css selector", "div.mat-mdc-form-field-infix")


        # Sélectionner le 1er champ (par exemple : Catégorie)
        sb.highlight(fields[0])
        fields[0].click()
        sb.wait_for_element_visible("//mat-option//span[contains(text(),'SUV')]", timeout=10)
        sb.click("//mat-option//span[contains(text(),'SUV')]")

        # Sélectionner le 2e champ (par exemple : Modele)
        sb.highlight(fields[1])
        fields[1].click()
        sb.wait_for_element_visible("//mat-option//span[contains(text(),'7 places')]", timeout=10)
        sb.click("//mat-option//span[contains(text(),'7 places')]")

        # Sélectionner le 3e champ (par exemple :Ville de départ)
        sb.highlight(fields[2])
        fields[2].click()
        sb.wait_for_element_visible("//mat-option//span[contains(text(),'nord foire')]", timeout=10)
        sb.click("//mat-option//span[contains(text(),'nord foire')]")

        # Sélectionner le 3e champ (par exemple :Ville de départ)
        sb.highlight(fields[3])
        fields[3].click()
        sb.wait_for_element_visible("//mat-option//span[contains(text(),'nord foire')]", timeout=10)
        sb.click("//mat-option//span[contains(text(),'nord foire')]")

        # Dates
        sb.sleep(0.5)
        sb.type('input[formcontrolname="startDate"]', "21/05/2025")
        sb.wait_for_element_visible("div.mat-mdc-form-field-icon-suffix", timeout=10)
        sb.highlight("div.mat-mdc-form-field-icon-suffix")
        sb.click("div.mat-mdc-form-field-icon-suffix")
        # Exemple pour sélectionner le jour 22 dans le calendrier
        sb.wait_for_element_visible("//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='22']", timeout=10)
        sb.highlight("//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='22']")
        sb.click("//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='22']")


        # Pour endDate
        sb.type('input[formcontrolname="endDate"]', "24/05/2025")
        endDatefields = sb.find_elements("css selector","div.mat-mdc-form-field-icon-suffix")[1]
        sb.highlight(endDatefields)
        endDatefields.click()

        sb.wait_for_element_visible("(//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='23'])[1]", timeout=10)
        sb.highlight("(//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='23'])[1]")
        sb.click("(//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='23'])[1]")


        fields2 = sb.find_elements("css selector", "input.mat-mdc-input-element")
        sb.highlight(fields2[2])
        fields2[2].click()
        fields2[2].send_keys("2")
        sb.sleep(2)
        sb.highlight("//button[contains(text(),'Suivant') and not(@disabled)]")
        sb.click("//button[contains(text(),'Suivant') and not(@disabled)]")
        sb.sleep(2)


        sb.assert_element(self.TITRE_P_SUIVANT)
        sb.highlight(self.TITRE_P_SUIVANT)
        texte = sb.get_text(self.TITRE_P_SUIVANT)
        print(texte)
        #assert self.TITLE_TEXT_SUIVANTE in texte

        sb.wait_for_element_visible("input[formcontrolname='firstName']", timeout=10)
        sb.type("input[formcontrolname='firstName']", "Talibouya")
        sb.type("input[formcontrolname='lastName']", "Danfa")
        sb.type("input[formcontrolname='phone']", "781254954")
        sb.type("input[formcontrolname='registrationNumber']", "1596200102060")
        sb.wait_for_element_visible("div.mat-mdc-form-field-icon-suffix", timeout=10)
        sb.highlight("div.mat-mdc-form-field-icon-suffix")
        sb.click("div.mat-mdc-form-field-icon-suffix")
        # Exemple pour sélectionner le jour 22 dans le calendrier
        sb.wait_for_element_visible("//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='22']", timeout=10)
        sb.highlight("//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='22']")
        sb.click("//span[contains(@class, 'mat-calendar-body-cell-content') and normalize-space()='22']")
        sb.type("input[formcontrolname='email']", "dtalibouya@ept.sn")
        sb.type("input[formcontrolname='address']", "Mbour, Thioce Ouest")
        sb.sleep(2)
        sb.highlight("//button[contains(text(),'Confirmer') and not(@disabled)]")
        sb.click("//button[contains(text(),'Confirmer') and not(@disabled)]")
        sb.sleep(4)
        sb.assert_equal(sb.get_current_url(), "https://recette-front.machallahtravels.com/accueil")




