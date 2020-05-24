class Basket:

    def _init_(self):
        self.products = []

    def add_product(self,product,amount):
        self.products.append(BasketEntry(product,amount))

    def count_total_price(self):
        total_price = 0
        for be in self.products:
           total_price += be.price
           return total_price

    def generate_report(self):
        #"Produkty w koszyku: \n - Woda (1), cena: 10.00 x 5\n - Chleb (2) cena 2 x 2\n W sumie: 54"
        report = print(f"Produkty w koszyku: \n")
        for be in self.products:
            report += be.report
        report += f"W sumie: {self.count_total_price()}"


class Product:

    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price


class BasketEntry:

    def __init__(self,product: Product ,amount: int):# przykład adnotacjii
        self.product = product
        self.amount = amount

    @property

    def price(self):
        return self.amount * self.product.price

    @property

    def report(self):
        #"Masło (2), cena: 8 x 5"
        return f"- {self.product.name} ({self.product.id}), cena: {self.product.price:.2f} x {self.amount}\n "




class testBasket:
    def test_init(self):
        basket = Basket()
        assert basket
        assert basket.products == []
    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].name == "Woda"
    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product, 5)
        basket.add_product(product2, 5)
        assert basket.count_total_price() == 5 * 10.0 + 5* 2
    def test_generate_report(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product, 5)
        basket.add_product(product2, 2)
        basket.generate_report() == "Produkty w koszyku: \n - Woda (1), cena: 10.00 x 5\n - Chleb (2) cena 2 x 2\n W sumie: 54"



class testProduct:

    def test_init(self):
        product = Product(1,"Woda", 10.00)
        assert product.id == 1
        assert product.[0].product.name == "Woda"
        assert product.price == 10.00

class testBasketEntry:

    def test_init(self):
        product = Product(2,"masło", 8)
        be = BasketEntry(product,5)
        assert be.product == product
        assert be.amount == 5

    def test_price(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.price == 5 * 8

    def test_report(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.report == "Masło (2), cena: 8.00 x 5\n"


