import emoji

def main():
    regex = input("Input: ")
    print(emoji.emojize(f"Output: {regex}", language="alias"))
    return (0)

main()
