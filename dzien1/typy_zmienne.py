a = 10
b = 10
c = 10

# a już nie jest dostępem do 10.. staje się dostępem do 15
a = 15

print(a)
print(b)

print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(c))

d:int = 10.4
print(d)
print(type(d))

d = "jedynka"
print(d)
print(type(d))

