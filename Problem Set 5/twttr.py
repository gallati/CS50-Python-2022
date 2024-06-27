def main():
    users_input = input("Input: ")
    print(shorten(users_input))


def shorten(word:str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        word = word.replace(vowel,"").replace(vowel.capitalize(),"")
    return word


if __name__ == "__main__":
    main()