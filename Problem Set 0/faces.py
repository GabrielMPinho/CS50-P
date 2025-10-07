def main(): #Função principal 
   msg = input() #Peguei uma msg aleatória
   resultado = convert(msg) #Joguei a mensagem na função convert que virará o resultado final
   print(resultado) #Printei o resultado

def convert(mg): #Criei a função convert com o argumento mg
   return mg.replace(':)' , '🙂').replace(':(', '🙁') #Retornei o mg, porém com as paradas subistituídas ai 
   
main() #rodei