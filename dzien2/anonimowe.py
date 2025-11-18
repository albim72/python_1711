from functools import reduce

#przykład 1
print((lambda x: x*2)(10))

#przykład 2 - lambda przypisana do zmiennej
double = lambda x,y,z=9,u=8: x-12+2*y/z+u
print(double(1,2))
print(double(1,2,3,2))
print(double(1,2,z=3))
print(double(1,z=3,y=2))

#zostaw deafault -> z ale zmień u!!
print(double(1,2,u=10))

#przykład 3 - lambda z funkcją map
nums = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, nums))
print(doubled)


def dodaj(c):
    return c+3

trojka = list(map(dodaj, nums))
print(trojka)

er = set(map(lambda x: x*6, nums))
print(er)

#przykład 4 - lambda z funkcją filter
lb = (433,62,6,89,35,9,0,3,6,-34,6)
even = tuple(filter(lambda x: x%2==0, lb))
print(even)

def warunek(a,b):
    return a%2==0 and b%2==0 and a+b>0

print(warunek(5,6))
print(warunek(4,6))
print(warunek(-10,6))

#przykład 5 - lambda z funkcją reduce

result = reduce(lambda x,y: x+y, lb)
print(result) # result = lb[0] + lb[1] + ... + lb[n]

result = reduce(lambda x,y: (x-y)/2, lb)
print(result)

#przykład 6 - lambda zwracająca lambdę
make_multi = lambda n: (lambda y: n*y)

t3 = make_multi(3)
t5 = make_multi(5)

print(t3(7))
print(t5(7))
print(make_multi(5)(10))

#przykład lambda w słownikach
actions = {
    "add": lambda x,y: x+y,
    "mul": lambda x,y: x*y,
    "div": lambda x,y: x/y,
    "sub": lambda x,y: x-y,
    "pow": lambda x,y: x**y,
    "mod": lambda x,y: x%y,
    "neg": lambda x: -x,
    "inv": lambda x: 1/x,
    "abs": lambda x: abs(x),
    "sqrt": lambda x: x**0.5
}
print(actions["add"](7,4))
print(actions["sub"](1,2))
print(actions["mul"](1,2))
print(actions["div"](1,2))
print(actions["pow"](1,2))
print(actions["mod"](1,2))
print(actions["neg"](1))
print(actions["inv"](1))
print(actions["abs"](1))
print(actions["sqrt"](1))

#przykład lambda w list comprehension

lc = [3*g for g in range(3_000_001)]
print(sum(lc))
print(lc[:100])
print(lc[2_999_800:])
