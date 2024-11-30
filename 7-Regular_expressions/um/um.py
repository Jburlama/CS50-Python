import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    pattern = r"(^um$|^um(\W|\s)|(\W|\s)um(\W|\s)|(\W|\s)um$)"
    patterns_found = re.findall(pattern, s)
    count = 0
    for _ in patterns_found:
       count += 1 
    return (count)

if __name__ == "__main__":
    main()
