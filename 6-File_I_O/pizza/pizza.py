import sys
import csv
from tabulate import tabulate


def main():
    filename = get_filename()
    table = get_table(filename)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    return (0)


def get_table(filename):
    table = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            table.append(row)
    return (table)


def get_filename():
    if (len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")
    if (sys.argv[1].endswith(".csv") == False):
        sys.exit("Not a CSV file")
    return (sys.argv[1])


if __name__ == "__main__":
    main()
