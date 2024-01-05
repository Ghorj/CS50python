import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # expects a line of text as input as a str
    um = re.findall(r"\bum\b", s, flags=re.IGNORECASE)

    i = 0

    #returns, as an int, the number of times that “um” appears in that text
    #as a word unto itself, not as a substring of some other word
    for _ in um:
        i += 1

    return i




if __name__ == "__main__":
    main()
