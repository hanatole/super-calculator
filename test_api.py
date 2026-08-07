import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from api import _calculate, app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_addition():
    response = client.post("/",json={"a": 10, "b":8, "operator":"+"})
    assert response.status_code == 200
    assert response.json() == {"result":18}


def test_substraction():
    response = client.post("/",json={"a": 10, "b":8, "operator":"-"})
    assert response.status_code == 200
    assert response.json() == {"result":2}


def test_multiplication():
    response = client.post("/",json={"a": 10, "b":8, "operator":"*"})
    assert response.status_code == 200
    assert response.json() == {"result":80}

def test_division():
    response = client.post("/",json={"a": 10, "b":8, "operator":"/"})
    assert response.status_code == 200
    assert response.json() == {"result":1.25}

def test_unknown_operator():
    with pytest.raises(HTTPException) as exc:
        _calculate(10, 8, "x")

    assert exc.value.status_code == 400
    assert exc.value.detail == "Unknown operator"

def test_division_by_zero():
    with pytest.raises(HTTPException) as exc:
        _calculate(10, 0, "/")

    assert exc.value.status_code == 400
    assert exc.value.detail == "Division by zero"

def test_modulus():
    response = client.post("/",json={"a": 10, "b":3, "operator":"%"})
    assert response.status_code == 200
    assert response.json() == {"result":1}