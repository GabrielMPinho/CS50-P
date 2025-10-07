import random


def main():
    level = get_level()
    pontuação = jogo(level)
    print("Score: ", pontuação)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def simu_round(x, y):
    tentativas = 0  # Contador começa em 0
    while tentativas < 3:  # Permitir até 3 tentativas
        try:
            # Solicitar a resposta do usuário
            answer = int(input(f"{x} + {y} = "))
            # Verificar se a resposta está correta
            if answer == (x + y):
                return True  # Resposta correta
            else:
                print("EEE")  # Resposta errada
                tentativas += 1  # Incrementar tentativas
        except ValueError:  # Capturar erro ao digitar algo que não seja número
            print("EEE")
            tentativas += 1  # Incrementar tentativas

    # Após 3 tentativas incorretas, exibir a resposta correta
    print(f"{x} + {y} = {x + y}")
    return False  # Retornar False porque todas as tentativas falharam


def jogo(level):
    rounde = 1
    pontos = 0

    while rounde <= 10:
        x, y = generate_integer(level)
        resposta = simu_round(x,y)
        if resposta == True:
            pontos += 1
        rounde += 1
    return pontos






if __name__ == "__main__":
    main()


