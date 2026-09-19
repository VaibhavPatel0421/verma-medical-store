# Verma Medical Store - Reports Manager

class ReportManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def show_low_stock_alert(self, threshold=10):
        low_stock = []
        for med in self.inventory.medicines.values():
            if med.quantity < threshold:
                low_stock.append(med)

        if low_stock:
            print(f"Warning: The following items have less than {threshold} units in stock!")
            print("-" * 45)
            for item in low_stock:
                print(f"- {item.name}: Only {item.quantity} left")
        else:
            print(f"All medicines have sufficient stock (above {threshold} units).")


