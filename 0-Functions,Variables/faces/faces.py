def main():
    str = convert(input())
    print(f"{str}")
    return 0

def convert(str):
    str = str.replace(":)", "🙂", -1)
    str = str.replace(":(", "🙁", -1)
    return str

main()
