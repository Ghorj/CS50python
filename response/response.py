from validator_collection import validators, errors
#You may not use re.
#do not validate whether the email address’s domain name actually exists.

def main():

    #prompts the user for an email address via input
    print(is_email(input("e-mail: ")))

def is_email(mail):
    try:
        validators.email(mail)

    # prints Valid or Invalid, respectively, if the input is a syntatically valid email address

    except (errors.InvalidEmailError, errors.EmptyValueError):
        return "Invalid"

    else:
        return "Valid"



if __name__ == "__main__":
    main()
