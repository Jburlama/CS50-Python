def main():
    while (True):
        try:
            regex = input("Fraction: ")
            percentage = convert(regex)
            if (percentage > 100):
                continue
            print(gauge(percentage))
            return (0)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
    return (0)


def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    percentage = round(x / y * 100)
    return (percentage)


def gauge(percentage):
    if (percentage <= 1):
        return ("E")
    elif (100 >= percentage >= 99):
        return ("F")
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()
