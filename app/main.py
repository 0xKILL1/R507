from fastapi import FastAPI
from .routers import equipements
from .bdd import configure_db

def on_startup():
    configure_db()

app= FastAPI(title="Supervision API",version="1.0.0",on_startup=[on_startup])

app.include_router(equipements.router,prefix="/api/v1",tags=["Gestion des équipements"])