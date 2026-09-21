
  # Verma Medical Store - Main Program

from inventory import add_medicine, show_all_medicines
from billing import start_new_bill
from reports import show_low_stock_alert

def main():
    # Adding sample data to start with
    add_medicine("Paracetamol 650", 15.0, 50)
    add_medicine("Dolo 650", 30.0, 8)
    add_medicine("Combiflam", 25.0, 40)
    add_medicine("Pantop 40", 55.0, 5)

    while True:
        print("     VERMA MEDICAL STORE SYSTEM     ")
        print("1. Show Available Medicines")
        print("2. Add New Stock")
        print("3. Make Customer Bill")
        print("4. Check Low Stock Items")
        print("5. Exit Program")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            show_all_medicines()

        elif choice == '2':
            print("\n--- Add New Stock ---")
            name = input("Enter medicine name: ").strip()
            try:
                price = float(input("Enter price per unit: "))
                quantity = int(input("Enter quantity: "))
                if price <= 0 or quantity <= 0:
                    print("Price and quantity must be positive numbers!")
                else:
                    add_medicine(name, price, quantity)
            except ValueError:
                print("Invalid input! Please enter valid numbers.")

        elif choice == '3':
            start_new_bill()

        elif choice == '4':
            show_low_stock_alert(threshold=10)

        elif choice == '5':
            print("Thank you for using Verma Medical Store System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()
