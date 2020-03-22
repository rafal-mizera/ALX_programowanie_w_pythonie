#Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić
# boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawda?),
# a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.

#Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
#Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:

#```

#import math

#x = math.sqrt(10)

#```
# By można zbudować trójkąt:
#a<b+c
#b<a+c
#c<a+b

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

p = float((a + b + c) / 2)

import math

if b + c > a and a + c > b and a + b > c:
    pole_trojkata = float(math.sqrt(p * (p - a) * (p - b) * (p - c)))
if b + c > a and a + c > b and a + b > c:
    print(f"Pole trójkąta wynosi: {pole_trojkata} cm2")
else:
    print("Z boków o podanych długościach nie da się utworzyć trójkąta")


