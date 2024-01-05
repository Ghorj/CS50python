import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    #expects zero or two command-line arguments
    #0 is the user would like to output in random font
    if len(sys.argv) == 1:
        fnt = random.choice(fonts)


    #2 if specific font
    elif len(sys.argv) == 3:
        #1st -f or --font
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            #2nd name of the font
            fnt = sys.argv[2]
            if fnt not in fonts:
                sys.exit("Not a valid font")
            else:
                ...
        else:
            sys.exit("Not a valid command")

    else:
        sys.exit("Invalid number of arguments")

    #set font
    figlet.setFont(font=fnt)

    #prompt user for a string of text
    text = input("Text: ")

    #outputs text in the desired font
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()