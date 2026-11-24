from fast_zero.schemas import (
    Atributo,
    CampanhaDB,
    CampanhaList,
    CampanhaPublic,
    CampanhaSchema,
    HabilidadeCreate,
    ItemCreate,
    Message,
    Pericia,
    PersonagemCreate,
    UsuarioCreate,
)


def test_message_schema():
    msg = Message(message="Grimório — API de Campanhas")
    assert msg.message == "Grimório — API de Campanhas"


def test_campanha_schemas():
    campanha_schema = CampanhaSchema(
        nome="A Mina Perdida",
        sistema="D&D 5e",
        descricao="Campanha para iniciantes",
    )
    assert campanha_schema.nome == "A Mina Perdida"
    assert campanha_schema.sistema == "D&D 5e"

    campanha_db = CampanhaDB(**campanha_schema.model_dump(), id=1)
    assert campanha_db.id == 1

    campanha_public = CampanhaPublic(
        id=1,
        nome="A Mina Perdida",
        sistema="D&D 5e",
        descricao="Campanha para iniciantes",
    )
    assert campanha_public.id == 1

    campanha_list = CampanhaList(campanhas=[campanha_public])
    assert len(campanha_list.campanhas) == 1


def test_usuario_schemas():
    usuario_in = UsuarioCreate(
        email="mestre@rpg.com",
        senha="password123",
        nome="Mestre dos Magos",
    )
    assert usuario_in.email == "mestre@rpg.com"
    assert usuario_in.nome == "Mestre dos Magos"


def test_personagem_schemas():
    personagem_in = PersonagemCreate(
        nome="Aragorn",
        sistema_rpg="D&D 5e",
        nivel=5,
        classe="Ranger",
        raca="Humano",
    )
    assert personagem_in.nome == "Aragorn"
    assert personagem_in.nivel == 5


def test_atributo_e_pericia_schemas():
    atributo = Atributo(nome="Força", valor=16, bonus=3)
    assert atributo.nome == "Força"
    assert atributo.valor == 16

    pericia = Pericia(nome="Atletismo", valor=5, proficiente=True)
    assert pericia.nome == "Atletismo"
    assert pericia.proficiente is True


def test_habilidade_e_item_schemas():
    hab = HabilidadeCreate(nome="Bola de Fogo", descricao="Causa 8d6 de fogo")
    assert hab.nome == "Bola de Fogo"

    item = ItemCreate(nome="Espada Longa", peso=1.5, valor=15.0)
    assert item.nome == "Espada Longa"
