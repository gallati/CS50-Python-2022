shopping_list = {}
while True:
    try:
        item = input().upper()
        shopping_list[item] = 1 + shopping_list.get(item,0)
    except EOFError:
        item_list = sorted(shopping_list)
        for item in item_list:
            print(f"{shopping_list[item]} {item}")
        break
