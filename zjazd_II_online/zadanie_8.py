#Napisz program, któru na podstawie wprowadzonych wymiarów opakowania, obliczy jego objętość oraz sprawdzi, czy jest
# ona większa od 1 litra

a = float(input("Podaj wymiar a (w cm): "))
b = float(input("Podaj wymiar b (w cm): "))
c = float(input("Podaj wymiar c (w cm): "))

objetosc = a * b * c

if objetosc > 1000:
    print("Objętość opakowania jest większa niż 1000 cm3")
else:
    print("Objętość opakowania nie jest większa niż 1000 cm3")