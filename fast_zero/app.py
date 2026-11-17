import secrets
from copy import deepcopy
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any
from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fast_zero.schemas import (
    AtributosPayload,
    CampanhaDB,
    CampanhaList,
    CampanhaPublic,
    CampanhaSchema,
    HabilidadeCreate,
    HabilidadePublic,
    ImportacaoPersonagem,
    ItemCreate,
    ItemPublic,
    Message,
    PericiasPayload,
    PersonagemCreate,
    PersonagemList,
    PersonagemPublic,
    PersonagemUpdate,
    TokenRequest,
    TokenResponse,
    UsuarioCreate,
    UsuarioPublic,
    UsuarioUpdate,
)
app = FastAPI(
    title="Grimório — API REST de Fichas de RPG",
    description="API REST pura para comunicação máquina a máquina.",
    version="0.2.0",
    docs_url=None,
    redoc_url=None,
)

database: list[CampanhaDB] = []
usuarios: list[dict[str, Any]] = []
personagens: list[dict[str, Any]] = []
habilidades: list[dict[str, Any]] = []
itens: list[dict[str, Any]] = []
tokens: dict[str, int] = {}

bearer = HTTPBearer(auto_error=False)


def agora() -> datetime:
    return datetime.now(UTC)

def senha_hash(senha: str) -> str:
    return sha256(senha.encode("utf-8")).hexdigest()


def erro(status_code: int, detail: str) -> HTTPException:
    return HTTPException(status_code=status_code, detail=detail)


def proximo_id(itens_lista: list[Any]) -> int:
    return max((item["id"] if isinstance(item, dict) else item.id for item in itens_lista), default=0) + 1


def usuario_publico(usuario: dict[str, Any]) -> UsuarioPublic:
    return UsuarioPublic(**{k: v for k, v in usuario.items() if k != "senha_hash"})


def get_usuario_atual(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer),
) -> dict[str, Any]:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise erro(status.HTTP_401_UNAUTHORIZED, "Token ausente ou inválido")
    usuario_id = tokens.get(credentials.credentials)
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if usuario is None:
        raise erro(status.HTTP_401_UNAUTHORIZED, "Token ausente ou inválido")
    return usuario


def get_personagem(personagem_id: int, usuario: dict[str, Any]) -> dict[str, Any]:
    personagem = next((p for p in personagens if p["id"] == personagem_id), None)
    if personagem is None or personagem["proprietario_id"] != usuario["id"]:
        raise erro(status.HTTP_404_NOT_FOUND, "Personagem não encontrado")
    return personagem


def personagem_publico(personagem: dict[str, Any]) -> PersonagemPublic:
    return PersonagemPublic(**personagem)


def campanha_publica(campanha: CampanhaDB) -> CampanhaPublic:
    return CampanhaPublic(
        id=campanha.id,
        nome=campanha.nome,
        sistema=campanha.sistema,
        descricao=campanha.descricao,
    )


@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def read_root() -> Message:
    return Message(message="Grimório — API de Campanhas")


@app.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=UsuarioPublic)
def create_usuario(payload: UsuarioCreate) -> UsuarioPublic:
    if any(u["email"].lower() == payload.email.lower() for u in usuarios):
        raise erro(status.HTTP_409_CONFLICT, "E-mail já cadastrado")
    registro = {
        "id": proximo_id(usuarios),
        "email": str(payload.email),
        "nome": payload.nome,
        "senha_hash": senha_hash(payload.senha),
        "criado_em": agora(),
        "atualizado_em": agora(),
    }
    usuarios.append(registro)
    return usuario_publico(registro)


@app.post("/auth/token", response_model=TokenResponse)
def login(payload: TokenRequest) -> TokenResponse:
    usuario = next((u for u in usuarios if u["email"].lower() == payload.email.lower()), None)
    if usuario is None or usuario["senha_hash"] != senha_hash(payload.senha):
        raise erro(status.HTTP_401_UNAUTHORIZED, "Credenciais inválidas")
    token = secrets.token_urlsafe(32)
    tokens[token] = usuario["id"]
    return TokenResponse(access_token=token)


@app.get("/usuarios/me", response_model=UsuarioPublic)
def read_me(usuario: dict[str, Any] = Depends(get_usuario_atual)) -> UsuarioPublic:
    return usuario_publico(usuario)


