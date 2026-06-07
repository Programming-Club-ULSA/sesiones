class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

calc = Calculator()
a = 5
b = 3

print(f"Numero A: {a}")
print(f"Numero B: {b}")

print(calc.add(a, b))