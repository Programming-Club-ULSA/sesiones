from dataclasses import dataclass
from enum import Enum
from material import Material, materials
from client import Client, cliente_1

class ServiceType(Enum):
    Diagnosis = 1
    Repair = 2
    Maintenance = 3

@dataclass
class Service:
    type : ServiceType
    description: str
    price: float
    client: Client

    # En dias
    estimated_time: int
    materials_used = list[Material]

services = [
    Service(
        client=cliente_1,
        type=ServiceType.Diagnosis, 
        description="Engine diagnosis", 
        price=50.00, estimated_time=1, 
        materials_used=[materials[0], materials[3]]
    ),
]