@app.patch("/usuarios/me", response_model=UsuarioPublic)
def update_me(payload: UsuarioUpdate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> UsuarioPublic:
    dados = payload.model_dump(exclude_unset=True)
    if "email" in dados and any(u["id"] != usuario["id"] and u["email"].lower() == str(dados["email"]).lower() for u in usuarios):
        raise erro(status.HTTP_409_CONFLICT, "E-mail já cadastrado")
    if "senha" in dados:
        usuario["senha_hash"] = senha_hash(dados.pop("senha"))
    usuario.update(dados)
    usuario["atualizado_em"] = agora()
    return usuario_publico(usuario)


@app.delete("/usuarios/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_me(usuario: dict[str, Any] = Depends(get_usuario_atual)) -> None:
    usuarios.remove(usuario)
    for token, user_id in list(tokens.items()):
        if user_id == usuario["id"]:
            del tokens[token]


@app.post("/personagens", status_code=status.HTTP_201_CREATED, response_model=PersonagemPublic)
def create_personagem(payload: PersonagemCreate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> PersonagemPublic:
    data = payload.model_dump(mode="json")
    data.update(id=proximo_id(personagens), proprietario_id=usuario["id"], criado_em=agora(), atualizado_em=agora())
    personagens.append(data)
    return personagem_publico(data)


@app.get("/personagens", response_model=PersonagemList)
def list_personagens(
    favorito: bool | None = None,
    sistema_rpg: str | None = None,
    busca: str | None = None,
    pagina: int = Query(1, ge=1),
    limite: int = Query(50, ge=1, le=100),
    ordenacao: str = Query("id", pattern="^-?(id|nome|nivel|experiencia)$"),
    usuario: dict[str, Any] = Depends(get_usuario_atual),
) -> PersonagemList:
    resultado = [p for p in personagens if p["proprietario_id"] == usuario["id"]]
    if favorito is not None:
        resultado = [p for p in resultado if p["favorito"] == favorito]
    if sistema_rpg:
        resultado = [p for p in resultado if p["sistema_rpg"].lower() == sistema_rpg.lower()]
    if busca:
        resultado = [p for p in resultado if busca.lower() in p["nome"].lower()]
    reverso = ordenacao.startswith("-")
    campo = ordenacao.removeprefix("-")
    resultado.sort(key=lambda personagem: personagem[campo], reverse=reverso)
    total = len(resultado)
    inicio = (pagina - 1) * limite
    return PersonagemList(personagens=[personagem_publico(p) for p in resultado[inicio : inicio + limite]], total=total)


@app.get("/personagens/importar", include_in_schema=False)
def importacao_placeholder() -> None:
    raise erro(status.HTTP_405_METHOD_NOT_ALLOWED, "Use POST para importar uma ficha")


@app.get("/personagens/{personagem_id}", response_model=PersonagemPublic)
def read_personagem(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> PersonagemPublic:
    return personagem_publico(get_personagem(personagem_id, usuario))


@app.patch("/personagens/{personagem_id}", response_model=PersonagemPublic)
def update_personagem(personagem_id: int, payload: PersonagemUpdate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> PersonagemPublic:
    personagem = get_personagem(personagem_id, usuario)
    personagem.update(payload.model_dump(exclude_unset=True, mode="json"))
    personagem["atualizado_em"] = agora()
    return personagem_publico(personagem)


@app.delete("/personagens/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_personagem(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> None:
    personagem = get_personagem(personagem_id, usuario)
    personagens.remove(personagem)
    habilidades[:] = [h for h in habilidades if h["personagem_id"] != personagem_id]
    itens[:] = [i for i in itens if i["personagem_id"] != personagem_id]


@app.post("/personagens/{personagem_id}/duplicar", status_code=status.HTTP_201_CREATED, response_model=PersonagemPublic)
def duplicate_personagem(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> PersonagemPublic:
    original = get_personagem(personagem_id, usuario)
    copia = deepcopy(original)
    copia.update(id=proximo_id(personagens), nome=f"{original['nome']} (cópia)", criado_em=agora(), atualizado_em=agora())
    personagens.append(copia)
    return personagem_publico(copia)


@app.get("/personagens/{personagem_id}/exportar", response_model=ImportacaoPersonagem)
def export_personagem(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> ImportacaoPersonagem:
    personagem = get_personagem(personagem_id, usuario)
    payload = PersonagemCreate(**{k: v for k, v in personagem.items() if k not in {"id", "proprietario_id", "criado_em", "atualizado_em"}})
    return ImportacaoPersonagem(personagem=payload)


@app.post("/personagens/importar", status_code=status.HTTP_201_CREATED, response_model=PersonagemPublic)
def import_personagem(payload: ImportacaoPersonagem, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> PersonagemPublic:
    return create_personagem(payload.personagem, usuario)


@app.get("/personagens/{personagem_id}/atributos", response_model=AtributosPayload)
def read_atributos(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> AtributosPayload:
    return AtributosPayload(atributos=get_personagem(personagem_id, usuario)["atributos"])


@app.put("/personagens/{personagem_id}/atributos", response_model=AtributosPayload)
def replace_atributos(personagem_id: int, payload: AtributosPayload, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> AtributosPayload:
    personagem = get_personagem(personagem_id, usuario)
    personagem["atributos"] = payload.atributos
    personagem["atualizado_em"] = agora()
    return payload


@app.get("/personagens/{personagem_id}/pericias", response_model=PericiasPayload)
def read_pericias(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> PericiasPayload:
    return PericiasPayload(pericias=get_personagem(personagem_id, usuario)["pericias"])


@app.post("/personagens/{personagem_id}/habilidades", status_code=status.HTTP_201_CREATED, response_model=HabilidadePublic)
def create_habilidade(personagem_id: int, payload: HabilidadeCreate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> HabilidadePublic:
    get_personagem(personagem_id, usuario)
    registro = {**payload.model_dump(), "id": proximo_id(habilidades), "personagem_id": personagem_id}
    habilidades.append(registro)
    return HabilidadePublic(**registro)


@app.patch("/habilidades/{habilidade_id}", response_model=HabilidadePublic)
def update_habilidade(habilidade_id: int, payload: HabilidadeCreate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> HabilidadePublic:
    habilidade = next((h for h in habilidades if h["id"] == habilidade_id), None)
    if habilidade is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Habilidade não encontrada")
    get_personagem(habilidade["personagem_id"], usuario)
    habilidade.update(payload.model_dump())
    return HabilidadePublic(**habilidade)


@app.delete("/habilidades/{habilidade_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_habilidade(habilidade_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> None:
    habilidade = next((h for h in habilidades if h["id"] == habilidade_id), None)
    if habilidade is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Habilidade não encontrada")
    get_personagem(habilidade["personagem_id"], usuario)
    habilidades.remove(habilidade)


@app.get("/personagens/{personagem_id}/inventario", response_model=list[ItemPublic])
def read_inventario(personagem_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> list[ItemPublic]:
    get_personagem(personagem_id, usuario)
    return [ItemPublic(**item) for item in itens if item["personagem_id"] == personagem_id]


@app.post("/personagens/{personagem_id}/inventario", status_code=status.HTTP_201_CREATED, response_model=ItemPublic)
def create_item(personagem_id: int, payload: ItemCreate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> ItemPublic:
    get_personagem(personagem_id, usuario)
    registro = {**payload.model_dump(), "id": proximo_id(itens), "personagem_id": personagem_id}
    itens.append(registro)
    return ItemPublic(**registro)


@app.patch("/itens/{item_id}", response_model=ItemPublic)
def update_item(item_id: int, payload: ItemCreate, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> ItemPublic:
    item = next((i for i in itens if i["id"] == item_id), None)
    if item is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Item não encontrado")
    get_personagem(item["personagem_id"], usuario)
    item.update(payload.model_dump())
    return ItemPublic(**item)


@app.delete("/itens/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, usuario: dict[str, Any] = Depends(get_usuario_atual)) -> None:
    item = next((i for i in itens if i["id"] == item_id), None)
    if item is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Item não encontrado")
    get_personagem(item["personagem_id"], usuario)
    itens.remove(item)


# Campanhas permanecem públicas para preservar a primeira versão e os testes existentes.
@app.post("/campanhas/", status_code=status.HTTP_201_CREATED, response_model=CampanhaPublic)
def create_campanha(campanha: CampanhaSchema) -> CampanhaPublic:
    registro = CampanhaDB(**campanha.model_dump(), id=proximo_id(database))
    database.append(registro)
    return campanha_publica(registro)


@app.get("/campanhas/", response_model=CampanhaList)
def read_campanhas() -> CampanhaList:
    return CampanhaList(campanhas=[campanha_publica(c) for c in database])


@app.get("/campanhas/{campanha_id}", response_model=CampanhaPublic)
def read_campanha(campanha_id: int) -> CampanhaPublic:
    campanha = next((c for c in database if c.id == campanha_id), None)
    if campanha is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Campanha not found")
    return campanha_publica(campanha)


@app.put("/campanhas/{campanha_id}", response_model=CampanhaPublic)
def update_campanha(campanha_id: int, campanha: CampanhaSchema) -> CampanhaPublic:
    indice = next((i for i, c in enumerate(database) if c.id == campanha_id), None)
    if indice is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Campanha not found")
    registro = CampanhaDB(**campanha.model_dump(), id=campanha_id)
    database[indice] = registro
    return campanha_publica(registro)


@app.patch("/campanhas/{campanha_id}", response_model=CampanhaPublic)
def patch_campanha(campanha_id: int, campanha: CampanhaSchema) -> CampanhaPublic:
    return update_campanha(campanha_id, campanha)


@app.delete("/campanhas/{campanha_id}", response_model=Message)
def delete_campanha(campanha_id: int) -> Message:
    campanha = next((c for c in database if c.id == campanha_id), None)
    if campanha is None:
        raise erro(status.HTTP_404_NOT_FOUND, "Campanha not found")
    database.remove(campanha)
    return Message(message="Campanha deleted")