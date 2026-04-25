from fastapi import APIRouter, HTTPException
import database as db

router = APIRouter(prefix = "/battle", tags=["Batallas"])

def calcular_score(stats):
    return (
        stats.fuerza * 2 +
        stats.agilidad * 1.5 +
        stats.magia * 1.8 +
        stats.conocimiento * 1.2
    )

@router.post("/")
def battle(id1: int, id2: int):
    if id1 not in db.caracteristicas_db or id2 not in db.caracteristicas_db:
        raise HTTPException(status_code = 404, detail = "Uno o ambos personajes no encontrados.")
    
    carac1 = db.caracteristicas_db[id1]
    carac2 = db.caracteristicas_db[id2]

    score1 = calcular_score(carac1)
    score2 = calcular_score(carac2)

    if score1 > score2:
        winner = carac1.nombre
    elif score2 > score1:
        winner = carac2.nombre
    else:
        winner = "Empate"

    return {
        "Ganador": winner,
        "Detalles": {
            carac1.nombre: {"Puntaje": score1, "Stats": carac1.model_dump()},
            carac2.nombre: {"Puntaje": score2, "Stats": carac2.model_dump()}
        },
        "Resumen": f"{carac1.nombre} ({score1: .1f} pts) vs {carac2.nombre} ({score2: .1f} pts) -> Ganador: {winner}"
    }