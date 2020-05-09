class Product:
    def __init__(self,ID,name,price):
        self.ID = ID
        self.price = price
        self.name = name
    def print_info(self):
        print(f"Produkt {self.name}, id: {self.ID}, cena: {self.price} PLN")

product = Product(1,"Woda",10.99)

product.print_info()

class TestProduct:
    def test_init(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt
        assert produkt.id == 1
        assert produkt.name == "Woda"
        assert produkt.price == 10.99
    def test_print_info(self):
        product = Product(1, "Woda", 10.99)
        assert product.print_info() == "Produkt \"Woda\", id: 1, cena: 10.99 PLN"
