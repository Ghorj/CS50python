from datetime import date
import inflect
import sys


def main():
    try:
        print(how_long(input("Date of Birth: ")))
    except ValueError:
        sys.exit("Invalid date")
    #prompt the user for their date of birth YYYY-MM-DD

def how_long(birth):
    try:
        birth = date.fromisoformat(birth)
    except ValueError:
        raise ValueError

    else:
        #use datetime.date.today to get today's date
        today = date.today()

        time = today - birth

        age = int(time.total_seconds() / 60)


        #prints how old they are in minutes, rounded to the nearest integer

        #using english words instead of numerals, without any and between words
        p = inflect.engine()
        return (p.number_to_words(age, andword="") + " minutes").capitalize()

        #assume the user was born at midnight that day

        #assume that it's midnight





if __name__ == "__main__":
    main()
