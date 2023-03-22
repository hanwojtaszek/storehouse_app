import validators as v


class Product:
    def __init__(self, type, quantity, price, description):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.description = description

    def change_price(self):
        """
                Allow changing product's price.

                Parameters: N/A
                Returns: N/A
        """
        self.price = v.check_price(input("Podaj nową cenę: "))

    def change_quantity(self):
        """
                Allow changing product's quantity.

                Parameters: N/A
                Returns: amount (int) : difference between last and current product's quantity
        """
        current_quantity = self.quantity
        self.quantity = int(v.check_digits(input("Podaj nowy stan magazynowy: ")))
        amount = self.quantity - current_quantity
        return amount

    def add_product(self):
        """
                Allow adding new product.

                Parameters: N/A
                Returns: amount (int) : difference between last and current product's quantity
        """
        amount = int(v.check_digits(input("Ile produktów dodać? ")))
        self.quantity += amount
        return amount

    def remove_product(self):
        """
                Allow removing a product.

                Parameters: N/A
                Returns: amount (int) : difference between last and current product's quantity
        """
        amount = int(v.check_digits(input("Ile produktów odjąć? ")))
        if v.check_amount(self.quantity, amount):
            self.quantity -= amount
            return -amount
        else:
            return 0
