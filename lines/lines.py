import sys

def main():
    #expects exactly one command-line argument (name of python file)
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].endswith(".py") == True:
                with open(sys.argv[1]) as file:
                    lines = file.readlines()

                    ln = 0
                    for line in lines:
                        if line.strip().startswith("#") == True:
                            ...
                        elif line.strip() == "\n":
                            ...
                        elif line.strip() == "":
                            ...
                        else:
                            ln += 1

                    #outputs number of lines of code in that file, excluding comments and blank lines
                    print(ln)



            #if the specified file's name does not exist exit via sys.exit
            else:
                sys.exit("Not a python file")


        except FileNotFoundError:
            sys.exit("File not found")


    #if the user does not specify one command line argument exit via sys.exit
    else:
        sys.exit("Incorrect number of arguments given")




if __name__ == "__main__":
    main()
