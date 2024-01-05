import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #expects a str in either of the 12-hour formats below
    #9:00 AM to 5:00 PM
    #9 AM to 5 PM
    #Expect that AM and PM will be capitalized (with no periods therein)
    #and that there will be a space before each
    if time := re.search(r"^(\d+)(?::00)? (AM|PM) to (\d+)(?::00)? (AM|PM)$", s):
        t1 = int(time.group(1))
        t2 = int(time.group(3))

        if t1 > 12 or t2 > 12:
            raise ValueError

        #returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00)
        else:

            #AM
            if time.group(2) == "AM":
                if t1 == 12:
                    t1 -= 12
                else:
                    ...
            #PM
            else:
                if t1 == 12:
                    ...
                else:
                    t1 += 12


            #AM
            if time.group(4) == "AM":
                if t2 == 12:
                    t2 -= 12
                else:
                    ...
            #PM
            else:
                if t2 == 12:
                    ...
                else:
                    t2 += 12


            return f"{t1:02}:00 to {t2:02}:00"

    else:
        raise ValueError




if __name__ == "__main__":
    main()
