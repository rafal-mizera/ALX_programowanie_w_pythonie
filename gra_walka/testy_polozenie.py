
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



