import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr("app.words", ["apple", "banana"], raising=True)
    return TestClient(app)
