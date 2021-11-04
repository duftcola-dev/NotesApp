from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_item():
    
    response=client.get("/note/")
    assert response.status_code == 200
  

def test_get_items():
    
    response=client.get()
    assert response.status_code == 200

def test_create_item():
    
    response=client.post()
    assert response.status_code == 201

def test_delete_item():

    response=client.delete()
    assert response.status_code == 204