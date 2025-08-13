"""
store.py

Contains the Store class
and handle some operations to get access.
"""

class Store:
    """Represents a store that handle products and orders."""

    def __init__(self, products=None):
        """Initialize the store with a list of products."""
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)


    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)


    def get_total_quantity(self):
        """Return the total quantity of the products in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self):
        """Return a list of all products in the store."""
        return [product for product in self.products
                if product.is_active()]


    def order(self, shopping_list):
        """Return the total price of the order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error: {e}")
        return total_price
