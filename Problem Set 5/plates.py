def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str) -> bool:
    if s[0:2].isalpha() and 1 < len(s) < 7 and s.isalnum() and numbers(s):
        return True
    else:
        return False


def numbers(s:str) -> bool:
    for character in s[2:-1]:
        if character.isdigit():
            index = s.index(character)
            if s[index:].isdigit() and int(character) != 0:
                return True
            else:
                return False


if __name__ == "__main__":
    main()