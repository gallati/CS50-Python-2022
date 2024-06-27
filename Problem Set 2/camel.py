camel = str(input("camelCase: "))
for letter in camel:
    if letter.isupper():
        camel = camel.replace(letter, f"_{letter.lower()}")
print(f"snake_case: {camel}")