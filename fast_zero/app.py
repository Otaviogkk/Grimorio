from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import (
    CampanhaDB,
    CampanhaList,
    CampanhaPublic,
    CampanhaSchema,
    Message,
)

app = FastAPI(
    title="Grimório — API de Campanhas",
    description="API REST pura (máquina para máquina) para gerenciamento de campanhas de RPG.",
    version="0.1.0",
)

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Grimório — API de Campanhas"}


@app.post(
    "/campanhas/",
    status_code=HTTPStatus.CREATED,
    response_model=CampanhaPublic,
)
def create_campanha(campanha: CampanhaSchema):
    campanha_with_id = CampanhaDB(
        **campanha.model_dump(), id=len(database) + 1
    )
    database.append(campanha_with_id)
    return campanha_with_id


@app.get("/campanhas/", response_model=CampanhaList)
def read_campanhas():
    return {"campanhas": database}


@app.get("/campanhas/{campanha_id}", response_model=CampanhaPublic)
def read_campanha(campanha_id: int):
    if campanha_id > len(database) or campanha_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Campanha not found"
        )
    return database[campanha_id - 1]


@app.put("/campanhas/{campanha_id}", response_model=CampanhaPublic)
def update_campanha(campanha_id: int, campanha: CampanhaSchema):
    if campanha_id > len(database) or campanha_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Campanha not found"
        )
    campanha_with_id = CampanhaDB(**campanha.model_dump(), id=campanha_id)
    database[campanha_id - 1] = campanha_with_id
    return campanha_with_id


@app.delete("/campanhas/{campanha_id}", response_model=Message)
def delete_campanha(campanha_id: int):
    if campanha_id > len(database) or campanha_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Campanha not found"
        )
    del database[campanha_id - 1]
    return {"message": "Campanha deleted"}
