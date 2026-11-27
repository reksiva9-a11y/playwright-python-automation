import pytest

@pytest.mark.skip(reason = "feature not ready")
def test_payment():
    assert payment_status == "success"