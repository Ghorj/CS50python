import random


def main():
    #prompt the user for a level
    lvl = get_level()

    score = 0

    #randomly generates 10 math problems formatted as "x + y ="
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        sol = x + y

        #prompt user up to 3 times for each problem
        err = 0
        while err < 3:
            #prompt the user to solve each of those problems
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == sol:
                    break
                else:
                    raise ValueError

            #if answer not correct output "EEE"
            except ValueError:
                print("EEE")
                err += 1
        #if user has not answered correctly output the correct answer
        if err == 3:
            print(f"{x} + {y} = {x + y}")
        else:
            score += 1

    #ultimately output the user's score
    print(f"Final score: {score}")


def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            #if user doesnt input 1, 2 or 3 prompt again
            if lev < 1 or lev > 3:
                raise ValueError

        except ValueError:
            ...
        else:
            return lev


def generate_integer(level):
    if level == 1:
        l_limit = 0
        h_limit = 9
    elif level == 2:
        l_limit = 10
        h_limit = 99
    else:
        l_limit = 100
        h_limit = 999
    return random.randint(l_limit, h_limit)


if __name__ == "__main__":
    main()