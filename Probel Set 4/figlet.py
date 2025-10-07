from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fontes = figlet.getFonts()

if len(sys.argv) == 1:
    frase = input("Input: ")
    fonte_random = random.choice(fontes)
    figlet.setFont(font=fonte_random)
    print('Output:', figlet.renderText(f"{frase}"))
elif len(sys.argv) == 3 and sys.argv[1] == '-f':
    frase = input("Input: ")
    fonte_escolhida = sys.argv[2]
    if fonte_escolhida in fontes:
        figlet.setFont(font=fonte_escolhida)
        print('Output:', figlet.renderText(f" {frase}"))
    else:
        sys.exit(1)
else:
    sys.exit(1)






















































