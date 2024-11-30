import inflect

def main():
    p = inflect.engine()
    names = []
    while (True):
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    print()
    mylist = p.join((names))
    print(f"Adieu, adieu, to {mylist}")
    return (0)

main()
