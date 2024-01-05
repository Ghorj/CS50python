def main():
    money = value(input("Greeting: "))
    print(f"${money}")


def value(greeting):

    #ask the user for a greeting
    greeting_mod = greeting.strip().lower()

    #if they say hello return 0
    if greeting_mod.startswith("hello") == True:
        return 0

    #if the greeting starts with an h but not hello output 20
    elif greeting_mod.startswith("h") == True:
        return 20

    #otherwise output 100
    else:
        return 100

if __name__ == "__main__":
    main()