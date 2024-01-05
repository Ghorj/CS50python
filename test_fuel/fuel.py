def main():
    while True:
        try:
            #input fraction
            fract = input("Fraction (X/Y): ")

            #convert fraction X/Y to percentage
            perc = convert(fract)

        except ValueError:
            ...

        except ZeroDivisionError:
            ...

        else:
            #print the converted value
            print(gauge(perc))
            break

def convert(fraction):
    try:
        sep = fraction.partition("/")
        num = int(sep[0])
        den = int(sep[2])
    except ValueError:
        raise ValueError
    else:

        if den == 0:
            raise ZeroDivisionError
        elif num > den:
            raise ValueError
        else:
            perc = int(100 * num / den)
            return perc


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return "F"

if __name__ == "__main__":
    main()
