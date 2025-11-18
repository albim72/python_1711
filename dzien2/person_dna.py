import dis

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(Person)

    def __repr__(self):
        return f"Person({self.name}, {self.surname})"

    def greet(self):
        print(f"Hello, my name is {self.name} {self.surname} and I'm {self.age} years old.")

p1 = Person("John", "Doe", 30)
p1.greet()

print("====== dis Person.__init__ ======")
dis.dis(Person.__init__)

print("====== dis Person.greet ======")
dis.dis(Person.greet)

print("====== dis wywołania p.greet() w funckji pomocniczej ======")

def call_greet(obj):
    obj.greet()

dis.dis(call_greet)


call_greet(p1)

print(p1)
print(p1.__dict__)
