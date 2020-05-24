#Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie, np.:
# H L O S R N E !
# E L T A G R

#text = input("Wpisz swój tekst: ")

#print(" ".join(text[::2]))
#print(" ".join(text[1::2]))

#text2 = input("Wpisz swój tekst: ")

#print("".join(text2[::2]))
#print("".join(text2[1::2]))

x = list(input("Wpisz swój tekst: "))
a = []
b = []

for y in x:
    if x.index(y) == 0 or x.index(y) % 2 == 0:
        a.append(y)
        d = " ".join(a)
    else:
        b.append(y)
        c = " ".join(b)

print(d)
print(c)




