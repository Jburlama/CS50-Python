import sys

def main():
    filename = get_filename()
    lines = read_lines(filename)
    count = 0
    for line in lines:
        line = line.lstrip(" ")
        if (line.startswith("#") or line.startswith("\n")):
            continue
        count += 1
    print(count)
    return (0)

def get_filename():
    if (len(sys.argv) != 2):
        sys.exit("Too few command-line arguments")
    filename = sys.argv[1]
    if (filename.endswith(".py") == False):
        sys.exit("Not a Python file")
    return (filename)

def read_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    return (lines)


if __name__ == "__main__":
    main()
