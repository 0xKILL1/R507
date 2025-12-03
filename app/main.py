from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from models import Ordinateur, Equipement, Routeur
from bdd import configure_db, configure_db_ordinateur, configure_db_routeur


def on_start_up():
    configure_db()
    configure_db_ordinateur()
    configure_db_routeur()

app = FastAPI(on_startup=[on_start_up])


@app.get("/equipements")
def read_hosts() -> list[Equipement]:
    engine = configure_db()
    with Session(engine) as session:
        return session.exec(select(Equipement)).all()


@app.get("/equipement/{host_id}")
def read_host(host_id: int) -> Equipement:
    engine = configure_db()
    with Session(engine) as session:
        host = session.get(Equipement, host_id)
        if not host:
            raise HTTPException(404, "Host not found")
        return host


@app.post("/equipement")
def create_host(host: Equipement) -> Equipement:
    engine = configure_db()
    with Session(engine) as session:
        session.add(host)
        session.commit()
        session.refresh(host)
        return host


@app.put("/equipement/{host_id}")
def update_host(host_id: int, updated_host: Equipement):
    engine = configure_db()
    with Session(engine) as session:
        host = session.get(Equipement, host_id)
        if not host:
            raise HTTPException(404, "Host not found")
        host.hostname = updated_host.hostname
        host.ip = updated_host.ip
        session.add(host)
        session.commit()
        session.refresh(host)
        return host


@app.delete("/equipement/{host_id}")
def delete_host(host_id: int):
    with Session(engine) as session:
        host = session.get(Equipement, host_id)
        if not host:
            raise HTTPException(404, "Host not found")
        session.delete(host)
        session.commit()
        return {"ok": True}


@app.get("/Ordinateurs")
def read_Ordinateurs() -> list[Ordinateur]:
    with Session(engine) as session:
        return session.exec(select(Ordinateur)).all()


@app.get("/Ordinateur/{host_id}")
def read_Ordinateur(host_id: int) -> Ordinateur:
    engine = configure_db_ordinateur()
    with Session(engine) as session:
        ordinateur = session.get(Ordinateur, host_id)
        if not ordinateur:
            raise HTTPException(404, "Host not found")
        return ordinateur


@app.post("/Ordinateur")
def create_Ordinateur(ordinateur: Ordinateur) -> Ordinateur:
    engine = configure_db_ordinateur()
    with Session(engine) as session:
        session.add(ordinateur)
        session.commit()
        session.refresh(ordinateur)
        return ordinateur


@app.put("/Ordinateur/{host_id}")
def update_Ordinateur(host_id: int, updated_host: Ordinateur):
    engine = configure_db_ordinateur()
    with Session(engine) as session:
        ordinateur = session.get(Equipement, host_id)
        if not ordinateur:
            raise HTTPException(404, "Host not found")
        ordinateur.hostname = updated_host.hostname
        ordinateur.ip = updated_host.ip
        session.add(ordinateur)
        session.commit()
        session.refresh(ordinateur)
        return ordinateur


@app.delete("/Ordinateur/{host_id}")
def delete_Ordinateur(host_id: int):
    engine = configure_db_ordinateur()
    with Session(engine) as session:
        ordinateur = session.get(Ordinateur, host_id)
        if not ordinateur:
            raise HTTPException(404, "Host not found")
        session.delete(ordinateur)
        session.commit()
        return {"ok": True}
    

@app.get("/Routeurs")
def read_Routeurs() -> list[Equipement]:
    engine = configure_db_routeur()
    with Session(engine) as session:
        return session.exec(select(Equipement)).all()


@app.get("/Routeur/{host_id}")
def read_Routeur(host_id: int) -> Equipement:
    engine = configure_db_routeur()
    with Session(engine) as session:
        routeur = session.get(Routeur, host_id)
        if not routeur:
            raise HTTPException(404, "Host not found")
        return routeur


@app.post("/Routeur")
def create_Routeur(routeur: Routeur) -> Routeur:
    engine = configure_db_routeur()
    with Session(engine) as session:
        session.add(routeur)
        session.commit()
        session.refresh(routeur)
        return routeur


@app.put("/Routeur/{host_id}")
def update_Routeur(host_id: int, updated_host: Routeur):
    engine = configure_db_routeur()
    with Session(engine) as session:
        routeur = session.get(Routeur, host_id)
        if not routeur:
            raise HTTPException(404, "Host not found")
        routeur.hostname = updated_host.hostname
        routeur.ip = updated_host.ip
        session.add(routeur)
        session.commit()
        session.refresh(routeur)
        return routeur


@app.delete("/Routeur/{host_id}")
def delete_Routeur(host_id: int):
    engine = configure_db_routeur()
    with Session(engine) as session:
        routeur = session.get(Routeur, host_id)
        if not routeur:
            raise HTTPException(404, "Host not found")
        session.delete(routeur)
        session.commit()
        return {"ok": True}