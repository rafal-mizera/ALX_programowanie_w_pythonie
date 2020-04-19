#Napisz program, który na podstawie wprowadzonych wymiarów opakowania, obliczy jego objętość oraz sprawdzi, czy jest
# ona większa od 1 litra

a = float(input("Podaj wymiar a (w cm): "))
b = float(input("Podaj wymiar b (w cm): "))
c = float(input("Podaj wymiar c (w cm): "))

objetosc = a * b * c

if objetosc > 1000:
    print("Objętość opakowania jest większa niż 1000 cm3")
else:
    print("Objętość opakowania nie jest większa niż 1000 cm3")

# Napisz program, który sprawdzi czy na podstawie wprowadzonych podanych danych obliczy pole działki (zakłądając, że jest to prostokąt)
# zapyta także o koszt 1a i obliczy wartość działki.

a = float(input("Podaj długość działki w m: "))
b = float(input('Podaj szerokość działki w m: '))
cena_a = float(input("Podaj cenę 1a: "))

pole_w_a = (a * b) / 100
wartosc_dzialki = cena_a * pole_w_a

print(f"Pole działki wynosi {pole_w_a:.2f} ara a jej wartość to {wartosc_dzialki:.2f} zł")



