from pathlib import Path
from playwright.sync_api import sync_playwright

html_file = Path("index.html").resolve()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(f"file://{html_file}")

    if page.locator("text=Version: 1.0").count() > 0:
        print("Test Passed")
    else:
        print("Test Failed")

    browser.close()