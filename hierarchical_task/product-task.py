# (1). E-commerce Platform
# Product Hierarchy:
# Base class Product with attributes like name, price, description.
# Subclasses: ElectronicProduct, Clothing, Book, Furniture, etc., with specific attributes (e.g., brand, size, author, material) and methods (e.g., calculate_discount, get_product_details).
# Order and Shipping:
# Base class Order with attributes like order_id, customer, items.
# Subclasses: DomesticOrder, InternationalOrder with specific attributes (e.g., shipping_address, customs_duty) and methods (e.g., calculate_shipping_cost).

# Ans...

# # Product Hierarchy
# class Product:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description

#     def calculate_discount(self, discount_rate):
#         return self.price * (1 - discount_rate)

#     def get_product_details(self):
#         return f"Name: {self.name}, Price: ${self.price:.2f}, Description: {self.description}"

# # Subclass for Electronics
# class ElectronicProduct(Product):
#     def __init__(self, name, price, description, brand, warranty):
#         super().__init__(name, price, description)
#         self.brand = brand
#         self.warranty = warranty

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Brand: {self.brand}, Warranty: {self.warranty} years"

# # Subclass for Clothing
# class Clothing(Product):
#     def __init__(self, name, price, description, size, fabric):
#         super().__init__(name, price, description)
#         self.size = size
#         self.fabric = fabric

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Size: {self.size}, Fabric: {self.fabric}"

# # Subclass for Book
# class Book(Product):
#     def __init__(self, name, price, description, author, genre):
#         super().__init__(name, price, description)
#         self.author = author
#         self.genre = genre

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Author: {self.author}, Genre: {self.genre}"

# # Subclass for Furniture
# class Furniture(Product):
#     def __init__(self, name, price, description, material, dimensions):
#         super().__init__(name, price, description)
#         self.material = material
#         self.dimensions = dimensions

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Material: {self.material}, Dimensions: {self.dimensions}"

# # Order and Shipping
# # class Order:
# #     def __init__(self, order_id, customer, items):
# #         self.order_id = order_id
# #         self.customer = customer
# #         self.items = items


#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def get_order_details(self):
#         item_details = "\n".join([item.get_product_details() for item in self.items])
#         return f"\nOrder ID: {self.order_id}, Customer: {self.customer}, Items: \n{item_details}"

# # Subclass for Domestic Order
# class DomesticOrder(Order):
#     def __init__(self, order_id, customer, items, shipping_address):
#         super().__init__(order_id, customer, items)
#         self.shipping_address = shipping_address

#     def calculate_shipping_cost(self):
#         # Example flat rate for domestic shipping
#         return 5.00

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}"

# # Subclass for International Order
# class InternationalOrder(Order):
#     def __init__(self, order_id, customer, items, shipping_address, customs_duty):
#         super().__init__(order_id, customer, items)
#         self.shipping_address = shipping_address
#         self.customs_duty = customs_duty

#     def calculate_shipping_cost(self):
#         # Example rate for international shipping
#         return 20.00 + self.customs_duty

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}, Customs Duty: ${self.customs_duty:.2f}"

# # Example Usage
# if __name__ == "__main__": 
#     # Creating products
#     laptop = ElectronicProduct("Laptop", 1200.00, "High-end gaming laptop", "BrandX", 2)
#     tshirt = Clothing("T-shirt", 20.00, "Cotton T-shirt", "L", "Cotton")
#     book = Book("Data Science 101", 30.00, "Introduction to Data Science", "Jane Doe", "Educational")
#     sofa = Furniture("Sofa", 500.00, "Comfortable sofa", "Leather", "7x3 feet")

#     # Creating an order
#     order_items = [laptop, tshirt, book, sofa]
#     domestic_order = DomesticOrder(1, "John Smith", order_items, "123 Main St, Springfield")
#     international_order = InternationalOrder(2, "Jane Doe", order_items, "456 Global St, London", 50.00)

#     # Print order details
#     print(domestic_order.get_order_details())
#     print("\n" + "="*40 + "\n")
#     print(domestic_order.calculate_total())










# class Product:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description

#     def calculate_discount(self, discount_rate):
#         return self.price * (1 - discount_rate)

#     def get_product_details(self):
#         return f"Name: {self.name}, Price: ${self.price:.2f}, Description: {self.description}"

