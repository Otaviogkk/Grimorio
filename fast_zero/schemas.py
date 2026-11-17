from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


# Schemas de Usuário
class UsuarioSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UsuarioPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UsuarioList(BaseModel):
    usuarios: list[UsuarioPublic]


# Schemas de Personagem
class PersonagemSchema(BaseModel):
    nome: str
    sistema: str
    nivel: int = 1
    classe: str | None = None
    raca: str | None = None
    descricao: str | None = None
    imagem_url: str | None = None


class PersonagemPublic(BaseModel):
    id: int
    nome: str
    sistema: str
    nivel: int = 1
    classe: str | None = None
    raca: str | None = None
    descricao: str | None = None
    imagem_url: str | None = None


class PersonagemList(BaseModel):
    personagens: list[PersonagemPublic]


# Schemas de Atributos e Perícias
class AtributoSchema(BaseModel):
    nome: str
    valor: int
    modificador: int = 0


class PericiaSchema(BaseModel):
    nome: str
    valor: int
    proficiente: bool = False
    atributo_base: str | None = None


# Schemas de Habilidade
class HabilidadeSchema(BaseModel):
    nome: str
    descricao: str
    categoria: str | None = None
    custo: str | None = None
    requisitos: str | None = None


class HabilidadePublic(BaseModel):
    id: int
    nome: str
    descricao: str
    categoria: str | None = None
    custo: str | None = None
    requisitos: str | None = None


# Schemas de Item / Inventário
class ItemSchema(BaseModel):
    nome: str
    descricao: str | None = None
    categoria: str | None = None
    quantidade: int = 1
    peso: float = 0.0
    valor: float = 0.0
    equipado: bool = False


class ItemPublic(BaseModel):
    id: int
    nome: str
    descricao: str | None = None
    categoria: str | None = None
    quantidade: int = 1
    peso: float = 0.0
    valor: float = 0.0
    equipado: bool = False


# Schemas de Campanha
class CampanhaSchema(BaseModel):
    nome: str
    sistema: str
    descricao: str | None = None


class CampanhaPublic(BaseModel):
    id: int
    nome: str
    sistema: str
    descricao: str | None = None
