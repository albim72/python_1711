import dis

class KontoBankowe:
    def __init__(self,wlasciciel: str, saldo: float = 0.0):
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    @property
    def wlasciciel(self) -> str:
        return self._wlasciciel

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self,kwota: float):
        if kwota < 0:
            raise ValueError("Saldo musi być dodatnie!")
        self._saldo = kwota

    @saldo.deleter
    def saldo(self):
        print("saldo zostało wyzerowane!")
        self._saldo = 0.0
        # del self._saldo

def use(k):
    return k.wlasciciel

k = KontoBankowe("Jakub",5000)
print(k.wlasciciel)

dis.dis(use)

k.saldo = 10000
print(k.saldo)

del k.saldo
print(k.saldo)
