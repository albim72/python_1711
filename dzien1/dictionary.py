#twworzenie słownika
person = {
    "name": "John",
    "age": 27,
    "role": "developer"
}

print(person)
print(type(person))

print(person["name"])
print(person["age"])

#nowa para klucz-wartość
person["country"] = "Poland"

print(person)

person["age"] = 30
print(person)

print("name" in person)
print("xyz" in person)
print("John" in person.values())

#iterowanie
for key,value in person.items():
    print(f"klucz: {key}, wartość: {value}") #f-string służy do ekstrapolacji stringów

config = {
    "db": {
        "host": "localhost",
        "port": 3306
    },
    "debug": True
}

print(config)
print(config["db"]["host"])
