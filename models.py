# Verma Medical Store - Medicine Data Model

def create_medicine(name, price, quantity):
    # Returns a simple dictionary for a medicine item
    return {
        "name": name,
        "price": float(price),
        "quantity": int(quantity)
    }

