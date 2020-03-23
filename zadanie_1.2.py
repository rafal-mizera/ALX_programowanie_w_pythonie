### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)

#Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
#(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.

#Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
#Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

dzien_oddania = input("Dzień oddania butów do naprawy: ")
czas_naprawy = input("ile dni będzie trwała naprawa? ")


dzien_odbioru = int(dzien_oddania) + int(czas_naprawy)

if dzien_odbioru == 1 or dzien_odbioru % 7 == 1:
    dzien_odbioru = "Poniedziałek"
if dzien_odbioru == 2 or dzien_odbioru % 7 == 2:
    dzien_odbioru = "Wtorek"
if dzien_odbioru == 3 or dzien_odbioru % 7 == 3:
    dzien_odbioru = "Środa"
if dzien_odbioru == 4 or dzien_odbioru % 7 == 4:
    dzien_odbioru = "Czwartek"
if dzien_odbioru == 5 or dzien_odbioru % 7 == 5:
    dzien_odbioru = "Piątek"
if dzien_odbioru == 6 or dzien_odbioru % 7 == 6:
    dzien_odbioru = "Sobota"
if dzien_odbioru == 7 or dzien_odbioru % 7 == 0:
    dzien_odbioru = "Niedziela"

print(f"Dzień odbioru butów od szewca to: {dzien_odbioru}")








