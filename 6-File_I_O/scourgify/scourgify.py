import sys
import csv

def main():
    filename = get_filename()
    tables = []
    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last, first = row["name"].split(",")
                first = first.strip()
                tables.append({"first": first, "last":last, "house":row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")

    with open(sys.argv[2], "w") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for row in tables:
            writer.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})
    return (0)

def get_filename():
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    return (sys.argv[1])

if __name__ == "__main__":
    main()
