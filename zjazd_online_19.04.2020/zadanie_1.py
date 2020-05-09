#napisz funkcje sprawdzająca czy dana liczba jest liczbą pierwsza


def czy_jest_pierwsza(x):
    for number in range(2,x):
        if x % number == 0:
            return False
    return True

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(6) == False
    assert czy_jest_pierwsza(7) == True


(czy_jest_pierwsza(6))


if __name__ == "__main__":
    print("Wykonuję testy")
    assert czy_jest_pierwsza(6) == False
    assert czy_jest_pierwsza(7) == True
    print("Wszystko ok")

#Napisz  funkcje sprawdzajaca czy dana liczba jest wielokrotnością liczby 5

# def liczby_5(x):
#     if x % 5 == 0:
#         return True
#     return False
#
# print(liczby_5(10))
# print(liczby_5(11))
#
# def liczby_test():
#     assert liczby_test(5) == True
#     assert liczby_test(55) == True
#     assert liczby_test(12) == False
