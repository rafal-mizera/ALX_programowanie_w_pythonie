#Założenia:

#	- 0-6   - wiek przedszkolny - cena biletu: 0

#	- 7-17  - wiek szkolny      - cena biletu: 2.28

#	- 18-64 - wiek dorosły      - cena biletu: 3.80

#	- +65   - wiek emerytalny   - cena biletu: 1.90

#Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.

#Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
# Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.


wiek = int(input("Podaj swój wiek: "))
ilosc_biletow = int(input("Podaj ilość biletów: "))


if wiek <= 6:
    cena_biletu = 0
elif wiek >= 7 and wiek <= 17:
    cena_biletu = 2.28
elif wiek >= 18 and wiek <= 64:
    cena_biletu = 3.80
else:
    cena_biletu = 1.90

cena_razem = ilosc_biletow * cena_biletu

print(f"Cena zakupionych biletów wynosi: {cena_razem} zł")




