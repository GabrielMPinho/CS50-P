"""
POO: Programação Orientada a Objetos
classes: são modelos para criar dados.
    objetos: são coisas (atributos) dentro das classes.
    métodos: são funções dentro das classes.
    __init__(self, ...) : é o método construtor. Ele é chamado quando um objeto é criado.
    self: é uma referência ao objeto que está sendo criado, vai armazenar os atributos do objeto em variaveis 
    __str__(self): é um método que retorna uma representação em string do objeto.
    classmethod: é um método que é chamado pela classe e não pelo objeto.
"""
class Student:
    def __init__(self, nome, casa, patrono): #Método construtor
        if not nome:
            raise ValueError('Nome não pode ser vazio.') #Se o nome for vazio, vai dar erro.
        if casa not in ('gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin'):
            raise ValueError('Casa inválida.') #Se a casa não for uma das 4 casas, vai dar erro.
        self.name = nome #Armazena o nome do estudante na variável name
        self.house = casa #Armazena a casa do estudante na variável house
        self.patronus = patrono #Armazena o patrono do estudante na variável patronus
    
    def __str__(self):
        return f'{self.name} da casa {self.house}, com o patrono {self.patronus}' #Retorna o nome e a casa do estudante em formato de string
    
    def charme(self):
        match self.patronus: #Da metch no objeto patronus
            case "cachorro": #Caso for cachorro, retorna um emoji de cachorro
                return "🐶"
            case "leão":
                return "🦁"
            case "gato":
                return "🐱"           
            case "_":
                return "🤷‍♂️" #Caso não for nenhum dos anteriores.

def main():
    aluno = get_student()
    print('Expectro patrono')
    print(aluno.charme())

def get_student():
    nome = input('Nome: ')
    casa = input('Casa: ')
    patrono = input('Patrono: ')
    return Student(nome, casa, patrono)

if __name__ == '__main__':
    main()


















































