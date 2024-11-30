import sys
import requests
from tabulate import tabulate


def main():
    if (len(sys.argv) > 1 and len(sys.argv) != 4):
        sys.exit("Usage: 'python3 project.py' or \
'python3 project.py <what> <where> <how many>'")

    if (len(sys.argv) == 1):
        category = get_category(input("What is you looking for? "))
        city = get_city(input("Where? "))
        number_of_results = get_number_of_results(input("how many results? "))
    elif (len(sys.argv) == 4):
        category = sys.argv[1]
        city = sys.argv[2]
        number_of_results = sys.argv[3]

    response = requests.get(f"https://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyDhmt_xVDkKtoH6TwFsEmyUj78HCEKEwEg&query={city},{category}")
    results = response.json()

    places = []
    for place in results["results"]:
        places.append(
            {
                "name": place["name"],
                "rating": place["rating"],
                "address": place["formatted_address"]
            }
        )

    table = build_table(places, number_of_results)
    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
    return (0)


def build_table(places, number_of_results):
    table = []
    i = 0
    for place in sorted(places,
                        key=lambda place: place["rating"], reverse=True):
        table.append(place)
        i += 1
        if (i == number_of_results):
            break
    return (table)


def get_city(c):
    city = c
    return (city)


def get_category(c):
    category = c
    return (category)


def get_number_of_results(n):
    try:
        number_of_results = int(n)
    except ValueError:
        raise ValueError(f"Invalid number '{n}'")
    return (number_of_results)


if __name__ == "__main__":
    main()
