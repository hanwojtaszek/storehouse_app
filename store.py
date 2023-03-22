import json
from music import Music, add_music_data
from clothes import Clothes, add_clothes_data
from poster import Poster, add_poster_data
import validators as v
import utils as u


class Store:
    def __init__(self, inventory):
        self.inventory = self.load_inventory(inventory)

    def run(self):
        """
                Run the store. It includes classes' initialization, loading inventory from json file,
                loading store's menu and a loop to peform operations in the store.

                Parameters: N/A
                Returns: N/A
        """
        products = u.initialize_classes(self.inventory)
        end = False
        while not end:
            self.inventory = self.load_inventory("inventory.json")
            if self.get_total_products_quantity(self.inventory) == 0:
                print("-" * 68)
                menu_len = u.print_menu("empty_store_menu.txt")
                option = input("Wybierz opcję: ")
                option = v.check_option(option, menu_len)
                if option == "1":
                    self.stocking(products)
                    self.inventory = self.load_inventory("inventory.json")
                else:
                    u.print_message("exit")
                    end = True
            else:
                print("-" * 68)
                menu_len = u.print_menu("main_menu.txt")
                option = input("\nWybierz opcję: ")
                option = v.check_option(option, menu_len)
                end = self.run_store_function(products, option, end)

    def load_inventory(self, filename):
        """
                Load store inventory from json file.

                Parameters: filename (str) : Name of file with store's inventory in format <name>.json
                Returns: inventory (dict) : Dictionary of products in the inventory
        """
        try:
            with open(filename, encoding='utf-8') as f:
                self.inventory = json.load(f)
            return self.inventory
        except IOError as e:
            print(f"[BŁĄD] Coś poszło nie tak. Skontaktuj się z administratorem aplikacji.\n"
                  f"Kod błędu: {e}")

    @staticmethod
    def get_total_products_quantity(inventory):
        """
                Read total quantity of all products in a store from its inventory.

                Parameters: N/A
                Returns: inventory["total_quantity"] (int) : Total quantity of products in the store.
        """
        return inventory["total_quantity"]

    def run_store_function(self, products, option, end):
        """
                Trigger store's functions based on option selected by user.

                Parameters: products (list) : List of classes representing products in the store
                            option (str) : Option selected by user, representing one of store's functions
                            end (bool) : Boolean value to indicate if user selected "exit" option.
                Returns: end (bool) : Boolean value to indicate if user selected "exit" option.
        """
        if option == "1":
            self.search_store(products)
        elif option == "2":
            self.view_store(products)
        elif option == "3":
            self.edit_product(products, "add")
        elif option == "4":
            self.edit_product(products, "remove")
        elif option == "5":
            self.edit_product(products, "change price")
        elif option == "6":
            self.edit_product(products, "change quantity")
        elif option == "7":
            self.add_to_db(products)
        elif option == "8":
            self.remove_from_db(products)
        elif option == "9":
            u.print_message("exit")
            end = True
        return end

    def search_store(self, products):
        """
                Enable searching function in the store.

                Parameters: products (list) : List of classes representing products in the store
                Returns: search_results (list) : List indicating if given product satisfies search criteria
                         found (bool) : Boolean value to determine if any results were found during search
        """
        search = input("Wprowadź wyszukiwaną frazę: ")
        search_results = []
        results_count = 0
        found = False
        for product in products:
            if search.lower() in str(list(product.__dict__.values())).lower():
                search_results.append([True, results_count + 1])
                results_count += 1
                found = True
            else:
                search_results.append([False, 0])
        if not found:
            print("\nPrzecież doskonale wiesz - patrzymy tylko w dobrą stronę!\n"
                  "... Ale nie widzimy nigdzie szukanego produktu.\n")
        else:
            self.display_search_result(products, search_results, results_count)
        return search_results, found

    @staticmethod
    def display_search_result(products, search_results, results_count):
        """
                Display search results.

                Parameters: products (list) : List of classes representing products in the store
                            search_results (list) : List indicating if given product satisfies search criteria
                            results_count (int) : Number of products found during search
                Returns: N/A
        """
        print(f"\nZnalezione produkty: {results_count}\n")
        for i in range(0, len(products)):
            if search_results[i][0]:
                if type(products[i]) == Music:
                    print(f"ID: {search_results[i][1]}\nRodzaj: {products[i].type}\nTytuł: {products[i].title}\n"
                          f"Nośnik: {products[i].medium}\nData wydania: {products[i].release_date}\n"
                          f"Numer katalogowy: {products[i].catalog_number}\nCena: {products[i].price}\n"
                          f"Opis: {products[i].description}\nStan magazynowy: {products[i].quantity}\n")
                if type(products[i]) == Clothes:
                    print(f"ID: {search_results[i][1]}\nRodzaj: {products[i].type}\nRozmiar: {products[i].size}\n"
                          f"Cena: {products[i].price}\nOpis: {products[i].description}\n"
                          f"Stan magazynowy: {products[i].quantity}\n")
                if type(products[i]) == Poster:
                    print(f"ID: {search_results[i][1]}\nRodzaj: {products[i].type}\nTrasa: {products[i].tour}\n"
                          f"Format: {products[i].poster_format}\nCena: {products[i].price}\n"
                          f"Opis: {products[i].description}\nStan magazynowy: {products[i].quantity}\n")

    @staticmethod
    def view_store(products):
        """
                Display all products in the store with complete data.

                Parameters: products (list) : List of classes representing products in the store
                Returns: N/A
        """
        print("-" * 68, "\nPłyty:")
        for product in products:
            if type(product) == Music:
                print(f"Tytuł: {product.title}\nNośnik: {product.medium}\nCena: {product.price}\n"
                      f"Rok wydania: {product.release_date}\nNumer katalogowy: {product.catalog_number}\n"
                      f"Opis: {product.description}\nStan magazynowy:{product.quantity}\n")
        print("-" * 68, "\nOdzież:")
        for product in products:
            if type(product) == Clothes:
                print(f"Rodzaj: {product.type}\nRozmiar: {product.size}\nCena: {product.price}\n"
                      f"Opis: {product.description}\nStan magazynowy:{product.quantity}\n")
        print("-" * 68, "\nPlakaty:")
        for product in products:
            if type(product) == Poster:
                print(f"Format: {product.poster_format}\nTrasa koncertowa: {product.tour}\nCena: {product.price}\n"
                      f"Opis: {product.description}\nStan magazynowy:{product.quantity}\n")

    def edit_product(self, products, operation):
        """
                Group all functions to change product's values. Triggers product search and then an option to change
                given attribute of selected product.

                Parameters: products (list) : List of classes representing products in the store
                            operation (str) : String value used to trigger correct function for a product.
                Returns: N/A
        """
        search_results, found = self.search_store(products)
        counter = 0
        if not found:
            return 0
        else:
            for result in search_results:
                if result[0]:
                    counter += 1
            if counter > 1:
                print("Znaleziono więcej niż jeden produkt.")
                search_id = input("Podaj ID produktu: ")
                search_id = v.check_option(search_id, counter)
                for i in range(0, len(products)):
                    if search_results[i][1] == int(search_id):
                        if operation == "add":
                            amount = products[i].add_product()
                        elif operation == "remove":
                            amount = products[i].remove_product()
                        elif operation == "change price":
                            products[i].change_price()
                            amount = None
                        elif operation == "change quantity":
                            amount = products[i].change_quantity()
            else:
                for i in range(0, len(products)):
                    if search_results[i][0]:
                        if operation == "add":
                            amount = products[i].add_product()
                        elif operation == "remove":
                            amount = products[i].remove_product()
                        elif operation == "change price":
                            products[i].change_price()
                            amount = None
                        elif operation == "change quantity":
                            amount = products[i].change_quantity()
            self.update_inventory(products, amount)

    def add_to_db(self, products):
        """
                Allow adding a new product to the database and appends products list with new class instance.
                Parameters: products (list) : List of classes representing products in the store
                Returns: products (list) : List of classes representing products in the store
        """
        print("Co dodajemy?\n1. Muzyka\n2. Odzież\n3. Plakat")
        dictionary = {}
        option = v.check_option(input("Wprowadź opcję: "), 3)
        if option == "1":
            dictionary = add_music_data(dictionary)
            products.append(Music(dictionary))
        elif option == "2":
            dictionary = add_clothes_data(dictionary)
            products.append(Clothes(dictionary))
        elif option == "3":
            dictionary = add_poster_data(dictionary)
            products.append(Poster(dictionary))
        self.update_inventory(products, dictionary["quantity"])
        return products

    def remove_from_db(self, products):
        """
                Allow removing product from the database and removes class instance from products list.

                Parameters: products (list) : List of classes representing products in the store
                Returns: products (list) : List of classes representing products in the store
        """
        search_results, found = self.search_store(products)
        counter = 0
        amount = None
        for result in search_results:
            if result[0]:
                counter += 1
        if counter > 1:
            print("Znaleziono więcej niż jeden produkt.")
            search_id = v.check_option(input("Podaj ID produktu: "), counter)
            for i in range(0, len(products)):
                if search_results[i][1] == int(search_id):
                    confirm = input("Czy na pewno chcesz usunąć produkt? [Y/ N]: ")
                    if confirm.lower() == "y" or confirm.lower() == "yes" or confirm.lower() == "tak":
                        last_quantity = products[i].quantity
                        del(products[i])
                        amount = -last_quantity
                    else:
                        print("Anulowano usuwanie produktu.")
        else:
            for i in range(0, len(products)):
                if search_results[i][0]:
                    confirm = input("Czy na pewno chcesz usunąć produkt? [Y/ N]: ")
                    if confirm.lower() == "y" or confirm.lower() == "yes" or confirm.lower() == "tak":
                        last_quantity = products[i].quantity
                        del(products[i])
                        amount = -last_quantity
                    else:
                        print("Anulowano usuwanie produktu.")
        self.update_inventory(products, amount)

    def stocking(self, products):
        """
                Allow entering products to store in case it's empty.

                Parameters: products (list) : List of classes representing products in the store
                Returns: total_quantity (int) : Total quantity of products in the store
        """
        total_quantity = 0
        print("\nWprowadź stany magazynowe:")
        for product in products:
            if type(product) == Music:
                print(f"\nRodzaj: {product.type}, tytuł: {product.title}, nośnik: {product.medium}")
            elif type(product) == Clothes:
                print(f"\nRodzaj: {product.type}, rozmiar: {product.size}")
            elif type(product) == Poster:
                print(f"\nRodzaj: {product.type}, format: {product.poster_format}, trasa: {product.tour}")
            product.quantity = int(v.check_digits(input("Stan magazynowy: ")))
            total_quantity += int(self.count_all_products(product.quantity))
        dictionary = u.convert_list_to_dict(products, total_quantity)
        u.save_inventory_to_file("inventory.json", dictionary)
        return total_quantity

    def update_inventory(self, products, amount=None):
        """
                Update store's inventory in a file based on operations triggered by user.

                Parameters: products (list) : List of classes representing products in the store
                            amount (int) : Amount of products to add to/ remove from inventory (if applicable)
                Returns: N/A
        """
        if amount is not None:
            total_quantity = self.count_all_products(amount)
        else:
            total_quantity = self.get_total_products_quantity(self.inventory)
        dictionary = u.convert_list_to_dict(products, total_quantity)
        u.save_inventory_to_file("inventory.json", dictionary)

    def count_all_products(self, amount):
        """
                Count total quantity of products in the store based on operations triggered by user.

                Parameters: amount (int) : Amount of products to add to/ remove from inventory
                Returns: get_total_products_quantity() + amount (int) : Total quantity of products in the store
        """
        return self.get_total_products_quantity(self.inventory) + amount
