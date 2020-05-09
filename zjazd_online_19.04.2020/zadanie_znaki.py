#wiecej_niz('ala ma kota a kot ma ale',3 )
# {"a"," "}

def wiecej_niz(napis,liczba):
    zbior = set()
    for znak in set(napis):
        if napis.count(znak) > liczba:
            zbior.add(znak)

    return zbior

# def wiecej_niz(napis,liczba):
#     zbior = set()
#     zbior2 = set()
#     for znak in set(napis):
#         if znak not in zbior:
#             zbior.add(znak)
#         elif znak in zbior:
#             if len(zbior) < liczba:
#                 zbior.add(znak)
#             elif len(zbior) >= liczba:
#                 zbior2.add(znak)
#     return zbior2

print(wiecej_niz("ala ma kota", 1))

# def test_wiecej_niz_dla_pustego_napisu():
#     assert wiecej_niz("",0) == set()
#
# def test_wiecej_niz_dla_niepustego_napisu():
#     assert wiecej_niz("aaaa bbbb ccc dd e", 0) == {"a", "b", "c", "d", "e", " "}
#     assert wiecej_niz("aaaa bbbb ccc dd e", 3) == {"a", "b", " "}
