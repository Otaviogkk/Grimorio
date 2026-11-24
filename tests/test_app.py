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


def test_create_usuario_and_login(client):
    res_user = client.post(
        "/usuarios",
        json={
            "email": "mestre@rpg.com",
            "senha": "password123",
            "nome": "Mestre",
        },
    )
    assert res_user.status_code == HTTPStatus.CREATED
    assert res_user.json()["email"] == "mestre@rpg.com"

    res_login = client.post(
        "/auth/token",
        json={"email": "mestre@rpg.com", "senha": "password123"},
    )
    assert res_login.status_code == HTTPStatus.OK
    token = res_login.json()["access_token"]
    assert token is not None

    res_me = client.get(
        "/usuarios/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert res_me.status_code == HTTPStatus.OK
    assert res_me.json()["email"] == "mestre@rpg.com"


def test_create_and_get_personagem(client):
    client.post(
        "/usuarios",
        json={
            "email": "mestre@rpg.com",
            "senha": "password123",
            "nome": "Mestre",
        },
    )
    token = client.post(
        "/auth/token",
        json={"email": "mestre@rpg.com", "senha": "password123"},
    ).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    res_p = client.post(
        "/personagens",
        json={
            "nome": "Aragorn",
            "sistema_rpg": "D&D 5e",
            "nivel": 5,
        },
        headers=headers,
    )
    assert res_p.status_code == HTTPStatus.CREATED
    p_id = res_p.json()["id"]

    res_list = client.get("/personagens", headers=headers)
    assert res_list.status_code == HTTPStatus.OK
    assert res_list.json()["total"] == 1

    res_get = client.get(f"/personagens/{p_id}", headers=headers)
    assert res_get.status_code == HTTPStatus.OK
    assert res_get.json()["nome"] == "Aragorn"
