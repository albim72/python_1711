def czy_palindrom(slowo: str) -> bool:
    """
    Zwraca True, jeśli napis jest palindromem (ignoruje wielkość liter).
    Przykłady:
        czy_palindrom("kajak") -> True
        czy_palindrom("python") -> False
        czy_palindrom("Anna") -> True
    """
    s = slowo.casefold()  # lepsze niż .lower() dla porównań niezależnych od języka
    return s == s[::-1]

print(czy_palindrom("kajak"))    # True
print(czy_palindrom("python"))   # False
print(czy_palindrom("Anna"))     # True
