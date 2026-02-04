# Online Sales Analysis

## Project Description
This project demonstrates basic Git and GitHub functionalities through a Python application for managing products and a customer’s shopping cart.  
The goal is to showcase how classes, methods, and branches are used in a Git repository, as well as how conflicts are resolved and new features are added.

---

## Classes and Functionalities

### Product
- Represents a single product.
- **Attributes:**
  - `name` – product name
  - `price` – product price
  - (optional) `quantity` – product stock quantity

---

### ProductManager
- Manages the list of available products.
- **Methods:**
  - `add_product(product)` – adds a new product to the list
  - `remove_product_by_name(name)` – removes a product by its name
  - `show_products()` – displays all products
  - `calculate_total_value()` – calculates the total inventory value

---

### Cart
- Manages the customer’s shopping cart.
- **Attributes:**
  - `cart_items` – list of products in the cart
- **Methods:**
  - `add_to_cart(product)` – adds a product to the cart
  - `calculate_total()` – calculates the total cart value
  - `show_cart()` – displays the cart contents

---

## main.py
- Creates an instance of `ProductManager` and adds products.
- Creates an instance of `Cart`.
- Adds three randomly selected products from the product list to the cart.
- Prints the total cart value and the products inside the cart.