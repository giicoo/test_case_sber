from fastapi.testclient import TestClient
from src.main import app
from src.services import get_service
from .mock import MockLinkService

mock_service = MockLinkService()

def override_get_service():
    return mock_service

app.dependency_overrides[get_service] = override_get_service

client = TestClient(app)  


def test_health():
    response = client.get("/api/v1/links/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_link():
    response = client.post("/api/v1/links/", json={"original_url": "https://example.com"})
    assert response.status_code == 201
    assert response.json()["short_code"] == "mock123"


def test_get_link():
    response = client.get("/api/v1/links/mock123")
    assert response.status_code == 200
    assert response.json()["original_url"] == "https://example.com"

def test_delete_link():
    response = client.delete("/api/v1/links/mock123")
    assert response.status_code==204
