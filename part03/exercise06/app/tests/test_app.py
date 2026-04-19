def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200

def test_status(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.json['status'] == 'running'
