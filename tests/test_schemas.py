from fast_zero.schemas import (
    CampanhaDB,
    CampanhaList,
    CampanhaPublic,
    CampanhaSchema,
    Message,
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
