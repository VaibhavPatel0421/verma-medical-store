# Verma Medical Store - Billing System

class BillingSystem:
    def __init__(self, inventory):
        self.inventory = inventory

    def start_new_bill(self):
        if not self.inventory.medicines:
            print("Stock is empty! Add medicines before billing.")
            return

        total_amount = 0.0
        bill_items = []

        while True:
            med_name = input("Enter medicine name (or type 'done' to finish): ").strip()
            if med_name.lower() == 'done':
                break

            if med_name not in self.inventory.medicines:
                print("Medicine not found in stock! Check the spelling.")
                continue

            stock_item = self.inventory.medicines[med_name]

            try:
                qty = int(input(f"Enter quantity for {med_name}: "))
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                if qty > stock_item.quantity:
                    print(f"Only {stock_item.quantity} units available in stock!")
                    continue

                item_cost = stock_item.price * qty
                total_amount += item_cost
                stock_item.quantity -= qty # Stock kam kar rahe hain

                bill_items.append((med_name, qty, item_cost))
                print(f"Added {qty} x {med_name} to cart.")

            except ValueError:
                print("Please enter a valid number for quantity.")

        # Print Final Bill Receipt
        if bill_items:
            print("\n" + "=" * 35)
            print("       VERMA MEDICAL STORE")
            print("          CUSTOMER BILL")
            print("=" * 35)
            for name, qty, cost in bill_items:
                print(f"{name:<18} x{qty:<3} = Rs.{cost:.2f}")
            print("-" * 35)
            print(f"TOTAL AMOUNT:        Rs.{total_amount:.2f}")
            print("=" * 35)
            print("Thank you! Visit again.\n")
        else:
            print("No items added to bill.")
