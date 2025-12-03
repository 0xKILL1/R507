from typing import Optional
from sqlmodel import SQLModel, Field, Column, JSON

class Equipement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hostname: str
    ip: str

class Ordinateur(Equipement):
    ram : str
    disk: list[dict] = Field(default_factory=list, sa_column=Column(JSON))

class Routeur(Equipement):
    nb_interface: int = None
    ip : Optional[list[dict]] = Field(default_factory=list, sa_column=Column(JSON))
