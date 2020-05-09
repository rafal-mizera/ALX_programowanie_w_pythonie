# #Napisz program wybierający i zliczający wpisane przez użytkownika liczby z zakresu 0 - 100, będące liczbami parzystymi
#
# counter = 0
# liczby = set()
# warunek = set(range(0,101,2))
#
#
# while True:
#     liczba = input("Podaj liczbę: ")
#     if liczba == "k":
#         break
#     else:
#         liczba = int(liczba)
#         counter += 1
#         liczby.add(liczba)
#
# print(f"Wprowadzonych liczb było: {counter} ")
#
# print(f"Liczb spełniających warunek było: {len(liczby & warunek)}")


# Napisz program, który sprawdzi, które z wpisanych przez użytkownika tekstów są słowami kluczami


slowa_klucze = set(["Dziękuję","Przepraszam","Proszę","Dzień dobry"])
slowa = set()

while True:
    slowo = input("Wpisz słowo klucz lub k by zakonczyc: ")
    if slowo == "k":
        break
    else:
        slowa.add(slowo)

print(f"Z wpisanych przez Ciebie słów, słowami kluczami były: {slowa_klucze & slowa}")

