

while True: #Loop infinito
    try: #Tente:
        frac = input("Fração: ")

        num, den = frac.split('/')

        n_num = int(num)
        n_den = int(den)

        resul = round(n_num / n_den * 100) #Peguei a porcentagem da fração


        if resul <= 1:
            print("Vazio")
            break 
        elif resul >= 99:
            print("Cheio")
            break
        else:
            print(f"{resul}%")
            break

    except (ZeroDivisionError, ValueError): #Se der valor errado...
        pass #Passa e volta pro inicio
     


















































