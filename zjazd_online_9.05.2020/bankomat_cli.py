from zad_5 import CashMachine, NotEnoughSpaceforBills, BillException

cash_machine = CashMachine()
cash_machine.put_money([200,200,100,100,50,50])

while True:
    operation = input("Podaj typ operacji: [wplata, wyplata, koniec]: ")
    if operation == "koniec":
        break
    if operation == "wplata":
        bills = input("Podaj listę banknotów, rozdzielając je przecinkiem: ")
        bills = bills.split(",")
        bills = [int(bill) for bill in bills]
        try:
            cash_machine.put_money(bills)
        except NotEnoughSpaceforBills as e:
            print("Error: ", e)
    elif operation == "wyplata":
        amount = int(input("Podaj kwotę do wypłacenia: "))
        try:
            bills = cash_machine.withdraw_money(amount)
        except BillException:
            print("Brak wystarczającej ilości banknotów" )
        except KeyError as e :
            print("Błedna kwota do wypłaty", e)
