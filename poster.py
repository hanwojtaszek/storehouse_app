import validators as v
from product import Product


class Poster(Product):
    def __init__(self, dictionary):
        self.tour = dictionary["tour"]
        self.poster_format = dictionary["poster_format"]
        super().__init__(dictionary["type"], dictionary["quantity"], dictionary["price"], dictionary["description"])


def add_poster_data(dictionary):
    """
            Allow to enter data for new product of "poster" type (class Poster).

            Parameters: dictionary (dict) : Empty dictionary
            Returns: dictionary (dict) : Dictionary with values entered by user, used to create new class instance
    """
    dictionary["type"] = "Plakat"
    dictionary["tour"] = input("Trasa koncertowa: ")
    dictionary["poster_format"] = v.check_poster_size(input("Format: "))
    dictionary["quantity"] = int(v.check_digits(input("Stan magazynowy: ")))
    dictionary["price"] = float(v.check_price(input("Cena: ")))
    dictionary["description"] = input("Opis: ")
    return dictionary
