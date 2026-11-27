import pytest

@pytest.mark.xfail(reason = "konow bug")
def test_payment():
    assert 100 ==200