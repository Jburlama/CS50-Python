def main():
    word = input("Input: ")
    short_str = shorten(word)
    print(short_str)


def shorten(word):
    short_str = ""
    for c in word:
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or
            c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
            continue
        short_str += c
    return (short_str)


if __name__ == "__main__":
    main()
