import csv

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = int(age)
        self.city = city

    @classmethod
    def from_csv(cls, path):
        people = []

        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                person = cls(
                    row['Name'],
                    row['Age'],
                    row['City']
                )
                people.append(person)
            return people

    def info(self):
        return f'{self.name} is {self.age} years old and lives in {self.city}'

people = Person.from_csv('dane/people.csv')

for p in people:
    print(p.info())
