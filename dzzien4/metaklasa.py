import dis

d = 89
print(type(d))

class MKlasa:
    def __init__(self, x):
        self.x = x

print(type(MKlasa))

class MKlasa2(type):
    def __new__(cls,name,bases,attrs):
        attrs['info'] = lambda self:f"Jestem obiektem klasy {name}"
        return type.__new__(cls,name,bases,attrs)

class MKlasa3(metaclass=MKlasa2):
    pass

p = MKlasa3()
print(p.info())

class Person(MKlasa3):
    def info(self):
        print("to jest lokalna metoda -> info ...")

os = Person()
print(os.info())


class Dodatek:
    pass

class Opis(Dodatek,Person):
    def opis(self):
        print("To jest prosta metoda klasy Opis....")

op = Opis()
op.opis()
print(op.info())

print("__ doc__")
print(Opis.__doc__)

print("__ doc__")
print(Opis.__doc__)

print("__ MKlasa2")
print(MKlasa2.__new__)


def make_class():
    class NewPerson(metaclass=MKlasa2):
        x=10

        def hello(self):
            return "Hello"
    return NewPerson


dis.dis(make_class)
