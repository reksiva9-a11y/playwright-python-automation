import pytest

@pytest.fixture(scope = "session")
def browser():
    print("open browser")
    yield
    print("close browser")
def test_login(browser):
    print("login")

def test_logout(browser):
    print("logout")
