class Food:
    vida_inicial = 1
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
        self.coracao = Food.calcular_coracao(ingredientes)
    #Vai calcular o valor que vai curar a vida do jogador e armaazenar na variável self.coracao, ou so coracao.
    @classmethod #Pertençe a classe e não ao objeto. 
    def calcular_coracao(cls, ingredientes):
        vida = cls.vida_inicial
        for ingrediente in ingredientes:
            if "cogumelo" in ingrediente.lower():
                vida += 2
            else:
                vida += 1
        return vida

def main():
    cogumelo = Food(ingredientes=['Cogumelo', 'Arroz'])#Armazena estes objetos na variável cogumelo e passa para a classe Food em ingredientes.
    print(f"Sua vida foi curada em {cogumelo.coracao} pontos") #cogumelo.coracao vai retornar o valor que a vida foi curada, pq a variável coracao foi armazenada na classe Food.

main()















































