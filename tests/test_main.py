from fastapi.testclient import TestClient
from main import app
from datetime import datetime
import pytest

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Fly.io demo app"}

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_time_endpoint():
    response = client.get("/api/time")
    assert response.status_code == 200
    # Check if the returned time string is in ISO format
    time_str = response.json()["time"]
    try:
        datetime.fromisoformat(time_str)
    except ValueError:
        pytest.fail(f"Time string '{time_str}' is not in ISO format") 