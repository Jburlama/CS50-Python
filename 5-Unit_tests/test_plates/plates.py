def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    lenght = len(s)
    if (6 < lenght or lenght < 2 or s.isalnum() == False or s[0:2].isalpha() == False):
        return (False)
    first_number = False
    for i in range(len(s)):
        if (first_number == False and s[i].isdecimal()):
            first_number = True
            if (s[i] == "0"):
                return (False)
        if (s[i:i + 1].isalpha() and s[i - 1:i].isdecimal()):
            return (False)
    return (True)
    


if __name__ == "__main__":
    main()

