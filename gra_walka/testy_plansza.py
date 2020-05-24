class Postac:

    def _init_(self, imie, atak, obrona, energia):
        self.imie = imie
        self.atak = atak
        self.obrona = obrona
        self.energia = energia
        self.ekwipunek = []

    # @property
    # def atak(self):
    #     # "wylicza moc ataku"
    #     self.atak += self.bonus_atk

    def __str__(self):
        return print(f"Jestem {self.imie} mam {self.atak} ataku i {self.energia} życia\nEkwipunek: {self.ekwipunek}")

    def czy_zyje(self):
        return self.energia > 0

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def wylecz(self, ile):
        # "Leczy - ale tylko żywe postaci - sprawdź czy_zyje()"
        if self.czy_zyje() == True:
            self.energia += ile
            return self.energia
class Przedmiot:

    def __init__(self, nazwa, bonus_atk, polozenie):
        self.nazwa = nazwa
        self.bonus_atk = bonus_atk
        polozenie = Polozenie()
    def __str__(self):
        return f"{self.nazwa}, {self.bonus_atk} do ataku"

class Polozenie:

    def __init__(self, x, y, zasieg_x=10, zasieg_y=10):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __eq__(self, other):
        #"Sprawdza czy polozenia takie same"
        if self.x == other.x and self.y == other.y:
            return print("Położenia graczy są takie same")
        else:
            return print("Gracze znajdują się w różnych miejscach na planszy")

    def g(self):
        # "Ruch w górę"
        g = input("O ile pól w górę przesunać? ")
        return self.y + g

    def d(self):
        # "Ruch w dół"
        d = input("O ile pól w dół przesunać? ")
        return self.y - d

    def l(self):
        # "Ruch w lewo"
        l = input("O ile pól w lewo przesunać? ")
        return self.x - l

    def p(self):
        # "ruch w prawo"
        p = input("O ile pól w prawo przesunać? ")
        return self.x + p
    def __str__(self):
        return f"Twoja pozycja to: x={self.x}, y={self.y}"



class Plansza:

    def __init__(self, gracz, wrog, skarb, x=10, y=10):
        self.gracz = gracz
        self.wrog = wrog
        self.skarb = skarb
        self.x = x
        self.y = y

    def ruch(self):

        ruch_kier = input("Jaki ruch chesz wykonać? [góra/dół]:")

        if ruch_kier == "góra":
                self.g()
        elif ruch_kier == "dół":
                self.d()

        ruch_kier2 = input(("Jaki ruch chesz wykonać? [prawo/lewo: "))

        if ruch_kier2 == "prawo":
                self.p()
        elif ruch_kier2 == "lewo":
                self.l()


class TestPlansza:

    def test_init(self):
        bomber = Postac()
        bomber.imie = "Bomber"
        bomber.ekwipunek = []
        bomber.atak = 20
        nozownik = Postac()
        nozownik.imie = "Nozownik"
        nozownik.ekwipunek = []
        nozownik.atak = 20
        gracz = bomber
        wrog = nozownik
        skarb = Przedmiot
        plansza1 = Plansza(gracz,wrog,skarb)

        assert plansza1
        assert plansza1.wrog == nozownik
        assert plansza1.gracz.imie == "Bomber"




