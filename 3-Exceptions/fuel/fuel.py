def main():
    while (True):
        try:
            regex = input("Fraction: ")
            x,y = regex.split("/")
            x = int(x)
            y = int(y)
            percentage = round(x / y * 100)
            if (percentage <= 1):
                print("E")
            elif (100 >= percentage >= 99):
                print("F")
            elif (percentage > 100):
                continue
            else:
                print(percentage, "%", sep="")
            return (0)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
    return (0)

main()
