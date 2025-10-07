camelo = input("camelCase: ") #Input
print(f"snake_case: ", end="") #Printei em seguida essa frase e botei end="", assim o prox print vai ficar na msm linha
for letra in camelo: #Para cada letra em camelo
    if letra.isupper(): #Se a letra é maiúscula
        print('_' + letra.lower(), end='') #Printa _ + letra minuscula e o end p que todas as letras fiquem juntas
    else: #Se nao 
        print(letra, end="") #Printa a letra, o end p que todas as letras fiquem juntas
print() #Print final so p que o cadigo termine certinho      
        

