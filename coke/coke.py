def main():
    #initialise price and credit
    price: int = 50
    credit: int = 0

    #while the money isn't enough
    while credit < price:
        #inform about the ammount due
        print("Amount Due:", price - credit)

        #ask the user for a coin
        coin = int(input("Insert Coin: "))

        #update credit if the coin is a valid currency
        if coin == 5 or coin == 10 or coin == 25:
            credit += coin

    #after the payment is enough inform about the change owed
    print("Change Owed:", credit - price)

if __name__ == "__main__":
    main()