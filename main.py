# main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_iso_timestamp():
    """Return current timestamp in ISO format."""
    return datetime.now().isoformat()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Render the main page."""
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,  # Required by Jinja2Templates
            "message": "Welcome to the CICD Demo App from David",
            "timestamp": get_iso_timestamp()
        }
    )

@app.get("/health")
async def health():
    """Return service health status with timestamp."""
    return {
        "status": "ok",
        "timestamp": get_iso_timestamp()
    }

@app.get("/api/time")
async def get_time():
    """Return current time in ISO format."""
    return {"time": get_iso_timestamp()}


# Unit tests
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns HTML with expected content."""
    with patch('main.get_iso_timestamp', return_value="2023-01-01T00:00:00"):
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "Welcome to the CICD Demo App from David" in response.text
        assert "2023-01-01T00:00:00" in response.text

def test_health_endpoint():
    """Test the health endpoint returns correct JSON response."""
    with patch('main.get_iso_timestamp', return_value="2023-01-01T00:00:00"):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok", "timestamp": "2023-01-01T00:00:00"}

def test_time_endpoint():
    """Test the time endpoint returns correct JSON response."""
    with patch('main.get_iso_timestamp', return_value="2023-01-01T00:00:00"):
        response = client.get("/api/time")
        assert response.status_code == 200
        assert response.json() == {"time": "2023-01-01T00:00:00"}

# Integration tests
"""
Integration tests to run against a live server.
Example usage: 
    pytest integration_tests.py --server-url=http://localhost:8000

These tests assume the server is already running.
"""

import requests
import pytest
import re

@pytest.fixture
def server_url(request):
    """Get server URL from command line argument."""
    return request.config.getoption("--server-url")

def test_integration_root_endpoint(server_url):
    """Test the root endpoint on live server returns HTML with expected content."""
    response = requests.get(f"{server_url}/")
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]
    assert "Welcome to the CICD Demo App from David" in response.text
    # Check for ISO timestamp format
    assert re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", response.text)

def test_integration_health_endpoint(server_url):
    """Test the health endpoint on live server returns correct JSON response."""
    response = requests.get(f"{server_url}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    # Verify timestamp format
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", data["timestamp"])

def test_integration_time_endpoint(server_url):
    """Test the time endpoint on live server returns correct JSON response."""
    response = requests.get(f"{server_url}/api/time")
    assert response.status_code == 200
    data = response.json()
    # Verify timestamp format
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", data["time"])