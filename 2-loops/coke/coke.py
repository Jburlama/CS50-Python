def main():
    price = 50
    while (42):
        print("Amount Due:", price)
        coin = int(input("Insert Coin: "))
        if (coin == 5 or coin == 10 or coin == 25):
            price -= coin
        if (price <= 0):
            print("Change Owed:", abs(price))
            break
    return (0)

main()
