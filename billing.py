# Verma Medical Store - Billing System

from inventory import inventory_list

def start_new_bill():
    if not inventory_list:
        print("Stock is empty! Add medicines first.")
        return

    total_amount = 0.0
    bill_items = []

    while True:
        med_name = input("Enter medicine name (or type 'done' to finish): ").strip()
        if med_name.lower() == 'done':
            break

        # Search for medicine in inventory list
        selected_item = None
        for item in inventory_list:
            if item["name"].lower() == med_name.lower():
                selected_item = item
                break

        if not selected_item:
            print("Medicine not found! Check spelling.")
            continue

        try:
            qty = int(input(f"Enter quantity for {selected_item['name']}: "))
            if qty <= 0:
                print("Quantity must be greater than zero.")
                continue
            if qty > selected_item["quantity"]:
                print(f"Only {selected_item['quantity']} units left in stock!")
                continue

            # Calculate price and reduce stock
            cost = selected_item["price"] * qty
            total_amount += cost
            selected_item["quantity"] -= qty

            bill_items.append({"name": selected_item["name"], "qty": qty, "cost": cost})
            print(f"Added {qty} x {selected_item['name']} to bill.")

        except ValueError:
            print("Please enter a valid number for quantity.")

    # Print Final Bill
    if bill_items:
        print("VERMA MEDICAL STORE")
        print("CUSTOMER BILL")
        for item in bill_items:
            print(f"{item['name']:<18} x{item['qty']:<3} = Rs.{item['cost']:.2f}")
        print(f"TOTAL AMOUNT:        Rs.{total_amount:.2f}")