import requests
import sys

try:
    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        numero = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)



    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    resposta = requests.get(url)
    data = resposta.json()
    preço_bitcoin = data['bpi']['USD']["rate_float"]
    preço_bit = float(preço_bitcoin)
    valor_final = preço_bit * numero
    print(f"${valor_final:,.4f}")

except requests.RequestException:
    print('RequestException')
    sys.exit(1)












