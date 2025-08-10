import products
import store

def main():

    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2",
                                     price=1450,
                                     quantity=100),
                    products.Product("Bose QuietComfort Earbuds",
                                     price=250,
                                     quantity=500),
                    products.Product("Google Pixel 7",
                                     price=500,
                                     quantity=250)
                    ]


    best_buy = store.Store(product_list)


    def start(best_buy):
        while True:
            print("\nStore_Menu")
            print("\n-" * 10)
            print("\n1. List all products in the store")
            print("\n2. Show total amount in store")
            print("\n3. Make an order")
            print("\n4. Quit")

            user_input = input("\nPlease choose a number: ")


if __name__ == "__main__":
    main()