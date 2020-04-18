
counter = 0
liczby = set()
warunek = set()

for i in range(101):
    if i % 2 == 0:
        warunek.add(i)

while True:
    liczba = input("Podaj liczbę: ")
    if liczba == "k":
        break
    else:
        liczba = int(liczba)
        counter += 1
        liczby.add(liczba)

print(liczby & warunek)



