#Napisz program który obliczy stan konta za N lat, gdzie stan początkowy konta wynosi SPK, a stopa oprocentowania P % rocznie
#(obowiązuje roczna kapitalizacja odsetek). N, SPK i P podaje użytkownik programu.

SPK = float(input("Podaj stan początkowy konta w zł: "))
P = float(input("Podaj stopę oprocentowania konta: "))
N = float(input("Podaj ilość lat: "))
X = 1
SKT = SPK

while X <= N:
    X += 1
    if X == 1:
        SKT = SPK + (P * SPK / 100)
        X += 1
    else:
        SKT = SKT + (P * SKT / 100)


print(f"Twój stan konta po {N} latach, będzie wynosił {SKT} zł")

