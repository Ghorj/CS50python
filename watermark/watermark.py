import sys
from PIL import Image

def main():
    #import photo and watermark
    if len(sys.argv) == 3:
        photo = sys.argv[1]
        watermark = sys.argv[2]

        #resize photo
        ig = 128,128
        photo_rsz = resize(photo, ig)


        #blend watermark with photo and create a new image
        final_photo = blend(photo_rsz, watermark)

    else:
        sys.exit("Incorrect number of arguments given")

def resize(photo, size):

    with Image.open(photo) as im:
        return im.thumbnail(size)


def blend(photo, watermark):




if __name__ == "__main__":
    main()
