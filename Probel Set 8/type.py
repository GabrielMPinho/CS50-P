'''
type:  vai me falar o tipo que eh algo. Ex:type(50) vai ser um int

'''
import random
class Hat:
    def __init__(self):
        self.casas = ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']
    
    def sortear(self, nome):
        print(nome, 'is in', random.choice(self.casas))
        


chapeu = Hat()
chapeu.sortear('Harry')













































