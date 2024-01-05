def main():
    while True:
        try:
            #prompt the user for date anno Domini, M?M/D?D/YYYY
            date = input("Date: ")

            #then output the same date in YYYY-MM-DD format
            print(format_date(date))
        except ValueError:
            ...
        else:
            break


    #if the input is not on a valid date in either format, prompt the user again

def format_date(str):

    #there are only 12 months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    #if format MM/DD/YYYY
    if "/" in str:
        #extract year, month and day
        month, day, year = str.split("/")

        #valid month number
        if 0 < int(month) < 13:

            f_month = int(month)

        #not a valid month
        else:
            raise ValueError

    elif " " in str:
        #extract, day, year, month
        month, day, year = str.split(" ")

        #check format is ok
        if "," in day:
            #format day
            day = day.removesuffix(",")
        else:
            raise ValueError

        #valid month name
        if month in months:

            f_month = months.index(month) + 1

        else:
            raise ValueError

    else:
        raise ValueError



    #between 1 and 31 days (valid)
    if 0 < int(day) < 32:

        f_day = int(day)

        #valid year
        if int(year) > 0:

            f_year = int(year)

            #date valid
            #ISO 8601: YYYY-MM-DD (padding with leading zeroes as needed)


            return f"{f_year:04}-{f_month:02}-{f_day:02}"


        #not a valid year
        else:
            raise ValueError

    #days not a valid number
    else:
        raise ValueError




if __name__ == "__main__":
    main()