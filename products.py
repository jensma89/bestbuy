"""
products.py

Contains the Product class
and handle some operations for products.
"""

class Product:
    """Represents products that available in the store."""

    try:
        def __init__(self, name, price, quantity):
            """Initialize products and raise errors."""
            if not name:
                raise ValueError("Name cannot be empty")
            if price < 0:
                raise ValueError("Price cannot be negative")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")


            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

    except ValueError as e:
        print(f"Error: {e}")


    def get_quantity(self):
        """Get the quantity of the product."""
        return self.quantity


    def set_quantity(self, quantity):
        """Set the quantity of the product
        and check is not zero or negative."""

        try:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            self.quantity = quantity
            if quantity == 0:
                self.active = False

        except ValueError as e:
            print(f"Error: {e}")


    def is_active(self):
        """Check if product is active."""
        return self.active


    def activate(self):
        """Activate product."""
        self.active = True


    def deactivate(self):
        """Deactivate product."""
        self.active = False


    def show(self):
        """Show product."""
        return (f"{self.name}, "
                f"price: {self.price}, "
                f"quantity: {self.quantity}")


    def buy(self, quantity):
        """Function to buy product. With error handling."""

        try:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            if not self.active:
                raise Exception("Product is not active")
            if quantity > self.quantity:
                raise Exception("Not enough products in stock!")

            self.quantity -= quantity
            if self.quantity == 0:
                self.active = False

        except (ValueError, Exception) as e:
            print(f"Error: {e}")

        return self.price * quantity
