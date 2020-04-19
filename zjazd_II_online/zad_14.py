mini_x = None # przez none zaznaczamy, że podane zmienne są dostępne lecz w tym momencie nieokreślone
maxy_x = None

while True: # wykonujemy pętlę cały czas, dopóki nie zajdą okoliczności niżej podane
    number = input("wprowadź liczbę lub x by zakonczyc: ")
    if number == "x":
        break  # koniec pętli
    number = int(number)   # w tym miejscu można juz number określic jako int, wcześniej mógł to też być x
    if mini_x is None or number < mini_x:  # teraz tworzymy pętlę która w każdym kolejnym okrążeniu
        mini_x = number                    # czyli z każdą podaną przez użytkownika liczbą, sprawdza czy jest ona
    if maxy_x is None or number > maxy_x:  # mniejsza / większa od NAJMNIEJSZEJ/NAJWIĘKSZEJ napotkanej do tej pory
        maxy_x = number                    # jeżeli jest to prawda zapisuje ją jako nowy mini_x lub maxy_x

print(f"Wartość maksymalna: {maxy_x}")
print(f"Wartość minimalna: {mini_x}")








