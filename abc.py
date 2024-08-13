class Product:
    def __init__(self, name, price, description):
        self.n = name
        self.p = price
        self.d = description

    def calculate_discount(self, discount_rate):
        return self.price * (1 - discount_rate)

    def get_product_details(self):
        return f"Name : {self.n}, Price : ${self.p}, Description : {self.d}"


class ElectronicProduct(Product):
    def __init__(self, name, price, description, brand, warranty):
        super().__init__(name, price, description)
        self.b = brand
        self.w = warranty

    def get_product_details(self):
        base_details = super().get_product_details()
        return f"{base_details}, Brand : {self.b}, Warranty : {self.w} years"
    

class Clothing(Product):
    def __init__(self, name, price, description, size, fabric):
        self.s = size
        self.f = fabric

    def get_product_details(self):
        base_details = super().get_product_details()
        return f"{base_details}, Size : {self.s}, Fabric : {self.f}"

    
class Book(Product):
    def __init__(self, name, price, description, author, genre):
        self.a = author
        self.g = genre

    def get_product_details(self):
        base_details = super().get_product_details()
        return f"{base_details}, Author : {self.a}, Genre : {self.g}"


class Furniture(Product):
    def __init__(self, name, price, description, material, dimensions):
        self.m = material
        self.dimen = dimensions

    def get_product_details(self):
        base_details = super().get_product_details()
        return f"{base_details}, Material : {self.m}, Dimensions : {self.dimen}"


class Order:
    def __init__(self, order_id, customer_name, items):
        self.odr_id = order_id
        self.cn = customer_name
        self. i = items

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def get_order_details(self):
        item_details = "\n".join([item.get_product_details() for item in self.items])
        return f"\nOreder Id : {self.odr_id}, Customer name : {self.cn}, Items : \n{self.item_details}"


class DomesticOrder(Order):
    def __init__(self, order_id, customer, items, shipping_address):
        super().__init__(order_id, customer, items)
        self.sa = shipping_address

    def calculate_shipping_cost(self):
        return 5.00

    def get_order_details(self):
        base_details = super().get_order_details()
        return f"{base_details}, \nShipping Address : {self.sa}, Shipping Cost : ${self.calculate_shipping_cost():.2f}"


class InternationalOrder(Order):
    def __init__(self, order_id, customer, items, shipping_address, customs_duty):
        super().__init__(order_id, customer, items)
        self.sa = shipping_address
        self.cd = customs_duty

    def calculate_shipping_cost(self):
        return 20.00 + self.cd

    def get_order_details(self):
        base_details = super().get_order_details()
        return f"{base_details}, \nShipping Address : {self.sa}, Shipping Cost : ${self.calculate_shipping_cost():.2f,}, Customs Duty : ${self.cd:.2f}"



if __name__ == "__main__":
    tv = ElectronicProduct("Smart LED TV", 35000, "Samsung 108 cm (43 inches) D Series Crystal 4K Vivid Ultra HD Smart LED TV UA43DUE70BKLXL (Black)", 
                            "Samsung", 1)
    shirt = Clothing("Shirt", 416.88, "Casual Shirt for Men", "L", "Polyester")
    book = Book("11 Rules For Life", )
