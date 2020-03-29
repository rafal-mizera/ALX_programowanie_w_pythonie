# Napisz program sprawdzający, czy podana przez użytkownika liczba jest:
# wieksza od 10 , mniejsza równa 15, podzielna przez 2

liczba = int(input("Podaj liczbę: "))

print(f"Liczba jest większa od 10: {liczba > 10}")
print(f"Liczba jest mniejsza lub równa 15: {liczba <= 15}")
print(f"Liczba jest podzielna przez 2: {liczba % 2 == 0}")