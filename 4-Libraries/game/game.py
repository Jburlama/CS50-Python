import random
import sys

def main():
    while (True):
        try:
            level = input("Level: ")
            level = int(level)
            if (level <= 0):
                continue
            break
        except ValueError:
            pass
    r = random.randrange(1, level + 1)
    while (True):
        try:
            guess = int(input("Guess: "))
            if (guess == r):
                sys.exit("Just right!")
            elif (guess < r):
                print("Too small!")
            elif (guess > r):
                print("Too large!")
        except ValueError:
            pass

main()
