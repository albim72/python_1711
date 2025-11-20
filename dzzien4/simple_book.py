from dataclasses import dataclass
from datetime import datetime
import dis

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    year: int = 2024

    # def __init__(self, title, author):
    #     self.title = title
    #     self.author = author
    #
    # def __repr__(self):
    #     return f"Book({self.title!r}, {self.author!r})"

    #walidacja wydawnictw (1960,2025)

    def __post_init__(self):
        current_year = datetime.now().year
        min_year = current_year - 60
        if not (min_year <= self.year <= current_year):
            raise ValueError(f"Year must be between {min_year} and 2025")


b1 = Book("Python od podstaw", "Jan  Kot", 250, 54.88)
print(b1)

b2 = Book("Java od podstaw", "Jan  Kot",311,64.3,2025)
print(b2)

print("++++++++++  dis -> Book +++++++++++")
dis.dis(Book.__init__)

