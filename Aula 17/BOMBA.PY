class BombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        

    def abastecerPorValor(self):
        self.valorDinheiro = float(input('Digite o valor em R$: '))
        self.abastece = float(self.valorDinheiro/self.valorLitro)
        self.quantidadeCombustivel = self.quantidadeCombustivel - self.abastece
        print(f'O valor de R$ {self.valorDinheiro:.2f} abastece {self.abastece:.2f} l.')


gasolina = BombaCombustivel('Gasolina', 5.90, 1000)
gasolina.abastecerPorValor()