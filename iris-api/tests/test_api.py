from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_valid():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200

    body = response.json()
    assert body["label"] == "setosa"
    assert 0.0 <= body["confidence"] <= 1.0


def test_predict_malformed():
    payload = {"sepal_length": "not a number", "sepal_width": 3.5}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422