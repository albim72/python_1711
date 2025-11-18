import dis
#przykład 1

def log_calls(func):
    def wrapper(*args,**kwargs):
        print(f'Function {func.__name__} called with {args} and {kwargs}')
        result =  func(*args,**kwargs)
        print(f'Function {func.__name__} returned {result}')
        return result
    return wrapper

def add(a,b):
    return a+b

log_add = log_calls(add)
log_add(1,2)

@log_calls
def mul(a,b):
    return a*b

mul(2,3)


#przykład najprostszy dekorator

def simple_decorator(func):
    def wrapper():
        print("coś przed funkcją...")
        func()
        print("coś za funkcją...")
    return wrapper

def wiadomosc():
    print("to pierwsza wiadomość")

w = simple_decorator(wiadomosc)
w()

@simple_decorator
def hello():
    print("hej")

hello()

#dis - logcolls

print("===== log_calls =====")
dis.dis(log_calls)

print("===== w =====")
dis.dis(w)
