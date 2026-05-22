import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def capture_screenshot():
    # Setup chrome options
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Initialize WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Construct absolute path to the HTML report
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        report_path = os.path.join(current_dir, "reports", "report.html")
        file_url = f"file:///{report_path.replace(os.sep, '/')}"

        print(f"Opening report: {file_url}")
        driver.get(file_url)

        # Wait a moment for rendering
        time.sleep(3)

        # Ensure screenshots directory exists
        screenshots_dir = os.path.join(current_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshots_dir, "pytest_report.png")
        driver.save_screenshot(screenshot_path)
        print(f"Report screenshot successfully captured and saved to: {screenshot_path}")

    finally:
        driver.quit()

if __name__ == "__main__":
    capture_screenshot()
