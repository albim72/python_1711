class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)

    def __repr__(self):
        return f"<Person: {self.name}, {self.age}>"


p1 = Person("John", 36)
print(p1.name, p1.age)
print(repr(p1))
print(id(p1))

p2 = Person.from_birth_year("Jane", 1990)
print(p2.name, p2.age)
print(repr(p2))
print(id(p2))
