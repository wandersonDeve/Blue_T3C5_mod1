class Mamifero():
    def __init__(self,nome,pelo,cor,tamanho,idade):
        self.nome = nome
        self.pelo = pelo
        self.cor = cor
        self.tamanho = tamanho
        self.idade = idade

    def crescer(self):
        self.idade += 1

    def locomover(self):
        print('ele está andando')
    
    def comer(self):
        self.tamanho = 'Grande'

cachorro = Mamifero('Scooby','Curto','Marrom','Grande',3)
print(type(cachorro))
print(vars(cachorro))
print(type(vars(cachorro)))

cachorro.crescer()
cachorro.locomover()
cachorro.comer()
print(vars(cachorro))