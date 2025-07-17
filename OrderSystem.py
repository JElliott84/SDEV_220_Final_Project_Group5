""" The Available Coils is a place holder for the inventory so I can set up the order system. Feel free to adjust to reflect what is needed on the inventory or customer side as they link together."""
orders = []

# Define available coil types with item numbers and prices
avail_coils = {
    1: {"name": "Coil 1", "price": 10.50},
    2: {"name": "Coil 2", "price": 8.75},
    3: {"name": "Coil 3", "price": 7.25}
}

def take_order():
"""Takes a new order from the customer."""
    customer_name = input("Enter customer name: ")
    order_details = []  # List to store items for the current order

    while True:
        print("Available Coils:")
        for item_sku, coil_info in avail_coils.items():
            print(f"{item_sku}. {coil_info['name']} - ${coil_info['price']:.2f}")

        try:
            item_choice = int(input("Enter coil item number (or 0 to finish order): "))
            if item_choice == 0:
                break
            elif item_choice in available_coils:
                quantity = int(input(f"Enter quantity for {avail_coils[item_choice]['name']}: "))
                order_details.append({
                    "item_sku": item_choice,
                    "name": avail_coils[item_choice]["name"],
                    "price": avail_coils[item_choice]["price"],
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
        "customer_name": customer_name,
        "items": order_details,
        "total_cost": total_cost
    })
    print("Order placed successfully!")

def view_orders():
    """Displays all placed orders."""
    if not orders:
        print("No orders placed yet.")
        return

    for order in orders:
        print("Your Order Details")
        print(f"Customer Name: {order['customer_name']}")
        print("Items:")
        for item in order["items"]:
            print(f"  - {item['name']} (x{item['quantity']}) - ${item['price']:.2f} each")
        print(f"Total Cost: ${order['total_cost']:.2f}")

# Main loop for the ordering system
while True:
    print("Ordering Menu")
    print("1. New Order")
    print("2. View All Orders")
    print("3. Exit")
    
    choice = input("Select your option:")

    if choice == '1':
        take_order()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        print("Thank you! ")
        break
    else:
        print("Invalid choice. Please try again.")
