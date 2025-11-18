import dis

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self):
        self.value += 1
        return self.value

def use_counter(counter):
    c = Counter(10)
    c.inc()
    c.inc()
    c.inc()
    return c.value

print("====== dis Counter.__init__ ======")
dis.dis(Counter.__init__)

print("====== dis Counter.inc ======")
dis.dis(Counter.inc)

print("====== dis use_counter ======")
dis.dis(use_counter)

print(use_counter(Counter()))

