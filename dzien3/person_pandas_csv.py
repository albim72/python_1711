import pandas as pd

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = int(age)
        self.city = city

    @classmethod
    def from_csv(cls, path):
        df = pd.read_csv(path)
        people = [
            cls(row["Name"],row["Age"],row["City"])
            for _, row in df.iterrows()
        ]
        return people

    def info(self):
        return f'{self.name} is {self.age} years old and lives in {self.city}'

people = Person.from_csv('dane/people.csv')

for p in people:
    print(p.info())
