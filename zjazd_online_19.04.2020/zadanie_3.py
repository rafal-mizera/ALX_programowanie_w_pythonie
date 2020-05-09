#Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami.
# #Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi
# - odpowiednio < i >. Nawiasy mogę być zagnieżdżone i mogą wystąpić wiele razy.
# #Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.

# policz_znaki('ala ma <kota> a kot ma ale')
napis = "ala ma [kota] a [kot] ma ale"
#def liczba_znakow(napis, a = "<",b = ">"):
#         for znak in napis:
#             liczba = napis.index(b) - napis.index(a) - 1
#         return liczba

def liczba_znakow(text, start = "<", stop = ">"):
    poziom = 0
    licznik = 0

    for znak in text:
        if znak == start:
            poziom += 1
            continue
        elif znak == stop:
            poziom -= 1
            continue

        licznik += poziom

    return licznik


def test_liczba_znakow():
    assert liczba_znakow('ala ma <kota> a kot ma ale') == 4
    assert liczba_znakow('ala ma <ko>ta a kot ma ale') == 2
    assert liczba_znakow('ala ma [kota] a [kot] ma ale', "[", "]") == 7
    assert liczba_znakow('a <a<a<a>>>') == 6


# def zlacz_teksty(* lista_tekstow):
#     return " ".join(lista_tekstow)
#
# lista = ["a", "b", "c"]

