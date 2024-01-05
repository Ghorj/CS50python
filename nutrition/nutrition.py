def main():
    #input a fruit (case-insensitively)
    fruit = input("Fruit: ").lower()

    #outputs the number of calories in one portion of that fruit
    calories(fruit)


def calories(f):
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "canteloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
        }

    if f in fruit_calories:
        print(fruit_calories[f])
    else:
        ...



if __name__ == "__main__":
    main()