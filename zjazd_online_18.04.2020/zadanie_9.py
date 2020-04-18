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


print(f"Za dane produkty zapłacisz {suma:.2f} zł")
print(magazyn)
