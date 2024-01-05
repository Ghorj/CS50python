def main():
    #prompt the user for a text
    message = input("Your tweet: ")

    #output the same text with all vowels omitted (upper and lower case)
    shorten(message)

def shorten(tweet):

    #check each character in the string
    for letter in tweet:
    #if its a vowel remove it
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            ...

        #otherwise leave it as it is
        else:
            print(letter, end="")
    print()







if __name__ == "__main__":
    main()