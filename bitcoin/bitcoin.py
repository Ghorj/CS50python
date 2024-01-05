import sys
import requests


def main():
    #expects the user to specify number of bitcoins as a cmd argument
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])

        #if argument cannot convert to a float exit via sys.exit with an error msg
        except ValueError:
            sys.exit("Not a valid number")

        else:
            #queries API for bitcoin price index that returns a json object with current price as float
            r: int = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            file = r.json()

            # currencies = file["bpi"]
            # usd = currencies["USD"]
            # rate = usd["rate_float"]

            rate = file["bpi"]["USD"]["rate_float"]


            total = rate * n

            print(f"${total:,.4f}")


    else:
        sys.exit("Invalid number of arguments given")


    #catch exceptions

if __name__ == "__main__":
    main()