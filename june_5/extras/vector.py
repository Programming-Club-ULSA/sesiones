class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Define el operador de suma
    def __add__(self, other):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    # Define el como se ve visualmente (ej. en el "print")
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
v_total =  v1 + v2

print(f"{v1} + {v2} = {v_total}")

# En realidad el operador de suma es un metodo en si mismo
# Por lo que hacer a + b, es lo mismo que a.__add__(b)

print(v1 + v2)
print(v1.__add__(v2))


# Esto aplica tambien a los primitivos del lenguaje
print(2 + 3)
print((2).__add__(3))