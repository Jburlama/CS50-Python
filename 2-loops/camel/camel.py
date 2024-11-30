def main():
    str = input("camelCase: ")
    snake_case = str[0]
    for c in str:
        if (c == str[0]):
            continue
        if (c.isupper()):
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    print("snake_case: " + snake_case)
    return (0)

main()
