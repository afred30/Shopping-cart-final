class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_price * self.item_quantity)}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
        for item in self.cart_items:
            if item.item_name == new_item.item_name:
                if new_item.item_description != "none":
                    item.item_description = new_item.item_description
                if new_item.item_price != 0.0:
                    item.item_price = new_item.item_price
                if new_item.item_quantity != 0:
                    item.item_quantity = new_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${int(self.get_cost_of_cart())}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("Choose an option:\n").strip().lower()

        if choice == 'a':
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, qty, desc))

        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=qty))

        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            break
        else:
            continue


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)