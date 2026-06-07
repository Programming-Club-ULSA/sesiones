class Teacher:
    def __init__(self, name, age, subject, profession):
        self.name = name
        self.age = age
        self.subject = subject
        self.profession = profession
    
    def introduce(self):
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años, enseño {self.subject} y soy {self.profession}")


aarock = Teacher("Aaron Cisneros", 36, "Lenguaje de Programación II", "Ing. en Sistemas")
aarock.introduce()

toval = Teacher("Christian Toval", 33, "Sistemas Operativos", "Ing. en Sistemas")
toval.introduce()