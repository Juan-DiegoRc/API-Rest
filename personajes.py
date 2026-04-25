from pydantic import BaseModel
from typing import Optional


#Definiciones
class Crearpers(BaseModel):
    nombre: str
    color_piel: Optional[str] = None
    raza: Optional[str] = None
    fuerza: int
    agilidad: int
    magia: int
    conocimiento: int


class Personaje(Crearpers):
    id: int