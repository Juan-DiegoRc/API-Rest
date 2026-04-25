from fastapi import FastAPI
from routers import caracteristicas, battle

app = FastAPI(title = "RPG Battle API")


app.include_router(caracteristicas.router)
app.include_router(battle.router)

@app.get("/")
def root():
    return {"Mensaje": "Bienvenido a la API de Batallas RPG."}