# # Subclass for Electronics
# class ElectronicProduct(Product):
#     def __init__(self, name, price, description, brand, warranty):
#         super().__init__(name, price, description)
#         self.brand = brand
#         self.warranty = warranty

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Brand: {self.brand}, Warranty: {self.warranty} years"

# # Subclass for Clothing
# class Clothing(Product):
#     def __init__(self, name, price, description, size, fabric):
#         super().__init__(name, price, description)
#         self.size = size
#         self.fabric = fabric

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Size: {self.size}, Fabric: {self.fabric}"

# # Subclass for Book
# class Book(Product):
#     def __init__(self, name, price, description, author, genre):
#         super().__init__(name, price, description)
#         self.author = author
#         self.genre = genre

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Author: {self.author}, Genre: {self.genre}"

# # Subclass for Furniture
# class Furniture(Product):
#     def __init__(self, name, price, description, material, dimensions):
#         super().__init__(name, price, description)
#         self.material = material
#         self.dimensions = dimensions

#     def get_product_details(self):
#         base_details = super().get_product_details()
#         return f"{base_details}, Material: {self.material}, Dimensions: {self.dimensions}"

# # Order and Shipping
# class Order:
#     order_id = 0
#     def __init__(self, customer, items):
#         self.customer = customer
#         self.items = items
#         Order.order_id += 1
#         self.order_id = Order.order_id


#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def get_order_details(self):
#         item_details = "\n".join([item.get_product_details() for item in self.items])
#         return f"\n\nOrder ID: {self.order_id}, Customer: {self.customer}, Items: \n{item_details}"

# # Subclass for Domestic Order
# class DomesticOrder(Order):
#     def __init__(self, customer, items, shipping_address):
#         super().__init__(customer, items)
#         self.shipping_address = shipping_address

#     def calculate_shipping_cost(self):
#         # Example flat rate for domestic shipping
#         return 5.00

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}"

# # Subclass for International Order
# class InternationalOrder(Order):
#     def __init__(self, customer, items, shipping_address, customs_duty):
#         super().__init__(customer, items)
#         self.shipping_address = shipping_address
#         self.customs_duty = customs_duty

#     def calculate_shipping_cost(self):
#         # Example rate for international shipping
#         return 20.00 + self.customs_duty

#     def get_order_details(self):
#         base_details = super().get_order_details()
#         return f"{base_details}\nShipping Address: {self.shipping_address}, Shipping Cost: ${self.calculate_shipping_cost():.2f}, Customs Duty: ${self.customs_duty:.2f}"

# # Example Usage
# if __name__ == "__main__": 
#     # Creating products
#     laptop = ElectronicProduct("Laptop", 1200.00, "High-end gaming laptop", "BrandX", 2)
#     tshirt = Clothing("T-shirt", 20.00, "Cotton T-shirt", "L", "Cotton")
#     book = Book("Data Science 101", 30.00, "Introduction to Data Science", "Jane Doe", "Educational")
#     sofa = Furniture("Sofa", 500.00, "Comfortable sofa", "Leather", "7x3 feet")



#     laptop = ElectronicProduct("Laptop", 1200.00, "High-end gaming laptop", "BrandX", 2)
#     tshirt = Clothing("T-shirt", 20.00, "Cotton T-shirt", "L", "Cotton")
#     book = Book("Data Science 101", 30.00, "Introduction to Data Science", "Jane Doe", "Educational")
#     sofa = Furniture("Sofa", 500.00, "Comfortable sofa", "Leather", "7x3 feet")

#     # Creating an order
#     order_items = [laptop, tshirt, book, sofa]
#     domestic_order = DomesticOrder("John Smith", order_items, "123 Main St, Springfield")
#     international_order = InternationalOrder("Jane Doe", order_items, "456 Global St, London", 50.00)


    # order_items = [laptop, tshirt, book, sofa]
    # domestic_order = DomesticOrder("Max", order_items, "123 Main St, Springfield")
    # international_order = InternationalOrder("Bob", order_items, "456 Global St, London", 50.00)

    # # Print order details
    # print(domestic_order.get_order_details())
    # print("\n" + "="*40 + "\n")
    # print(domestic_order.calculate_total())


    # print(international_order.get_order_details())
    # print("\n" + "="*40 + "\n")
    # print(international_order.calculate_total())
