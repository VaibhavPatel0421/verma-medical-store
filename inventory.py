# Verma Medical Store - Inventory Manager

# Main inventory list to store medicine dictionaries
inventory_list = []

def add_medicine(name, price, quantity):
    # Check if medicine already exists in list
    for item in inventory_list:
        if item["name"].lower() == name.lower():
            item["quantity"] += quantity
            print(f"Updated quantity for {item['name']}.")
            return

    # Add new item
    new_item = {"name": name, "price": float(price), "quantity": int(quantity)}
    inventory_list.append(new_item)
    print(f"Added {name} to inventory.")

def show_all_medicines():
    if not inventory_list:
        print("No medicines available in stock.")
        return

    print("\nName                 | Price (Rs) | Quantity")
    print("-" * 45)
    for item in inventory_list:
        print(f"{item['name']:<20} | {item['price']:<10.2f} | {item['quantity']}")

