def main():
    #Chamei o input e coloquei a resposta em uma variavel
    hora = input('What time is it? ')

    #Essa variável, dps de ser convertida em decimal vira outra variável, que será usada abaixo
    hora_convertida = convert(hora)
    
    #Se a hora convertida estiver entre isso, printa ...
    if 7.0 <= hora_convertida <= 8.0:
        print("Breakfest time")
    elif 12 <= hora_convertida <= 13:
        print("Lunch time")
    elif 18 <= hora_convertida <= 19:
        print ("Dinner time")
    else:
        print()


#MAIS DIFICIL
def convert(time):
    horas, minutos = time.split(':') #Dividí o time(variavel colocada) no : em outras 2 variáveis
    
    #Transformei essas novas variáveis em outras varíaveis, soq vistas como numeros
    n_h = int(horas)
    n_m = int(minutos)

    #Essa equação serve p transformar em número decimal (7:30 -> 7.5 pq 30(minutos) / 60 = 0,5)
    tempo = n_h + n_m / 60
    
    #Retornei esse valor
    return tempo


if __name__ == "__main__": #Só mandaram colocar isso daq
    main()