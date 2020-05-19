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
        self.atak += self.bonus_atk

    def __str__(self):
        return print(f"Jestem {self.imie} mam {self.atak} ataku i {self.energia} życia\n Ekwipunek: {self.ekwipunek}")

    def wylecz(self, ile):
        # "Leczy - ale tylko żywe postaci - sprawdź czy_zyje()"
        if self.czy_zyje() == True:
            self.energia += self.ile
            return self.energia


    def otrzymaj_obrazenia(self, ile):
        # "Ile obrażeń - zależne od siły ataku i mocy obrony"
        self.ile = self.atakujacy.moc_ataku() - self.broniacy.obrona

    def czy_zyje(self):
        return self.energia > 0


    def moc_ataku(self):
        import random
        wynik = random.randint(self.atak // 2, self.atak)
        return wynik

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

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






class Przedmiot:

    def __init__(self, nazwa, bonus_atk, polozenie):
        self.nazwa = nazwa
        self.bonus_atk = bonus_atk
        self.polozenie = (self.x, self.y)

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
        if self.x == other.x and self.y == other.y:
            return print("Położenia graczy są takie same")
        else:
            return print("Gracze znajdują się w różnych miejscach na planszy")

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

    def gra(self):
        while True:
            self.ruch()

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

class TestPostac:

    def test_init(self):
        bomber = Postac()
        bomber.imie = "Bomber"
        bomber.ekwipunek = []
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

class TestyPolozenie:
    def test_init(self):
        polozenie1 = Polozenie(10,3,10,10)
        assert polozenie1
        assert polozenie1.x == 10
        assert polozenie1.y == 3
    def test_eq(self):
        polozenie1 = Polozenie(10, 3, 10, 10)
        polozenie2 = Polozenie(5,4,10,10)
        assert polozenie1.__eq__(polozenie2) == print("Gracze znajdują się w różnych miejscach na planszy")
    def test_str(self):
        polozenie1 = Polozenie(10, 3, 10, 10)
        assert polozenie1.__str__() == "Twoja pozycja to: x=10, y=3"
