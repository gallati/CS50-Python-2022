fruits:dict = {"apple":130, "banana":110 ,"avocado":50, "sweet cherries":100}
fruit = str(input("Item: ")).lower()
if fruit in fruits:
    print(f"Calories: {fruits[fruit]}")