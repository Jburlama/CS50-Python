def main():
    str = input("Input: ")
    print("Output:", end=" ")
    for c in str:
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or
            c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
            continue
        print(c, end="")
    print()
    return (0)

main()
