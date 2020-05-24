class Postac:

    def _init_(self, imie, atak, obrona, energia):
        self.imie = imie
        self.atak = atak
        self.obrona = obrona
        self.energia = energia
        self.ekwipunek = []

    @property
    def atak(self):
        # "wylicza moc ataku"
        bonus_atk_sum = 0
        for przedmiot in self.ekwipunek:
            bonus_atk_sum += przedmiot.bonus_atk
        return self.atak + bonus_atk_sum

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

    @staticmethod
    def walka(atakujacy, broniacy):
        atakujacy = Plansza.self.gracz
        broniacy = Plansza.self.wrog
        while True:
            if atakujacy.energia > 0 and broniacy.energia > 0:
                broniacy.otrzymaj_obrazenia
            else:
                atakujacy.__str__()
                broniacy.__str__()
            atakujacy = broniacy, broniacy = atakujacy

    @atak.setter
    def atak(self, value):
        self._atak = value


class Przedmiot:

    def __init__(self, nazwa, bonus_atk):
        self.nazwa = nazwa
        self.bonus_atk = bonus_atk
        # polozenie = (self.x, self.y)

    def __str__(self):
        return f"{self.nazwa}, {self.bonus_atk} do ataku"

class Polozenie:

    def __init__(self,x, y, zasieg_x=10, zasieg_y=10):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __eq__(self, other):
        #"Sprawdza czy polozenia takie same"
        return self.x == other.x and self.y == other.y

    def g(self):
        #"Ruch w górę"
        g = input("O ile pól w górę przesunać? ")
        return self.y + g

    def d(self):
        #"Ruch w dół"
        d = input("O ile pól w dół przesunać? ")
        return self.y - d

    def l(self):
        #"Ruch w lewo"
        l = input("O ile pól w lewo przesunać? ")
        return self.x - l

    def p(self):
        #"ruch w prawo"
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



class TestPostac:

    def test_init(self):

        bomber = Postac()
        bomber.imie = "Bomber"

        bomber.atak = 20

        assert bomber.atak == 20

        assert bomber
        assert bomber.imie == "Bomber"
        assert bomber.ekwipunek == []

    def test_str(self):
        bomber = Postac()

        bomber.imie = "Bomber"
        bomber.ekwipunek = "Magiczny kij"
        bomber.atak = 20
        bomber.energia = 100
        assert bomber.__str__() == print("Jestem Bomber mam 20 ataku i 100 życia\nEkwipunek: Magiczny kij")

    def test_czy_zyje(self):

        bomber = Postac()
        bomber.energia = 0
        assert bomber.czy_zyje() == False

    def test_daj_przedmiot(self):
        bomber = Postac()
        bomber.ekwipunek = []
        bomber.daj_przedmiot("ciupaga")
        assert bomber.ekwipunek == ["ciupaga"]

    def test_wylecz(self):
        bomber = Postac()
        bomber.energia = 10
        bomber.wylecz(90)
        assert bomber.energia == 100

    def test_walka(self):
        bomber = Postac()
        bomber.energia = 100
        bomber.atak = 50
        bomber.obrona = 50
        bomber.imie = "Bomber"
        kosa = Przedmiot("kosa",30)
        bomber.ekwipunek = [kosa]
        nozownik = Postac()
        nozownik.energia = 100
        nozownik.atak = 30
        nozownik.obrona = 40
        nozownik.imie = "Nozownik"
        pila = Przedmiot("piła",20)
        bomber.ekwipunek = [pila]
        gracz = bomber
        wrog = nozownik
        skarb = Przedmiot
        plansza1 = Plansza(gracz,wrog,skarb)









