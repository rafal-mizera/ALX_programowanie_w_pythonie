#elementy = [ 1, 2, 3, 4, 5, "xx", 2.0, 2]

#x = elementy.append("cos") # dodawanie elementu do zbioru

#print(elementy)
#print(x)
#print(len(elementy))

x = 10   # określamy liczność listy
elementy = []   # tworzymy listę i ustalamy, że jest pusta

while len(elementy) <= 9:                # ustalamy granicę pętli
    x = int(input("Wprowadź liczbę: "))
    elementy.append(x)                    # dodaje do listy wartość x

print(sum(elementy) / 10)                   # sum sumuje wartości z listy

# Z wprowadzonych przez użytkownika liczb naturalnych wybierz te, które są podzielne przez 3 oraz te podzielne prze
# 5, niech "x" kończy wprowadzanie

dividable_5 = []
dividable_3 = []


while True:
    num = input("Podaj liczbę lub x by zakonczyc: ")
    if num == "x":
        break
    else:
        num = int(num)
        if num % 3 == 0:
            dividable_3.append(num)
        elif num % 5 == 0:
            dividable_5.append(num)

print("Podzielne przez 3:", dividable_3, "Podzielne przez 5", dividable_5)


