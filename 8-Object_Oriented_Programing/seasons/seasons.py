from datetime import date
import datetime
import sys
import inflect

p = inflect.engine()

def main():
    birth = get_birth_date()
    today = date.today()
    min = calculate_minutes(today, birth)
    words = number_to_words(min)
    words = words.capitalize()
    print(words, "minutes")


def number_to_words(min):
    words = p.number_to_words(min, andword="")
    return (words)

def calculate_minutes(today, birth):
    days = today - birth
    min = days.days * 24 * 60
    return (min)


def get_birth_date():
    try:
        birth = input("Date of Birth: ")
        year, month, day = birth.split("-")
        birth = datetime.date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    return (birth)


if __name__ == "__main__":
    main()
