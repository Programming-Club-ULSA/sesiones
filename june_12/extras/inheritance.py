from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Student(Person):
    student_id: int
    major: str
    entry_year: int

@dataclass
class Professor(Person):
    title: str
    salary: float
    years_of_experience: int


ari = Student(
    name="Ari",
    age=20,
    student_id=123,
    major="Ingeniería Cibernética",
    entry_year=2023
)

aarock = Professor(
    name="Aaron Cisneros",
    age=35,
    title="Ingeniero en Sistemas",
    salary=900,
    years_of_experience=10
)

print(ari)
print(aarock)