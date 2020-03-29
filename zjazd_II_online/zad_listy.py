#elementy = [ 1, 2, 3, 4, 5, "xx", 2.0, 2]

#x = elementy.append("cos")

#print(elementy)
#print(x)
#print(len(elementy))

x = 10
elementy = []

while len(elementy) <= 9:
    x = int(input("Wprowadź liczbę: "))
    elementy.append(x)

print(sum(elementy) / 10)


