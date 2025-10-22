import pytest
from src.utils.driver_setup import get_driver

@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    #driver.get("https://ffpsmart.factfinderspro.com")
    driver.get("http://localhost:5173")  # comment/uncomment as needed
    yield driver
    driver.quit()

