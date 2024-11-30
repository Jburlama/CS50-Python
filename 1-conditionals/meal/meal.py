def main():
    time = input("What time is it? ")
    time = convert(time)
    if (7 <= time <= 8):
        print("breakfast time")
    elif (12 <= time <= 13):
        print("lunch time")
    elif (18 <= time <= 19):
        print("dinner time")


def convert(time):
    houre, min = time.split(":")
    houre = int(houre)
    min = float(min)
    min = min * 100 / 60
    return (houre + (min / 100))

if __name__ == "__main__":
    main()
