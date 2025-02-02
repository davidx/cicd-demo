import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient
from main import app
from datetime import datetime
import pytest

# def test_health_endpoint():
#     response = client.get("/health")
#     assert response.status_code == 200
#     assert response.json() == {"status": "ok"}

