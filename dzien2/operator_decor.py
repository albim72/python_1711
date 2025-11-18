def add(a,b):
    return a+b

"""
dekorator ->
1. przed wywołamniem fukcji pomnoszy argumenty przez factor
2. po wywołaniu funckji podzieli wynik przez factor
3. przepuści wszystko przez skalę - -ale wnętrze funckji będzie liczyło na inncyhb liczbach
"""

def scale(factor):
    def decorator(func):
        def wrapper(*args,**kwargs):
            #1. skalowanie argumentów
            scaled_args = [a*factor for a in args]

            print(f"[SCALE] factor = {factor}")
            print(f"[SCALE] oryginalne args = {args}")
            print(f"[SCALE] skalowane args = {scaled_args}")

            # wywołanie oryginalnej funckji
            result = func(*scaled_args,**kwargs)

            print(f"[SCALE] surowy wynik = {result}")
            #odwrócenie skalowania wyniku
            final_result = result/factor

            print(f"[SCALE] wynik po odskalowaniu = {final_result}")
            return final_result
        return wrapper
    return decorator

@scale(10)
def add(a,b):
    return a+b

print(add(5,3.5))
