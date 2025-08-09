import products

class Store:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self):
        return [product for product in self.products
                if product.is_active()]


    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price