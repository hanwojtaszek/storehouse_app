import json
from music import Music
from clothes import Clothes
from poster import Poster


def print_message(option):
    """
            Displays given message.

            Parameters: option (str) : Option based on which the selection of message is done.
            Returns: N/A
    """
    if option == "welcome":
        message = "\n    Witaj, nieznajomy! ...w oficjalnym sklepie Dawida Podsiadło    "
    else:
        message = "\n                        Żegnaj, nieznajomy!                        \n"
    print("-" * len(message) + message)


def print_menu(filename):
    """
            Loads and displays store's menu from text file.

            Parameters: filename (str) : Name of file with app menu in format <name>.txt
            Returns: N/A
    """
    with open(filename, encoding='utf-8') as f:
        menu = f.readlines()
        menu_display = [item.strip("\n") for item in menu]
    for item in menu_display:
        print(item)
    return len(menu) - 1


def convert_list_to_dict(products, total_quantity):
    """
            Transforms products list to dictionary.
            Parameters: products (list) : List of classes representing products in the store
                        total_quantity (int) : Total quantity of products in the store.
            Returns: dictionary (dict) : Dictionary with products in the store
    """
    dictionary = {"total_quantity": total_quantity, "type": [{"music": [], "clothes": [], "poster": []}]}
    for product in products:
        if type(product) == Music:
            dictionary["type"][0]["music"].append(product.__dict__)
        elif type(product) == Clothes:
            dictionary["type"][0]["clothes"].append(product.__dict__)
        elif type(product) == Poster:
            dictionary["type"][0]["poster"].append(product.__dict__)
    return dictionary


def save_inventory_to_file(filename, dictionary):
    """
            Saves store's inventory to a json file.
            Parameters: filename (str) : Name of file with store's inventory in format <name>.json
                        dictionary (dict) : Dictionary with products in the store
            Returns: N/A
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)


def initialize_classes(inventory):
    """
            Initializes all product classes and appends them to a list.

            Parameters: inventory (dict) : Store's inventory loaded from json file
            Returns: products (list) : List of classes representing products in the store
    """
    products = []
    for product in inventory["type"][0]["music"]:
        products.append(Music(product))
    for product in inventory["type"][0]["clothes"]:
        products.append(Clothes(product))
    for product in inventory["type"][0]["poster"]:
        products.append(Poster(product))
    return products
