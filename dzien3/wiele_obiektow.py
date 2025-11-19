class Product:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    #ctrl + /
    @classmethod
    def many(cls,names):
        return [cls(n) for n in names]

    # @staticmethod
    
    # def many(names):
    #     return [Product(n) for n in names]


names = ["mleko", "woda", "chleb","masło","dżem","szynka","serek","jogurt"]
products = Product.many(names)
print(products)

for p in products:
    print(p.get_name())
