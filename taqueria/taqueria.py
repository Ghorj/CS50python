def main():

    bill: float = 0
    while True:

        try:

            #prompt the user for items, one per line, case insensitively
            item = input("Item: ").lower()

            #ignore input that isn't an item
        except (ValueError, KeyError):
            ...

        #until user inputs ctrl+d
        except EOFError:
            print()
            break

        #update bill
        else:
            try:
                bill += add_item(item)

                #after each item display total cost of all items prefix $ 2 decimals
                print("$", end="")
                print(f"{bill:.2f}")

            except TypeError:
                ...


def add_item(item):

    #asume every item on the menu is titlecased
    dish = item.title()

    items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    try:
        return items[dish]

    except KeyError:
        return TypeError




if __name__ == "__main__":
    main()