def czy_jest_pierwsza(x):
    for number in range(2,x):
        if x % number == 0:
            return False
        else:
            return True

print(czy_jest_pierwsza(8))