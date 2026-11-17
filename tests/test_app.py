from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_mensagem():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "message": "Grimório — Organizador de Fichas de RPG"
    }


def test_pagina_sobre_em_html():
    client = TestClient(app)

    response = client.get("/sobre")

    assert response.status_code == HTTPStatus.OK
    assert (
        "<h1> Grimório — Organizador de Fichas de RPG </h1>" in response.text
    )
