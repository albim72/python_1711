import dis
from functools import wraps
def deco_out(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        return print(func(*args, **kwargs))
    return wrapper


@deco_out
def add(a, b):
    return a + b

add(b=6,a=4)

print(add.__name__)
print(hasattr(add, '__wrapped__'))

r = add.__wrapped__(2,4)
print(r)

print("_" *60)
dis.dis(add)

print("_" *60)
dis.dis(add.__wrapped__)
