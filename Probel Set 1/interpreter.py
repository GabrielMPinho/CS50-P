exp = input("Expression: ")

#Dividi a expressão em 3 variáveis qnd der espaço na excrita (EX: 1 + 2 ---> 1=x, +=y, 2=z )
x, y, z = exp.split(" ") 

#Transformei apenas o x e o z em números, ja que o y é o sinal de operação
n_x = float(x)
n_z = float(z)

#Se o y for igual a ..., printa n_x ... n_z
if y == '+':
    print(round(n_x + n_z, 2)) #Arredondei para duas casas decimais
elif y == '-':
    print(round(n_x - n_z, 2))
elif y == '*':
    print(round(n_x * n_z, 2))
elif y == '/':
    print(round(n_x / n_z, 2))
else:
    print()





