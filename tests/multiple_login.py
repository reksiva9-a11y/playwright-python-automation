import pytest

@pytest.mark.parametrize("username, password", [("user1", "pass1"), ("user2", "pass2"), ("user3", "pass3")])

def test_multple_loin(username,password):
     assert username != ""
     assert password != ""

    