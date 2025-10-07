frase = input("Input: ")
print("Output: ", end="")
for letra in frase:
    if letra.lower() not in ["a", "e", "i", "o", "u"]: #Se a letra n estiver entre essa lista, ela passa, se estiver, vai ser filtrada automaticamente filtrada
        print(letra, end="")