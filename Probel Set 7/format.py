import re

nome = input('Digite o nome: ').strip()
pares = re.search(r"^(.+), *(.+)$", nome) # * serve para dizer que o espaço é opcional, ent Manata,Gabriel cairia e Manata,     Gabriel tbm, ja que * = 0 ou mais
if pares: #So vai rodar se for digitado algo com ','
    nome = pares.group(2) + ' ' + pares.group(1) #Pega o grupo 2 e dps o grupo 1 e coloca um espaço entre eles. Em caso de escrever Manata, Gabriel
print(nome)
















































