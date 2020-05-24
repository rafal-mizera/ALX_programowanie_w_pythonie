#Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w ramce z gwiazdek, ​np.:

#?> HELLO STRANGER!
#**********************
#*   HELLO STRANGER!  *
#**********************

napis = input("Wpisz swój tekst: ")
dlugosc = len(napis)

print((dlugosc + 6) * "*")
print("* ", napis, " *")
print((dlugosc + 6) * "*")