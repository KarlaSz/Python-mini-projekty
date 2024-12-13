#Przygotuj funkcje, ktora na podstawie wysokosci
# oraz dlugosci podstawy wyswietli (print) pole trojkata
# wzor P = (a * h) / 2

#zad - jak przetestowac wyprintowana zawartosc


def get_triangle_field(base: int, heght:int) -> float:
    print(0.5 * base * heght)

#capsys - capture system czyli pobiera jakies eventy systemowe, np. to co zwraca program albo jego bledy
def test_triangle_area(capsys):
    #try
    base = 10
    height = 8

    #when
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    #then
    assert  out == '40.0\n'
    #gdy uzywam out to musze brac pod uwage,ze jest to ostatni element wiersza i zawiera znak konca wiersza

