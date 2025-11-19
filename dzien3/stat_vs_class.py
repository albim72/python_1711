from abc import ABC, abstractmethod

class Animal(ABC):
    counter = 0

    @abstractmethod
    def liczbalat(self,n):
        pass

    def __init__(self, name):
        self.name = name
        Animal.counter += 1

    @classmethod
    def create(cls, name):
        # używa cls → tworzy OBIEKT poprawnej klasy
        return cls(name)

    @staticmethod
    def create_static(name):
        # static NIE ma dostępu do cls → ZAWSZE tworzy Animal,
        # nawet jeśli wywołasz go na podklasie!
        return Animal(name)


class Dog(Animal):
    def liczbalat(self,n):
        print(f"Bwiek psa: {n}")


# TEST
a1 = Dog.create("Reksio")          # classmethod
a2 = Dog.create_static("Burek")    # staticmethod

print("type(a1):", type(a1))
print("type(a2):", type(a2))

print("isinstance(a1, Dog):", isinstance(a1, Dog))
print("isinstance(a2, Dog):", isinstance(a2, Dog))
