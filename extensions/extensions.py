def main():
    #asks the name of a file
    file = input("file:").strip().lower()
    #outputs the file media type
    print(Media_type(file))

def Media_type(fle):
    #split the file
    file = fle.rpartition(".")

    #take the end of the file name
    ending = file[2]

    #match the ending with a type of file
    match ending:
        case "gif":
            return "image/gif"
        case "jpeg" | "jpg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()