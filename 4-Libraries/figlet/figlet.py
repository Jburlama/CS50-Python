import sys
import random
from pyfiglet import Figlet

def main():
    if (len(sys.argv) == 3):
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            figlet = Figlet()
            fonts = figlet.getFonts()
            if (sys.argv[2] in fonts):
                figlet.setFont(font=sys.argv[2])
                text = input("Input: ")
                print(figlet.renderText(text))
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    elif (len(sys.argv) == 1):
        figlet = Figlet()
        fonts = figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))
        text = input("Input: ")
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")

main()
