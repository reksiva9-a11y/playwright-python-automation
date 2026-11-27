import pytest

@pytest.fixture(autouse = "True")

def browser():
   print("browser opened")
   yield
   print("browser closed")

def test_login():
   print("login")
   
   
