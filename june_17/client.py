from dataclasses import dataclass


@dataclass
class Client: 
    name : str
    identifier: str
    contact : str

cliente_1 = Client(name="Carlos Sanchez", identifier="281-230403-1000Z", contact="1122-8877")