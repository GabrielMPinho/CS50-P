def main(): #Defini a função principal
    resp = input('File name: ').strip().lower() #Botei em minúsculo e tirei os espaços para se digitar errado ainda funcionar
    #Se tem '.x' na variável escolhida, print(...) 
    if '.gif' in resp:
        print('image/gif')
    elif '.jpg' in resp:
        print('image/jpeg')
    elif '.jpeg' in resp:
        print('image/jpeg')
    elif '.png' in resp:
        print('image/png')
    elif '.pdf' in resp:
        print('application/pdf')
    elif '.txt' in resp:
        print('text/plain')
    elif '.zip' in resp:
        print('application/zip')
    else:
        print('application/octet-stream')



main()