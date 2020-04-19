#Napisz program, który sprawdzi pełnoletnosc osoby na podstawie
#roku jej urodzenia.
#Przykładowy komunikat programu:
#Podaj rok urodzenia: 1980
#Jestes pełnoletni!

import datetime
current_year = datetime.datetime.now().year

rok_urodzenia = int(input("Podaj rok urodzenia: "))

if (current_year - rok_urodzenia) >= 18:
    print("Jesteś Pełnoletni!")
else:
    print("Nie jesteś pełnoletni!")

#Napisz program, który sprawdzi i wypisze kiedy osoba
# może przejść na emeryture na podstawie roku jej urodzenia.
#Przykładowy komunikat programu:
#Podaj rok urodzenia: 1980
#Na emeryture możesz przejść w 2045 roku

birth_year = int(input("Podaj rok urodzenia: "))

retirement_year = birth_year + 65

print(f"Na emeryturę będziesz mógł przejść w {retirement_year} roku")



