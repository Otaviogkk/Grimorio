from pydantic import BaseModel


class Message(BaseModel):
    message: str


class CampanhaSchema(BaseModel):
    nome: str
    sistema: str
    descricao: str | None = None


class CampanhaPublic(BaseModel):
    id: int
    nome: str
    sistema: str
    descricao: str | None = None


class CampanhaDB(CampanhaSchema):
    id: int


class CampanhaList(BaseModel):
    campanhas: list[CampanhaPublic]
