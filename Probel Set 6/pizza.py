import sys
import csv
from tabulate import tabulate


menu = []

if len(sys.argv) < 2:
    print("Poucas linhas de comando")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Muitas linhas de comando")
    sys.exit(1)
elif sys.argv[1].endswith('.csv'):
    try:
        with open(sys.argv[1], 'r') as file:
            leitor = csv.reader(file)
            for linha in leitor:
                menu.append(linha)
            print(tabulate(menu, tablefmt='grid'))


    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1) 

















































