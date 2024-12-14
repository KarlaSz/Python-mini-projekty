#obiekt to zmienna w klasie, szufladka z dana instrukcja czyli jakas jednostka
#towrzyc osobne pliki dla kazdej klasy, 1 klasa jeden plik

#ustrukturyzowanie obiektu o adresie
class Address:
    def __init__(self,street:str, street_number:int, postal_code:str, city:str):
        self.street = street
        self.street_number = street_number
        self.postal_code = postal_code
        self.city = city

   #strukturalne dane dla adresu
address1 = Address(
    'Zofi Nałkowskiej',
    21,
    '87-888',
    'Gdynia'
)

address2 = Address(
    'Kochanowskiego',
    30,
    '65-868',
    'Warszawa'
)

class Flat:
    #konstruktor, init - rozpoczecie
    def __init__(self, address:Address, size:float, rooms:int):
        print('Tworze nowe mieszkanie')

        #self odnosi sie do kokretego obiektu na ktorym odnosze do adresow, na ktorym jest wywolane
        self.address = address
        self.rooms = rooms

#obiekt powstawly z danej klasy, schemat obiektu to nowa zmienna z gotowym przepisem czyli klasa
#obiekt to coś, co powstaje na podstawie tego przepisu to znaczy klasy
my_flat = Flat(address1, 60,5)
print(my_flat)
print(my_flat.address.city)

your_flat = Flat(address2, 80, 10)
print(your_flat)

#kompozycja - komponowanie obiektow ze soba
print(your_flat.address.city)