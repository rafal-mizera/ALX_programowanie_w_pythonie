#Napisz program sprawdzający czy podana przez użytkownika liczba jest podzilna przez 2, podzielna przez 3 i większa od 10
# lub jest to liczba 7

liczba = int(input("Podaj dowolną liczbę całkowitą: "))

print(liczba / 2 == 0 and liczba / 3 == 0 and liczba > 10 or liczba == 7)
