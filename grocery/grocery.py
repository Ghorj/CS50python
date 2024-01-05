def main():
    basket = {}
    while True:
        try:

            #prompt the user for items, case-insensitively
            item = input().upper()
            add_to_basket(item, basket)


        #until ctrl + d
        except EOFError:
            break


        #then output list in uppercase, sorted alphabetically prefix number of times
    print_basket(basket)

def add_to_basket(item, dict):
    #if item not in dict:
    if item not in dict.keys():
        dict[item] = 1
    #if it is, add one more
    else:
        dict[item] += 1


def print_basket(basket):
    for food in sorted(basket):
        print(basket[food], food)

if __name__ == "__main__":
    main()