# (5). Inventory Management System
# Product Hierarchy:
# Base class Product with attributes like product_id, name, price, quantity.
# Subclasses: ElectronicProduct, Clothing, Food, etc., 
# with specific attributes (e.g., warranty, size, expiry_date) 
# and methods (e.g., calculate_discount, check_stock).

# Order Hierarchy:
# Base class Order with attributes like order_id, customer, items.
# Subclasses: PurchaseOrder, SalesOrder, ReturnOrder, etc., 
# with specific attributes (e.g., supplier, reason_for_return) 
# and methods (e.g., process_order, generate_invoice).

# Ans...

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def check_stock(self):
        return self.quantity
    
    def product_details(self):
        return f"\nProduct name : {self.name} \nProduct ID - {self.product_id} \nPrice : {self.price} \nQuantity : {self.quantity}"
        

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, quantity, warranty):
        super().__init__(product_id, name, price, quantity)
        self.warranty = warranty

    def calculate_discount(self):
        return self.price * 0.2
    
    def product_details(self):
        base_details = super().product_details()
        return f"{base_details} \nWarranty: {self.warranty} years"

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity, size):
        super().__init__(product_id, name, price, quantity)
        self.size = size

    def calculate_discount(self):
        return self.price * 0.3
    
    def product_details(self):
        base_details = super().product_details()
        return f"{base_details} \nSize: {self.size}"

class Food(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = expiry_date

    def calculate_discount(self):
        return self.price * 0.2

    def product_details(self):
        base_details = super().product_details()
        return f"{base_details} \nExpiry Date - : {self.expiry_date}"

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def process_order(self):
        for item in self.items:
            if item.check_stock():
                item.quantity -= 1
            else:
                print(f"Item {item.name}is out of stock!")

    def generate_invoice(self):
        total = sum(item.price for item in self.items)
        invoice_details = f"\nInvoice Order Id : {self.order_id} \nCustomer Name : {self.customer} \nTotal Amount is : {total}"
        return invoice_details    

    def order_details(self):
        return f"\nOrder ID : {self.order_id} \nCustomer Name : {self.customer} \nItems : {self.items}"
    

class PurchaseOrder(Order): 
    def __init__(self, order_id, customer, items, supplier):
        super().__init__(order_id, customer, items)
        self.supplier = supplier

    def order_details(self):
        return f"\nPurchase Order ID : {self.order_id} \nSupplier : {self.supplier}"
    


class SalesOrder(Order):
    def __init__(self, order_id, customer, items):
        super().__init__(order_id, customer, items)

    def order_details(self):
        return f"\nSales Order ID : {self.order_id} \nCustomer Name : {self.customer}"
    

class ReturnOrder(Order):
    def __init__(self, order_id, customer, items, reason_for_return):
        super().__init__(order_id, customer, items)
        self.reason_for_return = reason_for_return

    def order_details(self):
        return f"\nReturn Order ID : {self.order_id} \nReason for return : {self.reason_for_return}"
    

mobile = ElectronicProduct(1, "Mobile", 715.14, 2, 4)
shirt = Clothing(2, "Shirt", 10.13, 4, "M")
mango = Food(3, "Mango", 0.1, 20, "10-10-2024")

print(mobile.product_details())
print(shirt.product_details())
print(mango.product_details())

order_items = [mobile, shirt, mango]
sales_order = SalesOrder(101, "Neha Shukla", order_items)

sales_order.process_order()

print(sales_order.generate_invoice())

return_order = ReturnOrder(156, "Max Smith", [shirt], "Size too small")
print(return_order.order_details())