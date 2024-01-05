import sys
from art import text2art

class Coffee_machine:

    """
    A virtual representation of a coffee machine.

    This class manages the functionality of a coffee machine, including handling
    coins, selecting coffee, checking credit and ingredients, and dispensing coffee.
    """

    # List of available coffees with their prices and grain and milk quantities required
    coffees = [
        {"name": "latte", "price": 1.0, "grains": 1, "milk": 2},
        {"name": "cortado", "price": 0.75, "grains": 1, "milk": 1},
        {"name": "espresso", "price": 0.50, "grains": 1, "milk": 0},
        {"name": "double espresso", "price": 0.85, "grains": 2, "milk": 0},
    ]

    # List of accepted coin values
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]


    def __init__(self, bank=5.0, grains=5, milk=5):

        """Initialize the coffee machine with default values.

        Args:
            bank (float): Initial amount of money in the machine.
            grains (int): Initial quantity of available coffee grains.
            milk (int): Initial quantity of available milk.
        """

        self.bank = bank
        self.credit = 0
        self.grains = grains
        self.milk = milk


    def __str__(self):

        """String representation of the Coffee_machine instance."""

        return "________._________\n|      | \\   -   /\n|  ||  |  \\  -  /\n|  ||  |___\\___/\n|  ||  |     X\n|      |    ___\n|      |   / - \\\n|______|  /  -  \\\n| ____ | /_______\\\n||COFI||__________\n||____|           |\n|_________________|\n"


    def take_coin(self, coin: str) -> float:

        """Accept coins and update the user's credit.

        Args:
            coin (str): The value of the coin inserted.

        Returns:
            float: The updated credit after taking the coin.
        """

        #remove £ and convert to float
        try:
            if "£" in coin:
                coin = float(coin.removeprefix("£"))
            else:
                coin = float(coin)

        #coin cannot convert to float
        except ValueError:
            raise ValueError("Not a coin")

        #validate coin and update credit
        else:
            if self.validate_coin(coin):
                self.credit += coin
                return self.credit

            #coin not accepted in the list of coins
            else:
                raise ValueError("Not a valid coin")


    def validate_coin(self, coin: float) -> bool:

        """Validate coin value is in self.coins

        Returns:
            bool: True if coin value is accepted, False otherwise
        """

        return True if coin in self.coins else False


    def choose_coffee(self, coffee: str) -> dict:

        """Prompt the user to choose a coffee and return the chosen coffee's details.

        Returns:
            dict: A dictionary containing details of the chosen coffee.
        """

        if coffee in [c["name"] for c in self.coffees]:
            return next(item for item in self.coffees if item["name"] == coffee)

        #coffee not in coffees
        else:
            raise ValueError(f"Invalid coffee choice: {coffee}")


    def check_credit(self, coffee: dict) -> bool:

        """Check if there's enough credit for the chosen coffee.

        Args:
            coffee (dict): A dictionary containing details of the chosen coffee.

        Returns:
            bool: True if there's enough credit, False otherwise.
        """

        return True if self.credit >= coffee["price"] else False



    def check_ingredients(self, coffee: dict) -> bool:

        """Check if there are enough ingredients for the chosen coffee.

        Args:
            coffee (dict): A dictionary containing details of the chosen coffee.

        Returns:
            bool: True if there are enough ingredients, False otherwise.
        """

        return True if self.grains >= coffee["grains"] and self.milk >= coffee["milk"] else False


    def fill_ingredients(self, n=5):

        """Refill the coffee machine with ingredients.

        Args:
            n (int): Number of units to add for both milk and grains (default is 5).
        """

        self.milk += n
        self.grains += n


    def give_change(self) -> float:

        """Return the user's credit as change and reset the credit.

        Returns:
            float: The user's credit to be returned as change.
        """

        change = self.credit
        self.credit = 0
        return change


    def convert_to_coins(self, money: float) -> dict:

        """Converts an ammount of money to the coins for that change

        Returns:
            dict: The coins that add up to that ammount
        """

        # Convert money to pennies to avoid floating-point precision issues
        try:
            money_in_pennies = int(round(money * 100))

        except TypeError:
            raise TypeError("Not a float value")

        else:

            #wallet
            purse = {}

            #coin values also have to be in pennies
            coins_in_pennies = [int(round(coin * 100)) for coin in self.coins]

            #convert money into coins
            for coin_value in coins_in_pennies:

                while money_in_pennies >= coin_value:

                    coin_name = f"£{coin_value // 100}.{coin_value % 100:02d}"
                    if coin_name not in purse:
                        purse[coin_name] = 1
                    else:
                        purse[coin_name] += 1

                    money_in_pennies -= coin_value


            #dict that contains the number of coins of each type
            return purse



    def make_coffee(self, coffee: dict) -> str:

        """Dispense the chosen coffee, deduct ingredients and credit.

        Args:
            coffee (dict): A dictionary containing details of the chosen coffee.

        Returns:
            str: A message indicating the success or failure of coffee preparation.
        """

        if self.check_ingredients(coffee):
            self.bank += coffee["price"]
            self.credit -= coffee["price"]
            self.grains -= coffee["grains"]
            self.milk -= coffee["milk"]
            return f"\n      )  (\n     (   ) )\n      ) ( (\n mrf_______)_\n .-\'---------|\n( C|/\\/\\/\\/\\/|\n \'-./\\/\\/\\/\\/|\n   \'_________\'\n    \'-------\'  your {coffee['name']}, thank you!\n"

        else:

            return "Not enough ingredients"


def main():

    """Main function to run the coffee machine simulation."""

    #presentation
    print(text2art("Coffee Machine\nSimulator", font="small"))

    #create an instance of the Coffee_machine class
    c = Coffee_machine()

    #print the coffee machine
    print(c)

    #print the menu
    print("----MENU----")
    for coffee in c.coffees:
        print(f"+ {coffee['name']}: £{coffee['price']:.2f}")
    print()

    while True:
        choice = input("[i]nsert coin / [c]hoose your coffee / [e]xit: ").lower()

        #take coins from the user
        if choice == "i":

            try:
                credit = c.take_coin(input("Insert coin: "))

            except ValueError:
                print("Invalid coin")

            else:
                print(f"Credit: £{credit:.2f}")

        #choose a coffee
        elif choice == "c":

            try:
                coffee = input("Choose your coffee: ")
                coffee_details = c.choose_coffee(coffee)

            except ValueError:
                print("Invalid coffee")

            else:
                #check if there's enough credit for the chosen coffee
                if c.check_credit(coffee_details):

                    # Check if there are enough ingredients
                    if c.check_ingredients(coffee_details):

                        #make the chosen coffee and give change
                        print(c.make_coffee(coffee_details))

                        change = c.give_change()

                        print(f"Change: £{change:.2f}")

                        #convert to coins
                        coins = c.convert_to_coins(change)

                        for coin in coins:
                            if coins[coin] != 0:
                                print(f"{coins[coin]} pieces of {coin}")

                    else:
                        print("Not enough ingredients. Filling up the machine")
                        c.fill_ingredients()
                else:
                    print("Not enough credit")


        elif choice == "e":
            print(text2art("Goodbye!", font="small"))
            sys.exit()



if __name__ == "__main__":
    main()
