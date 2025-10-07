def main():
    resp = input("Greeting: ").lower().strip() #Botei em minúsculo e tirei os espaços para se digitar errado ainda funcionar
    conver(resp) #Botei a variável p rodar na funçã0 q eu criei

def conver(x):
    if 'hello' in x: #Se tem 'hello' no x (AQ TEM Q COLOCAR EM MINÚSCULO POR CASA DO LOWER ALÍ EM CIMA), printa 0reais
        print('$0')
    elif 'how' in x: 
        print('$20')
    else: 
        print('$100')

main()