#ask the user for a greeting
greeting = input("Greting: ").strip().lower()

#if they say hello output "0$"
if greeting.startswith("hello") == True:
    print("$0")

#if the greeting starts with an h but not hello output "$20"
elif greeting.startswith("h") == True:
    print("$20")

#otherwise output "100$"
else:
    print("$100")