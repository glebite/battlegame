"""
test_server.py
"""
import pytest
import requests

@pytest.mark.test_id(1)
def test_status():
    """ test_status """
    response = requests.get('http://127.0.0.1:5150/status')
    assert response.status_code == 200
