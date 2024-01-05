import emoji


def main():

    #prompt the user for a string
    string = input("Input: ")

    #return emojized version of the string
    print(emoji.emojize(string, language="alias"))

if __name__ == "__main__":
    main()