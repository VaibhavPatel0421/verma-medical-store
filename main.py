from inventory import InventoryManager
from billing import BillingSystem
from reports import ReportGenerator

def main():
    inv = InventoryManager()
    bill = BillingSystem(inv)
    report = ReportGenerator(inv)

    while True:
        print("\n====================================")
        print("      VERMA MEDICAL STORE     ")
        print("====================================")
        print("1. View Medicine Inventory")
        print("2. Add New Medicine Stock")
        print("3. Process Patient Bill")
        print("4. Check Low Stock Report")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            inv.display_stock()
        elif choice == '2':
            name = input("Medicine Name: ").strip().capitalize()
            try:
                price = float(input("Unit Price (₹): "))
                qty = int(input("Quantity: "))
                inv.add_medicine(name, price, qty)
            except ValueError:
                print("Error: Invalid numeric input.")
        elif choice == '3':
            name = input("Medicine Name to buy: ").strip().capitalize()
            try:
                qty = int(input("Quantity required: "))
                bill.create_bill(name, qty)
            except ValueError:
                print("Error: Invalid quantity input.")
        elif choice == '4':
            report.low_stock_alert()
        elif choice == '5':
            print("Closing Medical Store. DHANYAWAAD!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
