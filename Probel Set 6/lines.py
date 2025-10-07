import sys

#Checando o tamanho do sys.argv
if len(sys.argv) < 2:
    print("Poucas linhas de comando")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Muitas linhas de comando")
    sys.exit(1)

elif sys.argv[1].endswith('.py'):
    try:
        with open(sys.argv[1], 'r') as file:
            conta = 0
            for linha in file:
                linha_corrigida = linha.strip() #Strip serve para descartar linhas em branco
                if linha_corrigida and not linha.startswith("#"): #Se a linha estiver corrigida, e nao começar com '#'
                    conta += 1
            print(f"O programa tem {conta} linhas de código")

    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1) 















































