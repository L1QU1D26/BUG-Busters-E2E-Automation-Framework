import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def capture_demo_screenshots():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshots_dir = os.path.join(current_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        pages = {
            "shop_page.png": "https://shop.qaautomationlabs.com/",
            "login_page.png": "https://shop.qaautomationlabs.com/my-account/",
            "cart_page.png": "https://shop.qaautomationlabs.com/cart/"
        }

        for filename, url in pages.items():
            print(f"Navigating to {url}...")
            driver.get(url)
            time.sleep(4)  # Wait for page load and assets to render
            
            screenshot_path = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(screenshot_path)
            print(f"Captured: {screenshot_path}")

    finally:
        driver.quit()

if __name__ == "__main__":
    capture_demo_screenshots()
