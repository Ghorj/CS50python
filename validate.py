import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)+(edu|org|com|net)$", email):
    print("valid")
else:
    print("invalid")

