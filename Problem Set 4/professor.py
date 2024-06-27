import random


def main():
    n = get_level()
    score = 0

    for _ in range(10):
        X, Y = generate_integer(n), generate_integer(n)
        attemps = 0
        for _ in range(3):
            problem = input(f"{X} + {Y} = ")
            if problem.isnumeric() and int(problem) == X + Y:
                score += 1
                break
            else:
                attemps += 1
                print("EEE")
        if attemps == 3:
            print(f"Solution: {X} + {Y} = {X+Y}")

    print(f"Score: {score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1 or level == 2 or level == 3:
        return random.randint(10 ** (level - 1), 10**level - 1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
