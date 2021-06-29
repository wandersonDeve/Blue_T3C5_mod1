# 1.a) Crie uma classe pessoa com os seguintes atributos: nome, sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e métodos.

class Pessoa():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostrar_dados(self):
        print(f'Nome Completo: {self.nome} {self.sobrenome}\nIdade: {self.idade}')

alguem = Pessoa('Wanderson','Santos',30)
alguem.mostrar_dados()

