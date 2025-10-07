import inflect
p = inflect.engine()
nomes = []

while True:
    try:
        nome = input("Nomes: ")
        nomes.append(nome)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(nomes)}")
















































