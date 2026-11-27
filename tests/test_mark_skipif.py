import pytest
browser = "Firefox"
@pytest.mark.skipif(browser == "Firefox", reason =" feature not supportd")
def test_payment():
    assert 1 == 1

