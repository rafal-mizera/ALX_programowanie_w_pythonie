#Odp 1. Poznane struktury danych:
# - listy
# -tuple
# -słowniki
# - zbiory
#Odp 2. Mutowalne są:
# - listy
# -słowniki
# Niemutowalne:
#-tuple
#-zbiory
#Odp 3. Zaimplementuj funkcję zawierającą algorytm sortowanie przez wybieranie:



# Odp 4.Masz słownik
zrodla = {"a": 10, "b":30}
#
# Jak bezpiecznie wybrać z tego słównika wartość i przypisać ją do zmiennej, to by nie był rzucony błąd?
# Np. chcesz sprawdzić dla wartości "c", której nie ma w słowniku

print(zrodla["a"])
print("c" in zrodla)
zrodla["c"] = 10
print(zrodla)

#Odp 5.5. Zdefiniuj funkcję foo, która przyjmie dowolną liczbę argumentów pozycyjnych i kluczowych
   # funkcja ma wypisać na ile ich jest
   # np.:
   # >>> foo(10, 20, a=1, b=2, c=3)
   # pozycyjnych: 2
   # kluczowych:  3

def foo(*args,**kwargs):
    print("pozycyjnych :",len(args))
    print("kluczowych: ",len(kwargs))

foo(10,20, a=1, b=2, c=3)