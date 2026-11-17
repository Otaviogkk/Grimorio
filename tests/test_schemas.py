from fast_zero.schemas import (
    AtributoSchema,
    CampanhaPublic,
    CampanhaSchema,
    HabilidadePublic,
    HabilidadeSchema,
    ItemPublic,
    ItemSchema,
    Message,
    PericiaSchema,
    PersonagemList,
    PersonagemPublic,
    PersonagemSchema,
    UsuarioList,
    UsuarioPublic,
    UsuarioSchema,
)


def test_message_schema():
    msg = Message(message="Grimório")
    assert msg.message == "Grimório"


def test_usuario_schemas():
    usuario_in = UsuarioSchema(
        username="mestre", email="mestre@rpg.com", password="secretpassword"
    )
    assert usuario_in.username == "mestre"
    assert usuario_in.email == "mestre@rpg.com"

    usuario_out = UsuarioPublic(
        id=1, username="mestre", email="mestre@rpg.com"
    )
    assert usuario_out.id == 1

    lista = UsuarioList(usuarios=[usuario_out])
    assert len(lista.usuarios) == 1


def test_personagem_schemas():
    personagem_in = PersonagemSchema(
        nome="Aragorn",
        sistema="D&D 5e",
        nivel=5,
        classe="Ranger",
        raca="Humano",
        descricao="Guerreiro do norte",
    )
    assert personagem_in.nome == "Aragorn"
    assert personagem_in.nivel == 5

    personagem_out = PersonagemPublic(
        id=1,
        nome="Aragorn",
        sistema="D&D 5e",
        nivel=5,
        classe="Ranger",
        raca="Humano",
    )
    assert personagem_out.id == 1

    lista = PersonagemList(personagens=[personagem_out])
    assert len(lista.personagens) == 1


def test_atributo_e_pericia_schemas():
    atributo = AtributoSchema(nome="Força", valor=16, modificador=3)
    assert atributo.nome == "Força"
    assert atributo.valor == 16
    assert atributo.modificador == 3

    pericia = PericiaSchema(
        nome="Atletismo", valor=5, proficiente=True, atributo_base="Força"
    )
    assert pericia.nome == "Atletismo"
    assert pericia.proficiente is True


def test_habilidade_schemas():
    hab_in = HabilidadeSchema(
        nome="Ataque Poderoso",
        descricao="Causa dano extra.",
        categoria="Combate",
    )
    assert hab_in.nome == "Ataque Poderoso"

    hab_out = HabilidadePublic(
        id=1,
        nome="Ataque Poderoso",
        descricao="Causa dano extra.",
        categoria="Combate",
    )
    assert hab_out.id == 1


def test_item_schemas():
    item_in = ItemSchema(
        nome="Espada Longa",
        descricao="Espada de aço.",
        categoria="Arma",
        quantidade=1,
        peso=1.5,
        valor=15.0,
        equipado=True,
    )
    assert item_in.nome == "Espada Longa"
    assert item_in.equipado is True

    item_out = ItemPublic(
        id=1,
        nome="Espada Longa",
        categoria="Arma",
        quantidade=1,
        peso=1.5,
        valor=15.0,
    )
    assert item_out.id == 1


def test_campanha_schemas():
    campanha_in = CampanhaSchema(
        nome="A Mina Perdida",
        sistema="D&D 5e",
        descricao="Aventura para iniciantes.",
    )
    assert campanha_in.nome == "A Mina Perdida"

    campanha_out = CampanhaPublic(
        id=1,
        nome="A Mina Perdida",
        sistema="D&D 5e",
        descricao="Aventura para iniciantes.",
    )
    assert campanha_out.id == 1
