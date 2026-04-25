from fastapi import APIRouter, HTTPException
from personajes import Personaje, Crearpers
import database as db

router = APIRouter(prefix = "/characters", tags=["Personajes"])

#crear
@router.post("/", response_model = Personaje)
def Crear_personaje(characters: Crearpers):
    nuevo_personaje = Personaje(id=db.next_id, **characters.model_dump())
    db.caracteristicas_db[db.next_id] = nuevo_personaje
    db.next_id += 1
    return nuevo_personaje


#Listar
@router.get("/", response_model = list[Personaje])
def list_personaje():
    return list(db.caracteristicas_db.values())


#Consultar ID
@router.get("/{character_id}", response_model = Personaje)
def get_character(character_id: int):
    if character_id not in db.caracteristicas_db:
        raise HTTPException(status_code = 404, detail = "Personaje no encontrado.")
    return db.caracteristicas_db[character_id]


#Actualizar
@router.put("/{character_id}", response_model = Personaje)
def update_personaje(character_id: int, updated: Crearpers):
    if character_id not in db.caracteristicas_db:
        raise HTTPException(status_code = 404, detail = "Personaje no encontrado.")
    update_perso = Personaje(id = character_id, **updated.model_dump())
    db.caracteristicas_db[character_id] = update_perso
    return update_perso

#Eliminar
@router.delete("/{character_id}")
def delete_personaje(character_id: int):
    if character_id not in db.caracteristicas_db:
        raise HTTPException(status_code = 404, detail = "Personaje no encontrado.")
    del db.caracteristicas_db[character_id]
    return {"Mensaje": "Personaje eliminado."}