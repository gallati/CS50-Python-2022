def main():
    print(convert(str(input("Write an input: "))))

def convert(users_input:str) -> str:
    return users_input.replace(":)","\N{slightly smiling face}").replace(":(","\N{slightly frowning face}")

main()