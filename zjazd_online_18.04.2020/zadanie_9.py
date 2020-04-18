cennik = {"ziemniaki": 5, "buraki": 3, "marchewka": 2.5, "pietruszka": 3.5}
produkt = input("Co chcesz kupić? ")
waga = float(input("Podaj wagę: "))


if produkt in cennik:
    koszt = waga * cennik[produkt]
    print(f"Za dany produkt zapłacisz {koszt} zł")