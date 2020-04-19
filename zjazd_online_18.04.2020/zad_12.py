lista = [4, 15, 12, 167, 2, 1]

for index_podstawienia in range(len(lista)):
    index_min = index_podstawienia
    for index_ogona in range(index_podstawienia + 1, len(lista)):
        if lista[index_ogona] < lista[index_min]:
            index_min = index_ogona
    lista[index_podstawienia], lista[index_min] = lista[index_min], lista[index_podstawienia]




print(lista)








