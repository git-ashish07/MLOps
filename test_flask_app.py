import pytest
from flask_app import app
import json

@pytest.fixture()
def client():
    return app.test_client()


def test_ping(client):
    result = client.get("/ping")
    assert result.status_code == 200
    assert b"Pinged the server" in result.data


def test_prediction(client):
    test_data = {
        "Gender": "Male",
        "Married": "Yes",
        "ApplicantIncome": 50,
        "LoanAmount": 200000,
        "Credit_History": "Clear Debts"
    }

    result = client.post("/predict", json = test_data)
    assert result.status_code == 200
    assert b"Approved" in result.data