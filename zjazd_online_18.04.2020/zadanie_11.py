
counter = 0
liczby = set()
warunek = set(range(0,101,2))


while True:
    liczba = input("Podaj liczbę: ")
    if liczba == "k":
        break
    else:
        liczba = int(liczba)
        counter += 1
        liczby.add(liczba)

print(f"Wprowadzonych liczb było: {counter} ")

print(f"Liczb spełniających warunek było: {len(liczby & warunek)}")




