import sys
from PIL import Image
from PIL import ImageOps


def main():

    #expects exactly 2 command-line arguments
    if len(sys.argv) == 3:


        #in sys.argv[1] the name of a jpeg or png to read
        read = sys.argv[1].strip()


        #in sys.argv[2] the name of a jpeg or png to write
        write = sys.argv[2].strip()


        #names end in .jpg, .jpeg or .png
        if read.endswith(".jpg") == True:
            end = ".jpg"


        elif read.endswith(".jpeg") == True:
            end = ".jpeg"


        elif read.endswith(".png") == True:
            end = ".png"

        #exit if the names don't end in .jpg, .jpeg or .png (case-insensitively)
        else:
            sys.exit("Not a valid image format")

        if write.endswith(".jpg") == True or write.endswith(".jpeg") ==True or write.endswith(".png") == True:

            #the input has the same extension as the ouput's name
            if write.endswith(end) == True:
                #get the width and height of the t-shirt
                shirt = Image.open("shirt.png")

                size = shirt.size

                #the input file exists
                try:
                    #open input with Image.open
                    img = Image.open(read)

                    #resize and crop with ImageOps.fit
                    img = ImageOps.fit(img, size)

                    #overlay shirt.png (transparent background) on the input after
                    img.paste(shirt, shirt)


                    # resizing and cropping to be the same size


                    #overlay the shirt with Image.paste

                    #save the result with Image.save
                    img.save(write)

                #exit if the specified input doesn't exist
                except FileNotFoundError:
                    sys.exit("File not found")

            else:

                sys.exit(f"Different image formats, expected {end}")

        else:
            sys.exit("Not a valid image format")












    #exit if the user does not specify 2 command-line arguments
    else:
        sys.exit("Incorrect number of command-line arguments given")







if __name__ == "__main__":
    main()
