import inflect

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print(f"Adieu, adieu, to {inflect.engine().join(names)}")
        break
