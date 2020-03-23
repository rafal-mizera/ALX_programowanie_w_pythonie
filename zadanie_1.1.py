## 1. Interakcja z użytkownikiem

### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)

#Napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.


cena_ziemniakow = input("Podaj cenę ziemniaków za kg: ")

koszt_5kg = 5 * float(cena_ziemniakow)

print(f"Koszt 5 kg ziemniaków: {koszt_5kg} PLN")



#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i
#ile kilo chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.

cena_ziemniakow = input("Podaj cenę ziemniaków za kg: ")
ilosc_kg = input("Podaj ilość kg: ")

koszt = float(cena_ziemniakow) * float(ilosc_kg)

print(f"Koszt ziemniaków {koszt} PLN")

#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
# ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i wyświetli,
# ile trzeba będzie zapłacić za te ziemniaki i banany razem. I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej
# - za banany czy za ziemniaki.

cena_ziemniakow = float(input("Podaj cenę ziemniaków: "))
ilosc_kg_ziemniakow = float(input("Podaj ilość kg ziemniakow: "))
cena_bananow = float(input("Podaj cenę bananów za kg: "))
ilosc_kg_bananow = float(input("Podaj ilosc kg bananow: "))

koszt_razem = cena_ziemniakow * ilosc_kg_ziemniakow + cena_bananow * ilosc_kg_bananow

print(f"Koszt ziemniaków i bananów razem to: {koszt_razem} PLN")

koszt_ziemniakow = cena_ziemniakow * ilosc_kg_ziemniakow
koszt_bananow = cena_bananow * ilosc_kg_bananow


if koszt_ziemniakow > koszt_bananow:
    print("Więcej trzeba zapłacić za ziemniaki")
elif koszt_ziemniakow < koszt_bananow:
    print("Więcej trzeba zapłacić za banany")
else:
    print("Za banany i za ziemniaki trzeba zapłącić tyle samo")






