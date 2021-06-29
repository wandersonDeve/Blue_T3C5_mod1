# 2) Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados

class Conta():
    def __init__(self,Titular,Saldo):
        self.Titular = Titular
        self.Saldo = Saldo

    def Sacar(self,valor):
        self.Saldo -= valor
    
    def Depositar(self,valor):
        self.Saldo += valor

pessoa = Conta('Wanderson',5000)

pessoa.Sacar(50)
print(f' O(a) {pessoa.Titular} sacou R$50.00 ele(a) tem agora em conta R${pessoa.Saldo:.2f}\n')
pessoa.Depositar(25)
print(f' O(a) {pessoa.Titular} depositou R$25.00 ele(a) tem agora em conta R${pessoa.Saldo:.2f}')


