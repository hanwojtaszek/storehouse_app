from store import Store
import utils as u


def main():
    store = Store("inventory.json")
    u.print_message("welcome")
    store.run()


if __name__ == '__main__':
    main()
