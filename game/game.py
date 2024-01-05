import sys
import random


def main():

    #prompt the user for a level, n
    while True:
        try:
            level = int(input("level: "))
            if level < 1:
                ...
            else:
                break


        #if n not an integer prompt again

        except ValueError:
            ...

        except level < 1:
            ...



    #randomly generates an integer between 1 and n, inclusive, using random module
    solution = random.randint(1, level)

    while True:
        #prompt the user to guess that integer
        try:
            guess = int(input("Guess: "))

        #if not a possitive integer prompt again
        except ValueError:
            ...
        else:
        #if guess is smaller than integer output "Too small!"
            if guess < solution:
                print("Too small!")

        #if guess larger than integer output "Too large!"
            elif guess > solution:
                print("Too large!")

        #if guess same as the integer output "Just right!" and exit
            else:
                print("Just right!")
                sys.exit()


if __name__ == "__main__":
    main()