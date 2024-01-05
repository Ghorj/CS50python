import sys
from tabulate import tabulate
import csv

def main():

    #expects one command-line argument
    if len(sys.argv) == 2:

        name = sys.argv[1].strip()

        #name or path of a csv file in pinocchios format
        if name.endswith(".csv") == True:


            try:
                with open(name) as file:
                    reader = csv.reader(file)

                    print(tabulate(reader, headers="firstrow", tablefmt="grid"))


            except FileNotFoundError:
                sys.exit("File not found")


                #outputs a table formatted as ascii art using tabulate package



                #format the table using the librarys grid format


        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) < 2:
        sys.exit("Too few arguments given")

    else:
        sys.exit("Too many arguments given")



if __name__ == "__main__":
    main()
