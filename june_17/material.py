from dataclasses import dataclass


@dataclass
class Material:
    description: str
    category: str
    price: float

materials = [
    Material(description="Oil Filter", category="Engine", price=15.99),
    Material(description="Brake Pads", category="Brakes", price=45.50),
    Material(description="Spark Plugs", category="Ignition", price=9.99),
    Material(description="Air Filter", category="Engine", price=12.75),
    Material(description="Battery", category="Electrical", price=120.00),
    Material(description="Tire", category="Wheels", price=80.00)
]