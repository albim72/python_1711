def greet(name,
          age,
          city="Warszawa", # parametr z wartością domyslną
          prefix = "Hello", # domyślmny prefix komunikatu
          *skills, # dodatkowe argumenty pozycyjne
          polite=True, #parametr po *args - tylko nazwany
          **meta #słownik dodatkowych parametrów
          ):
    print(f"{prefix}, {name}! You are {age} years old, you live in {city}.")
    if skills:
        print(f"Skills: {', '.join(skills)}")
    if polite:
        print("Have a nice day!")
    if meta:
        print(f"Meta: {meta}")


greet("Marcin",52)
greet("Ula",35,"Kraków")
greet("Piotr",44,"Gdańsk","Hi","Python","Java","C++",polite=False)
greet("Marcin",50,polite=False)
greet("Ala",22,meta={"language":"Python","country":"Poland"})
greet("Konrad",67,meta={"language":"Python","country":"Poland"},polite=False)

print("___ metapytania ___")
#parametry domyślne ->
print(greet.__defaults__)
#parametry domyślne po *args
print(greet.__kwdefaults__)
#nazwa wszytkich parametrów lokalnych
print(greet.__code__.co_varnames)
