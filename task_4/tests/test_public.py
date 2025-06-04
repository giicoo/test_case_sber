from fastapi.testclient import TestClient
from src.main import app
from src.services import get_service
from .mock import MockLinkService

mock_service = MockLinkService()

def override_get_service():
    return mock_service

app.dependency_overrides[get_service] = override_get_service

client = TestClient(app)  


def test_get_redirect():
    response = client.post("/api/v1/links/", json={"original_url": "https://example.com"})
    assert response.status_code == 201
    short_code = response.json()["short_code"]

    response = client.get(f"/{short_code}", follow_redirects=False)
    assert response.status_code == 302
