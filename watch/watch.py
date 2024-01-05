import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #expects a str of HTML as input
    #extracts any YouTube URL that’s the value of a src attribute of an iframe element therein
    if url := re.search(r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"></iframe>", s):
        #returns its shorter, shareable youtu.be equivalent as a str
        return "https://youtu.be/" + url.group(1)

    #Expect that any such URL will be in one of the formats below
    #http://youtube.com/embed/xvFZjo5PgG0
    #https://youtube.com/embed/xvFZjo5PgG0
    #https://www.youtube.com/embed/xvFZjo5PgG0
    #Assume that the value of src will be surrounded by double quotes
    #assume that the input will contain no more than one such URL
    #If the input does not contain any such URL at all, return None
    else:
        return None


if __name__ == "__main__":
    main()
