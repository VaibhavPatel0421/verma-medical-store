# Verma Medical Store - Main Program

from models import Medicine
from inventory import InventoryManager
from billing import BillingSystem
from reports import ReportManager

def display_menu():
    print("\n====================================")
    print("     VERMA MEDICAL STORE SYSTEM     ")
    print("====================================")
    print("1. Show Available Medicines")
    print("2. Add New Stock")
    print("3. Make Customer Bill")
    print("4. Check Low Stock Items")
    print("5. Exit Program")
    print("====================================")

def main():
    inventory = InventoryManager()
    billing = BillingSystem(inventory)
    reports = ReportManager(inventory)

    # Sample medicines
    inventory.add_medicine(Medicine("Paracetamol 500", 15.0, 50))
    inventory.add_medicine(Medicine("Dolo 650", 30.0, 8))
    inventory.add_medicine(Medicine("Combiflam", 25.0, 40))
    inventory.add_medicine(Medicine("Pantop 40", 55.0, 5))

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            print("\n--- Current Inventory ---")
            inventory.show_all_medicines()

        elif choice == '2':
            print("\n--- Add New Medicine ---")
            name = input("Enter medicine name: ").strip()
            
            try:
                price = float(input("Enter price per unit: "))
                quantity = int(input("Enter quantity to add: "))
                
                if price <= 0 or quantity <= 0:
                    print("Error: Price and quantity must be positive numbers!")
                else:
                    inventory.add_medicine(Medicine(name, price, quantity))
                    print(f"Success: {name} added to inventory.")
            except ValueError:
                print("Invalid input! Please enter numbers for price and quantity.")

        elif choice == '3':
            print("\n--- Create Customer Bill ---")
            billing.start_new_bill()

        elif choice == '4':
            print("\n--- Low Stock Alert ---")
            reports.show_low_stock_alert(threshold=10)

        elif choice == '5':
            print("\nThank you for using Verma Medical Store System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()

