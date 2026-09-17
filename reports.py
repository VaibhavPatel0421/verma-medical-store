class ReportGenerator:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager.stock

    def low_stock_alert(self, threshold=10):
        print(f"\n--- LOW STOCK REPORT (< {threshold} units) ---")
        found = False
        for med, info in self.inventory.items():
            if info['qty'] < threshold:
                print(f"ALERT: {med} is low on stock! Remaining: {info['qty']} units")
                found = True
        if not found:
            print("All medicines have sufficient stock level.")
