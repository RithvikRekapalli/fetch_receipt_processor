from app.main import app
from fastapi.testclient import TestClient
import pytest, uuid, json

client = TestClient(app)

def load_example():
    return {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
            {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00"},
        ],
        "total": "24.25"
    }

def test_happy_path():
    # 1) process
    resp = client.post("/receipts/process", json=load_example())
    assert resp.status_code == 201
    rid = resp.json()["id"]
    assert uuid.UUID(rid)

    # 2) get points
    resp2 = client.get(f"/receipts/{rid}/points")
    assert resp2.status_code == 200
    assert resp2.json()["points"] > 0

def test_not_found():
    fake_id = str(uuid.uuid4())
    resp = client.get(f"/receipts/{fake_id}/points")
    assert resp.status_code == 404

def test_validation_error():
    bad = load_example()
    bad["total"] = "24"         # missing cents → schema should reject
    resp = client.post("/receipts/process", json=bad)
    assert resp.status_code == 422   # Unprocessable Entity


def load_example():
    """Return a minimal valid receipt dict that we can patch."""
    return {
        "retailer": "Test",
        "purchaseDate": "2025-05-26",
        "purchaseTime": "14:30",
        "items": [
            {"shortDescription": "Water", "price": "1.00"}
        ],
        "total": "1.00"
    }

# ▸▸ Negative-schema tests  ◂◂
@pytest.mark.parametrize("patch", [
    {"purchaseDate": "2025-13-01"},  # invalid month
    {"purchaseTime": "25:00"},       # invalid hour
    {"items": [{"shortDescription": "x", "price": "9.9"}]},  # bad price format
])
def test_invalid_schema(patch):
    data = load_example()
    data.update(patch)               # overwrite the field with bad data
    resp = client.post("/receipts/process", json=data)
    assert resp.status_code == 422   # FastAPI/Pydantic should reject it
