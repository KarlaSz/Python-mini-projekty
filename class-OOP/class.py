#klasy - dodaj funkcjonalnosci, sa sposobem na uporzadkowanie
#instancja jest konkretnym egzemplarzem klasy. 
#Wyobraź sobie klasę jako szablon, plan lub przepis na stworzenie obiektu. Instancja to już gotowy obiekt, stworzony na podstawie tego szablonu.

class Car:
    #metody w klasach, sa podobne do funkcji trzeba je tez wywolac,a nie tylko zdefiniowac
    def foo(self):
        print('Hello')

# kropka w py nadaje kierunkowosc, wiec klasa Car wywoluje funkcje foo
Car().foo()

#klasy daja mozliwosc budowania instacji klasy czyli kopu


#instacja klasy Car i zapisa do zmiennej
x = Car()
x.foo()


#oprocz funkcji w klasie sa tez magic methods - funkcje zarezerwowane dla py i kazda ma inne uporzadkowanie
#__init__(self) paametry trzeba podac zawsze kiedy bedzie tworzona nowa instancja, 
#funkcja wykona sie zawsze kiedy bedzie tworzona nowa instancja

class Car:
    def __init__(self,brand):
        # print(brand)
        #wewnatrz klas tworze zmienna 
        #self reprezentuej dana instancje
        self.brand = brand
        
    def info(self):
        print("Brand:" , self.brand)
        
#mozna utowrzyc dowolna liczbe instancji       
first_car = Car('Opel')        
second_car = Car('Skoda')       

first_car.info()

second_car.info() #to samo inaczej zapisane, patrz nizej
Car.info(second_car) #to samo inaczej zapisane, patrz wyzej


