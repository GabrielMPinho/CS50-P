menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
conta = 0 #Criei uma variável inicialmente valendo 0, que vamos alterar mais p frente
while True:
    try:
        pedido = input("Item: ").title() #Tltle() serve p deixar tudo minúsculo
        if pedido in menu:
            conta += menu[pedido] #somar o valor do pedido no menu a conta. Como é um loop infinito, vai continuar somando
            print(f"${conta:.2f}")
    except EOFError:
        print()
        break