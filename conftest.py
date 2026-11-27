import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    headless = os.getenv("CI") == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

def login_data():
    return {
    
        "username" : "admin123",
        "password" :  "admin123"
    }

def baseurl():
    return "https://www.example.com"
