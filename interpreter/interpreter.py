def main():
    #prompt the user for an arithmetic expression
    alg = input("CALC: ")

    #separate the string into the different inputs
    data = alg.split(" ")

    #calculates and outputs the result as a floating-point value one decimal
    match data[1]:
        case "+":
            print(round((float(data[0]) + float(data[2])), 1))
        case "-":
            print(round((float(data[0]) - float(data[2])), 1))
        case "/":
            print(round((float(data[0]) / float(data[2])), 1))
        case "*":
            print(round((float(data[0]) * float(data[2])), 1))
        case _:
            print("Error")


main()