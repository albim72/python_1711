Person = type('Person',
              (object,),
              {
                    "city":"Kraków",
                    "hello": lambda self: print("Hello, my city", self.city)
              }
        )

p = Person()
p.hello()

print(type(p))
print(id(p))
