def main():
    fruta = input("Item: ").lower() #Peguei a fruta
    calo = calorias(fruta) #Taquei ela na função q eu criei
    if calo is True: #Se for uma das frutas selecionadas
        print(f"Calories: {calo}") #Printa isso 
    else:
        print("") #Se n, printa isso


def calorias(x):
    if x == "apple":
        print("130")
    elif x == "avocado":
        print("50")
    elif x == "banana":
        print("110")
    elif x == "cantaloupe":
        print("50")
    elif x == "grapefruit":
        print("60")
    elif x == "grapes":
        print("90")
    elif x == "melon":
        print("50")
    elif x == "kiwifruit":
        print("90")
    elif x == "lemon":
        print("15")
    elif x == "lime":
        print("20")
    elif x == "nectarine":
        print("60")
    elif x == "orange":
        print("80")
    elif x == "peach":
        print("60")
    elif x == "pear":
        print("100")
    elif x == "pineapple":
        print("50")
    elif x == "plums":
        print("70")
    elif x == "strawberries":
        print("50")
    elif x == "sweet cherries":
        print("100")
    elif x == "tangerine":
        print("50")
    elif x == "watermelon":
        print("80")
    else:
        print("")

main()
