import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# Test home page
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

# Test valid form submission
def test_form_submission(client):
    response = client.post('/submit', data={
        "name": "Test User",
        "usn": "1MS23CS001",
        "title": "Demo",
        "link": "https://github.com/test"
    })
    assert response.status_code in [200, 302]

# Test empty form fields
def test_missing_fields(client):
    response = client.post('/submit', data={
        "name": "",
        "usn": "",
        "title": "",
        "link": ""
    })
    assert response.status_code in [200, 302, 400]

# Test invalid route
def test_invalid_route(client):
    response = client.get('/randompage')
    assert response.status_code == 404