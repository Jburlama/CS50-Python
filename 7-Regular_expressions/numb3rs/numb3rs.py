import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip = ip.strip()
    pattern = r"^((?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.(?:\d|\d\d|1\d\d|2[0-4]\d|25[0-5]))$"
    if (match := re.search(pattern, ip)):
        return (True)
    else:
        return (False)

if __name__ == "__main__":
    main()
