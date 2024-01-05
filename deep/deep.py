#ask input from the user
life = input("What is the Answer to the great Question of Life? ").strip().lower()

#Do they know the true meaning of life?
if life == "42" or life == "forty two" or life == "forty-two":
    print("Yes")
else:
    print("No")