# Verma Medical Store - Reports Manager

from inventory import inventory_list

def show_low_stock_alert(threshold=10):
    low_stock = []
    for item in inventory_list:
        if item["quantity"] < threshold:
            low_stock.append(item)

    if low_stock:
        print(f"\nWarning: Items with less than {threshold} units in stock!")
        print("-" * 45)
        for item in low_stock:
            print(f"- {item['name']}: Only {item['quantity']} left")
    else:
        print(f"\nAll medicines have sufficient stock (above {threshold} units).")

