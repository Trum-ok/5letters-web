import random

from fastapi.testclient import TestClient


def test_index(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_random_word_deterministic(client: TestClient, monkeypatch):
    monkeypatch.setattr(random, "choice", lambda seq: "banan")
    response = client.get("/get_random_word")
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert data["word"] == "BANAN"
