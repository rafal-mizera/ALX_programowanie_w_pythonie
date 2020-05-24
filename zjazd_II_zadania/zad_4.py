

# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli romb o wysokości 2X, np.:
# /\
#/  \
#\  /
# \/

num = int(input("Podaj liczbę: "))
num_2 = 2 * num
z = 0
t = 1
g = num

while z < num:
    if t == 1:
        print((num - 1) * " ", "/\\")
        z += 1
        g -= 1
        t += 1
    elif t > 1:
        print((g - 1) * " ", "/", (t - 2) * " ", "\\")
        z += 1
        g -= 1
        t += 2
while z >= num and z < num_2:
    if z >= num and z < (num_2 - 1):
        print(g * " ", "\\", (t - 4) * " ", "/")
        z += 1
        t -= 2
        g += 1
    elif z == (num_2 - 1):
        print((num - 1) * " ", "\\/")
        z += 1




