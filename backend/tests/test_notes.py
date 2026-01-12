from fastapi.testclient import TestClient
from app.main import app
import pytest

# Fixture für die Tests
@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()


def test_create_and_read_note(client):
    payload = {"title": "Test", "content": "Hello"}
    res = client.post("/notes", json=payload)
    assert res.status_code == 200

    notes = client.get("/notes").json()
    assert len(notes) >= 1
