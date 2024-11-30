def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while (True):
        try:
            regex = input("Date: ")
            if ('/' in regex):
                month, day, year = regex.split('/')
                month = int(month)
                day = int(day)
                year = int(year)
            elif (',' in regex):
                month, day, year = regex.split(' ')
                month = months.index(month.capitalize()) + 1
                day = day.split(',')
                day = int(day[0])
                year = int(year)
            else:
                continue
            if (month > 12 or month < 0 or 0 > day or day > 31):
                continue
            break
        except ValueError:
            pass

    print(year, f"{month:02}", f"{day:02}", sep='-')
    return (0)

main()
