import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    patterns = r"<iframe(?:.*?)src=\"(?:https?://)(?:www.)?youtube.com/embed/(\w+)\"(:?.*?)iframe>"
    if (match := re.search(patterns, s)):
        return "https://youtu.be/" + match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()

