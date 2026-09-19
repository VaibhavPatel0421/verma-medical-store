# Verma Medical Store - Inventory Manager

class InventoryManager:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, medicine):
        # If medicine already exists, update quantity
        if medicine.name in self.medicines:
            self.medicines[medicine.name].quantity += medicine.quantity
        else:
            self.medicines[medicine.name] = medicine

    def show_all_medicines(self):
        if not self.medicines:
            print("No medicines in stock currently.")
            return
        
        print("\nName                 | Price         | Quantity")
        print("-" * 45)
        for med in self.medicines.values():
            print(med)

