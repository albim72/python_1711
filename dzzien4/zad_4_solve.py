from dataclasses import dataclass
import numpy as np
import pandas as pd

@dataclass
class Book:
    title: str
    author: str
    price: float
    year: int

    def info(self):
        return f"{self.title} ({self.year})"


def main():
    # 1. Utworzenie obiektów Book
    books = [
        Book("Harry Potter", "J.K. Rowling", 39.90, 1997),
        Book("Hobbit", "J.R.R. Tolkien", 45.00, 1937),
        Book("Wiedźmin", "A. Sapkowski", 41.99, 1986),
    ]

    # 2. Obliczenie średniej ceny
    avg_price = sum(b.price for b in books) / len(books)

    # av_price = sum(books)
    np_price = np.array([b.price for b in books])
    print(f"suma: {sum(np_price)}")

    tb = np.array([[5,3],[86,5],[7,46]])
    print(tb)
    print(tb.sum(axis=0))
    print(tb.sum(axis=1))

    print(type(np_price))

    a1 = [43,54,7]
    a2 = [12,34,56]

    a = a1+a2
    print(a)

    na1 = np.array(a1)
    na2 = np.array(a2)

    na = na1+na2

    print(na)


    # 3. Wypisanie danych
    for b in books:
        print(b.info())

    print(f"Średnia cena: {avg_price:.2f} zł")

    # Konwersja listy obiektów Book do DataFrame
    df = pd.DataFrame([b.__dict__ for b in books])

    # Suma po polu "price"
    total_price = df["price"].sum()

    print(f"Suma cen: {total_price}")


if __name__ == "__main__":
    main()
