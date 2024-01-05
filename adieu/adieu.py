import inflect

p = inflect.engine()

def main():
    names = []
    #prompt the user for names
    while True:
        try:
            names.append(input("Name: "))

        #until user inputs ctrl+d
        except EOFError:
            list = p.join(names)
            print(f"Adieu, adieu, to {list}")
            break

if __name__ == "__main__":
    main()
