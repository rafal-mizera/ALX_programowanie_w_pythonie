cennik = {"ziemniaki": 5, "buraki": 3, "marchewka": 2.5, "pietruszka": 3.5}

magazyn = {"ziemniaki": 10, "buraki": 10, "marchewka": 10, "pietruszka": 10}


print("Nasz zielnik oferuje: ")

for produkt, cena in cennik.items():
    print(f"{produkt} w cenie {cena} zł ")

suma = 0
while True:
    komenda = input("Co chcesz zrobić? [k-kup], [z-zakończ] [m-magazyn]: ")
    if komenda == "z":
        break
    elif komenda == "k":
        produkt = input("Co chcesz kupić? ")
        waga = float(input("Podaj wagę: "))
        if produkt in cennik:
            if waga > magazyn[produkt]:
                print("Niestety brak wystarczającej ilości towaru na magazynie")
            else:
                koszt = waga * cennik[produkt]
                suma += koszt
                magazyn[produkt] = magazyn[produkt] - waga
    elif komenda == "m":
        komenda2 = input("Co chcesz zrobić? [d - dodaj nowy produkt, s - zwiększ stan istniejącego produktu]")
        if komenda2 == "d":
                nowy = input("Wpisz nazwę: ")
                nowy_ilość = input("Podaj ilość: ")
                magazyn[nowy] = [nowy_ilość]
        elif komenda2 == "s":
                produkt = input("Co chcesz dodać do magazynu? ")
                dostawa = input(f"Ile {produkt} chcesz dodać do magazynu: ")
                magazyn[produkt] = magazyn[produkt] + dostawa
    else:
        print("Niezrozumiała komenda")

print(f"Za dane produkty zapłacisz {suma:.2f} zł")
print(magazyn)
