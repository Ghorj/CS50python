import re
#import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):


        for n in range(4):

            if 0 <= int(matches.group(n + 1)) <= 255:
                ...
            else:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()
