from dataclasses import dataclass
from enum import Enum
from service import Service, services
from client import Client

@dataclass
class Workshop:
    capacidad: int
    mechanics: list[Mechanic]

@dataclass
class Mechanic:
    name : str
    age : int
    address: str

taller_juan = Workshop(capacidad=5, mechanics=[
    Mechanic(name="Juan Perez", age=30, address="El Viejo, Chinatown"),
    Mechanic(name="Maria Lopez", age=28, address="Nindiri, Masaya"),
])







