import dis

#funkcja wyzszego rzedu - fukcja której prametrem jest inna funkcja
def apply_twice(fn,x):
    return fn(fn(x))

def inc(n):
    return n+1

print(apply_twice(inc,5))
print(apply_twice(inc,7.85))
print(apply_twice(inc,-0.99))

print(apply_twice(lambda v:v*2,3))

print("===== bytcode apply_twice =====")

dis.dis(apply_twice)

print("===== bytcode inc =====")
dis.dis(inc)

print("===== bytcode lambda =====")
dis.dis(lambda v:v*2)
