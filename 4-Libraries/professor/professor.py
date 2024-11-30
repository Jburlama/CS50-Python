import random
import sys

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        tries = 0
        while (True):
            if (tries == 3):
                print(f"{x} + {y} = {result}")
                break
            try:
                answer = int(input(f"{x} + {y} = "))
                if (answer == result):
                    score += 1
                    break
                elif (answer != result):
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
            except EOFError:
                sys.exit()
    print(f"Score: {score}")
    return (0)

def get_level():
    while (True):
        try:
            level = int(input("Level: "))
            if (3 < level or level < 1):
                continue
            else:
                break
        except ValueError:
            pass
        except EOFError:
            sys.exit()
    return (level)


def generate_integer(level):
    if (level == 1):
        return (random.randrange(start=10))
    elif (level == 2):
        return (random.randrange(10, 99))
    elif (level == 3):
        return (random.randrange(100, 999))


if __name__ == "__main__":
    main()

