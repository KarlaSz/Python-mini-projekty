
# zad 0

#przygotuj funkcje sprawdzajaca czy osoba o
# przekazanym wieku jest osoba pelnoletnia


def is_adult(age: int) -> bool:
    return  age >= 18

#wszystkie funkcje ktore sa testami musza miec prefiks test_

def test_is_adult():
    #czy jest pelnoletni
    #given - wszystko co mamy do przerpowadzanie testu
    age = 18

    #when - to co sie wydarza i daje wynik
    result = is_adult(age)

    #then - spr. poprawnosc
    assert result
    #assert czyli to jest za nim jest prawda to test przejdzie
    #jak nie jest to wtedy test  nie przeszedl
    assert  is_adult((20))

def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(3)

#testy to swiedna dokumentacja, bo opisuje jak co dziala

