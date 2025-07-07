import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_user(client):
    response = client.get('/get-user')
    assert response.status_code == 200
    
    data = response.get_json()
    
    assert data['status'] == 'success'
    assert 'user' in data
    assert data['user']['name'] == 'Kuldeep singh'
    assert data['user']['mobile_number'] == '6367888865'