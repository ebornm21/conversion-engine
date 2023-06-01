#A program that will take a photo of a muppet and overlay a photo of a CS50 tshirt onto them, matching their respective size and position.

import sys
from PIL import Image
from PIL import ImageOps


def main():
    check_arg()
    shirt = Image.open("shirt.png")
    try:
        photo = Image.open(sys.argv[1])
    except:
        print(f"{sys.argv[1]} does not exist")
        sys.exit(1)
    size = shirt.size
    muppet = ImageOps.fit(photo, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


def check_arg():
    suffixes = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if sys.argv[1].lower().endswith(suffixes) and sys.argv[2].lower().endswith(suffixes) == False:
        print("Not image files")
        sys.exit(1)
    file1 = sys.argv[1].split(".")
    file2 = sys.argv[2].split(".")
    if file1[1].lower() != file2[1].lower():
        print("Input and output have different extensions")
        sys.exit(1)


if __name__ == "__main__":
    main()
