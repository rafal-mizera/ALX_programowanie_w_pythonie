#napisz program, który posortuje liczby z listy od najmniejszej do największej

lista = [4, 15, 12, 167, 2, 1]

for index_podstawienia in range(len(lista)):
    index_min = index_podstawienia
    for index_ogona in range(index_podstawienia + 1, len(lista)):
        if lista[index_ogona] < lista[index_min]:
            index_min = index_ogona
    lista[index_podstawienia], lista[index_min] = lista[index_min], lista[index_podstawienia]

print(lista)

#napisz program, który posortuje liczby z listy od największej do najmniejszej

liczby = [10, 157, 4, 20, 1, 15, 12000]

for pozycja in range(len(liczby)):
    najwieksza = pozycja
    for pozycja_ogona in range(pozycja + 1, len(liczby)):
        if liczby[pozycja_ogona] > liczby[najwieksza]:
            najwieksza = pozycja_ogona
    liczby[pozycja], liczby[najwieksza] = liczby[najwieksza], liczby[pozycja]
print(liczby)










