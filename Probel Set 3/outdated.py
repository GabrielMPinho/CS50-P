meses = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    data = input("Data: ")

    try: #Parte que vai ser qnd a data tiver /
        mes, dia, ano = data.split('/')
        
        n_mes = int(mes)
        n_dia = int(dia)
        
        if 1 <= n_mes <= 12 and 1 <= n_dia <= 31: #Serve p checar se o numero do dia e mes colocado é valido
            print(f"{ano}-{n_mes:02}-{n_dia:02}") #:02 serve p adicionar 0 a esquerda
            break


    except: #Parte que vai ser qnd a data tiver por extenso
        try:
            mes, dia, ano = data.split(' ')
            dia = dia.strip(',') #Tira a ','. Ex: September 8, 1963 -----> September 8 1963, assim o split acima funciona certin
            n_dia = int(dia)

            if mes in meses and 1 <= n_dia <= 31:
                print(f"{ano}-{int(meses[mes]):02}-{n_dia:02}")
                break
        except:
            break










        













































