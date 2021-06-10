### OBETIVO - DAR OPÇÃO AO USUARIO PARA ESCOLHER QUAL MOEDA ELE QUER VER CONVERTIDA ###
dolar = 5.05
euro = 6.16

while True:
    print('=-'*30)
    valor_inicial = input('Qual valor deseja converter: R$').strip().replace(',','.')
    if valor_inicial.replace('.','').isnumeric() == True:
        valor_inicial = float(valor_inicial)
        break
    else:
        print('Dados incorretos')

while True:
    opcao = int(input(f'Para qual moeda o valor R$ {valor_inicial} será convertido? '
    '\n[ 1 ] - Dolar'
    '\n[ 2 ] - Euro'
    '\n->  '))
    if opcao not in [1,2]:
        print('Opção Invalida')
        print('=-'*30)
    else:
        break

converte_dolar = valor_inicial/dolar
converte_euro = valor_inicial/euro

if opcao == 1:
    print(f'O valor R${valor_inicial} em Dolar é de {converte_dolar:.2f}')
elif opcao == 2:
    print(f'O valor R${valor_inicial} em Euro é de {converte_euro:.2f} ')
print('=-'*30)