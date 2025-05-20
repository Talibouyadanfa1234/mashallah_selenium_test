import pytest
from utils.browser import create_driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Navigateur à utiliser : chrome ou firefox")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = create_driver(browser=browser)
    yield driver
    driver.quit()
