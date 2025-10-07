import sys

def main():
    user = get_dados()
    faixa_etaria = get_faixa_etaria(user['idade'])
    imc = get_imc(user["peso"], user["altura"])
    resultado = resultado_imc(faixa_etaria, imc)
    gasto_cal = get_gasto_cal(user['sexo'], user['peso'], user['altura'], user['idade'])

    print(f"Seu IMC é {imc:.2f}, portanto você está {resultado}.")
    print(
        f"Seu gasto calórico diário é de {gasto_cal:.2f} calorias. "
        "Para manter o seu peso atual, você deve consumir essa quantidade de calorias diariamente, "
        "para emagrecer consuma menos e para ganhar peso consuma mais, isto fazendo acompanhamento e musculação."
    )

def get_dados():
    while True:
        try:
            sexo = input('Informe o seu sexo (M/F): ').upper()
            if sexo not in ['M', 'F']:
                print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")
                continue
            
            idade = int(input('Informe a sua idade: '))
            if idade < 5:
                print("Idade inválida. O mínimo permitido é 5 anos.")
                continue

            peso = float(input('Informe o seu peso em Kg: '))
            altura = float(input('Informe a sua altura em centímetros: ')) / 100
            
            return {'sexo': sexo, 'idade': idade, 'peso': peso, 'altura': altura}
        except ValueError:
            print('Entrada inválida. Digite novamente.')

def get_faixa_etaria(idade):
    if 5 <= idade <= 19:
        return 'criança/adolescente'
    elif 20 <= idade <= 59:
        return 'adulto'
    elif idade >= 60:
        return 'idoso'

def get_imc(peso, altura):
    try:
        return peso / (altura ** 2)
    except ZeroDivisionError:
        print('Erro: altura inválida.')
        sys.exit(1)

def resultado_imc(faixa_etaria, imc):
    if faixa_etaria == 'criança/adolescente':
        if imc < 16:
            return 'abaixo do peso'
        elif 16 <= imc <= 25.6:
            return 'com peso normal'
        elif  25.7 <= imc <= 29:
            return 'com sobrepeso'
        else:
            return 'com obesidade'
        
    elif faixa_etaria == 'adulto':
        if imc < 18.5:
            return 'abaixo do peso'
        elif 18.5 <= imc <= 24.9:
            return 'com peso normal'
        elif 25 <= imc < 29.9:
            return 'com sobrepeso'
        elif 30 <= imc <= 34.9:
            return 'com obesidade grau 1'
        elif 35 <= imc <= 39.9:
            return 'com obesidade grau 2'
        else:
            return 'com obesidade grau 3'

    elif faixa_etaria == 'idoso':
        if imc < 22:
            return 'Abaixo do peso'
        elif 22 <= imc <= 27:
            return 'Peso normal'
        else:
            return 'Acima do peso'

def get_gasto_cal(sexo, peso, altura, idade):
    if sexo == 'M':
        gasto_cal = 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * idade)
    else: 
        gasto_cal = 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * idade)
    
    while True:
        nivel_atv = input("Quão regular você se exercita? (Sedentário, Levemente ativo, Moderadamente ativo, Muito ativo, Extremamente ativo): ").strip().lower()
        if nivel_atv == 'sedentário':
            return gasto_cal * 1.2
        elif nivel_atv == 'levemente ativo':
            return gasto_cal * 1.375
        elif nivel_atv == 'moderadamente ativo':
            return gasto_cal * 1.55
        elif nivel_atv == 'muito ativo':
            return gasto_cal * 1.725
        elif nivel_atv == 'extremamente ativo':
            return gasto_cal * 1.9
        else:
            print("Nível de atividade inválido. Tente novamente.")

if __name__ == "__main__":
    main()




























