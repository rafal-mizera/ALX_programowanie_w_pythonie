tekst = input("Wpisz tekst: ")
tekst_new = ""

#for litera in tekst:
 #   if tekst.index(litera) % 2 == 0:
 #       tekst_new += litera
#    elif tekst.index(litera) % 2 != 0:
 #       tekst_new += 2 * litera

#print(tekst_new)

nr = 0

for litera in tekst:
    nr += 1
    if nr % 2 == 0:
        tekst_new += 2 * litera
    elif nr % 2 != 0:
        tekst_new += litera

print(tekst_new)


























