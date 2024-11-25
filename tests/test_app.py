import sys
import os
import pytest

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_is_up(client):
    # Send a GET request to the root endpoint
    response = client.get('/')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200