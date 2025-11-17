#przykład 1
def info():
    print("To jest funkcja info()")

info()

#przykład 2
def f(x):
    return 3*x+1

print(f(3))

g = f

print(g(3))

#przykład 3 - closures

def make_counter():
    count = 0 # zmienna z zewnętrznego scope'a

    def inc():
        nonlocal count# korzystamy z count z zewnętrznej funkcji  -> free variable
        count += 1
        return count
    return inc #zwracamy funckję która pamięta count

counterA  = make_counter()
counterB  = make_counter()
counterC = make_counter()

print(counterA())
print(counterB())
print(counterA())
print(counterC())
print(counterB())
print(counterA())
print(counterB())

print(counterA.__closure__)
print(counterB.__closure__)
print(counterC.__closure__)

def single_inc():
    count = 0
    count += 1
    return count

s = single_inc()
print(s)
print(s)
print(s)

#przykład 4

def make_multiplier(n):
    def mul(x):
        return n*x
    return mul

t2 = make_multiplier(2)
t5 = make_multiplier(5)
print(t2,t5)

print(t2(7))
print(t5(7))

print(make_multiplier(5)(10))

