import sys, csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv")):
    sys.exit("Not a CSV file")


try:
    with open(sys.argv[1], "r") as before, open(sys.argv[2], "a") as after:
        before_reader = csv.DictReader(before)
        after_writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        after_writer.writeheader()
        for row in before_reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            after_writer.writerow({"first":first, "last":last, "house":house})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
