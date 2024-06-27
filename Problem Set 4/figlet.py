import sys
from random import choice
from pyfiglet import Figlet, FontNotFound

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=choice(fonts))
elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and sys.argv[2] in fonts
):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

input_text = input("Input: ")
print(figlet.renderText(input_text))
