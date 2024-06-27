from emoji import emojize

users_input = input("Input: ")
print(f"Output: {emojize(users_input, language="alias")}")