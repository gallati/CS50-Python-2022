users_input = str(input("What is the Answer to the Great Question Of Life, the Universe and Everything?: ")).lower()
match users_input:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")