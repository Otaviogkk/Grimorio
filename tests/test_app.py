from http import HTTPStatus


def test_root_deve_retornar_ok_e_mensagem(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Grimório — API de Campanhas"}


def test_create_campanha(client):
    response = client.post(
        "/campanhas/",
        json={
            "nome": "A Mina Perdida",
            "sistema": "D&D 5e",
            "descricao": "Campanha para iniciantes",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "nome": "A Mina Perdida",
        "sistema": "D&D 5e",
        "descricao": "Campanha para iniciantes",
    }


def test_read_campanhas(client):
    client.post(
        "/campanhas/",
        json={
            "nome": "A Mina Perdida",
            "sistema": "D&D 5e",
            "descricao": "Campanha para iniciantes",
        },
    )
    response = client.get("/campanhas/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "campanhas": [
            {
                "id": 1,
                "nome": "A Mina Perdida",
                "sistema": "D&D 5e",
                "descricao": "Campanha para iniciantes",
            }
        ]
    }


def test_read_campanha_by_id(client):
    client.post(
        "/campanhas/",
        json={
            "nome": "A Mina Perdida",
            "sistema": "D&D 5e",
            "descricao": "Campanha para iniciantes",
        },
    )
    response = client.get("/campanhas/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "nome": "A Mina Perdida",
        "sistema": "D&D 5e",
        "descricao": "Campanha para iniciantes",
    }


def test_read_campanha_not_found(client):
    response = client.get("/campanhas/999")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Campanha not found"}


def test_update_campanha(client):
    client.post(
        "/campanhas/",
        json={
            "nome": "A Mina Perdida",
            "sistema": "D&D 5e",
            "descricao": "Campanha para iniciantes",
        },
    )
    response = client.put(
        "/campanhas/1",
        json={
            "nome": "A Maldição de Strahd",
            "sistema": "D&D 5e",
            "descricao": "Campanha gótica de horror",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "nome": "A Maldição de Strahd",
        "sistema": "D&D 5e",
        "descricao": "Campanha gótica de horror",
    }


def test_update_campanha_not_found(client):
    response = client.put(
        "/campanhas/999",
        json={
            "nome": "A Maldição de Strahd",
            "sistema": "D&D 5e",
            "descricao": "Campanha gótica de horror",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Campanha not found"}


def test_delete_campanha(client):
    client.post(
        "/campanhas/",
        json={
            "nome": "A Mina Perdida",
            "sistema": "D&D 5e",
            "descricao": "Campanha para iniciantes",
        },
    )
    response = client.delete("/campanhas/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Campanha deleted"}


def test_delete_campanha_not_found(client):
    response = client.delete("/campanhas/999")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Campanha not found"}
