def main():
    dollars = dollars_to_float(input("How much was the meal? ")) #Joguei a resp dessa pergunta na função e dps na variável dollars
    percent = percent_to_float(input("What percentage would you like to tip? ")) #Joguei a resp dessa pergunta na função e dps na variável percent
    tip = dollars * percent #A gorjeta vai ser os valores multiplicados
    print(f"Leave ${tip:.2f}") # Printei q eh p deixar $ gorjeta com 2 casas decimais (:2f). 


def dollars_to_float(d): #Primera função
    return float(d.replace("$","")) #Mandei retornar o valor float(cm casas decimais) de d, trocando as paradas ai


def percent_to_float(p): #Segunda função
    return float(p.replace("%","")) / 100  #Mandei retornar o valor float(cm casas decimais) de p, trocando as paradas ai e dividindo por 100 para ajeitar as casas



main()

#   O argumento das funções (p,d) sao como variáveis temporárias, ou seja, a resposta da primeira pergunta virou a variável d, ai eu mexi nela
#dentro da função, retornei o resultado dela, só ai ela virou o variável dollars 