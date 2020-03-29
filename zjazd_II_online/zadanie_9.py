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
