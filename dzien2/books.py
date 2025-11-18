class Book:
    __kolor = "czerwony"

    def __init__(self, title, author, price, pages, bookstore_nb):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.bookstore_nb = bookstore_nb
        self._binding = "miękka"
        self.newbook()

        # _ -> protected
        # __ -> private

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.price}, {self.pages}, {self.bookstore_nb})"

    def newbook(self):
        print("Nowy obiekt klasy Book został utworzony!")

    def get_bind(self):
        return self._binding

    def set_bind(self, value):
        self._binding = value

    def cena_rabat(self,procent):
        self.price = self.price - (self.price * procent / 100)
        return self.price

    def obwoluta(self):
        return self.__kolor

    def info(self):
        komunikat = "nfgksdnvkdsnvksdmvm"
        return komunikat 



bk1 = Book("Hobbit","JRR Tolkien",45,212,[67,35,78])
print(bk1)

# bk1.binding = "twarda"
# print(bk1.binding)

bk1.set_bind("twarda")
print(bk1.get_bind())

print(bk1.cena_rabat(10))
print(bk1.obwoluta())

bk2 = Book("ABC Kulturysty","Jan Kowalski",56,415,[765,345,4363])
print(bk2)

bk2.set_bind("lakierowana")
print(bk2.get_bind())

print(bk2.cena_rabat(15))
print(bk2.obwoluta())

bk2.info()





