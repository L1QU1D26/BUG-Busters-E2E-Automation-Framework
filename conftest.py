import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    from selenium.webdriver.chrome.options import Options
    options = Options()
    is_headless = os.getenv("HEADLESS") == "true" or os.getenv("GITHUB_ACTIONS") == "true"
    if is_headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )
    if not is_headless:
        driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.fixturenames:
                web_driver = item.funcargs.get("driver")
                if web_driver:
                    screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
                    os.makedirs(screenshots_dir, exist_ok=True)
                    
                    screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
                    web_driver.save_screenshot(screenshot_path)
                    print(f"\nScreenshot saved to: {screenshot_path}")
                    
                    try:
                        import allure
                        allure.attach.file(
                            screenshot_path,
                            name="failure-screenshot",
                            attachment_type=allure.attachment_type.PNG
                        )
                    except ImportError:
                        pass
        except Exception as e:
            print(f"Failed to capture failure screenshot: {e}")