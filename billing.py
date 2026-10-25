def calculate_total(subtotal):
    if subtotal < 0 :
        raise ValueError("Subtotal Cannot be Less than 0.")

    discount = subtotal * 0.10 if subtotal > 300 else 0
    return round((subtotal - discount) * 1.05,2)