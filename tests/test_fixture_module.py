import pytest

@pytest.fixture(scope = "module")

def database():
    print("db connected")
    yield
    print("db disconnected")

def test_create_user(database):
    print("user created")

def test_update_user(database):
    print("user updated")

def test_delete_user(database):
    print("user deleted")
