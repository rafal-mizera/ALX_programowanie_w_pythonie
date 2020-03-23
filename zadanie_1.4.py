#Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu,
# a program wylicza, ile trzeba zapłacić. Zasady są takie:
#- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
#- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
    #- 200 zł za noc, jeśli nocują jedną noc
    #- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
    #- 150 zł za noc, jeśli nocują pięć lub więcej nocy
#- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

#Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
# czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

wiek = int(input("Podaj swój wiek: "))
ilosc_nocy = int(input("Podaj ile spędzisz nocy w hotelu: "))

if wiek < 18:
    cena_za_noc = 100
elif wiek >= 18 and wiek < 65 and ilosc_nocy == 1:
    cena_za_noc = 200
elif wiek >= 18 and wiek < 65 and ilosc_nocy > 1 and ilosc_nocy < 5:
    cena_za_noc = 180
elif wiek >= 18 and wiek < 65 and ilosc_nocy > 5:
    cena_za_noc = 150
elif wiek >= 65 and ilosc_nocy == 1:
    cena_za_noc = 0.9 * 200
elif wiek >= 65 and ilosc_nocy > 1 and ilosc_nocy < 5:
    cena_za_noc = 0.9 * 180
else:
    cena_za_noc = 0.9 * 150

koszt_pobytu = float(cena_za_noc) * int(ilosc_nocy)



print(f"Koszt pobytu w hotelu wynosi: {koszt_pobytu} PLN")
