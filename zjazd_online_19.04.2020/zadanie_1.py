def czy_jest_pierwsza(x):
    for number in range(1,x):
        if x % number == 0:
            print(False)
            return
            break
        else:
            print(True)
            return

czy_jest_pierwsza(2)