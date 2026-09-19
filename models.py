# Verma Medical Store - Medicine Class

class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name:<20} | Price: Rs.{self.price:<8.2f} | Stock: {self.quantity}"


