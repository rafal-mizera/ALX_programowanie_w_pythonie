#Napisz program zliczający liczbę wystąpień każdego znaku w podanym przez użytkownika napisie

napis = input("Wpisz tekst: ")

# rozwiazanie 1
dict = {}

for litera in napis:
    if litera in dict:
        dict[litera] += 1
    else:
        dict[litera] = 1

print(dict)

# rozwiazanie 2

for litera in napis:
    dict[litera] = dict.get(litera, 0) + 1

print(dict)

# rozwiazanie 3

from collections import defaultdict

dict = defaultdict(int)

for litera in napis:
    dict[litera] += 1

print(dict)
