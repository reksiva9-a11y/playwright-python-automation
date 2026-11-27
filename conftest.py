import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
@pytest.fixture

def login_data():
    return {
    
        "username" : "admin123",
        "password" :  "admin123"
    }

def baseurl():
    return "https://www.example.com"
