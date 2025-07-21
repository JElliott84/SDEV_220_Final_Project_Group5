orders = []
order_number = 1

# Define available coil types with item numbers and prices
available_coils = {
    1: {"name": "Coil 1", "price": 0.01},
    2: {"name": "Coil 2", "price": 0.02},
    3: {"name": "Coil 3", "price": 0.03}
}

def take_order():
    global order_number
    """Takes a new order from the customer."""
    customer_name = input("Enter customer name: ")
    order_details = []  # List to store items for the current order

    while True:
        print("Available Coils:")
        for item_num, coil_info in available_coils.items():
            print(f"{item_num}. {coil_info['name']} - ${coil_info['price']:.2f}")

        try:
            item_choice = int(input("Enter coil item number (or 0 to finish order): "))
            if item_choice == 0:
                break
            elif item_choice in available_coils:
                quantity = int(input(f"Enter quantity for {available_coils[item_choice]['name']}: "))
                order_details.append({
                    "item_number": item_choice,
                    "name": available_coils[item_choice]["name"],
                    "price": available_coils[item_choice]["price"],
                    "quantity": quantity
                })
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate total cost for the current order
    total_cost = sum(item["price"] * item["quantity"] for item in order_details)

    # Store the complete order
    orders.append({
        "order_number": order_number,
        "customer_name": customer_name,
        "items": order_details,
        "total_cost": total_cost
    })
    print(f"Your Order (#{order_number}) has been placed successfully!")
    order_number += 1

def view_orders():
    if not orders:
        print("You have no orders placed yet.")
        return

    for order in orders:
        print("Order Details")
        print(f"Customer Name: {order['customer_name']}")
        print("Items:")
        for item in order["items"]:
            print(f"  - {item['name']} (x{item['quantity']}) - ${item['price']:.2f} each")
        print(f"Total Cost: ${order['total_cost']:.2f}")

# Main loop for the ordering system
while True:
    print("Coil Ordering/Sales System")
    print("1. New Order")
    print("2. View All Orders")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        take_order()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        print("Thank you! ")
        break
    else:
        print("Invalid choice. Please try again.")
