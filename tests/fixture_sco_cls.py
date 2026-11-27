import pytest

@pytest.fixture(scope = "class")

def browser():
    print("open browser")
    yield
    print("close browser")

class Testlogin:
    def test_login(self, browser):
        print("login")

class Testlogout:
    def test_logout(self, browser):
        print("logout")

   