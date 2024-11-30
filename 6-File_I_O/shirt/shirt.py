import sys
import glob, os
import PIL
from PIL import Image
from PIL import ImageOps

def main():
    check_commandline()
    try:
        before = PIL.Image.open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png", "r")
    after = ImageOps.fit(before, shirt.size)
    after.paste(shirt, shirt)
    after.save(sys.argv[2])
    return (0)

def check_commandline():
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    infile = sys.argv[1].lower()
    outfile = sys.argv[2].lower()
    infile_root, infile_ext = os.path.splitext(infile)
    outfile_root, outfile_ext = os.path.splitext(outfile)
    if (check_extension(infile_ext) == False):
        sys.exit("Invalid input")
    elif (check_extension(outfile_ext) == False):
        sys.exit("Invalid output")
    if (infile_ext != outfile_ext):
        sys.exit("Input and output have different extensions")

def check_extension(ext):
    if (ext == ".jpg"):
        return (True)
    elif(ext == ".jpeg"):
        return (True)
    elif(ext == ".png"):
        return (True)
    else:
        return (False)

if __name__ == "__main__":
    main()
