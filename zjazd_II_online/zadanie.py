# Napisz program sprawdzający, czy podana przez użytkownika liczba jest:
# wieksza od 10 , mniejsza równa 15, podzielna przez 2

liczba = int(input("Podaj liczbę: "))
print(bool(liczba > 10))
print(bool(liczba <= 15))
print(bool(liczba % 2 == 0 ))