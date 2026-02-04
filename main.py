from product import Product
from product_manager import ProductManager

m = ProductManager()

p1 = Product("Phone", 850, 8)
p2 = Product("TV", 1200, 5)
p3 = Product("Laptop", 680, 7)

m.add_product(p1)
m.add_product(p2)
m.add_product(p3)

print("List of products:")
m.show_products()

print(f"\nTotal value of products: ${m.total_value()}")