import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime, timedelta

client = TestClient(app)

def test_create_payment_request_api():
    payload = {
        "requester_id": 1,
        "amount_in_cents": 999,
        "currency": "EUR",
        "valid_duration_in_hours": 24
    }
    response = client.post("/payment_requests", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["requester_id"] == 1
    assert body["status"] == "PENDING"
    assert body["amount_in_cents"] == 999
    assert body["currency"] == "EUR"
    assert body["valid_till"] > datetime.now() + timedelta(hours=23)

def test_create_payment_attempt_api():
    request_payload = {
        "requester_id": 1,
        "amount_in_cents": 2500,
        "currency": "USD",
        "valid_duration_in_hours": 24
    }
    request_response = client.post("/payment_requests", json=request_payload)
    request_id = request_response.json()["id"]

    attempt_payload = {
        "payer_id": 2,
        "requester_id": request_id,
        "amount_in_cents": 2500,
        "currency": "USD"
    }
    res = client.post("/payment_attempts", json=attempt_payload)
    assert res.status_code == 200
    body = res.json()
    assert body["payer_id"] == 2
    assert body["status"] == "COMPLETED"

def test_create_payment_attempt_api_not_found():
    attempt_payload = {
        "payer_id": 1,
        "requester_id": 999, # doesn't exist
        "amount_in_cents": 2500,
        "currency": "USD"
    }
    res = client.post("/payment_attempts", json=attempt_payload)
    assert res.status_code == 404
