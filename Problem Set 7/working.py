import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    hours, minutes = r"[0-9]|1[0-2]", r"[0-5][0-9]|60"
    pattern = r"(" + hours + r")(?:(:" + minutes + r"))? ([AP]M) to (" + hours + ")(?:(:" + minutes + r"))? ([AP]M)"
    match = re.fullmatch(pattern, s)
    if match:
        return change_format(match.group(1), match.group(2), match.group(3)) + " to " + change_format(match.group(4), match.group(5), match.group(6))
    else:
        raise ValueError


def change_format(hours, minutes, meridian):
    if "AM" == meridian:
        return hours + str(minutes or ":00")
    else:
        return f"{int(hours)+12}" + str(minutes or ":00")

if __name__ == "__main__":
    main()
