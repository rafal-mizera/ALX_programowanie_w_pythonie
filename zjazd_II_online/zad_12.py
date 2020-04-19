# Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych i wypisujący wyniki na konsolę:

i = 0             # ustalamy początek, liczbę od której zaczynamy pętlę


while i < 100:       # While zaczyna pętlę (W TYM WYPADKU BĘDZIEMY Z KAŻDĄ PĘTLĄ ZWIĘKSZAć LICZBĘ GDYŻ i+=1
    print(i ** 2)     # działanie, które będzie powtarzane
    i += 1            # ustalamy co liczb będzie działąć pętle, "jedno okrążenie"
    if i == 101:      # można dodać ify - trzeba pamiętać o wcięciach
        print("KONIEC")

# Napisz program obliczający iloczyn sąsiednich 50 pierwszych liczb całkowitych i wypisujący wyniki na konsolę:

x = 1

while x <= 50:
    print(x * (x - 1))
    x += 1

# Napisz program który oblicza pierwiastek każdej z pierwszych 100 liczb naturalnych
import math

x = 0

print("X" * 100)
while x < 100:
    print(math.sqrt(x))
    math.sqrt(x)
    x += 1





