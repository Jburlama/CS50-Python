import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    s = s.upper().strip()
    houre = r"(?:1[0-2]|0\d|\d)"
    min = r"(?::[0-5]\d)?"
    pattern = fr"^({houre}{min}) (AM|PM) TO ({houre}{min}) (AM|PM)$"
    if (match := re.search(pattern, s)):
        start = match.group(1)
        if (":" not in start):
            if (len(start) == 1):
                start = "0" + start
            start += ":00"
        if (match.group(2) == "PM"):
            h, m = start.split(":")
            h = int(h)
            if (h != 12):
                h += 12
            h = str(h)
            if (len(h) == 1):
                h = "0" + h
            end = h + ":" + m
            start = h + ":" + m
        elif (match.group(2) == "AM"):
            h, m = start.split(":")
            h = int(h)
            if (h == 12):
                h = 0
            h = str(h)
            if (len(h) == 1):
                h = "0" + h
            end = h + ":" + m
            start = h + ":" + m
        end = match.group(3)
        if (":" not in end):
            if (len(start) == 1):
                end = "0" + start
            end += ":00"
        if (match.group(4) == "PM"):
            h, m = end.split(":")
            h = int(h)
            if (h != 12):
                h += 12
            h = str(h)
            if (len(h) == 1):
                h = "0" + h
            end = h + ":" + m
        elif (match.group(4) == "AM"):
            h, m = end.split(":")
            h = int(h)
            if (h == 12):
                h = 0
            h = str(h)
            if (len(h) == 1):
                h = "0" + h
            end = h + ":" + m
            end = h + ":" + m
        return (start + " to " + end)
    else:
        raise ValueError(f"Ivalid {s}")

if __name__ == "__main__":
    main()
