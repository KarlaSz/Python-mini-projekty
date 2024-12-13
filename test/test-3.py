#rozwin zad2, w taki sposob by nie mozna bylo wyplacac wiecej niz jest w kasie.w takim przypadku program powinien wyrzucic wyjatek
import pytest

class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self,money:int):
        self.amount += money

    def withdraw_money(self,money):
        if money > self.amount:
            raise NotEnoughCash('Nie mam tyle kasie!')
        self.amount -= money

        return money

class NotEnoughCash(Exception):
    pass
    #daje pass jak nie chce zadnej logiki

class TestBank:
    def test_withdraw_over_amount(self):
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw_money(200)

