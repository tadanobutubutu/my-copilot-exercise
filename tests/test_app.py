from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert "Chess Club" in response.json()

def test_signup_success():
    response = client.post("/activities/Basketball Team/signup?email=new@example.edu")
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up new@example.edu for Basketball Team"

def test_signup_already_registered():
    client.post("/activities/Chess Club/signup?email=test@example.edu")
    response = client.post("/activities/Chess Club/signup?email=test@example.edu")
    assert response.status_code == 400
