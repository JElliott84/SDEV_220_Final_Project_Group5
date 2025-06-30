class Inventory:
    def __init__(self, sku, name, description, price, stock):
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

class Customer:
    def __init__(self, customer_id, name, address, phonenumber):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

class Employee:
    def __init__(self, employee_id, emp_name, emp_address, emp_phone):
        self.employee_id = employee_id
        self.emp_name = emp_name
        self.emp_address = emp_address
        self.emp_phone = emp_phone

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = "Pending"  

    def update_status(self, order_status):
        self.status = order_status

