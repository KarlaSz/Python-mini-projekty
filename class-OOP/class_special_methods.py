# Specjalne metody w Pythonie, nazywane również
# metodami magicznymi lub dunder methods (od "double underscore"),
# to metody zdefiniowane w klasach, które mają specjalne znaczenie.
# Są otoczone podwójnymi podkreśleniami (__), np. __init__, __repr__.
# Python używa ich do definiowania zachowań wbudowanych funkcji,
# operatorów i wbudowanych mechanizmów języka

#metody specjalne - magic methos, zawsze maja 2 podkreslenia z przodu i z tylu

class BankAccount:
    # metoda specjalna, konstruktor
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount

    def get_info(self):
        return f'Konto: ({self.title}), saldo {self.amount}'

    #wyswietlanie obiektu, opis zamiast info systemowe na jakiej pozycji w pamieci jest obiekt
    #metoda specjalna str sluzy do zwracania stringa, a nieprintowania go
    def __str__(self):
        # return f'W banku jest {self.amount}'
        return self.get_info()

    # Reprezentacja
    # obiektu
    # dla
    # debugowania
    def __repr__(self):
        return self.get_info()

    #sortowanie less then - lt, sortowanie obiekty
    def __lt__(self, other):
        return self.amount < other.amount

    #typ zmiennej other, dodawanie obiektow do siebie
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"unsupported operand type(s) for +: 'BankAccount' and {type(other)}")

        new_account = BankAccount(
            self.title +','+other.title,
            self.amount + other.amount)

        return new_account


karo_account = BankAccount('Karo',100)
saving_account = BankAccount('Oszczednosci',300)
print(karo_account)

accounts = [karo_account,saving_account]
accounts.sort(reverse=True)
print(accounts)

group_account = karo_account + saving_account
print(group_account)