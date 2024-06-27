months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        MM, DD, YYYY = map(int, date.split("/"))
        if 0 < MM < 13 and 0 < DD < 32 and 0 < YYYY:
            break
    except:
        try:
            date_split = date.split(" ")        
            month, DD, YYYY = date_split[0], int(date_split[1][:-1]), int(date_split[2])
            MM = months.index(month) + 1
            if 0 < MM < 13 and 0 < DD < 32 and 0 < YYYY:
                break
        except ValueError:
            pass

print(f"{YYYY:04}-{MM:02}-{DD:02}")