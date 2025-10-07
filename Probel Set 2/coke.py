valor_coca = 50 #Falei o valor q a gnt vai mexer 

while valor_coca > 0: #Enquanto este valor for maior q 0
    print(f"Valor devido: {valor_coca}") #Printa o valor da coca no momento
    valor_moeda = int(input('Insira moeda: ')) #Peguei o valor da moeda como int
    if valor_moeda in [5, 10, 25]: #Se a moeda estiver nessa lista
        valor_coca -= valor_moeda #Subtrai o valor da coca - a moeda
#Como é um loop while vai ficar se repedindo até q a primeira condição se torne falsa 
troco = abs(valor_coca) #O troco vai ser o valor absoluto (Sem sinais) do valor da coca qnd o loop while acaba
print(f"Seu troco: {troco}")
    