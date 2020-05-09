class Product:
    def __init__(self,ID,name,price):
        self.ID = ID
        self.price = price
        self.name = name
    def print_info(self):
        print(f"Produkt {self.name}, id: {self.ID}, cena: {self.price} PLN")

product = Product(1,"Woda",10.99)

product.print_info()