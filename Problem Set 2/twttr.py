users_input = str(input("Input: "))
vowels = ["a","e","i","o","u"]
for letter in vowels:
    users_input = users_input.replace(letter,"")
    users_input = users_input.replace(letter.upper(),"")
print(f"Output: {users_input}")