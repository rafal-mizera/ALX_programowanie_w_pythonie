#Napisz program który obliczy wszystkie pierwiastki rzeczywiste równania kwadratowego o postaci ax2+bx+c=0,
# gdzie a, b i c podaje użytkownik.
#Program powinien na początku sprawdzić, czy wprowadzone równanie jest rzeczywiście kwadratowe.

a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
c = float(input("Podaj liczbę c: "))

delta = b ** 2 - 4 * (a * c)
print(delta)

import math

if a == 0:
    print("Twoje równanie nie jest kwadratowe")
elif a != 0 and delta > 0:
    m1 = (-1 * b - math.sqrt(delta)) / (2 * a)
    m2 = (-1 * b + math.sqrt(delta)) / (2 * a)
    print(f"Rozwiązaniami Twojego równania są liczby {m1} i {m2}")
elif a != 0 and delta == 0:
    m1 = (- 1 * b) / 2 * a
    print(f"Rozwiązaniem Twojego równania jest liczba {m1}")
elif a != 0 and delta < 0:
    print("Równanie nie posiada rozwiązań")

