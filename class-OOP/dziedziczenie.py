#jesli dziedzimy po jakiejs klasie to asza klasa
# ktora dziedziczy to bedzie posiadac wszystkie metody i wlasciwosci
# tej klasy z ktorej chcemy dziedziczyc

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def dispay_info(self):
        return f"Name: {self.name}, Age: {self.age}"

#nowa klasa ktora dziedziczy dane personalne dla praocwnika
class Employee(Person):
    def work(self):
        return f'{self.name} is working as an employee'

    def dispay_info(self):
        #to super jest do tego uzywany,zeby return nie byl pomijany bo jest
        # dublem tej samej metody ze zrodlowej klasy bo tam ta sama metoda
        # zostala uzyta i obok widac tez niebieska (w pycharmie) strzalke ktora naiwguje do tego
        return f'{super().dispay_info()} - Role: Employee'

class Engineer(Person):
    def work(self):
        return f'{self.name} is working as an engineer'

    def dispay_info(self):
        return f'{super().dispay_info()} - Role: Engineer'

# employee = Employee('Anna Kowalczyk', 30)
employee = Engineer('Anna Kowalczyk', 30)

print(employee.dispay_info())
print(employee.work())