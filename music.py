import validators as v
from product import Product


class Music(Product):
    def __init__(self, dictionary):
        self.title = dictionary["title"]
        self.medium = dictionary["medium"]
        self.release_date = dictionary["release_date"]
        self.catalog_number = dictionary["catalog_number"]
        super().__init__(dictionary["type"], dictionary["quantity"], dictionary["price"], dictionary["description"])


def add_music_data(dictionary):
    """
            Allows to enter data for new product of "music" type (class Music).
            Parameters: dictionary (dict) : Empty dictionary
            Returns: dictionary (dict) : Dictionary with values entered by user, used to create new class instance
    """
    dictionary["type"] = "Płyta"
    dictionary["title"] = input("Tytuł: ")
    dictionary["medium"] = v.check_medium(input("Nośnik: "))
    dictionary["release_date"] = v.check_release_date(input("Rok wydania: "))
    dictionary["catalog_number"] = v.check_digits(input("Numer katalogowy: "))
    dictionary["quantity"] = int(v.check_digits(input("Stan magazynowy: ")))
    dictionary["price"] = float(v.check_price(input("Cena: ")))
    dictionary["description"] = input("Opis: ")
    return dictionary
