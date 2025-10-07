class Pacotes:
    def __init__(self, numero, remetente, destinatario, peso):
        self.numero = numero
        self.remetente = remetente
        self.destinatario = destinatario
        self.peso = peso
    
    def __str__(self):
        return f'Pacote {self.numero} de {self.remetente} para {self.destinatario} com peso de {self.peso}kg'
    
    def calcular_peso(self, custo):
        return self.peso * custo
    
def main():
    pacotes = [
        Pacotes(numero=1, remetente='Gabriel', destinatario='Maria Vallentina', peso=5),
        Pacotes(numero=2, remetente='Gabriel', destinatario='Lucas', peso=3)
    ]
    for pacote in pacotes:
        print(f"{pacote} custa R${pacote.calcular_peso(2)}")





main()








































