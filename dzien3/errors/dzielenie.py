try:
    x = int(input("Podaj liczbę: "))
    print(f"wynik = {10/x}")
except ValueError:
    print("Błąd: to nie jest liczba")
except ZeroDivisionError:
    print("Błąd: nie wolno dzielić przez zero")
except Exception as e:
    print(e)
