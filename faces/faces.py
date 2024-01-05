#takes input from the user and calls the convert function
def main():
    text = input("Are you happy :) or sad :( ? ")
    convert(text)

#receives a string and prints emojis
def convert(message):
    emoji = message.replace(":)", "🙂").replace(":(", "🙁")
    print(emoji)

main()