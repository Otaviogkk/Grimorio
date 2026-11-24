import pytest
from fastapi.testclient import TestClient

from fast_zero.app import (
    app,
    database,
    habilidades,
    itens,
    personagens,
    tokens,
    usuarios,
)


@pytest.fixture
def client():
    database.clear()
    usuarios.clear()
    personagens.clear()
    tokens.clear()
    habilidades.clear()
    itens.clear()
    return TestClient(app)
