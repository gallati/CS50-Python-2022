def main():
    greeting = input("Greeting: ")
    print(f"${value}")


def value(greeting:str) -> int:
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()