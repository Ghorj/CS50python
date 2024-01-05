def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #may contain a maximum of 6 characters and a minimum of 2
    if 2 <= len(s) <= 6:

        #no periods, spaces or punctuation marks
        if s.isalnum() == True:


            #all vanity plates must start with at least 2 letters
            if s[0:2].isalpha() == True:

                #numbers not in middle of plate, always at end. first number not 0
                i = len(s) - 1
                lett = False
                while i > 0:

                    #first number is 0
                    if s[i] == "0" and s[i - 1].isalpha() == True:
                        return False

                    #if its a letter
                    elif s[i].isalpha() == True:
                        i -=1
                        lett = True

                    #if it's a number but there was a letter after
                    elif s[i].isnumeric() == True and lett == True:
                        return False

                    #if it's a number
                    else:
                        i -= 1

                #if the loop was succesful return True
                return True


            #it doen't start with 2 letters
            else:
                return False

        #spaces or punctuation marks
        else:
            return False

    #characters dont meet the requirements
    else:
        return False






main()