#Napisz program zliczający liczbę wystąpień każdego znaku w podanym przez użytkownika napisie

napis = input("Wpisz tekst: ")

dict = {}

for litera in napis:
    if litera in dict:
        dict[litera] += 1
    else:
        dict[litera] = 1

print(dict)