#przygotuj funkcje, ktora bedzie sortowala otrzymywana liste imion:
# - w kolejnosci alfabetycznej pierwszej litery,
# - w kolejnosci alf. ostatniej litery,
# - wedlug dlugosci imienia
from operator import length_hint

import pytest


def sort_by(names, first_letter=False, last_letter=False , length=False):
    if first_letter:
        names.sort()

    if last_letter:
        names.sort(key=lambda name: name[::-1])

    if length:
        names.sort(key=len)

    return names


class TestSort:
    #dekorator
    @pytest.fixture
    def names(self):
        return ['Alina', 'Ewa', 'Paulina', 'Maciej']


    #sortowanie po 1 lieterze
    def test_sort(self,names):
        #given, mam dekoratora wyzej,wiec moge skozystac z fixture po przeicnku do metod testu funkcji
        # names = ['Alina', 'Ewa', 'Paulina', 'Maciej']

        #when
        sorted_names = sort_by(names, first_letter = True)

        #then
        assert sorted_names == ['Alina', 'Ewa', 'Maciej','Paulina' ]

    #sortowaie od tylu
    def test_reverse_sort(self, names):
        #given
        # names = ['Alina', 'Ewa', 'Paulina', 'Maciej']

        #when
        sorted_names = sort_by(names, last_letter=True)

        #then
        assert sorted_names == ['Alina', 'Paulina','Ewa', 'Maciej']

    #sorotwanie po dlugosci
    def test_by_length(self, names):
        #when
        sorted_names = sort_by(names, length=True)

        assert sorted_names == ['Ewa','Alina', 'Maciej','Paulina']