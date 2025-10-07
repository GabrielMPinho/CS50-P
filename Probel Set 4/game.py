import random

while True:
    try:
        numero_max = int(input("Level: "))
        numero_aleatorio = random.randint(1, numero_max)
        while True:

            resposta = int(input("Guess: "))
            if resposta > numero_aleatorio:
                print("Ta alto")
            elif resposta < numero_aleatorio:
                print("Ta baixo")
            else:
                print("Acertou!")
                break
        break
    except ValueError:
        break















































