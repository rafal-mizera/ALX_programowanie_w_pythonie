with open("zadanie_1.txt", "a") as f:
    f.write("pierwsza linia\n")
    f.write("druga linia\n")
    f.write("trzeciaa linia\n")

def opener(nazwa):
    try:
        with open(nazwa) as f:
            x = 1
            for line in f:
                print(x,":", line,end="")
                x += 1
    except FileNotFoundError:
        print("Nie znaleziono pliku")

    except TypeError:
        print("Podaj nazwę pliku")

opener("zadanie_1.txt")