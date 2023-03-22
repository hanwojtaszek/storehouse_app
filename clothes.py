import validators as v
from product import Product


class Clothes(Product):
    def __init__(self, dictionary):
        self.size = dictionary["size"]
        super().__init__(dictionary["type"], dictionary["quantity"], dictionary["price"], dictionary["description"])


def add_clothes_data(dictionary):
    """
            Allow to enter data for new product of "clother" type (class Clothes).

            Parameters: dictionary (dict) : Empty dictionary
            Returns: dictionary (dict) : Dictionary with values entered by user, used to create new class instance
    """
    dictionary["type"] = input("Rodzaj: ")
    dictionary["size"] = v.check_size(input("Rozmiar: "))
    dictionary["quantity"] = int(v.check_digits(input("Stan magazynowy: ")))
    dictionary["price"] = float(v.check_price(input("Cena: ")))
    dictionary["description"] = input("Opis: ")
    return dictionary
