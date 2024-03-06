import app
import colors
from warnings import *
import os

def Banner():
    os.system("cls")
    filterwarnings('ignore')

    print (f"{colors.CYAN}Welcome to")
    print(f"{colors.BLUE}██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗   _____        ")
    print("██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝  |A .  | _____               ")
    print("██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝   | /.\ ||A ^  | _____        ")
    print("██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗   |(_._)|| / \ ||A _  | _____ ")
    print("██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗  |  |  || \ / || ( ) ||A_ _ |")
    print(" ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ |____V||  .  ||(_'_)||( v )|")
    print("                                                                                 |____V||  |  || \ / |")
    print("                                                                                        |____V||  .  |")
    print("                                                                                               |____V|\n", colors.END)


def main():
    Banner()
    while True:
        i = eval(input("How many decks would you like to use? : "))
        BJ = app.BlackJack(i)
        BJ.Start()

    

main()