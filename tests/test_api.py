import pytest
from app import api

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    with api.app.test_client() as client:
        yield client

def test_shorten_url(client):
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert "short_code" in data
    assert "short_url" in data

def test_shorten_url_invalid(client):
    response = client.post('/api/shorten', json={"url": "invalid-url"})
    assert response.status_code == 400

def test_redirect(client):
    # First, shorten a URL
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    code = response.get_json()["short_code"]
    # Then, try to redirect
    response = client.get(f'/{code}', follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["Location"] == "https://example.com"

def test_redirect_not_found(client):
    response = client.get('/abcdef', follow_redirects=False)
    assert response.status_code == 404

def test_stats(client):
    # Shorten a URL
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    code = response.get_json()["short_code"]
    # Get stats
    response = client.get(f'/api/stats/{code}')
    assert response.status_code == 200
    data = response.get_json()
    assert data["original_url"] == "https://example.com"
    assert data["short_code"] == code
    assert "clicks" in data