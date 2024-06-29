import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b(um)\b"
    match = re.findall(pattern, s, re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()