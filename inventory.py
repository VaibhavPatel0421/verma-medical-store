class InventoryManager:
    def __init__(self):
        self.stock = {
            "Paracetamol": {"price": 15.0, "qty": 100},
            "Amoxicillin": {"price": 45.0, "qty": 30},
            "Cetirizine": {"price": 10.0, "qty": 8}
        }

    def display_stock(self):
        print("\n--- CURRENT MEDICINE STOCK ---")
        for med, info in self.stock.items():
            print(f"Name: {med:<15} | Price: ₹{info['price']:<6} | Stock: {info['qty']} units")

    def add_medicine(self, name, price, qty):
        if name in self.stock:
            self.stock[name]['qty'] += qty
        else:
            self.stock[name] = {"price": price, "qty": qty}
        print(f"Success: Added/Updated {qty} units of {name}.")
