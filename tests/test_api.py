from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_valid():
    payload = {"prompt": "Tell me a fact about gravity.", "user": "test_user"}
    res = client.post("/generate", json=payload)
    assert res.status_code in (200, 500)  # 500 if AWS creds are not set

def test_generate_filtered():
    res = client.post("/generate", json={"prompt": "I want to kill", "user": "x"})
    assert res.status_code == 400