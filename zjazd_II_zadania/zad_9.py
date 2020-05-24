#Napisz program "numer.py", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
# a) znaki nie będące cyframi mają być ignorowane b) konwertujemy cyfry, nie liczby, a zatem:

#    911 to "dziewięć jeden jeden"
#    1100 to "jeden jeden zero zero"

x = list(input("Podaj liczbę: "))
z = []

for y in x:
    if y == "0":
        z.append("zero")
    elif y == "1":
        z.append("jeden")
    elif y == "2":
        z.append("dwa")
    elif y == "3":
        z.append("trzy")
    elif y == "4":
        z.append("cztery")
    elif y == "5":
        z.append("pięć")
    elif y == "6":
        z.append("sześć")
    elif y == "7":
        z.append("siedem")
    elif y == "8":
        z.append("osiem")
    elif y == "1":
        z.append("jeden")
    elif y == "9":
        z.append("dziewięć")


print(" ".join(z))