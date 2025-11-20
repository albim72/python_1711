import threading
import time

def worker(name,delay):
    for i in range(3):
        time.sleep(delay)
        print(f"wątek {name}: krok {i+1}")


#tworzymy dwa wątki
t1 = threading.Thread(target=worker, args=("A", 1))
t2 = threading.Thread(target=worker, args=("B", 1.5))

#start wątków
t1.start()
t2.start()

#czekanie na zamknięcie obu
t1.join()
t2.join()

print("wszystkie wątki zostały zamknięte")
