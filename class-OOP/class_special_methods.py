# Specjalne metody w Pythonie, nazywane również
# metodami magicznymi lub dunder methods (od "double underscore"),
# to metody zdefiniowane w klasach, które mają specjalne znaczenie.
# Są otoczone podwójnymi podkreśleniami (__), np. __init__, __repr__.
# Python używa ich do definiowania zachowań wbudowanych funkcji,
# operatorów i wbudowanych mechanizmów języka

#wywolywane sa nie jawnie i wtedy kiedys cos robimy

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
    #1. wtedy gdy zamieniamy obiekt na string i wyswietlenie jego zawartosci
    def __str__(self):
        # return f'W banku jest {self.amount}'
        return self.get_info()

    # jest podobna do str metody,ale nie zawsze string jest wywolywany
    #wtedy gdy odwolujemy sie do listy i obiekty sa elementami tej listy, wiec mozemy je zmienic na stringi
    # sa dwie metody bo roznia sie wywolywanie, w zalezno od danej sytuacji co chcemy uzyskac
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

    #kazda metoda specjlan musi cos zwracac i zarazem jest poleceniem operacji i taka warunkiem


karo_account = BankAccount('Karo',100)
saving_account = BankAccount('Oszczednosci',300)
print(karo_account)

accounts = [karo_account,saving_account]
accounts.sort(reverse=True)
print(accounts)

group_account = karo_account + saving_account
print(group_account)

##ine metody
# 4. __len__ – Długość obiektu
# Definiuje zachowanie wbudowanej funkcji len() dla obiektów klasy.
#5 __getitem__, __setitem__, __delitem__ – Dostęp do elementów
# Używane do implementacji zachowania jak w listach lub słownikach.
#6. __eq__, __lt__, __le__, __gt__, __ge__, __ne__ – Porównywanie obiektów
# Definiują zachowanie operatorów porównania (==, <, >, itd.).
#  __add__, __sub__, __mul__, __truediv__ – Operatory arytmetyczne
# Definiują zachowanie operatorów matematycznych.