def main():

    #initialising control variable
    ctrl = True

    while ctrl:
        try:
            #prompt user "X/Y"
            fraction = input("Fraction: ")

            #assign variables x, y
            var = fraction.split(sep="/")
            x = int(var[0])
            y = int(var[1])

            #x <= y
            if x > y:
                 raise ValueError

        #if Error retry input
        except (ValueError, ZeroDivisionError):
            ...

        #if the input is valid print the fuel percentage
        else:
            print(fuel_percentage(x, y))

            #ctrl = False to exit loop
            ctrl = False

#inputs int, outputs str
def fuel_percentage(num, den):

    try:

        #if 1% or less remains output E
        if num / den <= 0.01:
            return "E"


        #if 99% or more remains output F
        elif num / den >= 0.99:
            return "F"


        #output as a percentage rounded to the next integer
        else:
            return (str(round(100 * num / den)) + "%")

    except ZeroDivisionError:
            ...
    except ValueError:
            ...


if __name__ == "__main__":
    main()