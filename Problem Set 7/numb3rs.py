import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number = r"(?:\d|[1-9]\d|1\d\d|2[0-5][0-5])"
    pattern = r"(?:" + number + r"\.){3}" + number
    match = re.fullmatch(pattern, ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
