'''
set: elimina duplicatas


'''

alunos = [ 
    {"nome": "Ana", "casa": "Violoes"},
    {"nome": "Pedro", "casa": "Violoes"},
    {"nome": "Joao", "casa": "Equador"},
    {"nome": "Maria", "casa": "Equador"},
    {"nome": "Jose", "casa": "Coreu"}
]

casas = set()

for aluno in alunos:
    casas.add(aluno["casa"])

for casa in sorted(casas):
    print(casa)














































