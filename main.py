"""
main.py

Show the menu options
and has the logic to handle the app.
"""

from store import Store
from products import Product


def start(best_buy):
    """Main menu options and logic."""

    # Listener loop to show the menu
    while True:
        print("\nStore Menu")
        print("-" * 10)
        print("1. List all products in the store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_input = input("Please choose a number: ")

        # Menu logic
        if user_input == "1":
            for product in best_buy.get_all_products():
                print(product.show())

        elif user_input == "2":
            print("Total quantity in store:",
                  best_buy.get_total_quantity())

        elif user_input == "3":
            shopping_list = []
            product_index = int(input("Which product do you want?"
                                      "(enter a number) ")) - 1
            quantity = int(input("What amount do you want?"
                                 "(enter a number) "))
            product = best_buy.get_all_products()[product_index]
            shopping_list.append((product, quantity))
            total = best_buy.order(shopping_list)
            print("Total price: ", total)

        elif user_input == "4":
            print("\nBye!")
            break

        else:
            print("Invalid choice. Try again.")

def main():
    """Initialisation to have products in the store."""
    product_list = [
        Product("MacBook Air M2",
                price=1450,
                quantity=100),
        Product("Bose QuietComfort Earbuds",
                price=250,
                quantity=500),
        Product("Google Pixel 7",
                price=500,
                quantity=250)
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
