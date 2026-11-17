from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(
    title="Grimório — Organizador de Fichas de RPG",
    description="API REST para gerenciamento de fichas de personagens de RPG, campanhas e inventário.",
    version="0.1.0",
)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Grimório — Organizador de Fichas de RPG"}


@app.get("/sobre", response_class=HTMLResponse)
def pagina_sobre():
    return """
    <html>
      <head>
        <title>Grimório — Organizador de Fichas de RPG</title>
      </head>
      <body>
        <h1> Grimório — Organizador de Fichas de RPG </h1>
        <p>Aplicação web para gerenciar fichas de personagens de RPG.</p>
      </body>
    </html>"""
