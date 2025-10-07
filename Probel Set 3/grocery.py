lista = [] #Criei uma lista p adicionar as frutas     
freq = {} #Criei um dic, ja que quero a frequencia (Valor) das frutas

while True:
    try:
        fruta = input()
        lista.append(fruta) #Coloca a fruta digitada na lista
        lista.sort() #Organiza a lista de forma alfabética

    except EOFError:
        break

print() 

for i in lista: #Para cada item na lista
    if i in freq: #Se o item ja estiver no dic 
        freq[i] += 1 #Adiciona mais 1 no valor dele, pq quer dizer q ele ja apareceu.
    else: #Se n tiver aparecido ainda, ou seja, é a primeira vez que ele é visto no dic
        freq[i] = 1 #O valor dele é 1, ou seja, ele é add na lista
    
for n_fruta, quant in freq.items(): #Dic tem chave e valor, devidi ambos em variáveis. O items() retorna ambos como duplas
    print(f"{quant} {n_fruta.upper()}")











































