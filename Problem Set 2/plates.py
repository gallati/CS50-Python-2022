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

main()

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
