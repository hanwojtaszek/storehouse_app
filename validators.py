def check_option(option, number_of_options):
    """
            Verifies if user entered valid option from a given number of options.
            Parameters: option (str) : Option entered by user
                        number_of_options (int) : Number of possible options
            Returns: option (str) : Option after validation
    """
    options = list(range(1, number_of_options + 1))
    options_str = [str(option) for option in options]
    while option not in options_str:
        option = input("Niepoprawna opcja. Podaj opcję: ")
    return option


def check_price(price):
    """
            Verifies if user entered valid price for a product.
            Parameters: price (str) : Price entered by user
            Returns: price (float) : Price after validation
    """
    valid = False
    while not valid:
        try:
            price = float(price)
            if price < 0:
                price = input("Niepoprawna wartość. Podaj wartość: ")
            else:
                valid = True
        except ValueError:
            price = input("Niepoprawna wartość. Podaj wartość: ")
    return price


def check_amount(quantity, amount):
    """
            Verifies if user entered valid amount of products to remove from the store.
            Parameters: quantity (int): Quantity of given product in the store
                        amount (int) : Amount entered by user
            Returns: valid (bool) : Boolean value to determine if given amount of products can be removed from store
    """
    if amount > quantity:
        print("Nie można odjąć więcej produktów niż znajduje się w sklepie.")
        valid = False
    else:
        valid = True
    return valid


def check_digits(digit):
    """
            Verifies if user entered valid digit value.
            Parameters: digit (str): Value entered by user
            Returns: digit (str) : Value after validation
    """
    while not digit.isdigit():
        digit = input("Niepoprawna wartość. Podaj wartość: ")
    return digit


def check_poster_size(size):
    """
            Verifies if user entered valid poster size.
            Parameters: size (str): Value entered by user
            Returns: size (str) : Value after validation
    """
    sizes = ["a5", "a4", "a3", "a2", "a1", "a0", "b1", "b0"]
    while size.lower() not in sizes:
        size = input("Niepoprawna wartość. Podaj wartość: ")
    return size.upper()


def check_size(size):
    """
            Verifies if user entered valid size for clothes.
            Parameters: size (str): Value entered by user
            Returns: size (str) : Value after validation
    """
    sizes = ["xs", "s", "m", "l", "xl", "onesize"]
    while size.lower() not in sizes:
        size = input("Niepoprawna wartość. Podaj wartość: ")
    return size.upper()


def check_medium(medium):
    """
            Verifies if user entered valid medium for music product.
            Parameters: medium (str): Value entered by user
            Returns: medium (str) : Value after validation
    """
    medium_types = ["cd", "lp", "cassette", "dvd", "blu-ray"]
    while medium.lower() not in medium_types:
        medium = input("Niepoprawna wartość. Podaj wartość: ")
    return medium.upper()


def check_release_date(release_date):
    """
            Verifies if user entered valid release date for music product.
            Parameters: release_date (str): Value entered by user
            Returns: release_date (str) : Value after validation
    """
    while not release_date.isdigit() or not len(release_date) == 4:
        release_date = input("Niepoprawny rok. Podaj rok: ")
    return release_date
