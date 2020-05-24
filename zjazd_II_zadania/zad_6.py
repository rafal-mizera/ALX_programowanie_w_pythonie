#Napisz program, który wczyta od użytkownika liczbę X,
#a następnie wyświetli TRÓJKĄT prostokątny o długości przyprostokątnej X, np.: ?> 5 * * * * * * * * * * * *

x = int(input("Podaj liczbę: "))
y = 0
z = 1
g = 0

while y < x:
    if z == 1:
        print("*")
        z += 1
        g += 1
        y += 1
    elif z > 1 and z < x:
        print("*",(g - 1) * " ","*")
        z += 1
        g += 2
        y += 1
    elif z == x:
        print(x * "* ")
        z += 1


