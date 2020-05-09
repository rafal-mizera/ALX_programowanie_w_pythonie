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

napisz program zliczający wielkie litery w napisie

text = input("Wprowadź tekst: ")

licznik = {}

for x in text:
    if x in licznik:
        if x.isupper():
            licznik[x] += 1
    else:
        if x.isupper():
            licznik[x] = 1

print(licznik)


