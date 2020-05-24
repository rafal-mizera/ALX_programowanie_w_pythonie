# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli "kwadrat" z gwiazdek o długości boku X, np.:

x = int(input("Podaj liczbę: "))

y = 0
z = x - 2

while y <= x:
        y += 1
        if y == 1 or y == x:
            print(x * "*")
        elif y > 1 and y < x:
            print("*", z * " ", "*")

