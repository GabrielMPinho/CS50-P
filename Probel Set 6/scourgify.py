import sys
import csv

if len(sys.argv) < 3:
    print("Poucas linhas de comando")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Muitas linhas de comando")
    sys.exit(1)
elif sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv'):
    try:
        with open(sys.argv[1], 'r') as file:
            leitor = csv.DictReader(file)
            n_arqv = []
            for linhas in leitor:
                ultimo, primeiro = linhas['name'].split(', ')
                n_arqv.append({
                    "Primeiro nome": primeiro,
                    "Último nome": ultimo,
                    "Casa": linhas['house']           
                })
        with open(sys.argv[2], 'w') as file2: 
            escritor = csv.DictWriter(file2, fieldnames= ['Primeiro nome','Último nome','Casa'])
            escritor.writeheader()
            for linha in n_arqv:
                escritor.writerow(linha)


        
    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1) 

















































