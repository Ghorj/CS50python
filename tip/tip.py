def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#transforms string to float and removes dollar symbol
def dollars_to_float(d):
    return float(d.removeprefix("$"))

#transforms percentage into per one and removes percentage symbol
def percent_to_float(p):
    return 0.01 * float(p.removesuffix("%"))


main()