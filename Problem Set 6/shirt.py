from PIL import Image, ImageOps
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")):
    sys.exit(f"{sys.argv[1]} is not a JPG, JPEG or PNG file")
elif not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
    sys.exit(f"{sys.argv[2]} is not a JPG, JPEG or PNG file")
elif sys.argv[1][-3:] != sys.argv[1][-3:]:
    sys.exit(f"{sys.argv[1]} has not the same extension as {sys.argv[2]}")

try:
    with Image.open(sys.argv[1]) as shirt, Image.open(sys.argv[2]) as person:
        person_fitted = ImageOps.fit(person, shirt.size)
        person_shirt = person_fitted.paste(shirt, shirt)
        person_shirt.save("final.png")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]} or {sys.argv[2]}")
