import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_view_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert b"The Hobbit" in response.data

def test_add_book(client):
    response = client.post('/add', json={"title": "Brave New World", "author": "Aldous Huxley"})
    assert response.status_code == 201
    assert b"Brave New World" in response.data