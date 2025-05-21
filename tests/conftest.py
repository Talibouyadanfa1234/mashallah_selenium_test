import pytest
from seleniumbase import BaseCase

@pytest.fixture
def sb(request):
    # Paramètre navigateur via ligne de commande SeleniumBase ou pytest
    # Ici on crée une instance BaseCase
    base_case = BaseCase()
    yield base_case
    base_case.quit()
