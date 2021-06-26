#03.Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    taxa = custo*(taxaImposto/100)
    total = custo + taxa
    print(f'O preço do produto com custo de R${custo:.2f}, com a taxa de {taxaImposto}% é de R${total:.2f}')

preço = float(input('Qual o preço do produto: '))
imposto = float(input('Qual a taxa de imposto em %: '))

somaImposto(imposto,preço)