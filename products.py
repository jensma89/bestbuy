class Product:

    def __init__(self, name, price, quantity):
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


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return (f"{self.name}, "
                f"price: {self.price}, "
                f"quantity: {self.quantity}")


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("Not enough products in stock!")

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False

        return self.price * quantity
