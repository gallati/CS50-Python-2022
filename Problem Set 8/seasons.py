from datetime import date
import inflect
import sys


def main():
    birth, today = get_date(), date.today()
    sing((today-birth).days*24*60)


def get_date():
    try:
        return date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")


def sing(number):
    print(f"{inflect.engine().number_to_words(number, andword=",").capitalize()} minutes")


if __name__ == "__main__":
    main()

