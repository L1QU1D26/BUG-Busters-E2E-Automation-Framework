import pytest
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def setup():

    driver = get_driver()

    driver.maximize_window()

    driver.get("https://shop.qaautomationlabs.com/index.php?route=common/home")

    yield driver

    driver.quit()