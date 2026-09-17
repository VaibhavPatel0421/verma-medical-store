class BillingSystem:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager.stock

    def create_bill(self, med_name, qty):
        if med_name not in self.inventory:
            print("Error: Medicine not found!")
            return
        
        if qty > self.inventory[med_name]['qty']:
            print(f"Error: Only {self.inventory[med_name]['qty']} units available.")
            return

        self.inventory[med_name]['qty'] -= qty
        total = qty * self.inventory[med_name]['price']
        
        print("\n================ RECEIPT ================")
        print(f"Medicine : {med_name}")
        print(f"Quantity : {qty}")
        print(f"Total    : ₹{total:.2f}")
        print("=========================================")
