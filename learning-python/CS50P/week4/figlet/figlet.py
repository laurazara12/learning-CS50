from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
used_fonts = []
if len(sys.argv) == 1:
    used_fonts = figlet.getFonts()
    used_font = random.choice(used_fonts)
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
elif len(sys.argv) == 3 and (sys.argv[1]) == "-f" or (sys.argv[1]) =="--font"  :
    font_name = sys.argv[2]
    figlet.setFont(font=font_name)
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
else:
    sys.exit("Error")
