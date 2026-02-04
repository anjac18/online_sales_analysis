from product import Product
from product_manager import ProductManager

m = ProductManager()

p1 = Product("iPhone", 850, 8)
p2 = Product("TV", 1200, 3)
p3 = Product("Gaming Laptop", 680, 7)

m.add_product(p1)
m.add_product(p2)
m.add_product(p3)