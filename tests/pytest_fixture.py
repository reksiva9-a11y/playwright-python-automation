import pytest

@pytest.fixture

def browser():
    print("browser opened")
    yield
    print("browser closed")

def test_login(browser):
    print("exdcuting login")

