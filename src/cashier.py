# cashier.py

def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def main():
    items = [
        {'name': 'Apple', 'price': 0.5, 'quantity': 2},
        {'name': 'Banana', 'price': 0.3, 'quantity': 3},
        {'name': 'Orange', 'price': 0.4, 'quantity': 1}
    ]
    total = calculate_total(items)
    print("Total: $", total)

if __name__ == "__main__":
    main()
