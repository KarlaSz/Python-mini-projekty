#klasa ktora reprezentuja osobe
#klasa zawiera tez metody zwykle i specjalne
#dlatego ze uzywamy tych metod musza miec to slowo self zeby wiadomo,ze jakie imie ma ta osoba bo to cech przypisany jest name

#obikety moga miec w srodku metody i moga sluzyc do odwolywania poszczegolnych wlasciwosci albo modyfikowac
class Person:
    def __init__(self, name):
        self.name = name

    #metody specjalne wyzej niz zwykle
    #str wywowylany jest gdy robimy print na obiekciie
    def __str__(self):
        return f'Nazywam sie {self.name}'

    def greet(self):
        return f'Hello, {self.name}'

    def farewel(self):
        return f'Goodbye, {self.name}'

halinka = Person('Halinka')
#tutaj trzeba uzyc printa bo jest to zwykla metoda, a nie specjalna ktora zwraca stringa

obje_str = str(halinka)
print(obje_str)
print(halinka.greet())
print(halinka.farewel())

#obiekt na metodzie specjalnie, krocej mozna zapisac nie potrzeba dodatkowej kompozycji sklejania metod z obiektem
print(halinka)