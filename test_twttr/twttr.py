def main():

    #prompt the user for a text
    message = input("Your tweet: ")

    #output the same text with all vowels omitted (upper and lower case)
    print(shorten(message))


def shorten(tweet):

    final_twt = ""
    #check each character in the string
    for letter in tweet:

        #if its a vowel don't add to the message
        if letter.lower() == "a":
            ...
        elif letter.lower() == "e":
            ...
        elif letter.lower() == "i":
            ...
        elif letter.lower() == "o":
            ...
        elif letter.lower() == "u":
            ...

        #otherwise add to the final message
        else:
            final_twt = final_twt + letter


    return final_twt



if __name__ == "__main__":
    main()