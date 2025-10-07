'''
variáveis globais:

'''
balanço = 0

def main():
    adicionar(50)
    retirar(10)
    print(f'Você tem R${balanço:.2f} em sua conta.')

def adicionar(n):
    global balanço
    balanço += n

def retirar(n):
    global balanço
    balanço -= n





if __name__ == '__main__':
    main()















































