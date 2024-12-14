# Enkapsulacja = ukrywanie,  podkreslenia przy odwolaniach do self i cechy
#jest to iformacja dla programisty ze sa to dane prywatne chronione i tego nie stosowac

class Account:
    def __init__(self):
        self._amount = 0

    def deposit(self, amount:float):
        self._amount += amount

    def withdraw(self, amount:float):
        if self._amount < amount:
            raise ValueError("You don't have enought money to withdraw")

        self._amount -= amount
        return {
            'amount_left': self._amount,
            'amount_withdraw': amount
        }

try:
    my_account = Account()
    my_account.deposit(1000)
    my_account.withdraw(900)
    #tego nie ruszamy, wiec nie uzywac tego w wywolaniach, tak jakby tego nie bylo
    # my_account._amount = 200
    result = my_account.withdraw(900)
    print(result)
except ValueError as message:
    print(message)

# Enkapsulacja to jedno z podstawowych pojęć w programowaniu obiektowym (OOP). Polega na ukrywaniu szczegółów implementacji obiektu oraz udostępnianiu tylko niezbędnych interfejsów do komunikacji z nim. Dzięki enkapsulacji, dane i funkcje związane z obiektem są zamknięte w jednym miejscu i dostęp do nich jest kontrolowany, co zapewnia większą bezpieczeństwo oraz modularność.
#
# Kluczowe cechy enkapsulacji:
# Ukrywanie danych (data hiding):
#
# Enkapsulacja pozwala na ukrycie wewnętrznych szczegółów implementacji obiektu przed użytkownikami klasy (np. innymi obiektami lub kodem poza klasą). To oznacza, że nie trzeba znać szczegółów działania obiektu, by go używać. Na przykład, nie musisz wiedzieć, jak działa funkcja wewnątrz klasy, wystarczy, że znasz jej interfejs.
# Publiczny interfejs:
#
# Zamiast bezpośrednio manipulować danymi obiektu, użytkownicy klasy używają publicznych metod (tzw. getterów, setterów lub innych metod), które zapewniają dostęp do tych danych w sposób kontrolowany. Dzięki temu można kontrolować, jak dane są modyfikowane lub odczytywane.
# Ochrona danych:
#
# Enkapsulacja zapewnia, że dane są chronione przed nieautoryzowanymi modyfikacjami. Dzięki ukrywaniu wewnętrznych danych przed bezpośrednim dostępem, łatwiej jest zarządzać i monitorować sposób, w jaki te dane są używane.

class Osoba:
    def __init__(self, imie, wiek):
        self._imie = imie  # "prywatny" atrybut (konwencja)
        self.__wiek = wiek  # "bardzo prywatny" atrybut (prywatny w nazwie)

    def get_wiek(self):
        return self.__wiek  # dostęp do prywatnego atrybutu poprzez metodę

    def set_wiek(self, wiek):
        if wiek >= 0:  # walidacja danych
            self.__wiek = wiek
        else:
            print("Wiek musi być większy lub równy 0.")

    def przedstaw_sie(self):
        print(f"Cześć, mam na imię {self._imie} i mam {self.get_wiek()} lat.")

# W klasie Osoba mamy:
#
# Getter i Setter dla __wiek, które pozwalają na kontrolowanie dostępu do tej zmiennej oraz zapewniają walidację danych (np. upewniają się, że wiek nie jest ujemny).
# Przedstawienie się za pomocą metody przedstaw_sie, która wykorzystuje dane z obiektu.