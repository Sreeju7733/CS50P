import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv = ["-f", "--font"]

if len(sys.argv) > 1:
    if sys.argv[1] in argv:
        if len(sys.argv) > 2 and sys.argv[2] in figlet.getFonts():
            font = sys.argv[2]
        else:
            sys.exit("Invalid useage")
    else:
        sys.exit("Invalid useage")
else:
    font = random.choice(figlet.getFonts())

figlet.setFont(font=font)

# Getting input from the user
user_input = input("Input: ")

print("Output:")
print(figlet.renderText(user_input))
