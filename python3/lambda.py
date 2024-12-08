#programowanie funkcyjne - wyrazenie lambda, funkcja anonimowa 

def funkcja(f, liczba):
    return f(liczba)


    #tworzymy funkcje ktora nie ma swojej nazwy i parametry na jakich ma dzialac i jakie przyjmuje 
    #x to 1 parametr i po : jaka operacja ma byc wykonana czyli to zwracamy, a 3 to drugi argument czyli liczba
print(funkcja(lambda x: x * x, 3))

#rozne sposoby zapisu lambdy

#I
def kwadrat(x):
    return x * x
    
print(kwadrat(5))

#dla funkcji lanbda chce 1 parametr i od razu po jej deklaracji przekazujemy parametr
#II
wyn = (lambda x: x * x)(5)
print(wyn)

#III
lam = lambda x: x * x
print(lam(5))

#po : jest cialo lambdy
lam2 = lambda x, y: x * y
print(lam2(3,4))
print((lambda x, y: x + y)(5,6))

