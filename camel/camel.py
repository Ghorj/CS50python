def main():
    #ask input from the user
    file = input("File name in camel code: ")
    #convert to snake case
    print_snake_code(file)

def print_snake_code(name):
    #format the string
    camel_code = name.strip()
    #find capital letters in the string
    for letter in range(len(camel_code)):
    #if you find a capital letter, (add a _ or separate the string)
        if camel_code[letter].istitle() == True and letter != 0:
            #add _
            print("_", end="")
        print(camel_code[letter].lower(), end="")
    print()


if __name__ == "__main__":
    main()