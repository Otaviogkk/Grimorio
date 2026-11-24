from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class Message(BaseModel):
    message: str


class ErrorDetail(BaseModel):
    campo: str
    motivo: str


class ErrorResponse(BaseModel):
    erro: dict[str, Any]


class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str = Field(min_length=8, max_length=128)
    nome: str | None = Field(default=None, max_length=120)


class UsuarioUpdate(BaseModel):
    email: EmailStr | None = None
    nome: str | None = Field(default=None, max_length=120)
    senha: str | None = Field(default=None, min_length=8, max_length=128)


class UsuarioPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    nome: str | None = None
    criado_em: datetime
    atualizado_em: datetime


class TokenRequest(BaseModel):
    email: EmailStr
    senha: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Atributo(BaseModel):
    nome: str = Field(min_length=1, max_length=80)
    valor: int = Field(ge=-100, le=1000)
    bonus: int = Field(default=0, ge=-100, le=1000)
    penalidade: int = Field(default=0, ge=-100, le=1000)
    modificador: int | None = None


class Pericia(BaseModel):
    nome: str = Field(min_length=1, max_length=80)
    valor: int = Field(default=0, ge=-100, le=1000)
    proficiente: bool = False
    atributo: str | None = Field(default=None, max_length=80)
    bonus: int = 0


class HabilidadeCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=120)
    descricao: str | None = None
    categoria: str | None = Field(default=None, max_length=80)
    nivel: int | None = Field(default=None, ge=0, le=100)
    custo: str | None = Field(default=None, max_length=80)
    alcance: str | None = Field(default=None, max_length=80)
    duracao: str | None = Field(default=None, max_length=80)
    pre_requisitos: list[str] = Field(default_factory=list)
    efeitos: list[str] = Field(default_factory=list)
    usos_disponiveis: int | None = Field(default=None, ge=0)


class HabilidadePublic(HabilidadeCreate):
    id: int
    personagem_id: int


class ItemCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=120)
    descricao: str | None = None
    categoria: str | None = Field(default=None, max_length=80)
    quantidade: int = Field(default=1, ge=0)
    peso: float = Field(default=0, ge=0)
    valor: float = Field(default=0, ge=0)
    equipado: bool = False
    propriedades: dict[str, Any] = Field(default_factory=dict)


class ItemPublic(ItemCreate):
    id: int
    personagem_id: int


class PersonagemCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=120)
    apelido: str | None = Field(default=None, max_length=120)
    idade: int | None = Field(default=None, ge=0, le=10000)
    genero: str | None = Field(default=None, max_length=80)
    raca: str | None = Field(default=None, max_length=80)
    especie: str | None = Field(default=None, max_length=80)
    classe: str | None = Field(default=None, max_length=80)
    profissao: str | None = Field(default=None, max_length=80)
    arquetipo: str | None = Field(default=None, max_length=80)
    nivel: int = Field(default=1, ge=1, le=100)
    experiencia: int = Field(default=0, ge=0)
    alinhamento: str | None = Field(default=None, max_length=80)
    sistema_rpg: str = Field(min_length=1, max_length=80)
    origem: str | None = None
    historia: str | None = None
    personalidade: str | None = None
    objetivos: str | None = None
    anotacoes: str | None = None
    image_url: HttpUrl | None = None
    campanha_id: int | None = Field(default=None, ge=1)
    favorito: bool = False
    atributos: dict[str, Atributo | int] = Field(default_factory=dict)
    pericias: list[Pericia] = Field(default_factory=list)


class PersonagemUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=1, max_length=120)
    apelido: str | None = None
    idade: int | None = Field(default=None, ge=0)
    genero: str | None = None
    raca: str | None = None
    especie: str | None = None
    classe: str | None = None
    profissao: str | None = None
    arquetipo: str | None = None
    nivel: int | None = Field(default=None, ge=1, le=100)
    experiencia: int | None = Field(default=None, ge=0)
    alinhamento: str | None = None
    sistema_rpg: str | None = None
    origem: str | None = None
    historia: str | None = None
    personalidade: str | None = None
    objetivos: str | None = None
    anotacoes: str | None = None
    image_url: HttpUrl | None = None
    campanha_id: int | None = Field(default=None, ge=1)
    favorito: bool | None = None
    atributos: dict[str, Atributo | int] | None = None
    pericias: list[Pericia] | None = None


class PersonagemPublic(PersonagemCreate):
    id: int
    proprietario_id: int
    criado_em: datetime
    atualizado_em: datetime


class PersonagemList(BaseModel):
    personagens: list[PersonagemPublic]
    total: int


class AtributosPayload(BaseModel):
    atributos: dict[str, Atributo | int] = Field(default_factory=dict)


class PericiasPayload(BaseModel):
    pericias: list[Pericia] = Field(default_factory=list)


class ImportacaoPersonagem(BaseModel):
    versao_schema: str = "1.0"
    personagem: PersonagemCreate


class CampanhaSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=120)
    sistema: str = Field(min_length=1, max_length=80)
    descricao: str | None = None
    mestre: str | None = None
    participantes: list[int] = Field(default_factory=list)
    sessoes: list[dict[str, Any]] = Field(default_factory=list)
    missoes: list[dict[str, Any]] = Field(default_factory=list)
    notas: list[str] = Field(default_factory=list)


class CampanhaPublic(BaseModel):
    id: int
    nome: str
    sistema: str
    descricao: str | None = None


class CampanhaDB(CampanhaSchema):
    id: int


class CampanhaList(BaseModel):
    campanhas: list[CampanhaPublic]
