def main():
    time = str(input("What time is it?: "))
    time = convert(time)
    if 18 <= time <= 19:
        print("dinner time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 7 <= time <= 8:
        print("breakfast time")

def convert(time:str) -> float:
    hours, minutes = time.split(":")
    hours, minutes = float(hours), float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()
