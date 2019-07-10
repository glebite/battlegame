"""
test_server.py

All tests will be in @pytest markup format.

test_status
...
test_last
"""
import pytest
import requests

@pytest.mark.test_id(1)
def test_status():
    """ test_status
    Confirms that the running server will return a 200 status_code
    when a get is performed on it.
    """
    response = requests.get('http://127.0.0.1:5150/status')
    assert response.status_code == 200

@pytest.mark.test_id(10000)
def test_last():
    """ test_last """
    assert True
