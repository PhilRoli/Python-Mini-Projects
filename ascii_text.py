import os
from pyfiglet import Figlet

def print_cool(text):
    # fonts: slanted, 3-d, 3x5, alligator, dotmatrix, bubble, digital
    cool_tetxt = Figlet()
    os.system("cls")
    # sets the window to 70 spaces wide and 20 lines high
    os.system('mode con: cols=70 lines=20')
    return str(cool_tetxt.renderText(text))

if __name__ == "__main__":
    print(print_cool("Philipp Rolinek"))
    input()