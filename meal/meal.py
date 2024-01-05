def main():
    #request time from the user
    t_string = input("What's the time, mr Wolf? ")

    #convert that time into a float
    t_number = convert(t_string)

    #check if it's time to eat
    if 7 <= t_number <= 8:
        print("breakfast time")
    elif 12 <= t_number <= 13:
        print("lunch time")
    elif 18 <= t_number <= 19:
        print("dinner time")
    else:
        ...


def convert(time):
    #check the format and modify if necessary
    tm = time.lower()
    #case pm
    if " p.m." in tm:
        t_split = tm.removesuffix(" p.m.").split(":")
        t_float = float(t_split[0]) + 12 + float(t_split[1]) / 60
    #case am
    elif " a.m." in tm:
        t_split = tm. removesuffix(" a.m.").split(":")
        t_float = float(t_split[0]) + float(t_split[1]) / 60

    #case 24h
    elif ":" in tm:
        t_split = time.split(":")
        t_float = float(t_split[0]) + float(t_split[1]) / 60
    #other (else)


    #return the time as a float
    return t_float


if __name__ == "__main__":
    main()