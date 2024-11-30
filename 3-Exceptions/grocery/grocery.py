def main():
    items = dict()
    while (True):
        try:
            item = input()
            item = item.upper()
            if (items.get(item) == None):
                items[item] = 1
            else:
                items[item] += 1
        except EOFError:
            break
        except KeyError:
            pass
    print()
    sorted_items = sorted(items)
    for item in sorted_items:
        print(items[item], item)
    return (0)

main()
