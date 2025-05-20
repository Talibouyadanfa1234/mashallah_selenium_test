from page_objects.home_page import HomePage
from config import BASE_URL


def test_homepage_content(driver):
    homepage = HomePage(driver)
    homepage.open(BASE_URL)

    homepage.verify_homepage_loaded()
    assert homepage.is_transport_section_visible()
    assert homepage.is_pelerinage_section_visible()

def test_transport_button(driver):
    homepage = HomePage(driver)
    homepage.open(BASE_URL)

    homepage.click_transport_commencer()
    assert "transport" in driver.current_url.lower()

def test_pelerinage_button(driver):
    homepage = HomePage(driver)
    homepage.open(BASE_URL)

    homepage.click_pelerinage_commencer()
    assert "pelerinage" in driver.current_url.lower()
