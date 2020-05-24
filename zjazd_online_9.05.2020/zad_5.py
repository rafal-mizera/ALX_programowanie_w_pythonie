class BillException(Exception):
    pass
class NotEnoughSpaceforBills(Exception):
    pass

class CashMachine:

    def __init__(self,capacity=100):
        self.__cash_machine_money = []
        self.capacity = capacity

    @property
    def is_available(self):
        return len(self.__cash_machine_money) > 0

    def put_money(self, bills):
        if len(self.__cash_machine_money) + len(bills) > self.capacity:
            raise NotEnoughSpaceforBills("Brak miejsca w bankomacie")
        self.__cash_machine_money += bills


    
    def withdraw_money(self,withdraw):
        if withdraw % 10 != 0:
            raise KeyError("Kwota powinna być podzielna przez 10")

        to_withdraw = []

        for bill in sorted(self.__cash_machine_money, reverse = True):
            if sum(to_withdraw) + bill <= withdraw:
                to_withdraw.append(bill)
        if sum(to_withdraw) == withdraw:
            for bill in to_withdraw:
                self.__cash_machine_money.remove(bill)
            return to_withdraw

        raise BillException(f"Brak wystarczającej liczby banknotów dla kwoty {withdraw}")


import pytest


class TestCashMachine:
    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_available_for_empty_machine(self):
        cash_machine = CashMachine()
        assert cash_machine.is_available is False
        # assert not cash_machine.is_available

    def test_put_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True

    def test_withdraw_money(self):
        cash_machine = CashMachine()
        assert cash_machine.withdraw_money(150) == []
        # assert CashMachine.withdraw_money(cash_machine, 150) == []
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.withdraw_money(300) == [200, 100]

        cash_machine = CashMachine()
        cash_machine.put_money([50, 100, 100, 200])
        assert cash_machine.withdraw_money(300) == [200, 100]
        assert cash_machine.withdraw_money(300) == []

        cash_machine = CashMachine()
        cash_machine.put_money([50, 100, 100, 200])
        assert cash_machine.withdraw_money(600) == []

    def test_value_error_when_amount_is_not_divided_by_10(self):
        cashmachine = CashMachine()
        cashmachine.put_money([100, 100, 100])
        with pytest.raises(KeyError):
            cashmachine.withdraw_money(123)

    def test_bills_exception_when_not_enough_bill_to_withdraw(self):
        cashmachine = CashMachine()
        cashmachine.put_money([100, 100, 100])
        with pytest.raises(BillException):
            cashmachine.withdraw_money(150)

    def test_not_enought_room_for_bills(self):
        cm = CashMachine(capacity=10)
        with pytest.raises(NotEnoughSpaceforBills):
            cm.put_money([100 for i in range(20)])