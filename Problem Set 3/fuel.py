def main():
    print(get_percentage())

def get_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            X, Y = int(fraction.split("/")[0]), int(fraction.split("/")[1])
            ratio = X/Y
            if X > Y:
                pass
            elif ratio >= 0.99:
                return "F"
            elif ratio > 0.625:
                return "75%"
            elif ratio > 0.375:
                return "50%"
            elif ratio > 0.01:
                return "25%"
            else:
                return "E"
        except (ValueError, ZeroDivisionError):
            pass

main()